""" Extract metrics as Pandas DataFrame."""

from typing import Any, Dict, Iterable, List, Optional, Union

import pandas as pd
from spacy.tokens import Doc
from wasabi import msg

from textdescriptives.utils import (
    _create_spacy_pipeline,
    _remove_textdescriptives_extensions,
    get_valid_metrics,
)


def __get_quality(doc: Doc) -> dict:
    """Get quality metrics as well as boolean indicator for passing filters."""
    return doc._.quality.to_flat_value_dict()


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
            "dependency_distance", "pos_proportions", "coherence", "quality",
            "information_theory"]. Defaults to None in which case it will
            extract metrics for which a pipeline compoenent has been set.
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
            metric = __get_quality(docs)
        elif component == "descriptive_stats":
            metric = __get_descriptive_stats_dict(docs)
        else:
            metric = getattr(docs._, component)
        if metric:
            extracted_metrics.update(metric)

    return [extracted_metrics]


def extract_df(
    docs: Union[Iterable[Doc], Doc],
    metrics: Union[List[str], str, None] = None,
    include_text: bool = True,
) -> pd.DataFrame:
    """Extract calculated metrics from a spaCy Doc object or a generator of Docs
    from nlp.pipe to a Pandas DataFrame.

    Args:
        docs (Union[Iterable[Doc],  Doc]): An iterable of spaCy Docs or a single Doc
        metrics (Union[list[str], str], optional): Which metrics to extract.
            One or more of ["descriptive_stats", "readability",
            "dependency_distance", "pos_proportions", "coherence", "quality",
            "information_theory"]. Defaults to None in which
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
    lang: Optional[str] = None,
    metrics: Optional[Iterable[str]] = None,
    spacy_model: Optional[str] = None,
    spacy_model_size: str = "lg",
) -> pd.DataFrame:
    """Extract metrics from a text or a list of texts to a Pandas dataframe.

    Args:
        text (Union[str, List[str]]): A text or a list of texts.
        lang (str, optional): Language of the text. If lang is set and no spacy
            model is provided, will automatically download and use a spacy
            model for the language. Defaults to None.
        metrics (List[str]): Which metrics to extract.
            One or more of ["descriptive_stats", "readability",
            "dependency_distance", "pos_proportions", "coherence", "quality",
            "information_theory"]. If None, will extract all metrics from
            textdescriptives. Defaults to None.
        spacy_model (str, optional): The spacy model to use. If not set,
            will download one based on lang. Defaults to None.
        spacy_model_size (str, optional): Size of the spacy model to download.

    Returns:
        pd.DataFrame: DataFrame with a row for each text and column for each metric.
    """
    if isinstance(metrics, str):
        metrics = [metrics]

    if spacy_model is None and lang is None:
        raise ValueError("Either a spacy model or a language must be provided.")

    if spacy_model is not None and lang is not None:
        msg.info(
            "Both a spacy model and a language were provided. "
            + "Will use the spacy model and ignore language.",
        )

    if metrics is None:
        metrics = get_valid_metrics()

    # remove previously set metrics to avoid conflicts
    _remove_textdescriptives_extensions()

    # load spacy model if any component requires it
    nlp = _create_spacy_pipeline(
        spacy_model=spacy_model,
        lang=lang,
        metrics=metrics,
        spacy_model_size=spacy_model_size,
    )

    # add pipeline components
    if "all" in metrics:
        nlp.add_pipe("textdescriptives/all")
    else:
        for component in metrics:
            nlp.add_pipe(f"textdescriptives/{component}")

    if isinstance(text, str):
        text = [text]
    docs = nlp.pipe(text)

    return extract_df(docs)
