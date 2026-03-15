---
layout: default
permalink: /index.php/Variance
tags:
- probability
title: Variance
---
## Motivation
[Expected Value](Expected_Value) can't describe a possible range of values for a [Random Variable](Random_Variable)

Consider the following two RVs

<table>
<tr>
<td>
|   $X$ !! -0.1  |  0.1  |   $p$ !!  0.5  |  0.5 |</td> |<td>
|   $Y$ !! -100  |  100  |   $p$ !!  0.5  |  0.5 |</td> |</tr>
</table>

In both cases $\mathbb{E}[X] = \mathbb{E}[Y] = 0$
- but values for $X$ are close to the expected value, and values of $Y$ are far


### Deviation
*Deviation of a Random Variable* - the absolute difference between the value of an RV and its expected value

The deviation is sometimes called a centered variable and denoted $\dot{X}$

Since $E\big[X - E[X] \big] = 0$, we need another way to describe the spread of some RV


## Variance
*Variance of a Random Variable* is a measure of spread that describes how far away values get from the expected value

$\text{Var}[X] = E \big[X - E[X] \big]^2 = \big[x_1 - E[X] \big]^2 \cdot p_1 + \big[x_2 - E[X] v]^2 \cdot p_2 + ... + \big[x_n - E[X] \big]^2 \cdot p_n$


### Formula for computing variance
**Theorem.** The variance equals the difference between the expected value of the square of the random variable and the square of its expected value:

$\text{Var}[X] = E[X^2] - E^2[X]$ (meaning $E[X^2] - (E[X])^2$)

Proof:
- $\text{Var} [X] = E\big[X - E[X]\big]^2 = ... $
- $... = E\big[X^2 - 2X \cdot E[X] + E^2 [X]\big] = ...$
- $... = E[X^2] - 2E[X] \cdot E[X] + E^2(X) = ...$
- $... = E[X^2] - 2E^2[X] + E^2[X] = E[X^2] - E^2[X]$


### Properties
1. $\text{Var}(C) = 0$
1. $\text{Var}(C \cdot X) = C^2 \cdot \text{Var}(X)$
1. $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2[E(XY) - E(X)E(Y)]$
1. : If $X$ and $Y$ are independent, then $E(XY) = E(X)E(Y)$ and $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$
1. : $E(XY) - E(X)E(Y)$ is also called [covariance](Correlation#Covariance)
1. for independent $X$ and $Y$ $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)$ ($\text{Var}(X - Y) = \text{Var}(X + (-1) Y) = \text{Var}(X) + (-1)^2 \text{Var}(Y)$)


## Standard Deviation
$\sigma(X) = \sqrt{ \text{Var} [X] }$


The variance has the dimension equal to the square of the dimension of the random variable, while the standard deviation has the same dimension as the variable itself.

- $\text{Var}(x) = \cfrac{1}{n - 1} \sum (x_i - \bar{x})^2$
- $s(x) = \text{std}(x) = \sqrt{\text{Var}(x)}$

($n - 1$ gives "unbiased" estimate of the variance <!-- TODO: add link -->)
in R:
```text only
st.dev = sd(data)
```


## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
