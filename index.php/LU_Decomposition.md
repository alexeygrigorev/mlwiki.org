---
title: "LU Decomposition"
layout: default
permalink: /index.php/LU_Decomposition
---

# LU Decomposition

## $LU$ Factorization
This is the simplest factorization that can be seen as a by-product of [Gaussian Elimination](Gaussian_Elimination)

When we do elimination, we have some elimination matrices: 
- $E_1 \cdots E_k A = U$, where $E_1 \cdots E_k$ are elimination matrices for each elimination step 
- Let $E = E_1 \cdots E_k$


### $LU$
- $E_1 \cdots E_k \ A = U$
- or $EA = U$
- let $L = E^{-1}$, so we have $A = LU$
- $U$ is upper-triangular by construction - because we eliminate all elements down the main diagonal
- $L$ is lower-triangular 

$L$
- $L = E^{-1} = (E_1 \cdots E_k)^{-1} = E_k^{-1} \cdots E_1^{-1}$
- $E_i$ have zeros up the diagonal, so when we inverse them, they become lower-diagonal 
- when we multiply a bunch of lower-diagonal matrices, we get a lower-diagonal matrix


[Permutation Matrices](Permutation_Matrices)
- What if we need to permute some rows during the elimination?
- Then we have $EPA = U$ or $PA = LU$


### $LDU$
We can go further and obtain factorization $A = LU = LDU^*$, where $D$ is diagonal. I.e. we factorize $U = DU^*$


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)
[Category:Matrix Decomposition](Category_Matrix_Decomposition)