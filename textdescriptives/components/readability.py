"""Calculation of various readability metrics."""
from textdescriptives.components.utils import n_sentences
from spacy.tokens import Doc
from spacy.language import Language

from typing import Dict
import numpy as np

from .descriptive_stats import create_descriptive_stats_component


@Language.factory("readability")
def create_readability_component(nlp: Language, name: str):
    """Allows Readability to be added to a spaCy pipe using nlp.add_pipe("readability").
    Readability requires attributes from DescriptiveStatistics and adds it to the
    pipe if it not already loaded."""
    if "descriptive_stats" not in nlp.pipe_names:
        print(
            "'descriptive_stats' component is required for 'readability'. Adding to pipe."
        )
        nlp = nlp.add_pipe("descriptive_stats")
    return Readability(nlp)


class Readability:
    """spaCy v.3.0 component for adding readability metrics to `Doc` objects.
    Extracts metrics and returns them as a dictionary as the ._.readability attribute.
    """

    def __init__(self, nlp: Language):
        """Initialise components"""
        if not Doc.has_extension("readability"):
            Doc.set_extension("readability", getter=self.readability)

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        return doc

    def readability(self, doc: Doc) -> Dict[str, float]:
        """Apply readability functions and return a dict of the results."""
        hard_words = len([syllable for syllable in doc._._n_syllables if syllable >= 3])
        long_words = len([t for t in doc._._filtered_tokens if len(t) > 6])

        return {
            "flesch_reading_ease": self._flesch_reading_ease(doc),
            "flesch_kincaid_grade": self._flesch_kincaid_grade(doc),
            "smog": self._smog(doc, hard_words),
            "gunning_fog": self._gunning_fog(doc, hard_words),
            "automated_readability_index": self._automated_readability_index(doc),
            "coleman_liau_index": self._coleman_liau_index(doc),
            "lix": self._lix(doc, long_words),
            "rix": self._rix(doc, long_words),
        }

    def _flesch_reading_ease(self, doc: Doc):
        """
        206.835 - (1.015 X avg sent len) - (84.6 * avg_syl_per_word)

        Higher = easier to read

        Works best for English
        """
        avg_sentence_length = doc._.sentence_length["sentence_length_mean"]
        avg_syl_per_word = doc._.syllables["syllables_per_token_mean"]
        if avg_sentence_length == 0 or avg_syl_per_word == 0:
            return np.nan
        score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syl_per_word)
        return score

    def _flesch_kincaid_grade(self, doc: Doc):
        """
        Score = grade required to read the text
        """
        avg_sentence_length = doc._.sentence_length["sentence_length_mean"]
        avg_syl_per_word = doc._.syllables["syllables_per_token_mean"]
        if avg_sentence_length == 0 or avg_syl_per_word == 0:
            return np.nan
        score = 0.39 * avg_sentence_length + 11.8 * avg_syl_per_word - 15.59
        return score

    def _smog(self, doc: Doc, hard_words: int):
        """
        grade level = 1.043( sqrt(30 * (hard words /n sentences)) + 3.1291

        Preferably need 30+ sentences. Will not work with less than 4
        """
        n_sentences = doc._._n_sentences
        if n_sentences >= 3:
            smog = (1.043 * (30 * (hard_words / n_sentences)) ** 0.5) + 3.1291
            return smog
        return np.nan

    def _gunning_fog(self, doc, hard_words: int):
        """
        Grade level = 0.4 * ((avg_sentence_length) + (percentage hard words))

        hard words = 3+ syllables
        """
        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        avg_sent_len = doc._.sentence_length["sentence_length_mean"]
        percent_hard_words = (hard_words / n_tokens) * 100
        return 0.4 * (avg_sent_len + percent_hard_words)

    def _automated_readability_index(self, doc: Doc):
        """
        Score = grade required to read the text
        """
        if len(doc) == 0:
            return np.nan
        score = (
            4.71 * doc._.token_length["token_length_mean"]
            + 0.5 * doc._.sentence_length["sentence_length_mean"]
            - 21.43
        )
        return score

    def _coleman_liau_index(self, doc: Doc):
        """
        score = 0.0588 * avg number of chars pr 100 words - 0.296 * avg num of sents pr 100 words -15.8

        Score = grade required to read the text
        """
        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        l = doc._.token_length["token_length_mean"] * 100
        s = (doc._._n_sentences / n_tokens) * 100
        return 0.0588 * l - 0.296 * s - 15.8

    def _lix(self, doc: Doc, long_words: int):
        """
        (n_words / n_sentences) + (n_words longer than 6 letters * 100) / n_words
        """
        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        percent_long_words = long_words / n_tokens * 100
        return doc._.sentence_length["sentence_length_mean"] + percent_long_words

    def _rix(self, doc: Doc, long_words: int):
        """n_long_words / n_sentences"""
        n_sentences = doc._._n_sentences
        if doc._._n_tokens == 0:
            return np.nan
        return long_words / n_sentences
