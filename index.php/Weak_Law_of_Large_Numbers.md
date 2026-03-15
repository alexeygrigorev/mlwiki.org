---
layout: default
permalink: /index.php/Weak_Law_of_Large_Numbers
tags:
- probability
title: Weak Law of Large Numbers
---
## Weak Law of Large Numbers

(Chebyshev's Theorem)

**Theorem.** If $X_1, ..., X_n$ are pairwise independent random variables whose variances are uniformly bounded (i.e., do not exceed some constant $C$), then, no matter how small $\epsilon$ is, the probability that

$\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon$
will be arbitrarily close to one, provided the number of random variables is sufficiently large.

Or,

$\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon\right) = 1$

### Proof

- Consider the random variable $\bar{X} = \frac{X_1 + ... + X_n}{n}$
- Find $\mathbb{E}[\bar{X}] = \mathbb{E}\left[\frac{X_1 + ... + X_n}{n}\right] = \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n}$
- Applying [Chebyshev's Inequality](Chebyshev's_Inequality) to $\bar{X}$, we get
: $P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon\right) \geqslant 1 - \frac{\text{Var}\left(\frac{X_1 + ... + X_n}{n}\right)}{\epsilon^2}$
- Since $X_1, ..., X_n$ are independent,
: $\text{Var}\left(\frac{X_1 + ... + X_n}{n}\right) = \frac{\text{Var}(X_1) + ... + \text{Var}(X_n)}{n^2}$
- All variances $\text{Var}(X_i)$ are bounded by the constant $C$: $\text{Var}(X_i) \leqslant C$, therefore
: $\frac{\text{Var}(X_1) + ... + \text{Var}(X_n)}{n^2} \leqslant \frac{C + ... + C}{n^2} = \frac{nC}{n^2} = \frac{C}{n}$
: i.e. $\text{Var}\left(\frac{X_1 + ... + X_n}{n}\right) \leqslant \frac{C}{n}$
- Substituting into the inequality, we have
: $P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon\right) \geqslant 1 - \frac{C}{n \epsilon^2}$
- Taking the limit as $n \rightarrow \infty$, we get
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon\right) \geqslant 1$ |: since probability cannot exceed one, we obtain equality
: $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - \frac{\mathbb{E}[X_1] + ... + \mathbb{E}[X_n]}{n} \right| < \epsilon\right) = 1$
**Q.E.D.**



If all random variables $X_i$ have the same expected value $a$, the formula becomes
$\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - a \right| < \epsilon\right) = 1$

## Significance
Individual random variables may have significant spread, but their arithmetic mean has little dispersion, and one can predict what value it will take.

In other words, the arithmetic mean of a sufficiently large number of independent random variables loses its random character. This is because the deviations of each random variable from its expected value can be both positive and negative, and in the arithmetic mean they cancel each other out.


## See also
- [Chebyshev's Inequality](Chebyshev's_Inequality)
- [Laws of Large Numbers](Laws_of_Large_Numbers)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
