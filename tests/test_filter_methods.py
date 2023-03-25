"""This module is used to test the code for selecting features."""

import pandas as pd
from feature_engine.encoding import MeanEncoder

from src.filter_methods import BestFeatures


def test_best_features(test_data: pd.DataFrame) -> None:
    """This is used to test the BestFeatures class.
    TODO: Turn this to a mock test.

    Params:
        test_data (pd.DataFrame): The test data.
    """
    # Given
    features = ["Sex", "Age", "Pclass", "SibSp", "Parch", "Fare", "Embarked", "Survived"]
    df = test_data.copy()
    df = df[features].dropna()
    X = df.drop(columns=["Survived"])
    y = df["Survived"]
    mean_enc = MeanEncoder(variables=["Sex", "Embarked"])
    df = mean_enc.fit_transform(X=X, y=y)
    df = pd.concat([df, y], axis=1)

    expected = {
        "features": {"Sex", "Pclass", "Fare", "Embarked", "Parch", "SibSp", "Age"},
        "shape": 7,
        "string": (
            "BestFeatures(Data_shape=((712, 8)), target=('Survived'), "
            "type_='classification', random_state=(123), eval_metric='ROC_AUC')"
        ),
    }

    # When
    result = BestFeatures(data=df, target="Survived", type_="classification")

    # Then
    assert set(result.select_best_features().keys()) == expected.get("features")
    assert len([*result.select_best_features().keys()]) == expected.get("shape")
    assert repr(result) == expected.get("string")
