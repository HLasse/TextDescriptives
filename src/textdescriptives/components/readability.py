""" Calculation of various readability metrics."""

from typing import Callable, Dict

import numpy as np
from spacy.language import Language
from spacy.tokens import Doc
from wasabi import msg

from .descriptive_stats import (  # noqa
    create_descriptive_stats_component,
    language_exists_in_pyphen,
)
from .utils import filter_tokens


class Readability:
    """spaCy v.3.0 component for adding readability metrics to `Doc` objects.

    Extracts metrics and returns them as a dictionary as the ._.readability
    attribute.
    """

    def __init__(self, nlp: Language):
        """Initialise components."""
        self.can_calculate_syllables = language_exists_in_pyphen(lang=nlp.lang)

        if not Doc.has_extension("readability"):
            Doc.set_extension("readability", getter=self.readability)

    def _flesch_reading_ease(self, doc: Doc):
        """Calculate the Flesch Reading Ease score for a document. The equation
        for the Flesch Reading Ease score is:

        206.835 - (1.015 X avg sent len) - (84.6 * avg_syl_per_word)

        Higher = easier to read
        """
        if not self.can_calculate_syllables:
            return np.nan

        avg_sentence_length = doc._.sentence_length["sentence_length_mean"]
        avg_syl_per_word = doc._.syllables["syllables_per_token_mean"]
        if avg_sentence_length == 0 or avg_syl_per_word == 0:
            return np.nan
        score = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syl_per_word)
        return score

    def _flesch_kincaid_grade(self, doc: Doc):
        """Calculate the Flesch-Kincaid grade of the document. The equation for
        the Flesch-Kincaid grade is:

        0.39 * (avg sent len) + 11.8 * (avg_syl_per_word) - 15.59
        """
        if not self.can_calculate_syllables:
            return np.nan

        avg_sentence_length = doc._.sentence_length["sentence_length_mean"]
        avg_syl_per_word = doc._.syllables["syllables_per_token_mean"]
        if avg_sentence_length == 0 or avg_syl_per_word == 0:
            return np.nan
        score = 0.39 * avg_sentence_length + 11.8 * avg_syl_per_word - 15.59
        return score

    def _smog(self, doc: Doc, n_hard_words: int):
        """Calculate the SMOG index of the document. The equation for the SMOG index
        is:

        1.043( sqrt(30 * (hard words /n sentences)) + 3.1291

        Where hard words are words with 3 or more syllables.
        Preferably need 30+ sentences. Will not work with less than 4
        """
        if not self.can_calculate_syllables:
            return np.nan

        n_sentences = doc._._n_sentences
        if n_sentences >= 3:
            smog = (1.043 * (30 * (n_hard_words / n_sentences)) ** 0.5) + 3.1291
            return smog
        return np.nan

    def _gunning_fog(self, doc, n_hard_words: int):
        """Calculates the Gunning Fog index of the document. The equation for
        the Gunning Fog index is:

        Grade level = 0.4 * ((avg_sentence_length) + (percentage hard words))

        Where hard words are word with 3 or more syllables.
        """
        if not self.can_calculate_syllables:
            return np.nan

        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        avg_sent_len = doc._.sentence_length["sentence_length_mean"]
        percent_hard_words = (n_hard_words / n_tokens) * 100
        return 0.4 * (avg_sent_len + percent_hard_words)

    def _automated_readability_index(self, doc: Doc):
        """Calculates the Automated Readability Index of the document. The
        equation for the Automated Readability Index is:

        4.71 * (n_chars / n_words) + 0.5 * (n_words / n_sentences) - 21.43

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
        """Calculates the Colmean-Liau index of the document. The equation for
        the Coleman-Liau index is:

        score = 0.0588 * avg number of chars pr 100 words - 0.296 * avg num of sents pr
        100 words -15.8

        Score = grade required to read the text
        """
        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        lengths = doc._.token_length["token_length_mean"] * 100
        s = (doc._._n_sentences / n_tokens) * 100
        return 0.0588 * lengths - 0.296 * s - 15.8

    def _lix(self, doc: Doc, long_words: int):
        """Calculates the LIX index of the document. The equation for the LIX index
        is:

        (n_words / n_sentences) + (n_words longer than 6 characters * 100) / n_words
        """
        n_tokens = doc._._n_tokens
        if n_tokens == 0:
            return np.nan
        percent_long_words = long_words / n_tokens * 100
        return doc._.sentence_length["sentence_length_mean"] + percent_long_words

    def _rix(self, doc: Doc, long_words: int):
        """Calculates the RIX index of the document. The equation for the RIX index
        is:

        (n_words longer than 6 characters / n_sentences)
        """
        n_sentences = doc._._n_sentences
        if doc._._n_tokens == 0:
            return np.nan
        return long_words / n_sentences

    def readability(self, doc: Doc) -> Dict[str, float]:
        """Apply readability functions and return a dict of the results."""
        hard_words = (
            len([syllable for syllable in doc._._n_syllables if syllable >= 3])
            if self.can_calculate_syllables
            else 0
        )
        long_words = len([t for t in filter_tokens(doc) if len(t) > 6])

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

    def __call__(self, doc: Doc):
        """Run the pipeline component."""
        return doc


@Language.factory(
    "textdescriptives/readability",
    assigns=["doc._.readability"],
    default_config={"verbose": False},
)
def create_readability_component(
    nlp: Language,
    name: str,
    verbose: bool,
) -> Callable[[Doc], Doc]:
    """Allows Readability to be added to a spaCy pipe using
    nlp.add_pipe("textdescriptives/readability").

    Readability requires attributes from DescriptiveStatistics and adds
    it to the pipe if it not already loaded.

    Adding this component to a pipeline sets the following attributes:
        - doc._.readability

    Args:
        nlp (Language): spaCy language object, does not need to be specified in the
            nlp.add_pipe call.
        name (str): name of the component. Can be optionally specified in the
            nlp.add_pipe call, using the name argument.
        verbose (bool): Toggle to show a message if the
            "textdescriptives/descriptive_stats" component is added to the pipeline.
            Defaults to True.

    Returns:
        Callable[[Doc], Doc]: The Readability component

    Example:
        >>> import spacy
        >>> import textdescriptives as td
        >>> nlp = spacy.blank("en")
        >>> nlp.add_pipe("textdescriptives/readability")
        >>> # apply the pipeline to a document
        >>> doc = nlp("This is a test document.")
        >>> doc._.readability
    """
    if "textdescriptives/descriptive_stats" not in nlp.pipe_names:
        if verbose:
            msg.info(  # pylint: disable=logging-not-lazy
                "'textdescriptives/descriptive_stats' component is required for"
                + " 'textdescriptives.readability'. Adding to pipe.",
            )
        nlp.add_pipe("textdescriptives/descriptive_stats")
    return Readability(nlp)
