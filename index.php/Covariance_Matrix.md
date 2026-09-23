---
layout: default
permalink: /Covariance_Matrix
tags:
- statistics
- linear-algebra
title: Covariance Matrix
---

## Covariance Matrix
Let $\mathbf X = (\mathbf a_1, \ ... \ , \mathbf a_n)$

The covariance matrix $C$ represents pair-vise Covariances between each $\mathbf a_i$ and $\mathbf a_j$:
- $C_{ij} = \text{cov}(\mathbf a_i, \mathbf a_j)$

Usual way to compute is
- given that $\mathbf a_i$ are columns of $\mathbf X$:
- $C = \cfrac{1}{n-1}\mathbf X^T \mathbf X$

## Sources
- http://www.math.uchicago.edu/~may/VIGRE/VIGRE2009/REUPapers/Mei.pdf
