"""This module contains decorators."""

import time
from functools import wraps
from typing import Callable


def shape_of_array(func: Callable) -> Callable:
    """This returns the shape of the NumPy array, Pandas
    DataFrame or Series."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        input_ = func(*args, **kwargs)
        print(f"Shape of data: {input_.shape}\n")
        return input_

    return wrapper


def timer(func: Callable) -> Callable:
    """This is used to track the execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        print(f"Duration: {round((stop_time - start_time), 3)} seconds")
        return result

    return wrapper
