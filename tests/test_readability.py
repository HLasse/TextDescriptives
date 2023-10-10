import warnings

import ftfy
import numpy as np
import pytest
import spacy
from spacy.lang.en import English

from textdescriptives.utils import _remove_textdescriptives_extensions  # noqa: F401

from .books import (
    flatland,
    grade_1,
    grade_2,
    grade_3,
    grade_4,
    grade_6,
    grade_8,
    grade_10,
    grade_12,
    grade_14,
    oliver_twist,
    secret_garden,
)


@pytest.fixture(scope="function")
def nlp():
    nlp = English()
    nlp.add_pipe("textdescriptives/readability")
    return nlp


def test_readability_integration(nlp):
    assert "textdescriptives/readability" == nlp.pipe_names[-1]


def test_readability(nlp):
    doc = nlp("This is a short and simple sentence")
    assert doc._.readability


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", np.nan),
        ("#", np.nan),
    ],
)
def test_readability_edge(text, expected, nlp):
    doc = nlp(text)

    with warnings.catch_warnings():
        warnings.simplefilter("error")

        if np.isnan(expected):
            for v in doc._.readability.values():
                assert np.isnan(v)
        else:
            for v in doc._.readability.values():
                assert v == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 72.80),
        (secret_garden, 92.73),
        (flatland, 68.18),
        (grade_1, 116.08),
        (grade_2, 98.18),
        (grade_3, 101.51),
        (grade_4, 102.08),
        (grade_6, 97.96),
        (grade_8, 91.68),
        (grade_10, 76.67),
        (grade_12, 73.72),
        (grade_14, 65.25),
    ],
)
def test_flesch_reading_ease(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["flesch_reading_ease"]


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 9.48),
        (secret_garden, 4.04),
        (flatland, 12.05),
        (grade_1, -1.65),
        (grade_2, 1.85),
        (grade_3, 1.65),
        (grade_4, 1.20),
        (grade_6, 2.63),
        (grade_8, 4.99),
        (grade_10, 6.75),
        (grade_12, 6.42),
        (grade_14, 10.04),
    ],
)
def test_flesch_kincaid_grade(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2) == doc._.readability["flesch_kincaid_grade"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 9.47),
        (secret_garden, 6.63),
        (flatland, 9.91),
    ],
)
def test_smog(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["smog"]


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 12.19),
        (secret_garden, 6.98),
        (flatland, 15.05),
    ],
)
def test_gunning_fog(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["gunning_fog"]


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 11.99),
        (secret_garden, 5.40),
        (flatland, 14.98),
    ],
)
def test_automated_readability_index(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2)
        == doc._.readability["automated_readability_index"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 8.75),
        (secret_garden, 6.39),
        (flatland, 7.91),
    ],
)
def test_coleman_liau_index(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["coleman_liau_index"]


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 42.70),
        (secret_garden, 27.07),
        (flatland, 49.87),
    ],
)
def test_lix(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["lix"]


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 4.37),
        (secret_garden, 1.81),
        (flatland, 5.50),
    ],
)
def test_rix(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert pytest.approx(expected, rel=1e-2) == doc._.readability["rix"]


def test_readability_multi_process(nlp):
    texts = [oliver_twist, secret_garden, flatland]
    texts = [ftfy.fix_text(text) for text in texts]

    docs = nlp.pipe(texts, n_process=3)
    for doc in docs:
        assert doc._.readability


def test_language_not_in_pyphen():
    # need to add this to not inherit the Doc state (so much state!)
    # without it, the test works fine if run alone, but breaks if run with other tests
    _remove_textdescriptives_extensions()

    nlp = spacy.blank("fi")
    nlp.add_pipe("textdescriptives/readability")
    doc = nlp("Tämä on suomenkielinen lause.")

    assert np.isnan(doc._.readability["flesch_reading_ease"])
