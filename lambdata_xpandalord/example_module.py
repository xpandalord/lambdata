import numpy as np
import pandas as pd

raw_data = {
    "first_name": ["Jason", "Rachel", "Tina", "Jake", "Amy"],
    "last_name": ["Miller", "Williams", "Brown", "Milner", "Cooze"],
    "age": [22, 21, 23, 24, 25],
    "sex": ["m", "f", "f", "m", "f"],
    "Test1_Score": [4, 5, 2, 1, 3],
    "Test2_Score": [2, 2, 4, 5, 1],
}
results = pd.DataFrame(
    raw_data,
    columns=[
        "first_name",
        "last_name",
        "age",
        "sex",
        "Test1_Score",
        "Test2_Score",
    ],
)

COLORS = ("Blue", "Orange", "Red", "Green", "Violet", "Cyan")


def increment(number):
    """Increases a given number by 1."""
    return number + 1
