"""
Some functions to help cleaning and handling dataframes.
"""

import pandas as pd


class Report:
    def __init__(self, df):
        self.df = df

    # Check a dataframe for nulls, print/report them in a nice "pretty" format
    def report_missing_values(self):
        """Print a pretty report of missing values."""

        mis_val = self.df.isnull().sum()

        mis_val_precent = 100 * self.df.isnull().sum() / len(df)

        mz_table = pd.concat([mis_val, mis_val_precent], axis=1)

        mz_table = mz_table.rename(
            columns={0: "Missing Values", 1: "% of Total Values"}
        )

        mz_table = mz_table.sort_values("% of Total Values", ascending=False)

        print(
            "Your selected dataframe has "
            + str(self.df.shape[1])
            + " columns and "
            + str(self.df.shape[0])
            + " Rows."
        )

        print(
            "There are " + str(mz_table.shape[0]) + " columns that have missing values."
        )

        return mz_table

    # Report a confusion matrix, with labels for easier interpretation
    def report_confusion_matrix(actual, predicted):
        """Plot a confusion matrix given the actual values and predicted values."""

        data = {"y_Actual": actual, "y_Predicted": predicted}

        df = pd.DataFrame(data, columns=["y_Actual", "y_Predicted"])

        confusion_matrix = pd.crosstab(
            df["y_Actual"],
            df["y_Predicted"],
            rownames=["Actual"],
            colnames=["Predicted"],
        )
        print(confusion_matrix)
