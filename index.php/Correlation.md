---
layout: default
permalink: /index.php/Correlation
tags:
- probability
title: Correlation
---
## Independent Random Variables
If $X$ and $Y$ are independent, then the distribution of one does not affect the value of the other. Otherwise, the random variables are called dependent.


## Covariance
Covariance is a measure of the linear dependence of two random variables.

$\text{cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X]) \cdot (Y - \mathbb{E}[Y])] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$


### Boundedness of Covariance
**Theorem.**
The absolute value of the covariance of two random variables $X$ and $Y$ does not exceed $\sigma(X) \sigma(Y)$

$| \text{cov}(X, Y)| \leqslant \sigma(X) \sigma(Y)$

**Proof.** Consider two random variables $Z_1 = \sigma(Y) X - \sigma(X) Y$ and $Z_2 = \sigma(Y) X + \sigma(X) Y$


<details>
<summary>Derivation of $\text{Var}(Z_1) = 2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$</summary>

- $\text{Var}(Z_1) = \mathbb{E}[Z_1]^2 - \mathbb{E}^2[Z_1] = \mathbb{E}[\sigma(Y) X - \sigma(X) Y]^2 - \mathbb{E}^2[\sigma(Y) X - \sigma(X) Y] = $
- $\mathbb{E}[\sigma^2(Y) X^2 - 2\sigma(X)\sigma(Y)XY + \sigma^2(X) Y^2] + [\sigma(Y) \mathbb{E}[X] - \sigma(X) \mathbb{E}[Y]]^2 = $
- $\sigma^2(Y) \mathbb{E}[X^2] - 2\sigma(X)\sigma(Y) \mathbb{E}[XY] + \sigma^2(X) \mathbb{E}[Y^2]$ $ - \sigma^2(Y) \mathbb{E}^2[X] - \sigma(X)\sigma(Y) \mathbb{E}[X]\mathbb{E}[Y] + \sigma^2(X) \mathbb{E}^2[Y] = $
- $\sigma^2(Y)(\mathbb{E}[X^2] - \mathbb{E}^2[X]) - $ $ 2\sigma(X)\sigma(Y) (\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]) + \sigma^2(X)(\mathbb{E}[Y^2] - \mathbb{E}^2[Y]) =$
- $2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$
</details>


Similarly, $\text{Var}(Z_2) = 2\sigma^2(X)\sigma^2(Y) + 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$


Since any variance is non-negative, we obtain:
- $\text{Var}(Z_1) \geqslant 0$
- $2\sigma^2(X)\sigma^2(Y) - 2\sigma(X)\sigma(Y) \text{cov}(X, Y) \geqslant 0$
- $2\sigma^2(X)\sigma^2(Y) \geqslant 2\sigma(X)\sigma(Y) \text{cov}(X, Y)$
- $\text{cov}(X, Y) \leqslant \sigma(X)\sigma(Y)$

Similarly, for $\text{Var}(Z_2)$
- $2\sigma^2(X)\sigma^2(Y) + 2\sigma(X)\sigma($Y) \text{cov}(X, Y) \geqslant 0
- $\text{cov}(X, Y)  \geqslant -\sigma(X)\sigma(Y)$

That is, $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$.
**Q.E.D.**


### Properties of Covariance
- Covariance is symmetric
: $\text{cov}(X, Y) = \text{cov}(Y, X)$
- Covariance is bounded (see the theorem)
: $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$
- The covariance of a variable with itself is its variance
: $\text{cov}(X, X) = \mathbb{E}[X^2] - \mathbb{E}^2[X] = \text{Var}(X)$
- $\text{cov}(100 \cdot X, Y) = 100 \cdot \text{cov}(X, Y)$
- If $X$ and $Y$ are independent, then $\text{cov}(X, Y) = 0$


### Interpretation
- If the covariance is positive, then as one random variable increases, the values of the other random variable tend to increase as well; if the covariance is negative, they tend to decrease.


## Correlation
The absolute value of the covariance alone does not tell us how strongly the variables are related, since its scale depends on the variances.

However, the scale can be normalized by dividing by $\sigma(X) \sigma(Y)$, thus obtaining the *linear correlation coefficient* (also known as Pearson's correlation coefficient).

$r(X, Y) = r = \cfrac{\text{cov}(X, Y)}{\sigma(X) \sigma(Y)}$


Since $| \text{cov}(X, Y)| \leqslant \sigma(X)\sigma(Y)$, it follows that $-1 \leqslant r \leqslant 1$

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
- http://ru.wikipedia.org/wiki/Covariance
- http://ru.wikipedia.org/wiki/Correlation
