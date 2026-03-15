---
layout: default
permalink: /index.php/Hypergeometric_Distribution
tags:
- probability
- probability-distributions
title: Hypergeometric Distribution
---
## Hypergeometric Distribution

Suppose a batch of $N$ items contains $M$ standard items ($M < N$). From the batch, $n$ items are selected without replacement.

$X$ is a random variable representing the number $m$ of standard items among the $n$ selected. Possible values of $X: 0, 1, ..., \min(M, n)$


The probability that $X = m$:
- The total number of outcomes is $C_N^n$
- The number of outcomes favorable to $X = m$:

$C_M^m \cdot C_{N - M}^{m - n}$

(the number of ways to select $m$ from $M$ multiplied by the number of ways to select the remaining non-standard items)


Thus,

$P(X = m) = \frac{C_M^m \cdot C_{N - M}^{m - n}}{C_N^n}$

This formula defines the ''hypergeometric distribution''.


### Example
Among 50 items, 20 are painted. Find the probability that out of 5 drawn items, 3 will be painted.

- $N = 50, M = 20, n = 5, m = 3$
- $P(X = 3) = \frac{C_{20}^3 \cdot C_{30}^2}{C_{50}^5} = 0.234$

## See also
- [Geometric Distribution](Geometric_Distribution)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
