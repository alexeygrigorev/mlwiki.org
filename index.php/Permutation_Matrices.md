---
title: Permutation Matrices
layout: default
permalink: /index.php/Permutation_Matrices
---

# Permutation Matrices

## Permutation Matrix
A [Matrix](Matrix) that exchanges 2 or more rows is called a ''permutation matrix'' 
- a permutation matrix $P$ is a matrix that is obtained by permuting rows/columns of identity matrix $I$
- this is an important type of matrices - it's used for solving [System of Linear Equations](System_of_Linear_Equations) and for [LU Factorization](LU_Factorization)
- e.g. for [Gaussian Elimination](Gaussian_Elimination) when we have a zero in the pivot position, we would like to exchange this to get non-zero pivot - this is done with a Permutation Matrix


### $P$ for Square Matrices
Suppose we have a $3 \times 3$ matrix $A$ and we want to permute it's rows

Let's list all possible permutation matrices for $3 \times 3$
- $\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{bmatrix}$ - permutes nothing
- $\begin{bmatrix}
0 & 1 & 0\\
1 & 0 & 0\\
0 & 0 & 1
\end{bmatrix}$ - permutes 1st and 2nd rows
- $\begin{bmatrix}
0 & 0 & 1\\
0 & 1 & 0\\
1 & 0 & 0\\
\end{bmatrix}$ - 1st and 3rd
- $\begin{bmatrix}
1 & 0 & 0\\
0 & 0 & 1\\
0 & 1 & 0\\
\end{bmatrix}$ - 2nd and 3rd
- $\begin{bmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
1 & 0 & 0\\
\end{bmatrix}$ - 2nd, 3rd and 1st
- $\begin{bmatrix}
0 & 0 & 1\\
1 & 0 & 0\\
0 & 1 & 0\\
\end{bmatrix}$ - 3, 1, 2


### [Permutations](Permutations)
In how many ways we can permute rows of $I_n$?
- it's the number of permutations of $n$: $n|  $ | |
## Types
### Row Exchange
$\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix} \times \begin{bmatrix}
a & b\\
c & d
\end{bmatrix} = \begin{bmatrix}
c & d\\
a & b
\end{bmatrix}$


### Column Exchange
What if we want to exchange columns? 

$\left[ \; \; \LARGE ? \; \; \;  \right] \times 
\begin{bmatrix}
a & b\\
c & d
\end{bmatrix} = \begin{bmatrix}
b & a\\
d & c
\end{bmatrix}$


Can't put such a matrix on the left|   Put in on the right instead | |$\begin{bmatrix}
a & b\\
c & d
\end{bmatrix} \times 
\begin{bmatrix}
0 & 1\\
1 & 0
\end{bmatrix}
= \begin{bmatrix}
b & a\\
d & c
\end{bmatrix}$


## Properties
- When we transpose $P$ or inverse, the obtained matrix is also a permutation matrix 
- $P^{-1} = P^T$
- thus $P^T P = P P^T = I$


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)