---
layout: default
permalink: /index.php/Poisson_Limit_Theorem
tags:
- probability
title: Poisson Limit Theorem
---
## Poisson Limit Theorem

Suppose $n$ independent trials are performed, in each of which the probability of event $A$ occurring is $p$.

To determine the probability of $k$ occurrences of the event in these trials, one uses the [Bernoulli formula](Bernoulli_Formula). If $p$ is large, one can use the [Laplace asymptotic formula](Laplace_Asymptotic_Formula). However, that formula is also inapplicable when $p \leqslant 0.1$.

If $n$ is large, one can use the Poisson formula.

So, let us find the probability that in a large number of trials the event occurs exactly $k$ times.


- Since the product $np$ remains constant, let $np = \lambda$
- By the Bernoulli formula $P_n(k) = C_n^k p^k (1-p)^{n-k} $
- Since $np = \lambda$, we have $p = \frac{\lambda}{n}$
- $P_n(k) = C_n^k \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n - k}$
- Since $n$ is large, we find $\lim_{k \rightarrow \infty} P_n(k)$ [omitted -- see Gmurman, p. 68]
- We obtain $P_n(k) = \frac{\lambda^k}{k!} e^{-\lambda}$

This formula expresses the Poisson distribution law for the probability of mass ($n$ is large) and rare ($p$ is small) events.



## Example
A factory shipped 5000 items. The probability that an item gets damaged is 0.0002. Find the probability that 3 defective items arrive.

- $n = 5000, p = 0.0002, k = 3$
- $\lambda = np = 5000 \cdot 0.0002 = 1$
- By the Poisson formula, the desired probability is approximately
: $P_{5000}(3) = \lambda^k \frac{e^{-\lambda}}{k!} = \frac{e^{-1}}{3!} = \frac{1}{6e} \approx 0.06$

## See also
- [Bernoulli Formula](Bernoulli_Formula)
- [Poisson Process](Poisson_Process)
- [Poisson Distribution](Poisson_Distribution)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
