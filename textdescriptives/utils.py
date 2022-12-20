from pathlib import Path

import pandas as pd


def load_sms_data():
    """Load the sms dataset https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection"""
    path = Path(__file__).parent / "tests" / "data" / "spam.csv"
    spam_data = pd.read_csv(path, encoding="latin-1")
    spam_data.dropna(how="any", inplace=True, axis=1)
    spam_data.columns = ["label", "message"]
    return spam_data
