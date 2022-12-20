import pytest
import spacy

import textdescriptives as td

# pylint: disable=missing-function-docstring


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/all")
    return nlp


def test_extract_df_single_doc(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_df(doc)
    for metric in [
        "descriptive_stats",
        "readability",
        "dependency_distance",
        "quality",
    ]:
        td.extract_df(doc, metrics=metric)


def test_extract_df_pipe(nlp):
    text = [
        "I wonder how well the function works on multiple documents",
        "Very exciting to see, don't you think?",
    ]
    docs = nlp.pipe(text)
    td.extract_df(docs)


def test_extract_df_subsetters(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    df = td.extract_df(doc, include_text=False)
    assert "token_length_mean" not in df[td.readability_cols].columns
    assert "token_length_mean" not in df[td.dependency_cols].columns
    assert "lix" not in df[td.descriptive_stats_cols].columns


def test_extract_df_error(nlp):
    doc = nlp("Very brief text")

    with pytest.raises(Exception):
        td.extract_df("This is just a string")
    with pytest.raises(Exception):
        td.extract_df(doc, metrics="not a metric")
    with pytest.raises(Exception):
        td.extract_df(doc, metrics=True)


def test_extract_dict_single_doc(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_dict(doc)
    for metric in ["descriptive_stats", "readability", "dependency_distance"]:
        td.extract_dict(doc, metrics=metric)


def test_extract_df_pipe_specific_value(nlp):
    text = [
        "I wonder how well the function works on multiple documents",
        "Very exciting to see, don't you think?",
    ]
    docs = nlp.pipe(text)
    assert len(td.extract_dict(docs)["token_length_mean"]) == 2


def test_extract_df_only_pos():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/pos_proportions")

    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_df(doc)
