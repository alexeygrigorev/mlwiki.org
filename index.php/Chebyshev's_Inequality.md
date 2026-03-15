---
layout: default
permalink: /index.php/Chebyshev's_Inequality
tags:
- probability
title: Chebyshev's Inequality
---
## Chebyshev's Inequality
The probability that the deviation of a [random variable](Random_Variable) $X$ from its [expected value](Expected_Value) is less than a positive number $\epsilon$ in absolute value is at least $1 - \frac{\text{Var}(X)}{\epsilon^2}$:

$P(| X - \mathbb{E}[X]| < \epsilon) \geqslant 1 - \frac{\text{Var}(X)}{\epsilon^2}$
## Proof

- Consider the event complementary to $| X - \mathbb{E}[X]| < \epsilon$ -- this is the event that the deviation takes a value greater than or equal to $\epsilon$: $|X - \mathbb{E}[X]| \geqslant \epsilon$ |: These two events are complementary: $P(| X - \mathbb{E}[X]| < \epsilon) + P(|X - \mathbb{E}[X]| \geqslant \epsilon) = 1$ |: let us compute $P(| X - \mathbb{E}[X]| \geqslant \epsilon)$
- $\text{Var}(X) = \sum_{i = 1}^n (x_i - \mathbb{E}[X])^2 p_i$ (*)
: all terms of this sum are non-negative
- Drop all $(x_i - \mathbb{E}[X])^2 p_i$ for which $| x_i - \mathbb{E}[X]| < \epsilon$ |: After this, the sum (*) can only decrease
- Assume for convenience that the first $k$ terms are dropped
: $\text{Var}(X) \geqslant \sum_{j = k + 1}^n (x_j - \mathbb{E}[X])^2 p_j$
- $| x_j - \mathbb{E}[X]| \geqslant \epsilon, j = k + 1, ..., n$ (by assumption) |: both sides of the inequality are positive, so $| x_j - \mathbb{E}[X]|^2 \geqslant \epsilon^2$
- Using this, replace each factor with $\epsilon^2$, which only strengthens the inequality. We get
: $\text{Var}(X) \geqslant \epsilon^2 \cdot (p_{k+1} + ... + p_n) = \epsilon^2 \sum_{j = k + 1}^n p_j$
- By the [addition theorem of probabilities](Chain_and_Sum_Rules_in_Probability#Addition_Theorem_of_Probabilities), the sum $\sum_{j = k + 1}^n p_j$ is the probability that $X$ takes one of the values ${x_j}, j = k+1, ..., n$
: For any such $x_j$ the condition $| x_j - \mathbb{E}[X]| \geqslant \epsilon$ is satisfied |: i.e. $\sum_{j = k + 1}^n p_j$ represents the probability $P(| X - \mathbb{E}[X]| \geqslant \epsilon)$
- Therefore we have
: $\text{Var}(X) \geqslant \epsilon^2 \cdot P(| X - \mathbb{E}[X]| \geqslant \epsilon)$ |: or $P(| X - \mathbb{E}[X]| < \epsilon) \geqslant 1 - \frac{\text{Var}(X)}{\epsilon^2}$


## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
