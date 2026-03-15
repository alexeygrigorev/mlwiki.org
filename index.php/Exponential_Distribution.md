---
layout: default
permalink: /index.php/Exponential_Distribution
tags:
- probability
- probability-distributions
title: Exponential Distribution
---
## Exponential Distribution

Probability density function:
- $f(x) = \left\{ \begin{array}{lll} 0 & \mbox{if} & x < 0 \\ \lambda e^{-\lambda x} & \mbox{if} & x \geqslant 0 \end{array} \right.$

- $F(X) = \int_{-\infty}^{x} f(x) dx = \int_{-\infty}^{0} 0 dx + \lambda \int_{0}^{x} e^{-\lambda x} dx = 1 - e^{-\lambda x}$

### Moments
- $\mathbb{E}[X] = \frac{1}{\lambda}$
- $\text{Var}(X) = \frac{1}{\lambda^2}$
- $\mathbb{E}[X] = \sigma(X) = \frac{1}{\lambda}$
