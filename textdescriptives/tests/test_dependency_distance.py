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


@pytest.mark.parametrize("text", ["", "#"])
def test_dependency_distance_edge(text, nlp):
    doc = nlp(text)
    for v in doc._.dependency_distance.values():
        v is np.nan


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 3.19),
        (secret_garden, 2.32),
        (flatland, 3.42),
    ],
)
def test_mean_dep_distance(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2)
        == doc._.dependency_distance["dependency_distance_mean"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 1.24),
        (secret_garden, 0.85),
        (flatland, 1.11),
    ],
)
def test_std_dep_distance(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2)
        == doc._.dependency_distance["dependency_distance_std"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 0.41),
        (secret_garden, 0.42),
        (flatland, 0.45),
    ],
)
def test_mean_adj_dep(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2)
        == doc._.dependency_distance["prop_adjacent_dependency_relation_mean"]
    )


@pytest.mark.parametrize(
    "text,expected",
    [
        (oliver_twist, 0.068),
        (secret_garden, 0.098),
        (flatland, 0.056),
    ],
)
def test_std_adj_dep(text, expected, nlp):
    text = ftfy.fix_text(text)
    text = " ".join(text.split())
    doc = nlp(text)
    assert (
        pytest.approx(expected, rel=1e-2)
        == doc._.dependency_distance["prop_adjacent_dependency_relation_std"]
    )
