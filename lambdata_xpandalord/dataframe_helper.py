
"""
Some functions to help cleaning and handling dataframes.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix

# Check a dataframe for nulls, print/report them in a nice "pretty" format
def report_missing_values(df):
    """Print a pretty report of missing values."""

    mis_val = df.isnull().sum()

    mis_val_precent = 100 * df.isnull().sum() / len(df)

    mz_table = pd.concat([mis_val, mis_val_precent], axis=1)

    mz_table = mz_table.rename(columns = {0 : 'Missing Values', 1 : '% of Total Values'})

    mz_table = mz_table.sort_values('% of Total Values', ascending=False)

    print('Your selected dataframe has ' + str(df.shape[1]) + ' columns and ' + str(df.shape[0]) + ' Rows.')

    print('There are ' + str(mz_table.shape[0]) + ' columns that have missing values.')

    return mz_table

# Report a confusion matrix, with labels for easier interpretation
def report_confusion_matrix(data, target, estimator):
    """Plot a confusion matrix given an estimator, target, and data."""
    plot_confusion_matrix(estimator, data, target, values_format='.0f')