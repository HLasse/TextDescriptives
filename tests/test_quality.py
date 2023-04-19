""" Tests for the quality module."""

from typing import List, Tuple

import pytest
import spacy

import textdescriptives as td
from textdescriptives.components.quality import (
    alpha_ratio,
    duplicate_ngram_fraction,
    mean_word_length,
    n_stop_words,
    oov_ratio,
    proportion_bullet_points,
    proportion_ellipsis,
    symbol_to_word_ratio,
    top_ngram_chr_fraction,
)


@pytest.fixture
def nlp():
    """Load a blank English model."""
    return spacy.blank("en")


@pytest.mark.parametrize(
    "text, stop_words",
    [
        ("", 0),
        ("This is a test.", 3),
        ("This is a test. This is a test.", 6),
    ],
)
def test_n_stop_words(text: str, stop_words: int, nlp: spacy.Language):
    """Test the n_stop_words function."""
    doc = nlp(text)
    assert n_stop_words(doc) == stop_words


# test mean word length
@pytest.mark.parametrize(
    "text, mean_length",
    [
        ("", 0),
        ("This is a test.", 2.4),
        ("This is a test. This is a test.", 2.4),
    ],
)
def test_mean_word_length(text: str, mean_length: float, nlp: spacy.Language):
    """Test the mean_word_length function."""
    doc = nlp(text)
    assert mean_word_length(doc) == mean_length


# test alpha ratio
@pytest.mark.parametrize(
    "text, alpha",
    [
        ("", 0),
        ("This is a test.", 0.8),
        ("This,, is a test. 12355 is €%&/( a <<s.", 0.38),
        ("This is a test. This is a test. 123", 0.72),
    ],
)
def test_alpha_ratio(text: str, alpha: float, nlp: spacy.Language):
    """Test the alpha_ratio function."""
    doc = nlp(text)
    assert abs(alpha_ratio(doc) - alpha) < 0.01


# test proportion bullet points
@pytest.mark.parametrize(
    "text, bullet_points",
    [
        ("", 0),
        ("- This is a test.", 1),
        ("- This is a test. \nThis is a test.", 0.5),
        ("* This is a test.", 1),
    ],
)
def test_proportion_bullet_points(text: str, bullet_points: float, nlp: spacy.Language):
    """Test the proportion_bullet_points function."""
    doc = nlp(text)
    assert abs(proportion_bullet_points(doc) - bullet_points) < 0.01


# test proportion ellipsis
@pytest.mark.parametrize(
    "text, ellipsis",
    [
        ("", 0),
        ("This is a test...", 1),
        ("This is a test. \nThis is a test...", 0.5),
    ],
)
def test_proportion_ellipsis(text: str, ellipsis: float, nlp: spacy.Language):
    """Test the proportion_ellipsis function."""
    doc = nlp(text)
    assert proportion_ellipsis(doc) == ellipsis


# test symbol to word ratio
@pytest.mark.parametrize(
    "text, symbol_to_word",
    [
        ("", 0),
        ("This is a test.", 0),
        ("# test symbol to word ratio", 0.2),
        ("#### test symbol to word ratio", 0.8),
    ],
)
def test_symbol_to_word_ratio(text: str, symbol_to_word: float, nlp: spacy.Language):
    """Test the symbol_to_word_ratio function."""
    doc = nlp(text)
    assert abs(symbol_to_word_ratio(doc, symbol="#") - symbol_to_word) < 0.01


# test duplicate ngram fraction
@pytest.mark.parametrize(
    "text, duplicate_ngram, ngram_range",
    [
        ("", (0, 0), (2, 3)),
        ("This is a test.", (0, 0), (2, 3)),
        ("This is a test. This is a test.", (1,), (2, 2)),
        ("This is a test. This is a test.", (1, 1), (2, 3)),
        ("This is a test. This is a test. This is not a test.", (0.90, 0.90), (2, 3)),
        (
            "This is a test. This is maybe a test. This is not a test.",
            (0.789, 0.649),
            (2, 3),
        ),
        ("This is a test. This is a test. This is a test.", (1,), (3, 3)),
        ("This is a test. This is a test. This is a test.", (1, 1, 1, 1), (2, 5)),
        ("This is a test, where there is no duplicate ngram.", (0, 0), (2, 3)),
        ("This is a test. This is a test.", (0,), (8, 8)),
    ],
)
def test_duplicate_ngram_chr_fraction(
    text: str,
    duplicate_ngram: List[float],
    ngram_range: Tuple[int, int],
    nlp: spacy.Language,
):
    """Test the duplicate_ngram_fraction function."""
    doc = nlp(text)
    d = duplicate_ngram_fraction(doc, ngram_range=ngram_range)
    assert d, "duplicate_ngram_fraction should not be empty"
    for i, j in zip(d, duplicate_ngram):  # , strict=True): # for python >3.10
        assert abs(d[i] - j) < 0.01


# test top ngram chr fraction
@pytest.mark.parametrize(
    "text, top_ngram_chr_frac, ngram_range",
    [
        ("", (0, 0), (2, 3)),
        ("This is a test.", (0.466, 0.6), (2, 3)),
        ("This is a test. This is a monkey", (0.437, 0.562, 0.437), (2, 4)),
        (
            "This is a test. This is a monkey. This is a star.",
            (0.428, 0.551, 0.449),
            (2, 4),
        ),
    ],
)
def test_top_ngram_chr_fraction(
    text: str,
    top_ngram_chr_frac: List[float],
    ngram_range: Tuple[int, int],
    nlp: spacy.Language,
):
    """Test the top_ngram_chr_fraction function."""
    doc = nlp(text)
    top_ngram_fractions = top_ngram_chr_fraction(doc, ngram_range=ngram_range)
    for i, j in zip(top_ngram_fractions.values(), top_ngram_chr_frac):
        assert abs(i - j) < 0.01


def test_quality_component(nlp: spacy.Language):
    """Test the quality component."""
    nlp.add_pipe("textdescriptives/quality", config={"force": True})
    doc = nlp("This is a test. This is a test. This is a test.")
    quality = doc._.quality
    assert quality.n_stop_words == 9
    assert quality.mean_word_length == 2.4
    assert quality.alpha_ratio == 0.8
    assert quality.proportion_bullet_points == 0
    assert quality.proportion_ellipsis == 0
    assert quality.symbol_to_word_ratio["#"] == 0
    assert quality.duplicate_ngram_chr_fraction["5"] == 1
    assert abs(quality.top_ngram_chr_fraction["2"].value - 0.44) < 0.01
    assert doc._.passed_quality_check is False
    assert quality.oov_ratio.value is None
    assert quality.passed is False


def test_quality_component_with_config(nlp: spacy.Language):
    """Test the quality component with config."""
    quality_thresholds = td.QualityThresholds(
        n_stop_words=(3, None),
        alpha_ratio=(None, 0.8),
        mean_word_length=(1, 10),
        doc_length=(10, 100_000),
        symbol_to_word_ratio={".": (None, 0.3)},
        proportion_ellipsis=(None, 0.3),
        proportion_bullet_points=(None, 0.8),
        duplicate_line_chr_fraction=(None, 0.2),
        duplicate_paragraph_chr_fraction=(None, 0.2),
        top_ngram_chr_fraction={2: (None, 0.6), 3: (None, 0.6)},
        duplicate_ngram_chr_fraction={},
        contains={"lorem ipsum": False},
        oov_ratio=(None, 0.3),
    )

    quality_pipe = nlp.add_pipe(
        "textdescriptives/quality",
        config={
            "symbols": ["."],
            "force": True,
        },
    )
    quality_pipe.set_quality_thresholds(quality_thresholds)

    doc = nlp("This is a test. This is a test. This is a test.")
    assert doc._.quality.n_stop_words == 9
    assert doc._.quality.mean_word_length == 2.4
    assert doc._.quality.alpha_ratio == 0.8
    assert doc._.quality.proportion_bullet_points == 0
    assert doc._.quality.proportion_ellipsis == 0
    assert doc._.quality.symbol_to_word_ratio["."] == 0.25
    assert doc._.quality.duplicate_ngram_chr_fraction["5"] == 1
    assert doc._.quality.duplicate_ngram_chr_fraction["8"] == 1
    assert abs(doc._.quality.top_ngram_chr_fraction["3"].value - 0.57) < 0.01
    assert doc._.passed_quality_check is True
    assert doc._.quality.oov_ratio.value is None


@pytest.mark.parametrize(
    "text, passed",
    [
        ("", False),
        (
            "This is a reasonable text, which has a very good sentence structure and "
            + "will therefore pass the quality check.",
            True,
        ),
        (
            "This is repitious text, This is repitious text, This is repitious text.",
            False,
        ),
        ("This test has many symbols #!@#$%^&*()_+.", False),
        ("- this is a text of \n - bullet points", False),
        ("", False),  # test that it handles empty strings
    ],
)
def test_passed_quality_check(text: str, passed: bool, nlp: spacy.Language):
    """Test the passed_quality_check attribute."""
    nlp.add_pipe("textdescriptives/quality", config={"force": True})
    doc = nlp(text)
    assert doc._.passed_quality_check == passed


def test_quality_multi_process(nlp):
    texts = [
        "A couple of texts here, yeah yeah yeah.",
        "This is a second text, no repetition what so ever.",
    ]
    nlp.add_pipe("textdescriptives/quality", config={"force": True})
    docs = nlp.pipe(texts, n_process=2)
    for doc in docs:
        assert doc._.quality


@pytest.mark.parametrize(
    "text,expected,vocab",
    [
        ("This is a test", 0, None),
        ("This is a nonwrod", 0.25, None),
        ("This is a test", 0, {"This", "is", "a", "test"}),
        ("This is a nonwrod", 0.25, {"This", "is", "a", "test"}),
    ],
)
def test_oov_ratio(text, expected, vocab):
    """Test the oov_ratio function."""
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)
    assert oov_ratio(doc, vocab) == expected


def test_oov_ratio_small_model():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/quality")
    doc = nlp("This is a test")
    assert doc._.quality.oov_ratio.value is None
