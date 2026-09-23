---
layout: default
permalink: /index.php/Inverse_Iteration
tags:
- linear-algebra
title: Inverse Iteration
---
## Inverse Iteration

Inverse Iteration is a method for finding an eigenvector of a matrix $A$ for a known approximate eigenvalue $m$ :

- it's [Power Iteration](Power_Iteration) applied to $(A - m I)^{-1}$
- at each step the system $(A - m I) \, \mathbf x_{k+1} = \mathbf x_k$ is solved, e.g. with [LU Decomposition](LU_Decomposition), which can be computed once and then reused
- the eigenvalue of $(A - m I)^{-1}$ that has the largest magnitude is $1 / (\lambda - m)$, so the method converges to the eigenvector of the eigenvalue $\lambda$ closest to $m$

It's used in the [QR Algorithm](QR_Algorithm) for computing the eigenvectors once the eigenvalues are approximated.

## Sources
- [Numerical Recipes, ch. 11](http://www.aip.de/groups/soe/local/numres/bookcpdf/c11-3.pdf)
