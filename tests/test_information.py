import numpy as np
import pytest
import spacy

import textdescriptives as td
from textdescriptives.components.information_theory import (
    entropy_getter,
    per_word_perplexity_getter,
    perplexity_getter,
    set_lexeme_prob_table,
)
from textdescriptives.utils import _remove_textdescriptives_extensions


@pytest.fixture
def nlp():
    nlp = spacy.blank("en")
    return nlp


def test_unigram_information_metrics(nlp):  # noqa F811
    set_lexeme_prob_table(nlp.vocab, verbose=True)
    doc1 = nlp("This is a very likely sentence.")
    doc2 = nlp("This is a unlikely sentence sadsatrsxss.")

    assert doc1[0].prob != -20, "lexeme_prob table not loaded."
    assert perplexity_getter(doc1) > perplexity_getter(doc2)
    assert per_word_perplexity_getter(doc1) > per_word_perplexity_getter(doc2)
    assert entropy_getter(doc1) > entropy_getter(doc2)


def test_extract_df(nlp):  # noqa F811
    _remove_textdescriptives_extensions()
    nlp.add_pipe("textdescriptives/information_theory")
    doc = nlp("This is a very likely sentence.")

    df = td.extract_df(doc)
    for col in ["perplexity", "per_word_perplexity", "entropy"]:
        assert col in df.columns


def test_language_no_lexeme_prob_table():
    nlp = spacy.blank("hr")
    nlp.add_pipe("textdescriptives/information_theory")
    doc = nlp("Ez egy magyar mondat.")

    assert np.isnan(doc._.perplexity)
