"""Calculation of statistics that require a pos-tagger in the pipeline"""

from typing import Counter, Union

from spacy.language import Language
from spacy.tokens import Doc, Span


@Language.factory("textdescriptives.pos_proportions", default_config={"use_pos": True})
def create_pos_stats_component(nlp: Language, name: str, use_pos: bool) -> Language:
    """Allows PosPropotions to be added to a spaCy pipe using nlp.add_pipe("textdescriptives.pos_proportions")"""

    tagger = {"tagger", "attribute_ruler"}
    if not tagger.intersection(set(nlp.pipe_names)):
        raise ValueError(
            "The pipeline does not contain a component for POS tagging. Please load a spaCy model which includes a 'tagger' or an 'attribute ruler' component."
        )
    return POSProportions(nlp, use_pos=use_pos)


class POSProportions:
    """spaCy v.3.0 component that adds attributes for POS statistics to `Doc` and `Span` objects."""

    def __init__(self, nlp: Language, use_pos: bool):
        """Initialise components

        Args:
            use_pos: If True, uses the simple POS tag. If False, uses the detailed universal POS tag.
        """
        self.use_pos = use_pos

        if not Doc.has_extension("pos_proportions"):
            Doc.set_extension("pos_proportions", getter=self.pos_proportions)

        if not Span.has_extension("pos_proportions"):
            Span.set_extension("pos_proportions", getter=self.pos_proportions)

    def __call__(self, doc):
        """Run the pipeline component"""
        return doc

    def pos_proportions(self, text: Union[Doc, Span]) -> dict:
        """
        Calculates the proportion of tokens in a `Doc`|`Span` that are tagged with each POS tag.

        Returns:
            Dict containing {pos_prop_POSTAG: proportion of all tokens tagged with POSTAG. Does not create a key if no tokens in the document fit the POSTAG.
        """
        pos_counts = Counter()
        if self.use_pos:
            pos_counts.update([token.pos_ for token in text])
        else:
            pos_counts.update([token.tag_ for token in text])
        pos_proportions = {
            "pos_prop_" + tag: count / len(text) for tag, count in pos_counts.items()
        }

        return pos_proportions
