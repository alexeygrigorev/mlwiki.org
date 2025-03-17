---
title: Multinomial Distribution
layout: default
permalink: /index.php/Multinomial_Distribution
---

# Multinomial Distribution

{{stub}}

## Multinomial Distribution
It's an extension of [Binomial Distribution](Binomial_Distribution)


## [Maximum Likelihood Estimator](Maximum_Likelihood_Estimator)
- consider log likelihood function: $\log P(D \mid \theta) = \sum_{w \in V} c(w, D) \, \log P(w \mid \theta)$ 
- we want to maximize it s.t. $P(w \mid \theta)$ is a [Probability Distribution](Probability_Distribution) i.e. $\sum_{w \in V} P(w \mid \theta) = 1$
- use [Lagrange Multipliers](Lagrange_Multipliers) to convert this constrained optimization problem into an unconstrained one
- so let $L(\theta, \lambda) = \log P(D \mid \theta) + \lambda \left(1 - \sum P(w \mid \theta) \right) = \sum_{w \in V} c(w, D) \, \log P(w \mid \theta) + \lambda \left(1 - \sum P(w \mid \theta) \right)$ 
- by solving it, we get $P(w \mid \hat \theta) = \cfrac{c(w, D)}

## Sources
- Zhai, ChengXiang. "Statistical language models for information retrieval." 2008.


[Category:Distributions](Category_Distributions)