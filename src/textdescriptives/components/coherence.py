from typing import Callable, List

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc


def n_order_coherence(doc: Doc, order: int) -> List[float]:
    """Calculate coherence for a `Doc` for a given order.

    Args:
        doc: A `Doc` object.
        order: The order of coherence to calculate. For example, order=1 will
            calculate the semantic similarity between consecutive sentences. And
            order=2 will calculate the semantic similarity between sentences that
            are two sentences apart.

    Returns:
        A list of floats representing the semantic similarity between sentences
    """

    if not doc.has_annotation("SENT_START"):
        raise ValueError(
            "A sentence boundary detector has not been run on this Doc, which is "
            + "required to calculate coherence. Have you added a model with a "
            + "sentencizer and word vectors to the pipeline?",
        )
    sents = list(doc.sents)
    if len(sents) < order + 1:
        return [np.nan]

    if doc.vector.size == 0:
        raise ValueError(
            "Sentence vectors are not available. Thus it is not possible to "
            + "calculate the coherence between sentences. Please add a component "
            + "that includes word vectors or sentence embeddings."
            + "See https://spacy.io/usage/vectors-similarity for more details.",
        )

    similarities: List[float] = []
    for i, sent in enumerate(sents):
        if i == len(sents) - order:
            break
        similarities.append(sent.similarity(sents[i + order]))
    return similarities


class Coherence:
    """Spacy v.3.0 component that adds attributes with coherence to `Doc` and
    `Span` objects."""

    def __init__(self, nlp: Language):
        """Initialise component."""
        extensions = [
            "first_order_coherence_values",
            "second_order_coherence_values",
            "coherence",
        ]
        for extension in extensions:
            if not Doc.has_extension(extension):
                Doc.set_extension(extension, default=None)

    @staticmethod
    def _first_order_coherence(doc: Doc) -> List[float]:
        """Calculate first order coherence for a `Doc`, i.e. the semantic
        similarity between consecutive sentences."""
        return n_order_coherence(doc=doc, order=1)

    @staticmethod
    def _second_order_coherence(doc: Doc) -> List[float]:
        """Calculate second order coherence for a `Doc`, i.e. the semantic
        similarity between sentences that are two sentences apart."""
        return n_order_coherence(doc, order=2)

    def coherence(self, doc: Doc) -> None:
        """Calculate mean semantic coherence for a `Doc` and set the coherence
        attribute.

        Coherence is calculated by taking the mean of the similarity between
        sentence embeddings. See the documentation for more details.
        """
        first_order_coherence = self._first_order_coherence(doc)
        second_order_coherence = self._second_order_coherence(doc)

        # get mean of coherence values
        if len(first_order_coherence) < 2:
            first_order_coherence_mean = first_order_coherence[0]
        else:
            first_order_coherence_mean = np.nanmean(first_order_coherence)
        if len(second_order_coherence) < 2:
            second_order_coherence_mean = second_order_coherence[0]
        else:
            second_order_coherence_mean = np.nanmean(second_order_coherence)

        # set attributes
        setattr(doc._, "first_order_coherence_values", first_order_coherence)
        setattr(doc._, "second_order_coherence_values", second_order_coherence)
        setattr(
            doc._,
            "coherence",
            {
                "first_order_coherence": first_order_coherence_mean,
                "second_order_coherence": second_order_coherence_mean,
            },
        )

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        self.coherence(doc)
        return doc


@Language.factory(
    "textdescriptives/coherence",
    assigns=[
        "doc._.first_order_coherence_values",
        "doc._.second_order_coherence_values",
        "doc._.coherence",
    ],
)
def create_coherence_component(nlp: Language, name: str) -> Callable[[Doc], Doc]:
    """Allows Coherence to be added to a spaCy pipe using
    nlp.add_pipe("textdescriptives/coherence").

    Adding this component to a pipeline sets the following attributes:
        - doc._.first_order_coherence_values
        - doc._.second_order_coherence_values
        - doc._.coherence

    Args:
        nlp (Language): spaCy language object, does not need to be specified in the
            nlp.add_pipe call.
        name (str): name of the component. Can be optionally specified in the
            nlp.add_pipe call, using the name argument.

    Returns:
        Callable[[Doc], Doc]: The Coherence component to be added to the pipe.

    Examples:
        >>> import spacy
        >>> nlp = spacy.load("en_core_web_md")
        >>> nlp.add_pipe("textdescriptives/coherence")
        >>> # apply the pipeline to a text
        >>> doc = nlp("This is a sentence. This is another sentence.")
        >>> # get coherence values
        >>> doc._.coherence
    """
    return Coherence(nlp)
