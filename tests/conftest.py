"""This module is used to set up Pytest fixtures."""

import pandas as pd
import pytest


@pytest.fixture
def test_data() -> pd.DataFrame:
    """This is used to load the data."""
    fp = "./data/titanic_train.csv"
    data = pd.read_csv(fp)
    yield data
