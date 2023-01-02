import pytest
import spacy
import textdescriptives as td  # noqa: F401


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/all")
    return nlp


def test_integration(nlp):
    assert nlp.pipe_names[-1] == "textdescriptives/all"
    for component in [
        "textdescriptives/descriptive_stats",
        "textdescriptives/readability",
        "textdescriptives/dependency_distance",
        "textdescriptives/all",
        "textdescriptives/quality",
        "textdescriptives/pos_proportions",
    ]:
        assert component in nlp.pipe_names


def test_simple(nlp):
    doc = nlp("This is a short and simple text")
    assert doc
