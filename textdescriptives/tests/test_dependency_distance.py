import spacy
import pytest
from textdescriptives.components import DependencyDistance
from .books import *
import numpy as np
import ftfy


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("dependency_distance")
    return nlp


def test_dependency_distance_integration(nlp):
    assert "dependency_distance" == nlp.pipe_names[-1]


def test_dependency_distance(nlp):
    doc = nlp("This is a short and simple sentence")
    assert doc._.dependency_distance
    assert doc[0:3]._.dependency_distance
    assert doc[0]._.dependency_distance


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", np.nan),
        ("#", 0.0),
    ],
)
def test_dependency_distance_edge(text, expected, nlp):
    doc = nlp(text)
    for v in doc._.dependency_distance.values():
        if expected is np.nan:
            assert v is np.nan
        else:
            assert pytest.approx(expected, rel=1e-2) == v


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 3.19),
        (secret_garden, 2.29),
        (flatland, 3.33),
    ],
)
def test_mean_dep_distance(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=0.15)
        == doc._.dependency_distance["dependency_distance_mean"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 1.45),
        (secret_garden, 0.88),
        (flatland, 1.20),
    ],
)
def test_std_dep_distance(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=0.15)
        == doc._.dependency_distance["dependency_distance_std"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 0.395),
        (secret_garden, 0.41),
        (flatland, 0.44),
    ],
)
def test_mean_adj_dep(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=0.1)
        == doc._.dependency_distance["prop_adjacent_dependency_relation_mean"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 0.11),
        (secret_garden, 0.09),
        (flatland, 0.056),
    ],
)
def test_std_adj_dep(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=0.1)
        == doc._.dependency_distance["prop_adjacent_dependency_relation_std"]
    )
