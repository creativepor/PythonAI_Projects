"""Hypothesis testing with scipy only - Z-test and T-test."""

import math
from scipy import stats


def z_test_one_sample(sample, mu0, sigma):
    n = len(sample)
    z = (stats.tmean(sample) - mu0) / (sigma / math.sqrt(n))
    return z, 2 * stats.norm.sf(abs(z))          # two-sided p-value


def t_test_one_sample(sample, mu0):
    res = stats.ttest_1samp(sample, mu0)
    return res.statistic, res.pvalue


def z_test_two_sample(a, b, sigma_a, sigma_b):
    diff = stats.tmean(a) - stats.tmean(b)
    se = math.sqrt(sigma_a**2 / len(a) + sigma_b**2 / len(b))
    z = diff / se
    return z, 2 * stats.norm.sf(abs(z))


def t_test_two_sample(a, b):
    res = stats.ttest_ind(a, b, equal_var=False)   # Welch's t-test
    return res.statistic, res.pvalue


if __name__ == "__main__":
    scores = [72, 75, 68, 80, 74, 69, 77, 71, 73, 76]
    other = [65, 70, 62, 68, 66, 64, 69, 63, 67, 65]

    results = {
        "one-sample Z": z_test_one_sample(scores, 70, 5.0),
        "one-sample T": t_test_one_sample(scores, 70),
        "two-sample Z": z_test_two_sample(scores, other, 5.0, 4.0),
        "two-sample T (Welch)": t_test_two_sample(scores, other),
    }
    for name, (stat, p) in results.items():
        print(f"{name:<22} stat={stat:.4f}  p={p:.4f}")
