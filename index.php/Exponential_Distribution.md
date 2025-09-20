---
layout: default
permalink: /index.php/Exponential_Distribution
tags:
- probability
- probability-distributions
- russian
- подготовка-к-шад
title: Exponential Distribution
---
## Exponential Distribution

Плотность вероятности:
- $f(x) = \left\{ \begin{array}{lll} 0 & \mbox{if} & x < 0 \\ \lambda e^{-\lambda x} & \mbox{if} & x \geqslant 0 \end{array} \right.$

- $F(X) = \int_{-\infty}^{x} f(x) dx = \int_{-\infty}^{0} 0 dx + \lambda \int_{0}^{x} e^{-\lambda x} dx = 1 - e^{-\lambda x}$

### Моменты
- $M(X) = \frac{1}{\lambda}$
- $D(X) = \frac{1}{\lambda^2}$
- $M(X) = \sigma(X) = \frac{1}{\lambda}$
