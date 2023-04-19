import pytest
import spacy

import textdescriptives as td
from textdescriptives.utils import _create_spacy_pipeline, _download_spacy_model

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


@pytest.mark.parametrize("lang", ["en", "da"])
def test_download_spacy_model(lang):
    _download_spacy_model(lang=lang, size="sm")


def test_load_spacy_model():
    nlp = _create_spacy_pipeline(
        spacy_model=None,
        lang="en",
        metrics=["descriptive_stats", "readability", "coherence"],
        spacy_model_size="sm",
    )
    assert "tok2vec" in nlp.pipe_names


def test_load_spacy_model_blank():
    nlp = _create_spacy_pipeline(
        spacy_model=None,
        lang="en",
        metrics=["descriptive_stats"],
        spacy_model_size="sm",
    )
    assert "tok2vec" not in nlp.pipe_names


def test_extract_single_doc():
    df = td.extract_metrics(
        "This is just a cute little text. Actually, it's two sentences.",
        spacy_model="en_core_web_sm",
        metrics="readability",
    )
    assert "lix" in df.columns


def test_extract_with_lang():
    df = td.extract_metrics(
        "This is just a cute little text. Actually, it's two sentences.",
        metrics="dependency_distance",
        lang="en",
        spacy_model_size="sm",
    )
    assert "dependency_distance_mean" in df.columns


@pytest.mark.parametrize(
    "text",
    [
        "This is just a cute little text. Actually, it's two sentences. "
        + "No, it's three",
        [
            "This is just a cute little text. Actually, it's two sentences. "
            + "No, it's three.",
            "Two documents in this bad boy. Let's see how it works.",
        ],
    ],
)
def test_extract_similar_extract_df(text):
    df = td.extract_metrics(
        text,
        spacy_model="en_core_web_sm",
        metrics="coherence",
    )

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/coherence")
    if isinstance(text, str):
        text = [text]
    docs = nlp.pipe(text)
    df2 = td.extract_df(docs)
    assert df.equals(df2)


def test_extract_df_then_extract_metric():
    text = [
        "This is just a cute little text. Actually, it's two sentences. "
        + "No, it's three.",
        "Two documents in this bad boy. Let's see how it works.",
    ]
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives/coherence")
    docs = nlp.pipe(text)
    td.extract_df(docs)

    td.extract_metrics(
        text,
        spacy_model="en_core_web_sm",
        metrics="quality",
    )


def test_extract_model_not_needed():
    df = td.extract_metrics(
        "This is just a cute little text. Actually, it's two sentences.",
        metrics="descriptive_stats",
        lang="en",
    )
    assert "n_tokens" in df.columns


def test_extract_metrics_twice():
    text = "Just a small test"
    td.extract_metrics(
        text,
        metrics="descriptive_stats",
        lang="en",
    )
    td.extract_metrics(
        text,
        metrics="coherence",
        lang="en",
    )


def test_extract_metrics_multiple_metrics():
    df = td.extract_metrics(
        "This is just a cute little text. Actually, it's two sentences.",
        metrics=["readability", "dependency_distance"],
        spacy_model="en_core_web_sm",
    )
    assert "lix" in df.columns
    assert "dependency_distance_mean" in df.columns


@pytest.mark.parametrize(
    "text",
    ["just a little test", ""],
)
def test_extract_metrics_all_metrics(text: str):
    df = td.extract_metrics(text=text, spacy_model="en_core_web_sm", metrics=None)
    assert "n_tokens" in df.columns
