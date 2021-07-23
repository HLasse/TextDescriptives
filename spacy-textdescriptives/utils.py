"""Utility functions for calculating various text descriptives"""
from spacy.tokens import Doc
from spacy.language import Language
from pyphen import Pyphen


@Language.factory("utilities")
def create_utils_component(nlp: Language, name: str):
    return Utils(nlp)


class Utils:
    def __init__(self, nlp: Language):
        """Initialise components
        Only calculate n_sentences, n_words, n_syllabes when needed using getters"""
        if not Doc.has_extension("n_sentences"):
            Doc.set_extension("n_sentences", getter=self.n_sentences)

        if not Doc.has_extension("n_words"):
            Doc.set_extension("n_words", getter=self.n_words)

        if not Doc.has_extension("n_syllables"):
            Doc.set_extension("n_syllables", getter=self.n_syllables)

        if not Doc.has_extension("filtered_tokens"):
            Doc.set_extension("filtered_tokens", default=[])

    def __call__(self, doc):
        """Run the pipeline component"""
        doc._.filtered_tokens = self.filtered_tokens(doc)
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

    def n_words(self, doc: Doc):
        """Return number of words in the document."""
        return len(doc._.filtered_tokens)

    def n_syllables(self, doc):
        """
        Return number of syllables per token
        """
        dic = Pyphen(lang=doc.lang_)

        def count_syl(token):
            word_hyphenated = dic.inserted(token.lower_)
            return max(1, word_hyphenated.count("-") + 1)

        return [count_syl(token) for token in doc._.filtered_tokens]

"""
import spacy
nlp = spacy.load('da_core_news_sm')
nlp.add_pipe("utilities", last=True)

doc = nlp("Det her er en testsætning. Her er sætning nummer 2")

for sent_i, sent in enumerate(doc.sents):
    for token in sent:
        print(sent_i, token.i, token.text)
doc._.n_words
doc._.filtered_tokens
doc._.n_sentences
doc._.n_syllables

"""
