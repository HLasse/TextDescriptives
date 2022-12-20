from typing import List

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
    sents = list(doc.sents)
    if len(sents) < order + 1:
        return [np.nan]
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

        Coherence is calculated by taking the mean of the similarity
        between sentence embeddings. See the documentation for more
        details.
        """
        first_order_coherence = self._first_order_coherence(doc)
        second_order_coherence = self._second_order_coherence(doc)

        # get mean of coherence values
        first_order_coherence_mean = np.nanmean(first_order_coherence)
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


@Language.factory("textdescriptives.coherence")
def create_coherence_component(nlp: Language, name: str):
    """Allows Coherence to be added to a spaCy pipe using
    nlp.add_pipe("textdescriptives.coherence").

    If the pipe does not contain a parser or sentencizer, the
    sentencizer component is silently added.
    """
    return Coherence(nlp)
