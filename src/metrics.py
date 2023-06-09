"""This module is used for model evaluation."""

import itertools
from typing import Union

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.metrics import (
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import GridSearchCV


def evaluate_regression_model(*, y_true: npt.ArrayLike, y_pred: npt.ArrayLike) -> str:
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


# pylint: disable=too-many-locals
def plot_confusion_matrix(
    *,
    y_true: npt.ArrayLike,
    y_pred: npt.ArrayLike,
    classes: Union[bool, list[str], None] = None,
    figsize: tuple[int, int] = (12, 12),
) -> None:
    """This returns a confusion matrix plot.

    Params:
      y_true (np.ndarray): The ground truth. i.e the true values
      y_pred (np.ndarray): t=The predicted values.
      classes (Union[bool, List[str], None], default=None): The class label names.

    Returns:
      A Matplotlib Plot
    """
    PCT, SIZE = 100, 12
    WHITE, BLACK = "white", "black"

    # confusion matrix
    c_matrix = confusion_matrix(y_true=y_true, y_pred=y_pred)
    # Normalize the values
    c_matrix_norm = np.divide(c_matrix.astype(float), c_matrix.sum(axis=1))
    n_classes = c_matrix.shape[0]

    fig, ax = plt.subplots(figsize=figsize)
    # Display an array as a matrix in a new figure window.
    mat = ax.matshow(c_matrix, cmap=plt.cm.Blues)  # pylint: disable=no-member
    # Add a color bar to the side of the plot
    fig.colorbar(mat)

    labels = classes if classes else np.arange(c_matrix.shape[0])

    # Label the axes
    ax.set(
        title="Confusion Matrix",
        xlabel="Predicted Label",
        ylabel="True Label",
        xticks=np.arange(n_classes),
        yticks=np.arange(n_classes),
        xticklabels=labels,
        yticklabels=labels,
    )

    # Move the label to the bottom
    ax.xaxis.tick_bottom()

    # Adjust the font size
    ax.xaxis.label.set_size(SIZE)
    ax.yaxis.label.set_size(SIZE)
    ax.title.set_size(SIZE)

    # Set the threshold
    threshold = np.mean((c_matrix.max(), c_matrix.min()))

    # Add text
    # itertools.product: Cartesian product of input iterables.
    # It's equivalent to nested for-loops.
    for i, j in itertools.product(range(c_matrix.shape[0]), range(c_matrix.shape[1])):
        plt.text(
            i,
            j,
            f"{c_matrix[i, j]} ({c_matrix_norm[i, j] * PCT:.2f}%)",
            horizontalalignment="center",
            color=WHITE if c_matrix[i, j] > threshold else BLACK,
            size=SIZE,
        )


def hyperparam_space(
    *, search_grid: GridSearchCV, ylabel: str, ylim: tuple[float, float]
) -> pd.DataFrame:
    """This is used to plot the evaluation metric against the hyperparameter space.
    It returns a DF containing the GridSearchCV best hyperparameter space"""

    imp_vars = ["params", "mean_test_score", "std_test_score"]
    results = pd.DataFrame(search_grid.cv_results_)[imp_vars]

    # Sort the mean_test_scores in descending order and reset the index.
    results.sort_values(by="mean_test_score", ascending=False, inplace=True)
    results.reset_index(drop=True, inplace=True)

    results["mean_test_score"].plot(
        yerr=results["std_test_score"],
        xlabel="Hyperparameter Space",
        ylabel=f"{ylabel}",
        ylim=ylim,
    )

    plt.show()
    return results
