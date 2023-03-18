"""This module is used to load and manipulate data."""

import pandas as pd

# Custom imports
from src.decorators import shape_of_array, timer


@timer
@shape_of_array
def load_data(*, filename: str, sep: str = ",") -> pd.DataFrame:
    """This is used to load the data.

    Params;
        filename (str): The filepath.
        sep (str, default=","): The separator. e.g ",", "\t", etc

    Returns:
        data (pd.DataFrame): The loaded dataframe.
    """
    data = pd.read_csv(filename, sep=sep)
    print(f"Shape of data: {data.shape}\n")
    return data
