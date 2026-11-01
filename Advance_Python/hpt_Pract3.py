#
#
#

import numpy as np
import pandas as pd

wait_times = pd.Series([4.2, 5.1, 3.8, 6.0, 4.5, 5.5, 4.0, 5.2, 4.8, 5.0, 3.9, 4.7])
CLAIMED = 4.0


def one_sample_t(values, claimed):
    n = len(values)                      # TODO: number of values in the sample
    signal = values.mean() - claimed          # TODO: sample average minus the claimed value
    standard_error = 1.0                   # TODO: standard deviation divided by the square root of n
    t = signal / standard_error               # TODO: signal divided by the standard error
    return standard_error, signal, t


standard_error, signal, t = one_sample_t(wait_times, CLAIMED)
print("Standard error:", round(standard_error, 3))
print("Signal:", round(signal, 3))
print("t-statistic:", round(t, 3))
