"""Calculation of descriptive statistics"""
from spacy.tokens import Doc
from spacy.language import Language

import numpy as np


@Language.factory("descriptive_stats")
def create_descriptive_stats_component(nlp: Language, name: str):
    return DescriptiveStatistics(nlp)


class DescriptiveStatistics:
    def __init__(self, nlp: Language):
        """Initialise components"""
        if not Doc.has_extension("token_length"):
            Doc.set_extension("token_length", getter=self.token_length)

        if not Doc.has_extension("sentence_length"):
            Doc.set_extension("sentence_length", getter=self.sentence_length)

        if not Doc.has_extension("syllables"):
            Doc.set_extension("syllables", getter=self.syllables)

        if not Doc.has_extension("counts"):
            Doc.set_extension("counts", getter=self.counts)

    def __call__(self, doc):
        """Run the pipeline component"""
        return doc

    def token_length(self, doc):
        """Return dict with measures of token length"""
        token_lengths = [len(token) for token in doc._._filtered_tokens]
        return {
            "token_length_mean": np.mean(token_lengths),
            "token_length_median": np.median(token_lengths),
            "token_length_std": np.std(token_lengths),
        }

    def sentence_length(self, doc):
        """Return dict with measures of sentence length"""
        # get length of filtered tokens per sentence
        tokenized_sentences = [
            [
                token.text
                for token in sent
                if not token.is_punct and "'" not in token.text
            ]
            for sent in doc.sents
        ]
        len_sentences = [len(sentence) for sentence in tokenized_sentences]
        return {
            "sentence_length_mean": np.mean(len_sentences),
            "sentence_length_median": np.median(len_sentences),
            "sentence_length_std": np.std(len_sentences),
        }

    def syllables(self, doc):
        """Return dict with measures of syllables per token"""
        n_syllables = doc._._n_syllables
        return {
            "syllables_per_token_mean": np.mean(n_syllables),
            "syllables_per_token_median": np.median(n_syllables),
            "syllables_per_token_std": np.std(n_syllables),
        }

    def counts(self, doc, ignore_whitespace=True):
        n_tokens = doc._._n_tokens
        n_types = len(set([tok.lower_ for tok in doc._._filtered_tokens]))
        if ignore_whitespace:
            n_chars = len(doc.text.replace(" ", ""))
        else:
            n_chars = len(doc.text)
        return {
            "n_tokens": n_tokens,
            "n_unique_tokens": n_types,
            "percent_unique_tokens": n_types / n_tokens,
            "n_sentences": doc._._n_sentences,
            "n_characters": n_chars,
        }
