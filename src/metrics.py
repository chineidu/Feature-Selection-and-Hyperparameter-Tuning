"""This module is used for model evaluation."""
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


def evaluate_regression_model(*, y_true: np.ndarray, y_pred: np.ndarray) -> str:
    """This is used to evaluate a regression model."""
    # Mean Squared Error (The lower, the better)
    mse = mean_squared_error(y_true=y_true, y_pred=y_pred, squared=True)

    # Root Mean Squared Error (The lower, the better)
    # Remember to use squared=False
    rmse = mean_squared_error(y_true=y_true, y_pred=y_pred, squared=False)

    # Mean Absolute Error (The lower, the better)
    mae = mean_absolute_error(y_true=y_true, y_pred=y_pred)

    # R Squared (The higher, the better. Max (best) value is 1)
    R2 = r2_score(y_true=y_true, y_pred=y_pred)
    lower, higher = "Lower is better!", "Higher is better!"

    result_str = (
        "================ Evaluation Metrics ================"
        f"\nMean Squared Error ({lower}!): {round(mse, 3)}"
        f"\nRoot Mean Squared Error ({lower}!): {round(rmse, 3)}"
        f"\nMean Absolute Error ({lower}!): {round(mae, 3)}"
        "\n==================================================="
        f"\nR Squared ({higher}!): {round(R2, 3)} "
    )

    return result_str
