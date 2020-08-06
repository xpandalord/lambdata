# Lambdata
A package with DS helper functions.

## DataFrame Helper

    NAME
        dataframe_helper - Some functions to help cleaning and handling dataframes.

    CLASSES
        builtins.object
            Report

        class Report(builtins.object)
        |  Report(df, target)
        |
        |  Methods defined here:
        |
        |  __init__(self, df, target)
        |      Initialize self.  See help(type(self)) for accurate signature.
        |
        |  plot_confusion_matrix(self, estimator, X, y)
        |      Plot a confusion matrix given the estimator, data matrix, and target vector.
        |
        |  report_fit_predict_score(self, estimator, X_train, y_train, X_val, y_val)
        |      Report the training and validation accuracy.
        |      Returns the fitted estimator and the two prediction arrays.
        |
        |  report_missing_values(self)
        |      Print a pretty report of missing values.
        |
        |  target_split(self, df)
        |      Creates a
        |
        |  train_val_test_split(self)
        |      Spliting the dataframe into train, validation, and test sets.
        |
        |  ----------------------------------------------------------------------
        |  Data descriptors defined here:
        |
        |  __dict__
        |      dictionary for instance variables (if defined)
        |
        |  __weakref__
        |      list of weak references to the object (if defined)