"""
Reusable probability utilities for the 1MS041 exam.
"""

from math import factorial


# ── Combinatorics ──────────────────────────────────────────────────────────────

def binomial(n, k):
    """Binomial coefficient C(n, k) = n! / (k! * (n-k)!)"""
    return factorial(n) // (factorial(k) * factorial(n - k))


def binom_pmf(k, n, p):
    """P(X = k) where X ~ Binom(n, p)"""
    return binomial(n, k) * p**k * (1 - p)**(n - k)


def binom_cdf(k, n, p):
    """P(X <= k) where X ~ Binom(n, p)"""
    return sum(binom_pmf(i, n, p) for i in range(0, k + 1))


def binom_sf(k, n, p):
    """P(X > k) where X ~ Binom(n, p)  [survival function]"""
    return 1 - binom_cdf(k, n, p)


def binom_tail(k, n, p):
    """P(X >= k) where X ~ Binom(n, p)"""
    return binom_sf(k - 1, n, p)


# ── Hoeffding Confidence Intervals ────────────────────────────────────────────

import math

def hoeffding_interval(p_hat, n, confidence=0.95):
    """
    Hoeffding-based confidence interval for a bounded [0,1] random variable.

    Given empirical mean p_hat from n samples, returns (lower, upper) such that
    P(|p_hat - p_true| <= epsilon) >= confidence.

    Formula: epsilon = sqrt(log(2 / alpha) / (2n))
    where alpha = 1 - confidence.
    """
    alpha = 1 - confidence
    epsilon = math.sqrt(math.log(2 / alpha) / (2 * n))
    return (max(0.0, p_hat - epsilon), min(1.0, p_hat + epsilon))


def hoeffding_epsilon(n, confidence=0.95):
    """Return the half-width epsilon of a Hoeffding interval."""
    alpha = 1 - confidence
    return math.sqrt(math.log(2 / alpha) / (2 * n))
