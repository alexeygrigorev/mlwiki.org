---
title: Spectral Theorem
layout: default
permalink: /index.php/Spectral_Theorem
---

# Spectral Theorem

## Spectral Theorem
Spectral Theorem is also sometimes called Principal Axis Theorem
- In [Linear Algebra](Linear_Algebra) a Spectrum is a set of [Eigenvectors](Eigenvalues_and_Eigenvectors) of a matrix 


'''Theorem''':
- Every [Symmetric Matrix](Symmetric_Matrices) can be factorized as $A = Q \Lambda Q^T$
- with real eigenvalues $\Lambda$ and orthonormal eigenvectors in the columns of $Q$


The factorization is [Eigendecomposition](Eigendecomposition)
- Spectral Theorem is a special case for symmetric matrices
- See the proof in the [Symmetric Matrices](Symmetric_Matrices) article


### Sum of [Rank One](Outer_Product) Matrices
We can look differently at the results of [Eigendecomposition](Eigendecomposition) of $A$ 

- $A = Q \Lambda Q^T = \begin{bmatrix} 
|  & & | \\ |\mathbf q_1 & \cdots & \mathbf q_n \\
|  & & | \\ |\end{bmatrix} 
\begin{bmatrix} 
\lambda_1 & &  \\
 & \ddots &  \\
 & & \lambda_n  \\
\end{bmatrix}
\begin{bmatrix} 
- & \mathbf q_1^T & - \\
 & \vdots & \\
- & \mathbf q_n^T & - \\
\end{bmatrix}$
- can represent it as $A = Q \Lambda Q^T = \sum \lambda_i \mathbf q_i  \mathbf q_i^T$ - sum of [Outer Product](Outer_Product)s
- each of these outer products can be seen as a [Projection Matrix](Projection_Matrices)
- a projection matrix is $P_i = \cfrac{\mathbf q_i \mathbf q_i^T}{\|  \mathbf q_i \|^2} = \mathbf q_i \mathbf q_i^T$ |- so symmetric matrix can be represented as a combination of mutually orthogonal projection matrices


## Applications
[Principal Component Analysis](Principal_Component_Analysis)
- The Spectral Theorem guarantees that we will find an orthogonal basis in PCA
- Because the [Covariance Matrix](Covariance_Matrix) $C = \cfrac{1}{n - 1} X^T X$ is symmetric and [Positive-Definite](Positive-Definite_Matrices)


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)