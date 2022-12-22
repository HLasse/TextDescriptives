from pathlib import Path
from typing import List

import pandas as pd
from spacy import Language


def get_assigns(metric: str) -> List[str]:
    """Get columns for a given metric.

    Args:
        metric (str): Metric to get columns for
    """
    # extract the assign names from the factory meta (this assumes that the doc._.
    # only includes elements which are also extracted as a part of the dataframe.
    return [
        col[6:]
        for col in Language.get_factory_meta(f"textdescriptives/{metric}").assigns
        if col.startswith("doc._.")
    ]


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


def load_sms_data():
    """Load the sms dataset
    https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection."""
    path = Path(__file__).parent / "tests" / "data" / "spam.csv"
    spam_data = pd.read_csv(path, encoding="latin-1")
    spam_data.dropna(how="any", inplace=True, axis=1)
    spam_data.columns = ["label", "message"]
    return spam_data
