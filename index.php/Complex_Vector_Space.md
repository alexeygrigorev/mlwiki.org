---
title: Complex Vector Space
layout: default
permalink: /index.php/Complex_Vector_Space
---

# Complex Vector Space

## Complex Vector Space
A $\mathbf z$ is a complex vector (denoted by $\mathbf z \in \mathbb C^n$)
- when it's components $z_i$ are [Complex Numbers](Complex_Numbers)
- complex vectors also form a [Vector Space](Vector_Space)


## Norm
How do we define the length of a complex vector? 
- $\|  \mathbf z \|^2 = \langle \mathbf z, \mathbf z \rangle = \mathbf z^T \mathbf z$ is no good: |  - length should be positive
  - consider, for example, vector $(1, i)$
  - $\|  (1, i) \|^2$ would be $1^2 + i^2 = 0$ |- what we really want is $\langle \mathbf z, \mathbf z \rangle = \overline {\mathbf z}^T \mathbf z$
  - where $\overline {\mathbf z}$ is a [Complex Conjugate](Complex_Conjugate), i.e. $\overline {\mathbf z} = (\overline z_1, \ ... \ , \overline z_n)$
  - this way each component of $\langle \mathbf z, \mathbf z \rangle$ contributes a strictly positive number to the overall dot product
  - so $\|  (1, i) \|^2$ is $1 - i^2 = 2$ |  - thus, $\|  (1, i) \| = \sqrt{2}$ |

### Hermitian
The way to transpose and take the conjugate at the same time
- $\mathbf z^H$ is $\overline {\mathbf z}^T$
- so we say $\|  \mathbf z \|^2 = \mathbf z^H \mathbf z = \sum | z_i |^2$ |- hermitian operator also applies to matrices
- $A^H$ is $\overline A^T$


### Inner Product
The same for the dot product
- $\langle x, y \rangle$  is not $\mathbf x^T \mathbf y$
- it's $\langle x, y \rangle = \mathbf x^H \mathbf y$


## Symmetric Matrices
What about symmetric matrices in $\mathbb C^{n \times n}$?
- The definition that $A$ is symmetric if $A^T = A$ is for $\mathbb R$, not $\mathbb C$
- the complex version of symmetry is $\overline {A}^T = A$, or $A^H = A$ 0 using the Hermitian operator
- note that diagonal of a symmetric matrix must be real, because otherwise real values are complex conjugates of each others


### Unitary Matrices
Can a complex matrix be [orthogonal](Orthogonal_Matrices)? 
- $Q^T Q = I$ is orthogonal matrix for $\mathbb R$
- what about $\mathbb C$?
- yes, it's possible: $Q^H Q = I$ and all it's columns $\mathbf q_1, \ ... \ , \mathbf q_n$ are orthonormal 
- vectors $\mathbf q_1, \ ... \ , \mathbf q_n$ are orthonormal when $\mathbf q_i^H \mathbf q_j = \begin{cases}
1 & \text{ if } i = j \\ 
0 & \text{ if } i \ne j 
\end{cases}$
- but here instead of "orthogonal" they are usually called "unitary" matrices


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))


[Category:Vector Spaces](Category_Vector_Spaces)
[Category:Linear Algebra](Category_Linear_Algebra)