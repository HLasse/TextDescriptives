import pytest
import spacy
from spacy.tokens import Doc

import textdescriptives as td  # noqa: F401


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm", disable=("ner", "textcat"))
    nlp.add_pipe("textdescriptives/pos_proportions")

    return nlp


@pytest.fixture(scope="function")
def doc(nlp):
    words = [
        "Here",
        "is",
        "the",
        "first",
        "sentence",
        ".",
        "It",
        "was",
        "pretty",
        "short",
        ".",
        "Let",
        "'s",
        "make",
        "another",
        "one",
        "that",
        "'s",
        "slightly",
        "longer",
        "and",
        "more",
        "complex",
        ".",
    ]
    pos = [
        "ADV",
        "AUX",
        "DET",
        "ADJ",
        "NOUN",
        "PUNCT",
        "PRON",
        "AUX",
        "ADV",
        "ADJ",
        "PUNCT",
        "VERB",
        "PRON",
        "VERB",
        "DET",
        "NOUN",
        "PRON",
        "AUX",
        "ADV",
        "ADJ",
        "CCONJ",
        "ADV",
        "ADJ",
        "PUNCT",
    ]
    doc = Doc(
        nlp.vocab,
        words=words,
        pos=pos,
    )
    return doc


def test_pos_integrations(nlp):
    assert "textdescriptives/pos_proportions" == nlp.pipe_names[-1]


def test_pos_proportions_doc(doc):
    assert doc._.pos_proportions == pytest.approx(
        {
            "pos_prop_ADJ": 0.1666,
            "pos_prop_ADP": 0.0,
            "pos_prop_AUX": 0.125,
            "pos_prop_ADV": 0.1666,
            "pos_prop_CCONJ": 0.0416,
            "pos_prop_DET": 0.083,
            "pos_prop_INTJ": 0.0,
            "pos_prop_NOUN": 0.0833,
            "pos_prop_NUM": 0.0,
            "pos_prop_PART": 0.0,
            "pos_prop_PRON": 0.125,
            "pos_prop_PROPN": 0.0,
            "pos_prop_PUNCT": 0.125,
            "pos_prop_SCONJ": 0.0,
            "pos_prop_SYM": 0.0,
            "pos_prop_VERB": 0.083,
            "pos_prop_X": 0.0,
        },
        rel=0.05,
    )


def test_pos_proportions_span(doc):
    span = doc[:]

    assert span._.pos_proportions == pytest.approx(
        {
            "pos_prop_ADJ": 0.1666,
            "pos_prop_ADP": 0.0,
            "pos_prop_AUX": 0.125,
            "pos_prop_ADV": 0.1666,
            "pos_prop_CCONJ": 0.0416,
            "pos_prop_DET": 0.083,
            "pos_prop_INTJ": 0.0,
            "pos_prop_NOUN": 0.0833,
            "pos_prop_NUM": 0.0,
            "pos_prop_PART": 0.0,
            "pos_prop_PRON": 0.125,
            "pos_prop_PROPN": 0.0,
            "pos_prop_PUNCT": 0.125,
            "pos_prop_SCONJ": 0.0,
            "pos_prop_SYM": 0.0,
            "pos_prop_VERB": 0.083,
            "pos_prop_X": 0.0,
        },
        rel=0.01,
    )


def test_pos_proportions_correct_n_output(doc: Doc):
    assert len(doc._.pos_proportions) == 17
