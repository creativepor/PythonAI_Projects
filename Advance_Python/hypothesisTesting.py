"""
Hypothesis Testing from scratch: Z-Test and T-Test
==================================================
Every value (test statistic + p-value) is computed from its formula.
Only the Python standard library is used, so nothing extra to install.

Distributions used for the p-values are also built from formulas:
  * Normal CDF  -> math.erf
  * Student's t -> regularized incomplete beta function (continued fraction)
"""

import math
import statistics

from scipy import stats


# ---------------------------------------------------------------------------
# Distribution helpers (pure Python)
# ---------------------------------------------------------------------------
def normal_cdf(z):
    """Standard normal CDF:  P(Z <= z) = 0.5 * (1 + erf(z / sqrt(2)))."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _betacf(a, b, x):
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    MAXIT, EPS, FPMIN = 200, 3.0e-12, 1.0e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def _betai(a, b, x):
    """Regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = math.exp(
        math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        + a * math.log(x) + b * math.log(1.0 - x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def t_cdf(t, df):
    """Student's t CDF with df degrees of freedom: P(T <= t)."""
    x = df / (df + t * t)
    ib = 0.5 * _betai(0.5 * df, 0.5, x)
    return 1.0 - ib if t > 0 else ib


# ---------------------------------------------------------------------------
# p-value from a test statistic
# ---------------------------------------------------------------------------
def _p_value(stat, cdf, alternative):
    """Turn a test statistic into a p-value for the chosen alternative."""
    if alternative == "two-sided":
        return 2.0 * (1.0 - cdf(abs(stat)))
    if alternative == "greater":          # H1: mean > mu0
        return 1.0 - cdf(stat)
    if alternative == "less":             # H1: mean < mu0
        return cdf(stat)
    raise ValueError("alternative must be 'two-sided', 'greater' or 'less'")


# ---------------------------------------------------------------------------
# ONE-SAMPLE tests
# ---------------------------------------------------------------------------
def z_test_one_sample(sample, pop_mean, pop_std, alternative="two-sided"):
    """
    One-sample Z-test (population std KNOWN).

        z = (x_bar - mu0) / (sigma / sqrt(n))
    """
    n = len(sample)
    x_bar = statistics.mean(sample)
    std_error = pop_std / math.sqrt(n)
    z = (x_bar - pop_mean) / std_error
    return {
        "test": "one-sample Z-test",
        "n": n,
        "sample_mean": x_bar,
        "std_error": std_error,
        "statistic": z,
        "p_value": _p_value(z, normal_cdf, alternative),
    }


def t_test_one_sample(sample, pop_mean, alternative="two-sided"):
    """
    One-sample T-test (population std UNKNOWN, use sample std s).

        t = (x_bar - mu0) / (s / sqrt(n)),   df = n - 1
    """
    n = len(sample)
    x_bar = statistics.mean(sample)
    s = statistics.stdev(sample)          # ddof = 1
    std_error = s / math.sqrt(n)
    t = (x_bar - pop_mean) / std_error
    df = n - 1
    return {
        "test": "one-sample T-test",
        "n": n,
        "sample_mean": x_bar,
        "sample_std": s,
        "std_error": std_error,
        "df": df,
        "statistic": t,
        "p_value": _p_value(t, lambda x: t_cdf(x, df), alternative),
    }


# ---------------------------------------------------------------------------
# TWO-SAMPLE tests
# ---------------------------------------------------------------------------
def z_test_two_sample(sample1, sample2, pop_std1, pop_std2, alternative="two-sided"):
    """
    Two-sample Z-test (population stds KNOWN).

        z = (x_bar1 - x_bar2) / sqrt(sigma1^2/n1 + sigma2^2/n2)
    """
    n1, n2 = len(sample1), len(sample2)
    d = statistics.mean(sample1) - statistics.mean(sample2)
    std_error = math.sqrt(pop_std1**2 / n1 + pop_std2**2 / n2)
    z = d / std_error
    return {
        "test": "two-sample Z-test",
        "n1": n1, "n2": n2,
        "mean_diff": d,
        "std_error": std_error,
        "statistic": z,
        "p_value": _p_value(z, normal_cdf, alternative),
    }


def t_test_two_sample(sample1, sample2, alternative="two-sided"):
    """
    Two-sample T-test (Welch's, population stds UNKNOWN).

        t  = (x_bar1 - x_bar2) / sqrt(s1^2/n1 + s2^2/n2)
        df = (s1^2/n1 + s2^2/n2)^2 /
             ( (s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1) )
    """
    n1, n2 = len(sample1), len(sample2)
    s1, s2 = statistics.stdev(sample1), statistics.stdev(sample2)
    d = statistics.mean(sample1) - statistics.mean(sample2)
    v1, v2 = s1**2 / n1, s2**2 / n2
    std_error = math.sqrt(v1 + v2)
    t = d / std_error
    df = (v1 + v2) ** 2 / (v1**2 / (n1 - 1) + v2**2 / (n2 - 1))
    return {
        "test": "two-sample T-test (Welch)",
        "n1": n1, "n2": n2,
        "mean_diff": d,
        "std_error": std_error,
        "df": df,
        "statistic": t,
        "p_value": _p_value(t, lambda x: t_cdf(x, df), alternative),
    }


# ---------------------------------------------------------------------------
# SCIPY versions
# ---------------------------------------------------------------------------
def _z_p_value(z, alternative):
    """p-value for a z statistic using scipy.stats.norm."""
    if alternative == "two-sided":
        return 2.0 * stats.norm.sf(abs(z))
    if alternative == "greater":
        return stats.norm.sf(z)
    if alternative == "less":
        return stats.norm.cdf(z)
    raise ValueError("alternative must be 'two-sided', 'greater' or 'less'")


def z_test_one_sample_scipy(sample, pop_mean, pop_std, alternative="two-sided"):
    """One-sample Z-test; same formula, p-value from scipy.stats.norm."""
    n = len(sample)
    x_bar = statistics.mean(sample)
    std_error = pop_std / math.sqrt(n)
    z = (x_bar - pop_mean) / std_error
    return {
        "test": "one-sample Z-test (scipy)",
        "n": n,
        "sample_mean": x_bar,
        "std_error": std_error,
        "statistic": z,
        "p_value": _z_p_value(z, alternative),
    }


def t_test_one_sample_scipy(sample, pop_mean, alternative="two-sided"):
    """One-sample T-test computed by scipy.stats.ttest_1samp."""
    res = stats.ttest_1samp(sample, pop_mean, alternative=alternative)
    n = len(sample)
    s = statistics.stdev(sample)
    return {
        "test": "one-sample T-test (scipy)",
        "n": n,
        "sample_mean": statistics.mean(sample),
        "sample_std": s,
        "std_error": s / math.sqrt(n),
        "df": n - 1,
        "statistic": res.statistic,
        "p_value": res.pvalue,
    }


def z_test_two_sample_scipy(sample1, sample2, pop_std1, pop_std2, alternative="two-sided"):
    """Two-sample Z-test; same formula, p-value from scipy.stats.norm."""
    n1, n2 = len(sample1), len(sample2)
    d = statistics.mean(sample1) - statistics.mean(sample2)
    std_error = math.sqrt(pop_std1**2 / n1 + pop_std2**2 / n2)
    z = d / std_error
    return {
        "test": "two-sample Z-test (scipy)",
        "n1": n1, "n2": n2,
        "mean_diff": d,
        "std_error": std_error,
        "statistic": z,
        "p_value": _z_p_value(z, alternative),
    }


def t_test_two_sample_scipy(sample1, sample2, alternative="two-sided"):
    """Two-sample T-test (Welch) computed by scipy.stats.ttest_ind."""
    res = stats.ttest_ind(sample1, sample2, equal_var=False, alternative=alternative)
    n1, n2 = len(sample1), len(sample2)
    s1, s2 = statistics.stdev(sample1), statistics.stdev(sample2)
    v1, v2 = s1**2 / n1, s2**2 / n2
    return {
        "test": "two-sample T-test (Welch, scipy)",
        "n1": n1, "n2": n2,
        "mean_diff": statistics.mean(sample1) - statistics.mean(sample2),
        "std_error": math.sqrt(v1 + v2),
        "df": (v1 + v2) ** 2 / (v1**2 / (n1 - 1) + v2**2 / (n2 - 1)),
        "statistic": res.statistic,
        "p_value": res.pvalue,
    }


# ---------------------------------------------------------------------------
# Report helper
# ---------------------------------------------------------------------------
def report(result, alpha=0.05):
    """Print a result dict and the reject / fail-to-reject decision."""
    print(f"\n{result['test']}")
    print("-" * len(result["test"]))
    for key, value in result.items():
        if key in ("test", "statistic", "p_value"):
            continue
        label = key.replace("_", " ").capitalize()
        text = f"{value:.4f}" if isinstance(value, float) else f"{value}"
        print(f"  {label:<12}: {text}")
    print(f"  Statistic   : {result['statistic']:.4f}")
    print(f"  P-value     : {result['p_value']:.4f}")
    print(f"  Decision (alpha={alpha}): "
          + ("REJECT H0" if result["p_value"] < alpha else "FAIL TO REJECT H0"))


if __name__ == "__main__":
    # ----- Example data -----------------------------------------------------
    # Class scores (unknown population std)
    scores = [72, 75, 68, 80, 74, 69, 77, 71, 73, 76]
    # Known population std for the Z-test
    pop_std_known = 5.0
    # Hypothesised population mean
    mu0 = 70.0

    # 1) One-sample Z-test (sigma known)
    report(z_test_one_sample(scores, mu0, pop_std_known))
    report(z_test_one_sample_scipy(scores, mu0, pop_std_known))

    # 2) One-sample T-test (sigma estimated from the sample)
    report(t_test_one_sample(scores, mu0))
    report(t_test_one_sample_scipy(scores, mu0))

    # ----- Two-sample example ----------------------------------------------
    group_a = [72, 75, 68, 80, 74, 69, 77, 71, 73, 76]
    group_b = [65, 70, 62, 68, 66, 64, 69, 63, 67, 65]

    # 3) Two-sample Z-test (both population stds known)
    report(z_test_two_sample(group_a, group_b, 5.0, 4.0))
    report(z_test_two_sample_scipy(group_a, group_b, 5.0, 4.0))

    # 4) Two-sample T-test (Welch's)
    report(t_test_two_sample(group_a, group_b))
    report(t_test_two_sample_scipy(group_a, group_b))
