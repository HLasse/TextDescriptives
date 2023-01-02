import ftfy
import pytest
from spacy.lang.en import English

from textdescriptives.components import DescriptiveStatistics  # noqa: F401

from .books import flatland, oliver_twist, secret_garden

import warnings


@pytest.fixture(scope="function")
def nlp():
    nlp = English()
    nlp.add_pipe("sentencizer")
    nlp.add_pipe("textdescriptives/descriptive_stats")
    return nlp


def test_descriptive_stats_integration(nlp):
    assert "textdescriptives/descriptive_stats" == nlp.pipe_names[-1]


def test_descriptive_stats(nlp):
    doc = nlp("This is a short and simple sentence")
    assert doc._.token_length
    assert doc._.sentence_length
    assert doc._.syllables
    assert doc._.counts
    assert doc[0:3]._.token_length
    assert doc[0:3]._.counts


def test_token_length(nlp):
    doc = nlp("Gift cats your prey")
    assert doc._.token_length["token_length_mean"] == 4.0
    assert doc._.token_length["token_length_median"] == 4.0
    assert doc._.token_length["token_length_std"] == 0.0
    assert doc[0:2]._.token_length["token_length_mean"] == 4.0
    assert doc[0:2]._.token_length["token_length_median"] == 4.0
    assert doc[0:2]._.token_length["token_length_std"] == 0.0


def test_sentence_length(nlp):
    doc = nlp(
        "Here is the first sentence. It was pretty short. Let's make another one "
        + "that's slightly longer and more complex.",
    )
    assert (
        pytest.approx(6.33, rel=1e-2) == doc._.sentence_length["sentence_length_mean"]
    )
    assert (
        pytest.approx(5.0, rel=1e-3) == doc._.sentence_length["sentence_length_median"]
    )
    assert pytest.approx(2.62, rel=1e-2) == doc._.sentence_length["sentence_length_std"]


def test_syllables_simple(nlp):
    doc = nlp("These words are easy")
    assert doc._.syllables["syllables_per_token_mean"] == 1.0
    assert doc._.syllables["syllables_per_token_median"] == 1.0
    assert doc._.syllables["syllables_per_token_std"] == 0.0


def test_syllables_complex(nlp):
    doc = nlp("This sentence has complicated words in it")
    assert pytest.approx(1.43, rel=1e-2) == doc._.syllables["syllables_per_token_mean"]
    assert pytest.approx(1.0, rel=1e-3) == doc._.syllables["syllables_per_token_median"]
    assert pytest.approx(0.73, rel=1e-2) == doc._.syllables["syllables_per_token_std"]


def test_counts(nlp):
    doc = nlp(
        "Here is the first sentence. It was pretty short. Let's make another one "
        + "that's slightly longer and more complex.",
    )
    assert doc._.counts["n_tokens"] == 19
    assert doc._.counts["n_unique_tokens"] == 19
    assert doc._.counts["proportion_unique_tokens"] == 1.0
    assert doc._.counts["n_characters"] == 94
    assert doc._.counts["n_sentences"] == 3
    assert doc[0:6]._.counts["n_tokens"] == 5
    assert doc[0:6]._.counts["n_unique_tokens"] == 5
    assert doc[0:6]._.counts["proportion_unique_tokens"] == 1.0
    assert doc[0:6]._.counts["n_characters"] == 23


@pytest.mark.parametrize("text", ["", "#"])
def test_descriptive_edge(text, nlp):
    with warnings.catch_warnings():
        warnings.simplefilter("error")

        doc = nlp(text)

        assert doc._.token_length
        assert doc._.sentence_length
        assert doc._.syllables
        assert doc._.counts


def test_descriptive_multi_process(nlp):
    texts = [oliver_twist, secret_garden, flatland]
    texts = [ftfy.fix_text(text) for text in texts]

    docs = nlp.pipe(texts, n_process=3)
    for doc in docs:
        assert doc._.descriptive_stats
