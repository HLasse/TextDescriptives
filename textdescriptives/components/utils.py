"""
Utility functions for calculating various text descriptives
"""
from typing import Any, Callable, Union

from pyphen import Pyphen
from spacy.tokens import Doc, Span, Token


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
    return len(doc._._filtered_tokens)  # pylint: disable=protected-access


def n_syllables(doc: Doc):
    """
    Return number of syllables per token
    """

    dic = Pyphen(lang=doc.lang_)

    def count_syl(token: Token):
        word_hyphenated = dic.inserted(token.lower_)
        return max(1, word_hyphenated.count("-") + 1)

    return [
        count_syl(token)
        for token in doc._._filtered_tokens  # pylint: disable=protected-access
    ]


def span_getter_to_token_getter(
    span_getter: Callable[[Span], Any]
) -> Callable[[Token], Any]:
    """Converts a span getter to a token getter.

    Args:
        span_getter (Callable[[Span], Any]):
            The span getter function.

    Returns:
        Callable[[Token], Any]: The token getter function.
    """

    def token_getter(token):
        return span_getter(token.doc[token.i : token.i + 1])

    return token_getter


def span_getter_to_doc_getter(
    span_getter: Callable[[Span], Any]
) -> Callable[[Doc], Any]:
    """Converts a span getter to a document getter.

    Args:
        span_getter (Callable[[Span], Any]):
            The span getter function.

    Returns:
        Callable[[Doc], Any]: The document getter function.
    """

    def doc_getter(doc):
        return span_getter(doc[:])

    return doc_getter
