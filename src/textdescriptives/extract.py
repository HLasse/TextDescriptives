"""Extract metrics as Pandas DataFrame."""
from typing import Any, Dict, Iterable, List, Union

import pandas as pd
from spacy.tokens import Doc

from textdescriptives.utils import get_valid_metrics


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

    for component in metrics:
        extracted_metrics: Dict[str, Any] = {}
        if component == "quality":
            extracted_metrics.update(__get_quality(docs))
        elif component == "descriptive_stats":
            extracted_metrics.update(__get_descriptive_stats_dict(docs))
        else:
            extracted_metrics.update(getattr(docs._, component))
    if include_text:
        extracted_metrics["text"] = docs.text

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
                "dependency_distance", "pos_stats", "all"]. Defaults to None in which
                case it will extract metrics for which a pipeline compoenent has been
                set.
        include_text (bool, optional): Whether to add a column containing the text.
            Defaults to True.

    Returns:
        pd.DataFrame: DataFrame with a row for each doc and column for each metric.
    """
    return pd.DataFrame(extract_dict(docs, metrics, include_text))
