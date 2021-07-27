"""Utility functions for calculating various text descriptives"""
from spacy.tokens import Doc, Span, Token
from pyphen import Pyphen

from typing import Union


def filtered_tokens(doc: Union[Doc, Span]):
    """Return words in document or span.
    Filters punctuation and words that start with an apostrophe (contractions)"""
    filtered_tokens = [
        word for word in doc if not word.is_punct and "'" not in word.text
    ]
    return filtered_tokens


def n_sentences(doc: Union[Doc, Span]):
    """Return number of sentences in the document"""
    return len(list(doc.sents))


def n_tokens(doc: Union[Doc, Span]):
    """Return number of words in the document."""
    return len(doc._._filtered_tokens)


def n_syllables(doc: Doc):
    """
    Return number of syllables per token
    """

    dic = Pyphen(lang=doc.lang_)

    def count_syl(token: Token):
        word_hyphenated = dic.inserted(token.lower_)
        return max(1, word_hyphenated.count("-") + 1)

    return [count_syl(token) for token in doc._._filtered_tokens]
