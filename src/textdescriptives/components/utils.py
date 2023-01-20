"""Utility functions for calculating various text descriptives."""
from typing import Union

from spacy.tokens import Doc, Span, Token
from wasabi import msg

pyphen_warning_raised = False


def filter_tokens(doc: Union[Doc, Span]):
    """Return words in document or span.

    Filters punctuation and words that start with an apostrophe
    (contractions)
    """
    filtered_tokens = [
        word for word in doc if not word.is_punct and "'" not in word.text
    ]
    return filtered_tokens


def n_sentences(doc: Doc):
    """Return number of sentences in the document."""
    return len(list(doc.sents))


def n_tokens(doc: Union[Doc, Span]):
    """Return number of words in the document."""
    return len(filter_tokens(doc))


def n_syllables(doc: Doc):
    """Return number of syllables per token."""

    try:
        from pyphen import Pyphen
    except ImportError:
        if pyphen_warning_raised:
            return None
        msg.warn(
            "Pyphen which is used to calculate n_syllables is not installed."
            + "n_syllables will be set to None. To install pyphen with textdescriptives"
            + "run: pip install textdescriptives[all]",
        )
        return None
    dic = Pyphen(lang=doc.lang_)

    def count_syl(token: Token):
        word_hyphenated = dic.inserted(token.lower_)
        return max(1, word_hyphenated.count("-") + 1)

    return [count_syl(token) for token in filter_tokens(doc)]
