# Probability & Bayes — Cheat Sheet

## Binomial Distribution
$X \sim \text{Binom}(n, p)$: number of successes in $n$ independent Bernoulli$(p)$ trials.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

$$\mathbb{E}[X] = np \qquad \text{Var}(X) = np(1-p)$$

**In Python (from scratch):**
```python
from math import factorial
def binom_pmf(k, n, p):
    C = factorial(n) // (factorial(k) * factorial(n-k))
    return C * p**k * (1-p)**(n-k)
```

**With scipy:**
```python
from scipy.stats import binom
binom.pmf(k, n, p)   # P(X = k)
binom.cdf(k, n, p)   # P(X <= k)
binom.sf(k, n, p)    # P(X > k)
binom.sf(k-1, n, p)  # P(X >= k)  ← most useful
```

---

## Conditional Probability & Bayes

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

$$P(A \cap B) = P(A \mid B) \cdot P(B)$$

**Law of Total Probability** (marginalising over $X$):
$$P(B) = \sum_x P(B \mid X = x) \cdot P(X = x)$$

**Bayes' Theorem:**
$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

---

## Hierarchical / Compound Distributions

When $Z \mid N \sim \text{Binom}(20-N, \tfrac{1}{2})$ and $N \sim \text{Binom}(20, p)$:

$$P(Y \geq T) = \sum_{n=0}^{20} P(N=n) \cdot P(Z \geq T-n \mid N=n)$$

$$P(N < 10 \mid Y \geq T) = \frac{\sum_{n=0}^{9} P(N=n) \cdot P(Z \geq T-n \mid N=n)}{\sum_{n=0}^{20} P(N=n) \cdot P(Z \geq T-n \mid N=n)}$$

**Key pattern:** whenever a random variable is defined conditionally on another,
sum over all possible values of the conditioning variable (law of total probability).

---

## Hoeffding's Inequality

For i.i.d. random variables $X_i \in [a, b]$ with empirical mean $\bar{X}_n$:

$$P\!\left(\bar{X}_n - \mu \geq \epsilon\right) \leq e^{-2n\epsilon^2/(b-a)^2}$$

**Two-sided confidence interval** at level $1 - \alpha$:

$$\epsilon = \sqrt{\frac{(b-a)^2 \ln(2/\alpha)}{2n}}$$

For $[0,1]$-valued variables $(b-a=1)$: $\quad\epsilon = \sqrt{\dfrac{\ln(2/\alpha)}{2n}}$

**CI:** $\hat{p} \pm \epsilon$, clipped to $[0, 1]$.

**Common values:**
| Confidence | $\alpha$ | $\ln(2/\alpha)$ |
|---|---|---|
| 90% | 0.10 | 2.996 |
| 95% | 0.05 | 3.689 |
| 99% | 0.01 | 5.298 |

```python
import math
def hoeffding_epsilon(n, confidence=0.95):
    alpha = 1 - confidence
    return math.sqrt(math.log(2 / alpha) / (2 * n))
```
