"""Extract metrics as Pandas DataFrame"""
from spacy.tokens import Doc

from functools import reduce
from collections import defaultdict
from typing import Union, List
import types

import pandas as pd


class Extractor:
    def __init__(
        self,
        doc: Doc,
        metrics: Union[List[str], str] = "all",
        include_text: bool = True,
        as_dict=False,
    ):
        """Utility class to extract specified metrics to a Pandas DataFrame or dictionary

        Args:
            doc (Doc): a spaCy doc
            metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability", "dependency_distance", "pos_stats", "all"].
                Defaults to "all".
            include_text (bool, optional): Whether to add a column containing the text. Defaults to True.
        """
        if not isinstance(doc, (Doc)):
            raise TypeError(f"doc should be a spaCy Doc object, not {type(doc)}.")

        valid_metrics = set(
            [
                "descriptive_stats",
                "readability",
                "dependency_distance",
                "pos_stats",
                "all",
            ]
        )
        if isinstance(metrics, str):
            metrics = [metrics]
        if not isinstance(metrics, list):
            raise TypeError(
                f"'metrics' should be string or list of strings, not {type(metrics)}"
            )
        if not set(metrics).issubset(valid_metrics):
            raise ValueError(
                f"'metrics' contained invalid metric.\nValid metrics are: ['all', 'descriptive_stats', 'readability', 'dependency_distance', 'pos_stats']"
            )

        self.include_text = include_text
        self.as_dict = as_dict

        if include_text:
            extraction = [self.__extract_text(doc)]
        else:
            extraction = []

        if "all" in metrics:
            if doc.has_extension("counts"):
                extraction.append(self.__descriptive_stats(doc))
            if doc.has_extension("readability"):
                extraction.append(self.__readability(doc))
            if doc.has_extension("dependency_distance"):
                extraction.append(self.__dependency_distance(doc))
            if doc.has_extension("pos_proportions"):
                extraction.append(self.__pos_proportions(doc))
        else:
            if "descriptive_stats" in metrics:
                extraction.append(self.__descriptive_stats(doc))
            if "readability" in metrics:
                extraction.append(self.__readability(doc))
            if "dependency_distance" in metrics:
                extraction.append(self.__dependency_distance(doc))
            if "pos_stats" in metrics:
                extraction.append(self.__pos_proportins(doc))

        if self.as_dict:
            self.out = reduce(lambda a, b: {**a, **b}, extraction)
        else:
            self.out = pd.concat(extraction, axis=1)

    def __descriptive_stats(self, doc: Doc) -> pd.DataFrame:
        descriptive_stats = {
            **doc._.token_length,
            **doc._.sentence_length,
            **doc._.syllables,
            **doc._.counts,
        }
        if self.as_dict:
            return descriptive_stats
        return pd.DataFrame.from_records([descriptive_stats])

    def __readability(self, doc: Doc) -> pd.DataFrame:
        if self.as_dict:
            return doc._.readability
        return pd.DataFrame.from_records([doc._.readability])

    def __dependency_distance(self, doc: Doc) -> pd.DataFrame:
        if self.as_dict:
            return doc._.dependency_distance
        return pd.DataFrame.from_records([doc._.dependency_distance])

    def __extract_text(self, doc: Doc) -> Union[pd.DataFrame, str]:
        if self.as_dict:
            return {"text": doc.text}
        return pd.DataFrame([doc.text], columns=["text"])

    def __pos_proportions(self, doc: Doc) -> pd.DataFrame:
        if self.as_dict:
            return doc._.pos_proportions
        return pd.DataFrame.from_records([doc._.pos_proportions])


def extract_df(
    doc: Doc, metrics: Union[List[str], str] = "all", include_text: bool = True
) -> pd.DataFrame:
    """Extract calculated metrics from a spaCy Doc object or a generator of Docs from
    nlp.pipe to a Pandas DataFrame

    Args:
        doc (Doc): a spaCy doc or a generator of spaCy Docs
        metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability", "dependency_distance", "pos_stats", "all"].
                Defaults to "all".
        include_text (bool, optional): Whether to add a column containing the text. Defaults to True.

    Returns:
        pd.DataFrame: DataFrame with a row for each doc and column for each metric.
    """
    if isinstance(doc, types.GeneratorType):
        rows = []
        for d in doc:
            metric_df = Extractor(d, metrics, include_text).out
            rows.append(metric_df)
        return pd.concat(rows, axis=0, ignore_index=True)
    return Extractor(doc, metrics, include_text).out


def extract_dict(
    doc: Doc, metrics: Union[List[str], str] = "all", include_text: bool = True
) -> dict:
    """Extract calculated metrics from a spaCy Doc object or a generator of Docs from
    nlp.pipe to a dictionary

    Args:
        doc (Doc): a spaCy doc or a generator of spaCy Docs
        metrics (Union[list[str], str], optional): Which metrics to extract.
                One or more of ["descriptive_stats", "readability", "dependency_distance", "pos_stats", "all"].
                Defaults to "all".
        include_text (bool, optional): Whether to add an entry containing the text. Defaults to True.

    Returns:
        dict: Dictionary with a key for each metric.
    """
    if isinstance(doc, types.GeneratorType):
        dict_list = []
        for d in doc:
            metric_dict = Extractor(d, metrics, include_text, as_dict=True).out
            dict_list.append(metric_dict)
        # concatenate values from each dict in list
        out = defaultdict(list)
        for d in dict_list:
            for key, value in d.items():
                out[key].append(value)
        return dict(out)
    return Extractor(doc, metrics, include_text, as_dict=True).out


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
