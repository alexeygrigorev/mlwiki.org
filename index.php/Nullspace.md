---
title: "Nullspace"
layout: default
permalink: /index.php/Nullspace
---

# Nullspace

## Nullspace
Nullspace $N(A)$ of a matrix $A$ is one of the [Four Fundamental Subspaces](Four_Fundamental_Subspaces) of the matrix $A$

The nullspace of $A$ contains all $\mathbf x$ that solve the [system](System_of_Linear_Equations) $A \mathbf x = \mathbf 0$ (this system is called [''homogeneous''](Homogeneous_Systems_of_Linear_Equations))


### Example
$A = \begin{bmatrix}
1 & 1 & 2 \\
2 & 1 & 3 \\
3 & 1 & 4 \\
4 & 1 & 5 \\
\end{bmatrix}$, $\mathbf x = \begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}$, $\mathbf b = \mathbf 0_4 = \begin{bmatrix}
0 \\ 0 \\ 0 \\ 0
\end{bmatrix}$
- There are 3 columns and they are 4-dim vectors 
- the [Column Space](Column_Space) $C(A)$ is a subspace of $\mathbb R^4$, but $\text{dim } C(A) = 2$ (because the [rank](Rank_(Matrix)) of this matrix is 2)
- since there are only 3 columns, the number of unknowns is 3 - so $N(A)$ is a subspace of $\mathbb R^3$


Let's find what's inside $N(A)$
- i.e. all such $\mathbf x$ that solve $A \mathbf x = \mathbf 0$ 
- $\mathbf 0 \in N(A)$ always
- $\begin{bmatrix}
1 \\ 1 \\ -1
\end{bmatrix}$ or any multiple of this vector $c \cdot \begin{bmatrix}
1 \\ 1 \\ -1
\end{bmatrix}$
- so it's a subspace - a line in $\mathbb R^3$ through the origin


### Is $N(A)$ a Subspace?
Does it form a [Vector Space](Vector_Space) on its own?
- so we need to check that all possible $\mathbf x$ for that solve $A \mathbf x = \mathbf 0$  form a subspace
- let $\mathbf v$ and $\mathbf w$  be two solutions
  - $A \cdot (\mathbf v + \mathbf w) = A \mathbf v + A \mathbf w = \mathbf 0 + \mathbf 0 = \mathbf 0$. so $\mathbf v + \mathbf w$ is also a solution
- if $A \mathbf v = 0$, then $A \cdot (c \cdot \mathbf v) = (c \cdot A) \cdot  \mathbf v = 0$
  - this would just multiply all columns of $A$ on the same number 
- so yes, it is a subspace


### [Basis](Basis_(Linear_Algebra)) of $N(A)$
Basis for $N(A)$ is formed by the "special" solutions



## Left Nullspace
We can also consider another nullspace of $A$ - the nullspace of $A^T$ (this is the 4th [fundamental subspace](Four_Fundamental_Subspaces) of a matrix)

Let's have a look at a system $A^T \mathbf y = \mathbf 0$
- $A$ is an $n \times m$ matrix, so $A^T$ is $m \times n$
- $y$ is $n$-len column vector

Let's take the transpose of $A^T \mathbf y = \mathbf 0$:
- $(A^T \mathbf y)^T = \mathbf 0^T$
- $\mathbf y^T A  = \mathbf 0^T$
- so now we have a row vector $\mathbf y^T$ that is on the left side of $A$ 

$\big[ - \, \mathbf y^T - \big] \Bigg[ ~ ~ ~ ~ ~ {A} ~ ~ ~ ~ ~ \Bigg] = \big[ - \, \mathbf 0^T - \big]$


### [Basis](Basis_(Linear_Algebra)) of $N(A^T)$
Let's consider this example 

Let $A$ be some rectangular matrix and we find it's rref $R$
- $A = \begin{bmatrix}
1 & 2 & 3 & 1 \\
1 & 1 & 2 & 1 \\
2 & 3 & 5 & 2 \\
\end{bmatrix} \leadsto 
\begin{bmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 0 \\
0 & 0 & 0 & 0 \\
\end{bmatrix} = R$
- we see that one of the rows are $\mathbf 0$ - so the nullspace of $A^T$ should have something apart from $\mathbf 0$


How to best find this left nullspace?
- Let's do Gauss-Jordan Elimination: create the augmented matrix by appending $I$ and reduce it to the echelon form:
- $\big[  A_{m \times n} \ I_{n \times n} \big] \to \big[  R_{m \times n} \ E_{n \times n} \big]$
- So $E$ is the elimination matrix - the matrix that brings $A$ to rref $R$
- $E A = R$
  - If $A$ is square and invertible, then $E \equiv A^{-1}$
  - but since $A$ is rectangular, it has no inverse 

Example cont'd 
- $\left[ \begin{array}{cccc| ccc} |1 & 2 & 3 & 1 & 1 & 0 & 0 \\
1 & 1 & 2 & 1 & 0 & 1 & 0 \\
2 & 3 & 5 & 2 & 0 & 0 & 1 \\
\end{array}\right] \leadsto 
\left[ \begin{array}{cccc| ccc} |1 & 0 & 1 & 1 & -1 & 2 & 0 \\
0 & 1 & 1 & 0 & 1 & -1 & 0 \\
0 & 0 & 0 & 0 & -1 & 0 & 1 \\
\end{array}\right]$
- now if we take $E = \begin{bmatrix}
-1 & 2 & 0 \\
1 & -1 & 0 \\
-1 & 0 & 1 \\
\end{bmatrix}$ and multiply it by $A$, we get 
  - $\begin{bmatrix}
-1 & 2 & 0 \\
1 & -1 & 0 \\
-1 & 0 & 1 \\
\end{bmatrix} \cdot 
\begin{bmatrix}
1 & 2 & 3 & 1 \\
1 & 1 & 2 & 1 \\
2 & 3 & 5 & 2 \\
\end{bmatrix} = 
\begin{bmatrix}
- & - & - & - \\
- & - & - & - \\
0 & 0 & 0 & 0 \\
\end{bmatrix}$
  - so indeed we manage to get the last row with zeros 
- so we need the last row of $E$ to get $\mathbf 0^T$
  - recall the row picture from [Matrix Multiplication](Matrix_Multiplication)


## Numerical Computation
Use [SVD](SVD) to compute the nullspace
- $A = U \Sigma V^T$ 
- vectors of $V$ that correspond to $\sigma_i = 0$ are from the nullspace 


```python
def null(A, eps=1e-15):
    u, s, vh = np.linalg.svd(A)
    null_space = np.compress(s <= eps, vh, axis=0)
    return null_space.T
```

From [http://stackoverflow.com/questions/1835246/how-to-solve-homogeneous-linear-equations-with-numpy]



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://en.wikipedia.org/wiki/Kernel_%28linear_algebra%29#Numerical_computation

[Category:Linear Algebra](Category_Linear_Algebra)