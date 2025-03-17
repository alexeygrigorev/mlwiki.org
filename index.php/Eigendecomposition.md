---
title: Eigendecomposition
layout: default
permalink: /index.php/Eigendecomposition
---

# Eigendecomposition

## Eigen Decomposition
Eigen Decomposition or, sometimes, Eigenvalue Decomposition (shortcut EVD)
- is a way of diagonalizing a square $n \times n$ matrix $A$ 


We can turn a matrix into a diagonal one by using eigenvectors
- $A$ is square 


Eigenvalue decomposition is a decomposition of a matrix into a "canonical form"
- we want to constrict a diagonal matrix from a given one
- a matrix $A$ is ''diagonalizable'' if it's [similar](Similar_Matrices) to a diagonal matrix
  - (a matrix $A$ is similar to $B$ if there exists an invertible $M$ s.t. $B = M^{-1} A \, M$)
- $A$ is diagonalizable if there exists [invertible matrix](Inverse_Matrices) $P$ s.t.  $P^{-1} A \, P$ is diagonal



Why can we do it?
- if all eigenvalues $\lambda_1, \ ... \ , \lambda_n$ are different 
- then all eigenvalues $\mathbf x_1, \ ... \ , \mathbf x_n$ are linearly independent
- so any matrix with distinct eigenvalues can be decomposed by eigenvalue decomposition
- see proof in [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors)


Diagonalization:
- $S^{-1} A S = \Lambda$
- $\text{diag } \Lambda = (\lambda_1, \ ... \ , \lambda_n)$


Eigenvalue Decomposition:
- if $A$ is symmetric, then there exists $S$ and $\Lambda$ s.t.
- $A = S \Lambda S^T$
- because for symmetric $A$ the eigenvectors in $S$ are orthonormal, so $S$ is [Orthogonal](Orthogonal_Matrices)



### Intuition
Suppose we have $n$ linearly independent [eigenvectors](Eigenvalues_and_Eigenvectors) $\mathbf x_i$ of $A$
- let's put them in columns of a matrix $S$ - eigenvector matrix 
- $S = \begin{bmatrix}
|  & & | \\ |\mathbf x_1 & ... & \mathbf x_n \\
|  & & | \\ |\end{bmatrix}$


Now what if we multiply $AS$? 
- since all these $\mathbf x_i$ are eigenvectors, $A \mathbf x_i = \lambda_i \mathbf x_i$ 
- thus, $AS = A \begin{bmatrix}
|  & | & & | \\ |\mathbf x_1 & \mathbf x_2 & ... & \mathbf x_n \\
|  & | & & | \\ |\end{bmatrix} = \begin{bmatrix}
|  & | & & | \\ |\lambda_1 \, \mathbf x_1 & \lambda_2 \, \mathbf x_2 & ... & \lambda_m \, \mathbf x_n \\
|  & | & & | \\ |\end{bmatrix}$ 
- ok, now let's take the $\lambda_i$'s out: $\begin{bmatrix}
|  & & | \\ |\lambda_1 \, \mathbf x_1 &  \lambda_2 \, \mathbf x_2 & ... & \lambda_m \, \mathbf x_n \\
|  & & | \\ |\end{bmatrix} = \begin{bmatrix}
|  & | & & | \\ |\mathbf x_1 & \mathbf x_2 & ... & \mathbf x_n \\
|  & | &  & | \\ |\end{bmatrix} 
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n \\
\end{bmatrix}$
- let's call this diagonal matrix $\Lambda = \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n \\
\end{bmatrix}$
- so $AS = S \Lambda$


### Decomposition
- if $S$ is invertible (or all $\mathbf x_i$ are independent), then
- $\Lambda = S^{-1} A \, S$ - this is called ''diagonalization'' of $A$ 
- and $A = S \Lambda S^{-1}$ - another factorization of $A$ 
- if $A$ is diagonal, then $\Lambda = A$, but if it's triangular, we still need to calculate $\Lambda$


### [Symmetric Matrices](Symmetric_Matrices)
For symmetric $A$
- its eigenvalues are orthonormal,
- so the matrix $S$ is [orthogonal](Orthogonal_Matrices)
- thus, $A = S \Lambda S^{-1} = S \Lambda S^T$
- So we write $A = Q \Lambda Q^T$, where $Q$ is orthogonal



## Use Cases
### Calculating Powers: $A^k$
- if $A \mathbf x = \lambda \mathbf x$ then 
- $A^2 \mathbf x = \lambda A \mathbf x = \lambda^2 \mathbf x$
- so $\lambda$s are squared when $A$ is squared 

same for diagonalizable matrices:
- $A^2 = A A = (S \Lambda S^{-1}) (S \Lambda S^{-1}) = S \Lambda^2 S^{-1}$
- and $A^k = S \Lambda^k S^{-1}$
- so this factorization is better for powers than [LU Factorization](LU_Factorization)

This is useful for calculating the steady state probabilities of [Markov Chains](Markov_Chains) - by calculating the powers of [Stochastic Matrices](Stochastic_Matrices) - matrix representation of a Markov Chain


### [Recurrence Equation](Recurrence_Equation)
Suppose you are given a vector $\mathbf u_0$ and a recurrent formula $\mathbf u_{k+1} = A \mathbf u_{k}$
- how would you find $\mathbf u_{100}$?
- can repeat it 100 times 
- or, note that $\mathbf u_{100} = A \mathbf u_{99} = A^2 \mathbf u_{98} = \ ... \ =  A^{100} \mathbf u_{0}$

- Suppose $A$ is invertible. 
- Then one possible basis for $A$ is its eigenvectors $\mathbf v_i$
- let's express $\mathbf u_0$ in this basis: $\mathbf u_0 = c_1 \mathbf v_1 + \ ... \ + c_n \mathbf v_n = S \mathbf c$
- now let's multiply both parts by $A$:  
  - $A \mathbf u_0 = A c_1 \mathbf v_1 + \ ... \ + A c_n \mathbf v_n = A S \mathbf c$
  - $A \mathbf u_0 = c_1 \lambda_1 \mathbf v_1 + \ ... \ + c_n \lambda_n \mathbf v_n = \Lambda S \mathbf c$
- then $\mathbf u_{100} = c_1 \lambda_1^{100} \mathbf v_1 + \ ... \ + c_n \lambda_n^{100} \mathbf v_n = \Lambda^{100} S \mathbf c$


### [Fibonacci Numbers](Fibonacci_Numbers)
- Fibonacci numbers is a sequence 0, 1, 1, 2, 3, 5, 8, 13... 
- $F_{k + 2} = F_{k+ 1} + F_{k}$
- it's a second order Recurrence Equation
- Let's build a system: $\begin{cases}
F_{k+2} = F_{k+1} + F_{k} \\
F_{k+1} = F_{k+1} \\
\end{cases}$
- so let $\mathbf u_k = \begin{bmatrix} F_{k+1} \\ F_{k} \end{bmatrix}$, 
- then $\mathbf u_{k + 1} = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} F_{k+1} \\ F_{k} \end{bmatrix} = A \, \mathbf u_k$
- so we have the recurrence equation $\mathbf u_{k+1} = A \mathbf u_k$
- note that $A$ is symmetric, so it's diagonalizable 
- let's find eigenvalues:
  - $|  A - \lambda I | = \begin{vmatrix} |1 - \lambda & 1 \\ 
1  & -\lambda 
\end{vmatrix} = \lambda^2 - \lambda - 1 = 0$ 
  - or $\lambda_{1,2} = \cfrac{1 \pm \sqrt{1+4}}{2} = \cfrac{1 \pm \sqrt{5}}{2}$ 
  - $\lambda_1 = 0.5 (1 + \sqrt{5}) \approx  1.618$
  - $\lambda_1 = 0.5 (1 - \sqrt{5}) \approx -0.618$
- so, $\mathbf u_{100} = c_1 \lambda_1^{100} \mathbf v_1 + c_2 \lambda_2^{100} \mathbf v_2$
  - $\lambda_1 > 1$ so powers of it grow faster, and $| \lambda_2| < 1$, so its powers decay |  - thus $\lambda_1$ controls everything
- and we can approximate $F_{100} \approx c_1 \lambda_1^{100}$




## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://en.wikipedia.org/wiki/Diagonalizable_matrix
- Strang, G. Introduction to linear algebra.


[Category:Linear Algebra](Category_Linear_Algebra)
[Category:Matrix Decomposition](Category_Matrix_Decomposition)