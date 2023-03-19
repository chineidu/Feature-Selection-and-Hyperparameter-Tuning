"""This module is used to load and manipulate data."""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

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
    return data


@timer
def split_data(
    *,
    data: pd.DataFrame,
    target: str,
    random_state: int = 123,
    test_size: float = 0.2,
    display_shape: bool = True,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """This splits the data into X_train, X_validation, y_train, y_validation."""
    X = data.drop(columns=[target])
    y = data.get(target)

    X_train, X_validation, y_train, y_validation = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    if display_shape:
        print(f"Shape of X_train: {X_train.shape}, \nShape of X_validation: {X_validation.shape}")
    return (X_train, X_validation, y_train, y_validation)
