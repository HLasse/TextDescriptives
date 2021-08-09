"""Extract metrics as Pandas DataFrame"""
from spacy.tokens import Doc

from typing import Union, List
import types

import pandas as pd


class DataFrameExtractor:
    def __init__(
        self,
        doc: Doc,
        metrics: Union[List[str], str] = "all",
        include_text: bool = True,
    ):
        """Utility class to extract specified metrics to a Pandas DataFrame

        Args:
            doc (Doc): a spaCy doc
            metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability", "dependency_distance", "all"].
                Defaults to "all".
            include_text (bool, optional): Whether to add a column containing the text. Defaults to True.
        """
        if not isinstance(doc, (Doc)):
            raise TypeError(f"doc should be a spaCy Doc object, not {type(doc)}.")

        valid_metrics = set(
            ["descriptive_stats", "readability", "dependency_distance", "all"]
        )
        if isinstance(metrics, str):
            metrics = [metrics]
        if not isinstance(metrics, list):
            raise TypeError(
                f"'metrics' should be string or list of strings, not {type(metrics)}"
            )
        if not set(metrics).issubset(valid_metrics):
            raise ValueError(
                f"'metrics' contained invalid metric.\nValid metrics are: ['all', 'descriptive_stats', 'readability', 'dependency_distance']"
            )

        if include_text:
            df_list = [pd.DataFrame([doc.text], columns=["text"])]
        else:
            df_list = []

        if "all" in metrics:
            if doc.has_extension("counts"):
                df_list.append(self.__descriptive_stats(doc))
            if doc.has_extension("readability"):
                df_list.append(self.__readability(doc))
            if doc.has_extension("dependency_distance"):
                df_list.append(self.__dependency_distance(doc))
        else:
            if "descriptive_stats" in metrics:
                df_list.append(self.__descriptive_stats(doc))
            if "readability" in metrics:
                df_list.append(self.__readability(doc))
            if "dependency_distance" in metrics:
                df_list.append(self.__dependency_distance(doc))

        self.df = pd.concat(df_list, axis=1)

    def __descriptive_stats(self, doc: Doc) -> pd.DataFrame:
        descriptive_stats = {
            **doc._.token_length,
            **doc._.sentence_length,
            **doc._.syllables,
            **doc._.counts,
        }
        return pd.DataFrame.from_records([descriptive_stats])

    def __readability(self, doc: Doc) -> pd.DataFrame:
        return pd.DataFrame.from_records([doc._.readability])

    def __dependency_distance(self, doc: Doc) -> pd.DataFrame:
        return pd.DataFrame.from_records([doc._.dependency_distance])


def extract_df(
    doc: Doc, metrics: Union[List[str], str] = "all", include_text: bool = True
) -> pd.DataFrame:
    """Extract calculated metrics from a spaCy Doc object or a generator of Docs from
    nlp.pipe to a Pandas DataFrame

    Args:
        doc (Doc): a spaCy doc or a generator of spaCy Docs
        metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability", "dependency_distance", "all"].
                Defaults to "all".
        include_text (bool, optional): Whether to add a column containing the text. Defaults to True.

    Returns:
        pd.DataFrame: DataFrame with a row for each doc and column for each metric.
    """
    if isinstance(doc, types.GeneratorType):
        rows = []
        for d in doc:
            metric_df = DataFrameExtractor(d, metrics, include_text).df
            rows.append(metric_df)
        return pd.concat(rows, axis=0, ignore_index=True)
    return DataFrameExtractor(doc, metrics, include_text).df


"""Helpers to subset an extracted dataframe"""

readability_cols = [
    "flesch_reading_ease",
    "flesch_kincaid_grade",
    "smog",
    "gunning_fog",
    "automated_readability_index",
    "coleman_liau_index",
    "lix",
    "rix",
]

dependency_cols = [
    "dependency_distance_mean",
    "dependency_distance_std",
    "prop_adjacent_dependency_relation_mean",
    "prop_adjacent_dependency_relation_std",
]

descriptive_stats_cols = [
    "token_length_mean",
    "token_length_median",
    "token_length_std",
    "sentence_length_mean",
    "sentence_length_median",
    "sentence_length_std",
    "syllables_per_token_mean",
    "syllables_per_token_median",
    "syllables_per_token_std",
    "n_tokens",
    "n_unique_tokens",
    "proportion_unique_tokens",
    "n_sentences",
    "n_characters",
]
