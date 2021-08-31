"""Calculation of statistics that require a pos-tagger in the pipeline"""

from spacy.tokens import Doc, Span
from spacy.language import Language
from typing import Counter

from .utils import filtered_tokens

@Language.factory("pos_stats")
def create_pos_stats_component(nlp: Language, name: str):
    """Allows PosStats to be added to a spaCy pipe using nlp.add_pipe("pos_stats").
    If the pipe does not contain a tagger, it is silently added."""

    tagger = set(["tagger"])
    if not tagger.intersection(set(nlp.pipe_names)):
        nlp.add_pipe("tagger")  # add a tagger if not one in pipe
    return POSStatistics(nlp)

class POSStatistics:
    """spaCy v.3.0 component that adds attributes for POS statistics to `Doc` and `Span` objects.
    """

    def __init__(self, nlp: Language):
        """Initialise components"""
        if not Doc.has_extension("pos_proportions"):
            Doc.set_extension("pos_proportions", getter=self.pos_proportions)
 

    def __call__(self, doc):
        """Run the pipeline component"""
        return doc

    def pos_proportions(self, doc: Doc) -> dict:
        """
            Returns:
                Dict with proportions of part-of-speech tag in doc.
        """
        pos_counts = Counter()
        pos_counts.update([token.tag_ for token in doc])
        pos_proportions = {"pos_prop_" + tag : pos_counts[tag] / sum(pos_counts.values()) for tag in pos_counts}

        return pos_proportions
