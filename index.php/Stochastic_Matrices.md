---
title: "Stochastic Matrices"
layout: default
permalink: /index.php/Stochastic_Matrices
---

# Stochastic Matrices

## Stochastic Matrices
Stochastic matrices (or Markov matrices) - matrices used to describe transitions in [Markov Chains](Markov_Chains)

A stochastic matrix is a matrix $A$ which
- is square $n \times n$
- for all entires $0 \leqslant a_{ij} \leqslant 1$
- sum over columns is 1


## Properties
- for any $k$, $A^k$ is also stochastic 
- its largest [eigenvalue](Eigenvalues_and_Eigenvectors) is $\lambda_1 = 1$
- all other eigenvalues are $|  \lambda_i | \leqslant 1$, and usually it's strictly less |
### $\lambda_1 = 1$
Let take any stochastic $A$ 
- suppose $\lambda = 1$ is an eigenvalue
- then $A - \lambda I = A - I$ must be singular
- sum of columns of $A$ is 1. But when we subtract $1$ from diagonal, the sum is 0 for all columns
- so columns are now linearly dependent, and it means that rows are also linearly dependent
- then $(1,1,1) \in N(A^T)$ (left [Nullspace](Nullspace) of $A$)
- and the [Nullspace](Nullspace) $N(A)$ also contains something: it contains the eigenvector $\mathbf v_1$ that corresponds to $\lambda_1 = 0$

If $\lambda_1 < 0$, then $A^k$ for large $k$ will converge to $\mathbf O$ - a matrix with all zeros.

 

### Eigenvalues
- for stochastic matrices, eigenvalues of $A$ are the same as eigenvalues of $A^T$
- $\text{det } (A - \lambda I) = 0$
- $\text{det } (A - \lambda I)^T = \text{det } (A^T - \lambda I) = 0$


### [Recurrent Equation](Recurrent_Equation)
- $\mathbf u_k = A^k \mathbf u_0$
- Let's use the eigenvectors $\mathbf v_1 , \ ... \ , \mathbf v_n$ of $A$ as basis 
- then $\mathbf u_k = A^k \mathbf u_0 = c_1 \lambda_1^k \mathbf v_1 + c_2 \lambda_2^k \mathbf v_2 + \ ... \ c_n \lambda_n^k \mathbf v_n$
- $\lambda_1 = 1$ and the rest are less than 1, so for large $k$ we have 
- $\mathbf u_k \approx c_1 \mathbf v_1$
- $c_1 \mathbf v_1$ is the ''steady state''
- This an application of the [Power Iteration](Power_Iteration) method



## Example
### Example 1
- $A = \begin{bmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{bmatrix}$
- $\lambda_1 = 1, \lambda_2 = 0.5$
- eigenvectors $\mathbf v_1 = (0.6, 0.4)$ and $(1, -1)$
- let's apply [Eigendecomposition](Eigendecomposition) of $A$:
- $A = S \Lambda S^{-1}$: $\begin{bmatrix} 0.8 & 0.3 \\ 0.2 & 0.7 \end{bmatrix} =
\begin{bmatrix} 0.6 & 1 \\ 0.4 & -1 \end{bmatrix} \, 
\begin{bmatrix} 1 & 0 \\ 0 & 0.5 \end{bmatrix} \,
\begin{bmatrix} 1 & 1 \\ 0.4 & -0.6 \end{bmatrix}$

Steady state:
- $A^2$ has the same $S$: $A^2 = S \Lambda S^{-1} \, S \Lambda S^{-1} = S \Lambda^2 S^{-1}$
- $A^k = S \Lambda^k S^{-1}$
- Thus, $A^k =
\begin{bmatrix} 0.6 & 1 \\ 0.4 & -1 \end{bmatrix} \, 
\begin{bmatrix} 1^k & 0 \\ 0 & (0.5)^k \end{bmatrix} \,
\begin{bmatrix} 1 & 1 \\ 0.4 & -0.6 \end{bmatrix}$
- as $k$ increases, $0.5^k$ becomes very small, so
- as $k \to \infty$, $A^k \to
\begin{bmatrix} 0.6 & 1 \\ 0.4 & -1 \end{bmatrix} \, 
\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \,
\begin{bmatrix} 1 & 1 \\ 0.4 & -0.6 \end{bmatrix} = 
\begin{bmatrix} 0.6 & 0.6 \\ 0.4 & 0.4 \end{bmatrix}$



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- Strang, G. Introduction to linear algebra.
- http://en.wikipedia.org/wiki/Stochastic_matrix


[Category:Probability](Category_Probability)
[Category:Linear Algebra](Category_Linear_Algebra)