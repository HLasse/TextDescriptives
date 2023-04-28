from typing import Iterable, List, Optional

import pandas as pd

try:
    from sklearn.base import BaseEstimator, TransformerMixin
except ImportError as e:
    raise ImportError(
        "Failed to import sklearn. If you want to use the sklearn integration, "
        + "please install it with `pip install scikit-learn` or install "
        + "textdescriptives with the [sklearn] extra: "
        + "pip install textdescriptives[sklearn].",
    ) from e
from wasabi import msg

from textdescriptives import extract_metrics


def get_feature_names_from_metrics_and_model(
    lang: Optional[str],
    metrics: Optional[Iterable[str]],
    spacy_model: Optional[str],
    spacy_model_size: str,
) -> List[str]:
    """Get the names of the extracted features from the specified metrics
    and model. Does this by extracting the metrics from an empty dummy text."""
    df = extract_metrics(
        text="",
        lang=lang,
        metrics=metrics,
        spacy_model=spacy_model,
        spacy_model_size=spacy_model_size,
    )
    return list(df.drop("text", axis=1).columns)


class TextDescriptivesFeaturizer(TransformerMixin, BaseEstimator):
    """Wrapper for extracting text metrics using textdescriptives and
    using it in a sklearn pipeline."""

    def __init__(
        self,
        lang: Optional[str] = None,
        metrics: Optional[Iterable[str]] = None,
        spacy_model: Optional[str] = None,
        spacy_model_size: str = "lg",
    ):
        """Initialise the transformer with arguments to
        textdescriptives.extract_metrics.

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
        """
        self.lang = lang
        if isinstance(metrics, str):
            metrics = [metrics]
        self.metrics = metrics
        self.spacy_model = spacy_model
        self.spacy_model_size = spacy_model_size

        if spacy_model is None and lang is None:
            raise ValueError("Either a spacy model or a language must be provided.")
        if spacy_model is not None and lang is not None:
            msg.info(
                "Both a spacy model and a language were provided. "
                + "Will use the spacy model and ignore language.",
            )
        self.feature_names = get_feature_names_from_metrics_and_model(
            lang=self.lang,
            metrics=self.metrics,
            spacy_model=self.spacy_model,
            spacy_model_size=self.spacy_model_size,
        )

    def fit(self, X, y=None):
        """Fit the transformer to the data. This is not needed for this
        transformer, but is required for sklearn compatibility."""
        return self

    def transform(self, X) -> pd.DataFrame:
        """Transform the data using textdescriptives.

        Args:
            X: Iterable of strings.

        Returns:
            Numpy array of shape (n_samples, n_features).
        """
        metrics = extract_metrics(
            X,
            lang=self.lang,
            metrics=self.metrics,
            spacy_model=self.spacy_model,
            spacy_model_size=self.spacy_model_size,
        )
        return metrics.drop("text", axis=1)

    def get_feature_names(self) -> List[str]:
        """Get the names of the extracted features."""
        return self.feature_names

    def get_feature_names_out(self, input_features=None) -> List[str]:
        """Get the names of the extracted features. input_features is only
        present for API compatibility with sklearn."""
        return self.feature_names
        return self.feature_names
