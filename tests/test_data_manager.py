"""This module is used to test the code for loading and manipulating data."""

import pandas as pd

from src.data_manager import load_data, split_data


def test_load_data() -> None:
    """This tests the load_data function."""
    # Given
    fp = "./data/titanic_train.csv"
    expected = {
        "shape": (891, 12),
        "columns": {
            "PassengerId",
            "Survived",
            "Pclass",
            "Name",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "Ticket",
            "Fare",
            "Cabin",
            "Embarked",
        },
    }

    # When
    result = load_data(filename=fp)

    # Then
    assert result.shape == expected.get("shape")
    assert set(result.columns) == expected.get("columns")
    assert isinstance(result, pd.DataFrame)


def test_split_data(test_data: pd.DataFrame) -> None:
    """This is used to test the split_data logic."""
    # Given
    expected = {
        "X_train_shape": (712, 11),
        "X_validation_shape": (179, 11),
        "y_train_shape": (712,),
        "y_validation_shape": (179,),
    }

    # When
    X_train, X_validation, y_train, y_validation = split_data(
        data=test_data, target="Survived", display_shapes=True
    )

    # Then
    assert X_train.shape == expected.get("X_train_shape")
    assert X_validation.shape == expected.get("X_validation_shape")
    assert y_train.shape == expected.get("y_train_shape")
    assert y_validation.shape == expected.get("y_validation_shape")
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(y_validation, pd.Series)
