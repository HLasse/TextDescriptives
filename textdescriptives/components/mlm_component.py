"""
Copyright (C) 2022 Explosion AI and Kenneth Enevoldsen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.

Original code from:
https://github.com/explosion/spacy-transformers/blob/master/spacy_transformers/pipeline_component.py
"""

import warnings
from pathlib import Path
from typing import Callable, Iterable, Iterator, List, Optional, Union

import srsly
from spacy import Errors, util
from spacy.language import Language
from spacy.pipeline.pipe import deserialize_config
from spacy.pipeline.trainable_pipe import TrainablePipe
from spacy.tokens import Doc
from spacy.training import Example
from spacy.util import minibatch
from spacy.vocab import Vocab  # pylint: disable=no-name-in-module
from spacy_transformers.annotation_setters import null_annotation_setter
from spacy_transformers.data_classes import FullTransformerBatch
from spacy_transformers.util import batch_by_length
from thinc.api import Config, Model

from .util import install_extensions, softmax, split_by_doc

DEFAULT_CONFIG_STR = """
[sequence_classification_transformer]
max_batch_items = 4096
doc_extension_trf_data = "mlm_trf_data"
doc_extension_prediction = "mlm_prediction"

[sequence_classification_transformer.set_extra_annotations]
@annotation_setters = "spacy-transformers.null_annotation_setter.v1"

[sequence_classification_transformer.model]
@architectures = "spacy-wrap.MLMTransformerModel.v1"
tokenizer_config = {"use_fast": true}
transformer_config = {}
mixed_precision = false
grad_scaler_config = {}

[sequence_classification_transformer.model.get_spans]
@span_getters = "spacy-transformers.strided_spans.v1"
window = 128
stride = 96
"""

DEFAULT_CONFIG = Config().from_str(DEFAULT_CONFIG_STR)


@Language.factory(
    "sequence_classification_transformer",
    default_config=DEFAULT_CONFIG["sequence_classification_transformer"],
)
def make_sequence_classification_transformer(
    nlp: Language,
    name: str,
    model: Model[List[Doc], FullTransformerBatch],
    set_extra_annotations: Callable[[List[Doc], FullTransformerBatch], None],
    max_batch_items: int,
    doc_extension_trf_data: str,
    doc_extension_prediction: str,
    labels: Optional[List[str]] = None,
    assign_to_cats: bool = True,
):
    """Construct a MLMTransformer component, which lets you
    plug a model from the Huggingface transformers library into spaCy so you
    can use it in your pipeline. The component will add a Doc extension with
    the name specified in the config/arguments, which you can use to access the
    transformer's output.

    Args:
        nlp (Language): The current nlp object.
        model (Model[List[Doc], FullTransformerBatch]): A thinc Model object wrapping
            the transformer. Usually you will want to use the
            MLMTransformer layer for this.
        set_extra_annotations (Callable[[List[Doc], FullTransformerBatch], None]): A
            callback to set additional information onto the batch of `Doc` objects.
            The doc._.{doc_extension_trf_data} attribute is set prior to calling the
            callback as well as doc._.{doc_extension_prediction} and
            doc._.{doc_extension_prediction}_prob. By default, no additional annotations
            are set.
        max_batch_items (int): The maximum number of items to process in a batch.
        doc_extension_trf_data (str): The name of the Doc extension to add the
            transformer's output to.
        doc_extension_prediction (str): The name of the Doc extension to add the
            transformer's prediction to.
        labels (List[str]): A list of labels which the transformer model outputs, should
            be ordered.
        assign_to_cats (bool): Whether to assign the predictions to the doc.cats
            dictionary. Defaults to True.

    Returns:
        SequenceClassificationTransformer: The constructed component.

    Example:
        >>> import spacy
        >>> import spacy_wrap
        >>>
        >>> nlp = spacy.blank("en")
        >>>
        >>> config = {
        >>>     "doc_extension_trf_data": "clf_trf_data",  # document extention for the forward pass
        >>>     "doc_extension_prediction": "sentiment",  # document extention for the prediction
        >>>     "model": {
        >>>         "@architectures": "spacy-transformers.SequenceClassificationTransformer.v1",
        >>>         # the model name or path of huggingface model
        >>>         "name": "distilbert-base-uncased-finetuned-sst-2-english",
        >>>     },
        >>> }
        >>>
        >>> nlp.add_pipe("sequence_classification_transformer", config=config)
        >>>
        >>> doc = nlp("spaCy is a wonderful tool")
        >>> doc.cats
        {'NEGATIVE': 0.001, 'POSITIVE': 0.999}
    """
    clf_trf = SequenceClassificationTransformer(
        vocab=nlp.vocab,
        model=model,
        set_extra_annotations=set_extra_annotations,
        max_batch_items=max_batch_items,
        name=name,
        labels=labels,
        doc_extension_trf_data=doc_extension_trf_data,
        doc_extension_prediction=doc_extension_prediction,
        assign_to_cats=assign_to_cats,
    )
    return clf_trf


class SequenceClassificationTransformer(TrainablePipe):
    """spaCy pipeline component that provides access to a transformer model
    from the Huggingface transformers library. Usually you will connect
    subsequent components to the shared transformer using the
    TransformerListener layer. This works similarly to spaCy's Tok2Vec
    component and Tok2VecListener sublayer. The activations from the
    transformer are saved in the doc._.{doc_extension_trf_data} extension
    attribute. You can also provide a callback to set additional annotations.

    Args:
        vocab (Vocab): The Vocab object for the pipeline.
        model (Model[List[Doc], FullTransformerBatch]): A thinc Model object wrapping
            the transformer. Usually you will want to use the TransformerModel
            layer for this.
        set_extra_annotations (Callable[[List[Doc], FullTransformerBatch], None]): A
            callback to set additional information onto the batch of `Doc` objects.
            The doc._.{doc_extension_trf_data} attribute is set prior to calling the
            callback as well as doc._.{doc_extension_prediction} and
            doc._.{doc_extension_prediction}_prob. By default, no additional annotations
            are set.
        labels (List[str]): A list of labels which the transformer model outputs, should
            be ordered.
    """

    def __init__(
        self,
        vocab: Vocab,
        model: Model[List[Doc], FullTransformerBatch],
        labels: List[str],
        assign_to_cats: bool,
        doc_extension_trf_data: str,
        doc_extension_prediction: str,
        set_extra_annotations: Callable = null_annotation_setter,
        *,
        name: str = "sequence_classification_transformer",
        max_batch_items: int = 128 * 32,  # Max size of padded batch
    ):
        """Initialize the transformer component."""
        self.name = name
        self.vocab = vocab
        self.model = model
        if not isinstance(self.model, Model):
            raise ValueError(f"Expected Thinc Model, got: {type(self.model)}")
        self.set_extra_annotations = set_extra_annotations
        self.cfg = {"max_batch_items": max_batch_items}
        self.doc_extension_trf_data = doc_extension_trf_data
        self.model_labels = labels
        self.doc_extension_prediction = doc_extension_prediction
        self.assign_to_cats = assign_to_cats
        self.is_initialized = False

        install_extensions(self.doc_extension_trf_data)
        install_extensions(self.doc_extension_prediction)
        install_extensions(f"{self.doc_extension_prediction}_prob")

        self.__initialize_component()

    @property
    def is_trainable(self) -> bool:
        return False

    def prob_getter(self, doc) -> dict:
        trf_data = getattr(doc._, self.doc_extension_trf_data)
        if trf_data.tensors:
            return {
                "prob": softmax(trf_data.tensors[0][0]).round(decimals=3),
                "labels": self.model_labels,
            }
        warnings.warn(
            "The tensors from the transformer forward pass is empty this is likely"
            + " caused by an empty input string. Thus the model will return None",
        )
        return {
            "prob": None,
            "labels": self.model_labels,
        }

    def label_getter(self, doc) -> Optional[str]:
        prob = getattr(doc._, f"{self.doc_extension_prediction}_prob")
        if prob["prob"] is not None:
            return self.model_labels[int(prob["prob"].argmax())]
        return None

    def set_annotations(
        self,
        docs: Iterable[Doc],
        predictions: FullTransformerBatch,
    ) -> None:
        """Assign the extracted features to the Doc objects. By default, the
        TransformerData object is written to the doc._.{doc_extension_trf_data}
        attribute. Your set_extra_annotations callback is then called, if
        provided.

        Args:
            docs (Iterable[Doc]): The documents to modify.
            predictions: (FullTransformerBatch): A batch of activations.
        """
        doc_data = split_by_doc(predictions)
        for doc, data in zip(docs, doc_data):
            setattr(doc._, self.doc_extension_trf_data, data)
            probs = self.prob_getter(doc)
            setattr(doc._, f"{self.doc_extension_prediction}_prob", probs)
            label = self.label_getter(doc)
            setattr(doc._, self.doc_extension_prediction, label)
            if self.assign_to_cats:
                for prob, label in zip(probs["prob"], probs["labels"]):
                    doc.cats[label] = prob

        self.set_extra_annotations(docs, predictions)

    def __call__(self, doc: Doc) -> Doc:
        """Apply the pipe to one document. The document is modified in place,
        and returned. This usually happens under the hood when the nlp object
        is called on a text and all components are applied to the Doc.

        Args:
            docs (Doc): The Doc to process.

        Returns:
            (Doc): The processed Doc.
        """
        outputs = self.predict([doc])
        self.set_annotations([doc], outputs)
        return doc

    def pipe(self, stream: Iterable[Doc], *, batch_size: int = 128) -> Iterator[Doc]:
        """Apply the pipe to a stream of documents. This usually happens under
        the hood when the nlp object is called on a text and all components are
        applied to the Doc.

        Args:
            stream (Iterable[Doc]): A stream of documents.
            batch_size (int): The number of documents to buffer.

        Yield:
            (Doc): Processed documents in order.
        """
        for outer_batch in minibatch(stream, batch_size):
            outer_batch = list(outer_batch)
            for indices in batch_by_length(outer_batch, self.cfg["max_batch_items"]):
                subbatch = [outer_batch[i] for i in indices]
                self.set_annotations(subbatch, self.predict(subbatch))
            yield from outer_batch

    def predict(self, docs: Iterable[Doc]) -> FullTransformerBatch:
        """Apply the pipeline's model to a batch of docs, without modifying
        them. Returns the extracted features as the FullTransformerBatch
        dataclass.

        Args:
            docs (Iterable[Doc]): The documents to predict.
        Returns:
            (FullTransformerBatch): The extracted features.
        """
        if not any(len(doc) for doc in docs):
            # Handle cases where there are no tokens in any docs.
            activations = FullTransformerBatch.empty(len(docs))
        else:
            activations = self.model.predict(docs)
        return activations

    def __initialize_component(self) -> None:
        """Initialize the component. This avoid the need to call
        nlp.initialize().

        For related issue see:
        https://github.com/explosion/spaCy/issues/7027
        """
        if self.is_initialized:
            return
        self.model.initialize()

        # extract hf model
        hf_model = self.model.layers[0].shims[0]._model
        if self.model_labels is None:
            # extract hf_model.config.label2id.items()
            # convert to sorted list
            self.model_labels = [
                tag[0]
                for tag in sorted(hf_model.config.label2id.items(), key=lambda x: x[1])
            ]
        self.is_initialized = True

    def initialize(
        self,
        get_examples: Callable[[], Iterable[Example]],
        *,
        nlp: Optional[Language] = None,
    ):
        """Initialize the pipe for training, using data examples if available.

        Args:
            get_examples (Callable[[], Iterable[Example]]): Optional function that
                returns gold-standard Example objects.
            nlp (Language): The current nlp object.
        """
        self.__initialize_component()

    def to_disk(
        self, path: Union[str, Path], *, exclude: Iterable[str] = tuple()
    ) -> None:
        """Serialize the pipe to disk.

        Args:
            path (str / Path): Path to a directory.
            exclude (Iterable[str]): String names of serialization fields to exclude.
        """
        serialize = {}
        serialize["cfg"] = lambda p: srsly.write_json(p, self.cfg)
        serialize["vocab"] = self.vocab.to_disk
        serialize["model"] = self.model.to_disk
        util.to_disk(path, serialize, exclude)

    def from_disk(
        self, path: Union[str, Path], *, exclude: Iterable[str] = tuple()
    ) -> "SequenceClassificationTransformer":
        """Load the pipe from disk.

        Args:
            path (str / Path): Path to a directory.
            exclude (Iterable[str]): String names of serialization fields to exclude.

        Returns:
            (Transformer): The loaded object.
        """

        def load_model(p):
            try:
                with open(p, "rb") as mfile:
                    self.model.from_bytes(mfile.read())
            except AttributeError:
                raise ValueError(Errors.E149) from None

        deserialize = {
            "vocab": self.vocab.from_disk,
            "cfg": lambda p: self.cfg.update(deserialize_config(p)),
            "model": load_model,
        }
        util.from_disk(path, deserialize, exclude)
        return self
