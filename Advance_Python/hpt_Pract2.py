#
#
#

import numpy as np
import pandas as pd

deliveries = pd.Series([27, 29, 26, 31, 28, 25, 30, 27, 29, 28])
CLAIMED = 25


def one_sample_t(values, claimed):
    n = len(values)
    signal = values.mean()-claimed         # TODO: sample average minus the claimed value
    standard_error = values.std() / np.sqrt(n)  # TODO: standard deviation divided by the square root of n
    t = signal / standard_error             # TODO: signal divided by the standard error
    return standard_error, signal, t


standard_error, signal, t = one_sample_t(deliveries, CLAIMED)
print("Standard error:", round(standard_error, 3))
print("Signal:", round(signal, 3))
print("t-statistic:", round(t, 3))
