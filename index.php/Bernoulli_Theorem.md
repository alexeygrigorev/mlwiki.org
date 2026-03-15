---
layout: default
permalink: /index.php/Bernoulli_Theorem
tags:
- probability
title: Bernoulli Theorem
---
## Bernoulli Theorem
'*Theorem.*' If in each of $n$ independent trials the probability $p$ of event $A$ occurring is constant, then the probability that the deviation of the relative frequency from the probability $p$ will be arbitrarily small is arbitrarily close to one, provided the number of trials is sufficiently large.

$\lim_{n \rightarrow \infty} P\left(\left| \frac{m}{n} - p\right| < \epsilon\right) = 1$

### Proof
- $X_i$ is the number of occurrences of the event in trial $i$. It takes two values:
  - 1: the event occurred
  - 0: the event did not occur
  $P(X_i = 1) = p, P(X_i = 0) = q = 1 - p$
- All variables are pairwise independent (since the trials are independent)
- Their variances are bounded
  $\text{Var}(X_i) = pq$ (since the number of trials $n = 1$) ('*TODO*': link)
  and does not exceed 1/4
  (the product of two factors is maximized when they are equal, i.e. $p = q = 0.5$)
  $\text{Var} \leqslant \frac{1}{4}$, therefore, the variances are bounded by the constant $C = \frac{1}{4}$
- All conditions for applying [Chebyshev's theorem](Weak_Law_of_Large_Numbers) are satisfied, so
  $\lim_{n \rightarrow \infty} P\left(\left|  \frac{X_1 + ... + X_n}{n} - p \right| < \epsilon\right) = 1$ (since for all $\mathbb{E}[X_i]$ the expected value is $\mathbb{E}[X_i] = p$)
- $\frac{1}{n} \sum X_i = \frac{m}{n}$ is the relative frequency of event $A$ occurring, i.e.
  $\lim_{n \rightarrow \infty} P\left(\left|  \frac{m}{n} - p \right| < \epsilon\right) = 1$
'*Q.E.D.*'


## See also
- [Laws of Large Numbers](Laws_of_Large_Numbers)
- [Weak Law of Large Numbers](Weak_Law_of_Large_Numbers)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
