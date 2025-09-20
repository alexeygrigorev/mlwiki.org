---
layout: default
permalink: /index.php/Distribution_Function
tags:
- distributions
- probability
title: Distribution Function
---
{{stub}}

## (Cumulative) [Distribution](Distribution) Function
A ''distribution function'' $F_X(x)$ (''Функция распределения'') 
- is a function that defines the [Probability](Probability) of a [Random Variable](Random_Variable) $X$ having values less than $x$
- i.e. $F_X(x) = P(X < x)$
- this, $F_X(x)$ defines the probability of $X$ taking value on the left of $x$
- for continuous - the area under the [Probability Density Function](Probability_Density_Function) from $-\infty$ to $x$
- it describes the [Distribution](Distribution) of $X$


## Properties
### Property 1: Sum of Probabilities
$0 \leqslant F(x) \leqslant 1$

### Property 2: Monotonicity
$F_X(x)$ - monotonic non-increasing function (неубывающая)
- $\Rightarrow$ $P(a \leqslant X \leqslant b) = F_X(a) - F_X(b)$

### Property 3
if $\text{Dom}(X) = (a, b)$ (continuous)
- $F_X(x) = 0$ when $x < a$
- $F_X(x) = 1$ when $x \geqslant b$


## Probability Density Function
A ''density'' of $F_X(x)$ is a function $f_X(x)$ s.t.
- $f_X(x) = F_X'(x)$

The probability that $X$ will take some value from interval $(a, b)$
- $P(a < X < b) = \int_a^b f_X(x) dx$

The cumulate distribution function $F_X(x)$ can be found by taking an integral of $f_X(x)$
- $F_X(x) = \int_{-\infty}^x f_X(x) dx$


## Sources
- Гмурман В.Е., Теория вероятностей и математическая статистика -- 9-е издание. М.: Высш. шк., 2003.
- http://en.wikipedia.org/wiki/Probability_distribution
- http://en.wikipedia.org/wiki/Cumulative_distribution_function
- http://en.wikipedia.org/wiki/Probability_density_function
