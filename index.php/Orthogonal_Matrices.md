---
title: Orthogonal Matrices
layout: default
permalink: /index.php/Orthogonal_Matrices
---

# Orthogonal Matrices

## Orthogonal Matrices
### Orthonormal Vectors
Vectors $\mathbf q_1, \ ... \ , \mathbf q_n$ are ''orthonormal'' if they are [orthogonal](Vector_Orthogonality) and unit vectors 
- $\mathbf q_i \; \bot \; \mathbf q_j \ \forall i \ne j$ and
- $\mathbf q_i^T \mathbf q_j = 0$ if $i \ne j$ and $\mathbf q_i^T \mathbf q_j = 1$ otherwise
- these vectors make a good [basis](Basis_(Linear_Algebra)) 


### Orthogonal Matrix
What about a matrix form?
- The second part of the definition: $\mathbf q_i^T \mathbf q_j = 
\begin{cases} 
1 & \text{if } i \ne j \\
0 & \text{if } i = j
\end{cases}$
- how do we put it in a matrix form? 
- Consider a matrix $Q$ whose columns are vectors $\mathbf q_1, \ ... \ , \mathbf q_n$:
- let $Q = \Bigg[ \mathop{\mathbf q_1}\limits_| ^| \ \mathop{\mathbf q_2}\limits_|^| \ \cdots \  \mathop{\mathbf q_n}\limits_|^| \Bigg]$ |- $Q^T Q = 
\begin{bmatrix}
- \ \mathbf q_1^T - \\
- \ \mathbf q_2^T - \\
\\ 
- \ \mathbf q_n^T -
\end{bmatrix}
\Bigg[ \mathop{\mathbf q_1}\limits_| ^| \ \mathop{\mathbf q_2}\limits_|^| \ \cdots \  \mathop{\mathbf q_n}\limits_|^| \Bigg] = \begin{bmatrix} |1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
 &  & \ddots &  \\
0 & 1 & \cdots & 1
\end{bmatrix}$ by our definition|   |- so $Q^T Q = I$ |- such $Q$'s are called ''Orthogonal Matrices'' 


A matrix $Q$ is orthogonal if 
- its columns are orthonormal vectors 
- and it's square

What's special about being square?
- if $Q^T Q = I$, then $Q^T = Q^{-1}$


## Examples
### Identity Matrices
Identity matrices are orthogonal:
- $Q = \begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix} = I$
- $Q^T Q = I I = I$


### [Permutation Matrices](Permutation_Matrices)
[Permutation Matrices](Permutation_Matrices) are orthogonal
- consider $Q = \begin{bmatrix}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0 \\
\end{bmatrix}$
- then $Q^T = \begin{bmatrix}
0 & 1 & 0 \\
0 & 0 & 1 \\
1 & 0 & 0 \\
\end{bmatrix}$ and indeed $Q^T Q = I$
- also note that $Q^T$ is also orthogonal 


### [Rotation Matrices](Rotation_Matrices)
[Rotation Matrices](Rotation_Matrices) are also orthogonal
- let $Q = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta \\
\end{bmatrix}$
- it's orthogonal


### Not Orthogonal Example
Not orthogonal:
- $S = \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix}$
- why? $S^T S = \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix} \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix} = \begin{bmatrix}
2 & 0 \\
0 & 2 \\
\end{bmatrix}$
- how to fix it? they are not unit vectors, so need to normalize it:
- $Q = \cfrac{1}{\sqrt 2} \begin{bmatrix}
1 & 1 \\
1 & -1 \\
\end{bmatrix}$ 
- now $Q^T Q = \cfrac{1}{2} \begin{bmatrix}
2 & 0 \\
0 & 2 \\
\end{bmatrix} = I$
- this one is orthogonal



## Usage
### Projection
Why is it good to have orthogonal matrices? 
- projections are easy:
- suppose we want to project onto the column space of $Q$
- so we have $P = Q (Q^T Q)^{-1} Q^T = Q I Q^T = Q Q^T$
- $Q Q^T$ is symmetric
- see [Projection onto Subspaces#Projection onto Orthogonal Basis](Projection_onto_Subspaces#Projection_onto_Orthogonal_Basis)


### [Normal Equation](Normal_Equation)
- $A^T A \mathbf{\hat x} = A^T \mathbf b$
- usual case (when $A$ is not orthogonal): $\mathbf{\hat x} = (A^T A)^{-1} A^T \mathbf b$
- orthogonal case: $\mathbf{\hat x} = (Q^T Q)^{-1} Q^T \mathbf b = Q^T \mathbf b$ - no inversion involved
- so can use [$A = QR$ Factorization](QR_Factorization) and get $\mathbf{\hat x} = R^{-1} Q^T \mathbf b$


### Factorizations
Orthogonal matrices are very nice because it's very easy to invert them
- therefore some factorizations are very popular
- e.g. [Eigendecomposition](Eigendecomposition) or [SVD](SVD)


## Orthogonalization
How do we make matrices orthogonal? 
- [Gram-Schmidt Process](Gram-Schmidt_Process) and [QR Factorization](QR_Factorization)
- this preserves the column space $C(A)$|    | |Also, 
- [Eigendecomposition](Eigendecomposition) $A = Q \Lambda Q^T$ decomposes symmetric $A$ onto orthogonal $Q$ and diagonal $\Lambda$
- [SVD](SVD) $A = U \Sigma V^T$ decomposes $A$ onto orthogonal $U$ and $V$ and diagonal $\Sigma$



## Properties
### Transpose
If $Q$ is orthogonal matrix, then $Q^T$ is orthogonal as well


### [Matrix Multiplication](Matrix_Multiplication)
If $Q_1$ and $Q_2$ are orthogonal, so is $Q_1 \cdot Q_2$


### Linear Transformation Properties
$Q$ preserves the [$L_2$ norm](Euclidean_Distance):
- $\|  Q \mathbf x \| = \| \mathbf x \|$ |- proof: $\|  Q \mathbf x \|^2 = (Q \mathbf x)^T (Q \mathbf x) = \mathbf x^T Q^T Q \mathbf x = \mathbf x^T \mathbf x = \| \mathbf x \|^2$ |

$Q$ preserves the angle between $\mathbf x$ and $\mathbf y$
- $\langle Q \mathbf x, Q \mathbf y \rangle = \langle \mathbf x, \mathbf y \rangle$
- proof: $(Q \mathbf x)^T (Q \mathbf y) = \mathbf x^T Q^T Q \mathbf y = \mathbf x^T \mathbf y$



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://inst.eecs.berkeley.edu/~ee127a/book/login/l_mats_qr.html

[Category:Linear Algebra](Category_Linear_Algebra)