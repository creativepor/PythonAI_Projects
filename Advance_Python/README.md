# Hypothesis Testing Practice

Two practice scripts that build a **one-sample t-test from scratch** using numpy and pandas.

## What is Hypothesis Testing?

Hypothesis testing is a statistical method for making decisions using data. Instead
of guessing whether a claim is true, you collect a sample and let the numbers tell
you whether the evidence supports the claim or contradicts it.

The idea is simple — you start by assuming a "default" position and then check
whether your sample data gives you enough reason to doubt it:

- **Null hypothesis (H0):** the "no change / no difference" default assumption.
  - Example: "the average delivery time is 25 minutes."
- **Alternative hypothesis (H1):** what you suspect might be true instead.
  - Example: "the average delivery time is not 25 minutes."
- **Test statistic:** a single number (like t) that summarises how far your sample
  sits from the null hypothesis, accounting for sample size and spread.
- **Decision:** compare the test statistic against a threshold (critical value or
  p-value). If the evidence is strong enough, you **reject** H0; otherwise you
  **fail to reject** it (meaning there isn't enough proof to overturn the claim).

### Where is it used?

- **Business & product decisions** — does a new checkout design increase sales
  compared to the old one? (A/B testing is built on hypothesis testing.)
- **Quality control** — does a batch of manufactured parts meet the claimed
  average weight or strength?
- **Healthcare & medicine** — does a new drug lower blood pressure more than a
  placebo? Drug approvals rely on this.
- **Operations** — is a courier's average delivery time really what they claim?
  (Exactly what `hpt_Pract2.py` explores.)
- **Customer service** — are callers really waiting the claimed average time?
  (What `hpt_Pract3.py` checks.)
- **Finance** — is a fund's average return different from the market average?
- **Agriculture & science** — does a new fertilizer produce higher yields than
  the standard one?

In short: anytime you have a claim about an average, rate, or proportion and you
want to verify it with real sample data, hypothesis testing is the tool you reach for.

## What is a one-sample t-test?

A one-sample t-test checks whether the average of your sample data is meaningfully
different from a claimed (or known) average value.

- **Null hypothesis (H0):** the true average equals the claimed value.
- **Alternative (H1):** the true average is different from the claimed value.

The test produces a **t-statistic** — a signal-to-noise ratio. The bigger its
absolute value, the stronger the evidence that the claim is wrong.

## The three core numbers

Every test boils down to three values:

- **Signal** — the gap between your sample average and the claimed average.
  - Formula: `sample_mean - claimed_value`
  - A bigger gap hints the claim might be wrong.

- **Standard error** — the "noise" around the sample average.
  - Formula: `sample_std / sqrt(n)`
  - It shrinks as you collect more data, so bigger samples are more trustworthy.

- **t-statistic** — signal divided by noise.
  - Formula: `signal / standard_error`
  - Tells you how many standard errors the sample mean sits away from the claim.
  - A large |t| means the difference is unlikely to be just random chance.

## Files

### `hpt_Pract2.py` — Courier deliveries

- **Scenario:** a courier service claims an average of 25 deliveries per day.
- **Data:** 10 days of delivery counts.
- **Question:** does the actual daily average support the claim of 25?
- **Complete example** — all TODOs are filled in, so it shows the finished solution.

### `hpt_Pract3.py` — Call center wait times

- **Scenario:** a call center claims callers wait an average of 4.0 minutes.
- **Data:** 12 recorded wait times (in minutes).
- **Question:** is the real average wait time different from 4.0 minutes?
- **Starter code** — only `n` and `signal` are filled in; `standard_error` is left
  as a TODO for you to complete.

## How to run

```bash
python hpt_Pract2.py
python hpt_Pract3.py
```

Each script prints the standard error, signal, and t-statistic (rounded to 3 decimals).

## How to read the result

Once you have the t-statistic, compare its absolute value against a **critical value**
from a t-distribution table (using `n - 1` degrees of freedom):

- If |t| is **larger** than the critical value → reject the claim (the difference is significant).
- If |t| is **smaller** than the critical value → not enough evidence to reject the claim.

## Quick intuition

Signal alone ("the average is 28, the claim is 25") means nothing without knowing
the noise. Dividing signal by noise tells you whether that gap is statistically
real or just normal day-to-day variation.
