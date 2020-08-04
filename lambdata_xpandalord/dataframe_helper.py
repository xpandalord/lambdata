"""
Some functions to help cleaning and handling dataframes.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

class Report:
    def __init__(self, df, target):
        self.df = df
        self.target = target

    # Check a dataframe for nulls, print/report them in a nice "pretty" format
    def report_missing_values(self):
        """Print a pretty report of missing values."""

        mis_val = self.df.isnull().sum()

        mis_val_precent = 100 * self.df.isnull().sum() / len(self.df)

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

    def train_val_test_split(self):
        """Spliting the dataframe into train, validation, and test sets."""

        # Split df into train & test. 80/20 split.
        train, test = train_test_split(
            self.df, test_size=0.20, stratify=self.df[self.target], random_state=42
        )

        # Split train into train & val. 80/20 split.
        train, val = train_test_split(
            train, test_size=0.20, stratify=train[self.target], random_state=42
        )

        # return the wrangled dataframe
        return train, val, test

    def target_split(self, df):
        """Creates a """

        # Arrange data into X features matrix and y target vector
        X_df = df.drop(columns=self.target)
        y_df = df[self.target]

        return X_df, y_df

    def report_fit_predict_score(self, estimator, X_train, y_train, X_val, y_val):
        """Report the training and validation accuracy.
        Returns the fitted estimator and the two prediction arrays.
        """

        # Fit model on training data
        best_est = estimator.fit(X_train, y_train)

        # Check performance metric (accuracy) on train, validation, and test sets
        print("Training Accuracy:", best_est.score(X_train, y_train))
        print("Validation Accuracy:", best_est.score(X_val, y_val))

        # Generate prediction values
        y_train_pred = best_est.predict(X_train)
        y_val_pred = best_est.predict(X_val)

        return best_est, y_train_pred, y_val_pred

    # Report a confusion matrix, with labels for easier interpretation
    def plot_confusion_matrix(self, estimator, X, y):
        """Plot a confusion matrix given the estimator, data matrix, and target vector."""

        plot_confusion_matrix(estimator, X, y, values_format='.0f')
