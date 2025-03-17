---
title: "Matrix"
layout: default
permalink: /index.php/Matrix
---

# Matrix

{{stub}}

## Matrix
In [Linear Algebra](Linear_Algebra) a $m \times n$ matrix $A$ is a rectangular array with $m$ rows and $n$ columns:

$A = \begin{bmatrix}
a_{11} & a_{12} & ... & a_{1n}\\ 
a_{21} & a_{22} & ... & a_{2n}\\ 
... & ... &  ... & ... \\ 
a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}$

$\{a_{ij}\}$ (or $(A)_{ij}$) are components of the matrix $A$

if $m = n$, then $A$ is called ''rectangular''

$(a_{11}, a_{22}, ..., a_{nn})$ are diagonal elements


## Operations
- [Matrix Multiplication](Matrix_Multiplication): Can multiply a matrix by a scalar, by a vector or by another matrix
- [Matrix Transposition](Matrix_Transposition)
- [Inversion](Inverse_Matrices) 
- ...


## Types
Matrices can be:
- square $n \times n$ and rectangular $m \times n$ 
- [Rank-1 Matrices](Outer_Product)
- Identity matrices 
- [Symmetric Matrices](Symmetric_Matrices)
- [Orthogonal Matrices](Orthogonal_Matrices)
- [Rotation Matrices](Rotation_Matrices)
- [Similar Matrices](Similar_Matrices)
- [Positive-Definite Matrices](Positive-Definite_Matrices)


## Decompositions
- [LU Decomposition](LU_Decomposition): $A = LU$ where $L$ is lower triangular and $U$ is upper triangular
- [QR Decomposition](QR_Decomposition): $A = QR$ where $Q$ 
- [Eigendecomposition](Eigendecomposition): $A = S \Lambda S^{-1}$ with diagonal $\Lambda$ 
- special case of EVD: [Spectral Theorem](Spectral_Theorem): $A = Q \Lambda Q^T$ with diagonal $\Lambda$ and Orthogonal $Q$
- [Singular Value Decomposition](Singular_Value_Decomposition): $A = U \Sigma V^T$ with diagonal $\Sigma$ and orthogonal $U$ and $V$ 


## Matrices as Vectors
We can see matrices as vectors, and they also can form [Vector Spaces](Vector_Spaces)
- see [Matrix Vector Spaces](Matrix_Vector_Spaces)
- they have inner product (element-wise) and norm ([Frobenius Norm](Frobenius_Norm))


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- Курош А.Г. Курс Высшей Алгебры

[Category:Linear Algebra](Category_Linear_Algebra)