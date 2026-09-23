---
layout: default
permalink: /Hessenberg_Decomposition
tags:
- linear-algebra
- matrix-decomposition
title: Hessenberg Decomposition
---

## Hessenberg Decomposition
Also called "Hessenberg Reduction" or "Hessenberg Transformation"

Hassenberg Decomposition is a Matrix Decomposition:
- let $A$ be a matrix, then 
- the decomposition $A = U H U^T$ is Hessenberg Decomposition if
  - $U$ - orthogonal, $U^T U = I$ and
  - $H$ - Hessenberg Matrix
  - Hessenberg matrix is almost triangular matrix - but it has some non-zero elements right below (above) the main diagonal. The rest are zeros
- this reduction is typically performed with [Householder Transformation](Householder_Transformation)
  - in principle, it's also possible to get it with [Givens Transformation](Givens_Transformation)

## Repeated Householder Reflection
The idea:
- apply a series of $n-2$ Householder Transformations to $A$
- such that eventually it becomes lower-Hessenberg:
- https://habrastorage.org/web/819/b7b/b90/819b7bb903214f0e883f21c1c2bc0e5e.png

Initial step:
- let $H_0 = A$

First step, constructing $P_1$:
- <math>P_1 = 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \times & \times & \times \\
0 & \times & \times & \times \\
0 & \times & \times & \times \\
\end{bmatrix} = 
\begin{bmatrix}
1 & \mathbf 0 \\
\mathbf & I - 2 u_1 u_1^T \\
\end{bmatrix}
</math>
- so the actual Householder Matrix is in the lower right block
- hence $H_1 = P_1 H_0 P_1^T$

Second step, $P_2$: 
- same, but go one lever down:
- <math>P_2 = 
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & \times & \times \\
0 & 0 & \times & \times \\
\end{bmatrix} = 
\begin{bmatrix}
1 & 0 & \mathbf 0 \\
0 & 1 & \mathbf 0 \\
\mathbf 0 & \mathbf 0 & I - 2 u_2 u_2^T \\
\end{bmatrix}
</math>
- again, the Householder Matrix is in the lower right block 
- $H_2 = P_2 H_1 P_2^T$

And so on. At the end we have:
- $H_{n-1} = H = P_{n-1} H_{n-2} P_{n-1}^T  = \ ...$
  - $... \ = P_{n-1} P_{n-2} H_{n-3} P_{n-2}^T P_{n-1}^T = \ ...$
  - $... \ = P_{n-1} P_{n-2} H_{n-3} P_{n-2}^T P_{n-1}^T = \ ...$
  - $... \ = P_{n-1} P_{n-2} \ ... \ P_1 A P_{1}^T \ ... \ P_{n-2}^T P_{n-1}^T$
- now let $U = P_{n-1} P_{n-2} \ ... \ P_1$ 
- so we have: $H = U A U^T$

### Symmetric Matrices
When we apply the decomposition to a symmetric matrix, we get a tridiagonal matrix

### Properties
Hessenberg Decomposition is quite useful in a number of applications
- main application - [QR Algorithm](QR_Algorithm) for finding [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors)

Nice property: 
- if $QR = H$ is the [QR Decomposition](QR_Decomposition) of $H$ then 
- $RQ$ is also Hessenberg
- this is why it's very useful in $QR$ steps of the [QR Algorithm](QR_Algorithm)
- this way we can perform $QR$ iterations a lot faster: with $O(n^2)$ per iteration instead of $O(n^3)$

## Implementation
Implementation:
- Householder Reflection
- Matrices are updated in-place

```python
### Python and Numpy

 def hessenberg_form(A):
     A = A.copy()
     n = A.shape[1]
     U = np.eye(n)
 
     us = {}
 
     for k in range(n - 1):
         x = A[k+1:,k]
 
         nx = np.linalg.norm(x)
         rho = -np.sign(x[0])
 
         z = x.copy()
         z[0] = z[0] - rho * nx
         u = z / np.linalg.norm(z)
         us[k] = u
 
         # compute PA
         A_slice = A[k+1:,k:]
         PA = A_slice - 2 * np.outer(u, u.dot(A_slice))
         A[k+1:,k:] = PA
 
         # compute PAP
         A_slice = A[:, k+1:]
         PAP = A_slice - 2 * np.outer(A_slice.dot(u), u)
         A[:, k+1:] = PAP
 
     for k in range(n - 2, -1, -1):
         # update U = P_k U
         u = us[k]
         U_slice = U[k+1:,k+1:]
         PU = U_slice - 2 * np.outer(u, u.dot(U_slice))
         U[k+1:,k+1:] = PU
 
     return U, A

## Sources
```
- http://people.inf.ethz.ch/arbenz/ewp/Lnotes/chapter4.pdf
- [Matrix Computations (book)](Matrix_Computations_%28book%29)
