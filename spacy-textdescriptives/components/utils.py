"""Utility functions for calculating various text descriptives"""
from spacy.tokens import Doc
from spacy.tokens import Token
from spacy.language import Language
from pyphen import Pyphen


@Language.factory("utilities")
def create_utils_component(nlp: Language, name: str):
    return Utils(nlp)


class Utils:
    def __init__(self, nlp: Language):
        """Initialise components
        Only calculate n_sentences, n_words, n_syllables when needed using getters"""
        if not Doc.has_extension("_n_sentences"):
            Doc.set_extension("_n_sentences", getter=self.n_sentences)

        if not Doc.has_extension("_n_tokens"):
            Doc.set_extension("_n_tokens", getter=self.n_tokens)

        if not Doc.has_extension("_n_syllables"):
            Doc.set_extension("_n_syllables", getter=self.n_syllables)

        if not Doc.has_extension("_filtered_tokens"):
            Doc.set_extension("_filtered_tokens", default=[])

    def __call__(self, doc: Doc):
        """Run the pipeline component"""
        doc._._filtered_tokens = self.filtered_tokens(doc)
        return doc

    def filtered_tokens(self, doc: Doc):
        """Return words in document.
        Filters punctuation and words that start with an apostrophe (contractions)"""
        filtered_tokens = [
            word for word in doc if not word.is_punct and "'" not in word.text
        ]
        return filtered_tokens

    def n_sentences(self, doc: Doc):
        """Return number of sentences in the document"""
        return len(list(doc.sents))

    def n_tokens(self, doc: Doc):
        """Return number of words in the document."""
        return len(doc._._filtered_tokens)

    def n_syllables(self, doc: Doc):
        """
        Return number of syllables per token
        """
        dic = Pyphen(lang=doc.lang_)

        def count_syl(token: Token):
            word_hyphenated = dic.inserted(token.lower_)
            return max(1, word_hyphenated.count("-") + 1)

        return [count_syl(token) for token in doc._._filtered_tokens]
