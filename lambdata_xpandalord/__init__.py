"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
import lambdata_xpandalord.dataframe_helper


TEST = pd.DataFrame(np.ones(10))


def increment(number):
    """Increases a given number by 1."""
    return number + 1
