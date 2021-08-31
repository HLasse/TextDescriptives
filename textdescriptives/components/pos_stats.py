"""Calculation of statistics that require a pos-tagger in the pipeline"""

from spacy.tokens import Doc, Span
from spacy.language import Language
from typing import Counter

from .utils import filtered_tokens

@Language.factory("pos_stats")
def create_pos_stats_component(nlp: Language, name: str):
    """Allows PosStats to be added to a spaCy pipe using nlp.add_pipe("pos_stats").
    If the pipe does not contain a tagger, is is silently added."""

    tagger = set(["tagger"])
    if not tagger.intersection(set(nlp.pipe_names)):
        nlp.add_pipe("tagger")  # add a tagger if not one in pipe
    return POSStatistics(nlp)

class POSStatistics:
    """spaCy v.3.0 component that adds attributes for POS statistics to `Doc` and `Span` objects.
    """

    def __init__(self, nlp: Language):
        """Initialise components"""

        extensions = [
            "pos_proportions",
        ]
        ext_funs = [
            self.pos_proportions,
        ]
        
        # Unsure about how much of the below tooling code to keep; depends on whether we'll extend pos_stats in the future
        for ext, fun in zip(extensions, ext_funs): 
            if ext not in ["_n_sentences", "sentence_length", "syllables"]:
                if not Span.has_extension(ext):
                    Span.set_extension(ext, getter=fun)
            if not Doc.has_extension(ext):
                Doc.set_extension(ext, getter=fun)

        if not Doc.has_extension("_filtered_tokens"):
            Doc.set_extension("_filtered_tokens", default=[])
        if not Span.has_extension("_filtered_tokens"):
            Span.set_extension("_filtered_tokens", getter=filtered_tokens)

    def __call__(self, doc):
        """Run the pipeline component"""
        doc._._filtered_tokens = filtered_tokens(doc)
        return doc

    def pos_proportions(self, doc: Doc) -> dict:
        """
            Returns:
                Dict with proportions of part-of-speech tag in doc.
        """
        pos_counts = Counter()
    
        pos_counts.update([token.tag_ for token in doc])

        pos_proportions = {tag : pos_counts[tag] / sum(pos_counts.values()) for tag in pos_counts}

        return pos_proportions
