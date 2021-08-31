import spacy
import pytest
from textdescriptives import TextDescriptives


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives")
    return nlp


def test_integration(nlp):
    assert nlp.pipe_names[-1] == "textdescriptives"
    for component in [
        "descriptive_stats",
        "readability",
        "dependency_distance",
        "textdescriptives",
    ]:
        assert component in nlp.pipe_names


def test_simple(nlp):
    doc = nlp("This is a short and simple text")
    assert doc
