"""This module is used to find the best features in a dataset by building a simple 
ML model with a single feature to predict the target."""
from typing import NewType
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import metrics, model_selection

Plot = NewType("Plot", str)


class BestFeatures:
    """This is used to calculate the best features by creating a simple
    estimator with a single feature to predict the target and evaluating
    its performance with that feature."""

    MAE = "MAE"
    ROC_AUC = "ROC_AUC"
    REGRESSION = "regression"
    CLASSIFICATION = "classification"

    def __init__(
        self,
        *,
        data: pd.DataFrame,
        target: str,
        type_: str,
        random_state: int = 123,
    ) -> None:
        self.data = data
        self.target = target
        if type_ not in [self.REGRESSION, self.CLASSIFICATION]:
            raise Exception(f"{type_!r} must be {self.REGRESSION!r} or {self.CLASSIFICATION!r}")
        self.type_ = type_.lower().strip()
        self.random_state = random_state
        self.n_estimators = 40
        self.eval_metric = self.MAE if self.type_ == self.REGRESSION else self.ROC_AUC
        self.status = "lower is better!" if self.type_ == self.REGRESSION else "higher is better!"
        self.order = False if self.type_ == self.REGRESSION else True
        self.feature_rankings = {}

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(Data_shape=({self.data.shape}), "
            f"target=({self.target!r}), type_={self.type_!r}, "
            f"random_state=({self.random_state}), eval_metric={self.eval_metric!r})"
        )

    def select_best_features(self) -> dict[str]:
        """Determine the best features."""

        message = {
            "type": self.type_,
            "evaluation metric": self.eval_metric,
            "status": self.status,
        }

        print(message)

        for feat in self.data.columns:
            if feat != self.target:
                X = self.data[[feat, self.target]]
                # Split the data
                X_train, X_validation, y_train, y_validation = self._split_data(
                    data=X,
                    target=self.target,
                    random_state=self.random_state,
                    display_shape=False,
                )
                if self.type_ == self.REGRESSION:  # regression
                    estimator = RandomForestRegressor(
                        n_estimators=self.n_estimators, random_state=self.random_state
                    )
                    # Fit model
                    estimator.fit(X_train, y_train)
                    # Make predictions
                    y_pred = estimator.predict(X_validation)
                    # Evaluate estimator
                    mae = metrics.mean_absolute_error(y_true=y_validation, y_pred=y_pred)
                    self.feature_rankings[feat] = mae
                else:  # classification
                    estimator = RandomForestClassifier(
                        n_estimators=self.n_estimators, random_state=self.random_state
                    )
                    # Fit model
                    estimator.fit(X_train, y_train)
                    y_pred = estimator.predict_proba(X_validation)[:, 1]
                    mae = metrics.roc_auc_score(y_true=y_validation, y_score=y_pred)
                    self.feature_rankings[feat] = mae
        # Sort the dict
        if self.type_ == self.REGRESSION:
            self.feature_rankings = self._sort_dict(
                input_dict=self.feature_rankings, ascending=self.order
            )
        else:
            self.feature_rankings = self._sort_dict(
                input_dict=self.feature_rankings, ascending=self.order
            )
        return self.feature_rankings

    def visualize_rankings(self) -> Plot:
        """This returns a bar plot showing the features and the metric used."""
        # Determine best features and create DataFrame
        self.select_best_features()
        df = pd.DataFrame(self.feature_rankings, index=[0]).T
        eval_metric = self.MAE if self.type_ == self.REGRESSION else self.ROC_AUC

        df = df.rename(columns={0: eval_metric}).sort_values(by=eval_metric, ascending=self.order)

        THRESH = (
            np.percentile(df[eval_metric], q=40)
            if self.type_ == self.REGRESSION
            else np.median(df[eval_metric])
        )
        print(f"Threshold: {THRESH}")

        df.plot(
            kind="bar",
            title=f"{eval_metric!r} of The Features ({self.status})",
            xlabel=eval_metric,
            figsize=(8, 5),
        )
        plt.axhline(y=THRESH, color="red")
        plt.tight_layout()

    plt.show()

    @staticmethod
    def _split_data(
        *,
        data: pd.DataFrame,
        target: str,
        random_state: int = 123,
        test_size: float = 0.2,
        display_shape: bool = True,
    ) -> tuple[np.ndarray]:
        """This split the data into X_train, X_validation, y_train, y_validation."""
        X = data.drop(columns=[target])
        y = data.get(target)

        X_train, X_validation, y_train, y_validation = model_selection.train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        if display_shape:
            print(
                f"Shape of X_train: {X_train.shape}, \nShape of X_validation: {X_validation.shape}"
            )
        return (X_train, X_validation, y_train, y_validation)

    @staticmethod
    def _sort_dict(*, input_dict: dict, ascending: bool = True) -> dict:
        """This is used to sort a dict using the values."""
        sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1], reverse=ascending))
        return sorted_dict
