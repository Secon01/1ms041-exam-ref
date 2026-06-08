"""
2022 Exam — Problem 1: Probability Warmup (8 points)

Setup:
  N ~ Binom(20, 11/20)   — number of questions the student KNOWS
  Z | N ~ Binom(20-N, 1/2) — number of questions correctly GUESSED
  Y = N + Z              — total correct answers
  Threshold T: student passes if Y >= T

Part 1 (5p): For each T in {0,...,20}, compute P(N < 10 | Y >= T)
Part 2 (3p): Find the smallest T such that P(N >= 10 | Y >= T) >= 0.90
"""

from math import factorial


def binomial(n, k):
    """Binomial coefficient C(n, k)."""
    return factorial(n) // (factorial(k) * factorial(n - k))


# PMF of N ~ Binom(20, 11/20)
p = 11 / 20
p_N = lambda n: binomial(20, n) * (1 - p) ** (20 - n) * p ** n


def p_Y_T_N(T, n):
    """
    P(Z >= T-n | N=n) where Z ~ Binom(20-n, 1/2).
    = P(Y >= T | N=n)
    """
    total = 0
    for z in range(max(0, T - n), 20 - n + 1):
        total += binomial(20 - n, z) * (0.5) ** (20 - n)
    return total


def prob_numerator(T):
    """P(N < 10 and Y >= T)"""
    total = 0
    for n in range(0, 10):          # N < 10
        total += p_N(n) * p_Y_T_N(T, n)
    return total


def prob_denominator(T):
    """P(Y >= T)"""
    total = 0
    for n in range(0, 21):          # all N
        total += p_N(n) * p_Y_T_N(T, n)
    return total


# Part 1 — P(N < 10 | Y >= T) for each T
problem11_probabilities = [prob_numerator(t) / prob_denominator(t) for t in range(0, 21)]

# Part 2 — smallest T such that P(N >= 10 | Y >= T) >= 0.90
#         equivalent to: P(N < 10 | Y >= T) <= 0.10
smallest_t = 0
for t in range(0, 21):
    if problem11_probabilities[t] <= 0.10:
        smallest_t = t
        break

problem12_T = smallest_t  # Answer: 17
