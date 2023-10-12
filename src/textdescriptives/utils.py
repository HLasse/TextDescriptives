from pathlib import Path
from typing import Iterable, List, Optional, Type, Union

import pandas as pd
import spacy
from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from wasabi import msg


def get_valid_metrics() -> set:
    """Get valid metrics for extractor.

    Returns:
        set: Set of valid metrics
    """
    # extract textdescriptive components from the list of spacy Language factory
    return {
        k.split("/")[1]
        for k in Language.factories.keys()
        if k.startswith("textdescriptives")
    }


def get_doc_assigns(metric: str) -> List[str]:
    """Get doc extension attributes for a given metric.

    Args:
        metric (str): Metric to get columns for
    """
    # extract the assign names from the factory meta (this assumes that the doc._.
    # only includes elements which are also extracted as a part of the dataframe.
    if metric == "all":
        return [
            col[6:]
            for component in get_valid_metrics()
            for col in Language.get_factory_meta(
                f"textdescriptives/{component}",
            ).assigns
            if col.startswith("doc._.")
        ]
    return [
        col[6:]
        for col in Language.get_factory_meta(f"textdescriptives/{metric}").assigns
        if col.startswith("doc._.")
    ]


def get_span_assigns(metric: str) -> List[str]:
    """Get span extension attributes for a given metric.

    Args:
        metric (str): Metric to get columns for
    """
    return [
        col[7:]
        for col in Language.get_factory_meta(f"textdescriptives/{metric}").assigns
        if col.startswith("span._.")
    ]


def get_token_assigns(metric: str) -> List[str]:
    """Get token extension attributes for a given metric.

    Args:
        metric (str): Metric to get columns for
    """
    return [
        col[8:]
        for col in Language.get_factory_meta(f"textdescriptives/{metric}").assigns
        if col.startswith("token._.")
    ]


def load_sms_data():
    """Load the sms dataset
    https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection."""
    path = Path(__file__).parent / "data" / "spam.csv"
    spam_data = pd.read_csv(path, encoding="latin-1")
    spam_data.dropna(how="any", inplace=True, axis=1)
    spam_data.columns = ["label", "message"]
    return spam_data


def _download_spacy_model(lang: str, size: str) -> str:
    """Download a spacy model for a given language and size.

    Args:
        lang (str): Language to download a model for.
        size (str): Size of the model to download. One of "sm", "md", "lg", "trf".

    Returns:
        str: Name of the downloaded model.
    """
    data_source = "news" if lang != "en" else "web"
    spacy_model = f"{lang}_core_{data_source}_{size}"
    # don't download if model already exists
    if spacy_model in spacy.cli.info()["pipelines"]:  # type: ignore
        return spacy_model
    spacy.cli.download(spacy_model)
    return spacy_model


def _remove_spacy_extension(
    spacy_language: Union[Type[Doc], Type[Span], Type[Token]],
    extension: str,
) -> None:
    """Remove spacy extension from a Language object if it exists."""
    if spacy_language.has_extension(extension):
        spacy_language.remove_extension(extension)


def _remove_textdescriptives_extensions() -> None:
    """Remove spacy extensions added by textdescriptives.

    This is necessary to avoid errors if running `extract_metrics` multiple
    times with different metrics
    """
    for metric in get_valid_metrics():
        doc_assigns = get_doc_assigns(metric)
        for assigned in doc_assigns:
            _remove_spacy_extension(spacy_language=Doc, extension=assigned)
        span_assigns = get_span_assigns(metric)
        for assigned in span_assigns:
            _remove_spacy_extension(spacy_language=Span, extension=assigned)
        token_assings = get_token_assigns(metric)
        for assigned in token_assings:
            _remove_spacy_extension(spacy_language=Token, extension=assigned)


def _create_spacy_pipeline(
    spacy_model: Optional[str],
    lang: Optional[str],
    metrics: Iterable[str],
    spacy_model_size: str,
) -> Language:
    """Load a spacy pipeline suitable for the metrics to be extracted.

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

    metrics_requiring_spacy_model = {
        "dependency_distance",
        "pos_proportions",
        "coherence",
        "pos_proportions",
    }
    # if no spacy model is necessary for the metrics, return a blank model
    # for the language
    if not bool(metrics_requiring_spacy_model.intersection(metrics)):
        # always load spacy model if specified (if e.g. custom tokenizer)
        if spacy_model:
            return spacy.load(spacy_model)
        if lang is not None:
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
        spacy_model = _download_spacy_model(lang=lang, size=spacy_model_size)
    try:
        return spacy.load(spacy_model)
    except OSError:
        msg.info(
            f"""The specified spaCy model "{spacy_model}" was not 
            found on disk. Downloading...""",
        )
        spacy.cli.download(spacy_model)
        return spacy.load(spacy_model)
