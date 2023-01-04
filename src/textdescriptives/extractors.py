"""Extract metrics as Pandas DataFrame."""
from typing import Any, Dict, Iterable, List, Optional, Union

import pandas as pd
import spacy
import spacy.cli
from spacy import Language
from spacy.tokens import Doc
from wasabi import msg

from textdescriptives.utils import get_assigns, get_valid_metrics


def __get_quality(doc: Doc) -> dict:
    """Get quality metrics as well as boolean indicator for passing filters."""
    return {**doc._.quality, "passed_quality_check": doc._.passed_quality_check}


def __get_descriptive_stats_dict(doc: Doc) -> dict:
    """Get descriptive statistics as dictionary."""
    return {
        **doc._.token_length,
        **doc._.sentence_length,
        **doc._.syllables,
        **doc._.counts,
    }


def extract_dict(
    docs: Union[Iterable[Doc], Doc],
    metrics: Union[List[str], str, None] = None,
    include_text: bool = True,
) -> List[Dict[str, Any]]:
    """Extract calculated metrics from a spaCy Doc or an iterable of Docs to a
    list of dictionaries.

    Args:
        docs (Union[Iterable[Doc],  Doc]): An iterable of spaCy Docs or a single Doc
        metrics (Union[list[str], str, None], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability",
                "dependency_distance", "pos_stats", "all"]. Defaults to None in which
                case it will extract metrics for which a pipeline compoenent has been
                set.
        include_text (bool, optional): Whether to add an entry containing the text.
            Defaults to True.

    Returns:
        List[Dict[str, Any]]: List of dictionaries for each Doc with extracted metrics.
    """
    if not isinstance(docs, Doc):
        return [extract_dict(doc, metrics, include_text)[0] for doc in docs]

    # extract textdescriptive metrics from the list of spacy Language factory
    valid_metrics = get_valid_metrics()

    if isinstance(metrics, str):
        metrics = [metrics]

    if metrics is None:
        metrics = [
            component for component in valid_metrics if docs.has_extension(component)
        ]

    if not set(metrics).issubset(valid_metrics):
        raise ValueError(
            "'metrics' contained invalid metric.\n"
            + f"Valid metrics are: {valid_metrics}",
        )
    extracted_metrics: Dict[str, Any] = {}
    if include_text:
        extracted_metrics["text"] = docs.text
    for component in metrics:
        if component == "quality":
            extracted_metrics.update(__get_quality(docs))
        elif component == "descriptive_stats":
            extracted_metrics.update(__get_descriptive_stats_dict(docs))
        else:
            extracted_metrics.update(getattr(docs._, component))

    return [extracted_metrics]


def extract_df(
    docs: Union[Iterable[Doc], Doc],
    metrics: Union[List[str], str, None] = None,
    include_text: bool = True,
) -> pd.DataFrame:
    """Extract calculated metrics from a spaCy Doc object or a generator of
    Docs from nlp.pipe to a Pandas DataFrame.

    Args:
        docs (Union[Iterable[Doc],  Doc]): An iterable of spaCy Docs or a single Doc
        metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability",
                "dependency_distance", "pos_stats"]. Defaults to None in which
                case it will extract metrics for which a pipeline compoenent has been
                set.
        include_text (bool, optional): Whether to add a column containing the text.
            Defaults to True.

    Returns:
        pd.DataFrame: DataFrame with a row for each doc and column for each metric.
    """
    return pd.DataFrame(extract_dict(docs, metrics, include_text))


def extract_metrics(
    text: Union[str, List[str]],
    spacy_model=None,
    lang: str = None,
    metrics: Optional[Iterable[str]] = None,
    spacy_model_size: str = "lg",
) -> pd.DataFrame:
    """Extract metrics from a text or a list of texts to a Pandas dataframe.


    Args:
        text (Union[str, List[str]]): A text or a list of texts.
        spacy_model (spacy.lang, optional): The spacy model to use. If not set,
            will download one based on lang. We recommend always using `spacy_model`
            and downloading the model beforehand to have more control over the
            model as well as to avoid versioning issues. Defaults to None.
        lang (str, optional): Language of the text. If lang is set and no spacy
            model is provided, will automatically download and use a spacy
            model for the language. Defaults to None.
        metrics (List[str]): Which metrics to extract.
            One or more of ["descriptive_stats", "readability",
            "dependency_distance", "pos_stats", "coherence", "quality"]. If None,
            will extract all metrics from textdescriptives. Defaults to None.
        spacy_model_size (str, optional): Size of the spacy model to download.

    Returns:
        pd.DataFrame: DataFrame with a row for each text and column for each metric.
    """
    if isinstance(metrics, str):
        metrics = [metrics]

    if spacy_model is None and lang is None:
        raise ValueError("Either a spacy model or a language must be provided.")

    if metrics is None:
        metrics = get_valid_metrics()

    # load spacy model if any component requires it
    nlp = load_spacy_model(
        spacy_model=spacy_model,
        lang=lang,
        metrics=metrics,
        spacy_model_size=spacy_model_size,
    )

    # add pipeline components
    for component in metrics:
        nlp.add_pipe(f"textdescriptives/{component}")

    if isinstance(text, str):
        text = [text]
    docs = nlp.pipe(text)

    df = extract_df(docs)
    _clean_doc_extensions(metrics=metrics)

    return df


def load_spacy_model(
    spacy_model: Optional[str],
    lang: Optional[str],
    metrics: Iterable[str],
    spacy_model_size: str,
) -> Language:
    """Load a spacy model suitable for the metrics to be extracted.

    Args:
        spacy_model (Optional[str]): The spacy model to use. If not set,
            will download one based on lang.
        lang (Optional[str]): Language of the text. If lang is set and no spacy
            model is provided, will automatically download and use a spacy
            model for the language.
        metrics (Iterable[str]): Which metrics to extract.
        spacy_model_size (str): Size of the spacy model to download.

    Returns:
        Language: a spacy pipeline
    """

    metrics_requiring_spacy_model = {"dependency_distance", "pos_stats", "coherence"}
    # if no spacy model is necesarry for the metrics, return a blank model for the language
    if not bool(metrics_requiring_spacy_model.intersection(metrics)):
        if lang is not None:
            return spacy.blank(lang)
        if spacy_model:
            lang = spacy_model.split("_")[0]
            return spacy.blank(lang)
        raise ValueError(
            "No spacy model needed for the metrics and no language provided. "
            + "Please provide a language to create a blank spacy model.",
        )
    # if no spacy model is provided, download one
    if spacy_model is None:
        if lang is None:
            raise ValueError(
                "No spacy model provided and no language provided. "
                + "Please provide a language to download a spacy model.",
            )
        msg.info(f"No spacy model provided. Inferring spacy model for {lang}.")
        spacy_model = download_spacy_model(lang=lang, size=spacy_model_size)
    return spacy.load(spacy_model)


def download_spacy_model(lang: str, size: str) -> str:
    """Download a large spacy model for a given language.

    Args:
        lang (str): Language to download a model for.
        size (str): Size of the model to download. One of "sm", "md", "lg", "trf".

    Returns:
        str: Name of the downloaded model.
    """
    data_source = "news" if lang != "en" else "web"
    spacy_model = f"{lang}_core_{data_source}_{size}"
    # don't download if model already exists
    if spacy_model in spacy.cli.info()["pipelines"]:
        return spacy_model
    spacy.cli.download(spacy_model)
    return spacy_model


def _clean_doc_extensions(metrics: Iterable[str]) -> None:
    """Remove doc extensions added by textdescriptives. This is necesarry to avoid
    errors if running `extract_metrics` multiple times with different metrics"""
    for metric in metrics:
        assigns = get_assigns(metric)
        for assigned in assigns:
            Doc.remove_extension(assigned)
