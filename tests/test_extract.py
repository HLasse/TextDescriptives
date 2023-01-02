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
    df = td.extract_df(docs)
    assert "lix" in df.columns
    assert "dependency_distance_mean" in df.columns
    assert "n_stop_words" in df.columns
    assert "pos_prop_VERB" in df.columns
    assert "n_tokens" in df.columns
    assert "first_order_coherence" in df.columns
    assert len(df) == 2


def test_extract_dict_single_doc(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_dict(doc)
    for metric in ["descriptive_stats", "readability", "dependency_distance"]:
        dict_list = td.extract_dict(doc, metrics=metric)
        assert isinstance(dict_list, list)
        assert len(dict_list) == 1

        metrics_dict = dict_list[0]
        assert isinstance(metrics_dict, dict)
        assert metrics_dict.pop("text") == doc.text


def test_extract_df_only_pos():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/pos_proportions")

    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_df(doc, metrics="pos_proportions")
