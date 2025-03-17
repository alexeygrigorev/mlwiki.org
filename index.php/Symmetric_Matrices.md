---
title: "Symmetric Matrices"
layout: default
permalink: /index.php/Symmetric_Matrices
---

# Symmetric Matrices

## Symmetric Matrices
A matrix $A$ is symmetric if $A^T = A$ holds. 
- thus, $A$ must be a square matrix




## Properties
What's special about $A \mathbf x = \lambda \mathbf x$? when $A$ is symmetric?
- $A$ has real eigenvalues, and orthonormal eigenvectors
- therefore [Eigendecomposition](Eigendecomposition) of $A$ is $A = Q \Lambda Q^T$ instead of $A = S \Lambda S^{-1}$
- this fact is sometimes referred as the [Spectral Theorem](Spectral_Theorem)


### Orthogonal Eigenvectors
- [diagonalize](Eigendecomposition) $A = S \Lambda S^{-1}$
- $A^T = (S \Lambda S^{-1})^T = (S^{-1})^T \Lambda^T S^T = (S^{-1})^T \Lambda \, S^T$
- since $A = A^T$, we have:
- $S \Lambda S^{-1} = (S^{-1})^T \Lambda \, S^T$
- so maybe $S^{-1} = S^T$? Then $S$ is an [Orthogonal Matrix](Orthogonal_Matrix)
- thus, the eigenvectors $\mathbf v_1 , \ ... \ , \mathbf v_n$ are orthonormal
- So we write $A = Q \Lambda Q^T$


Let's show that
- Suppose $A$ has two eigenvalues $\lambda_1 \ne \lambda_2$ and their eigenvalues are $\mathbf v_1$ and $\mathbf v_2$
- so $A \mathbf v_1 = \lambda_1 \mathbf v_1$ and $A \mathbf v_2 = \lambda_2 \mathbf v_2$
- $A \mathbf v_1 = \lambda_1 \mathbf v_1$ multiply by $\mathbf v_2$ on the left:
  - $(A \mathbf v_1)^T \mathbf v_2 = \lambda_1 \mathbf v_1^T \mathbf v_2$
  - $\mathbf v_1^T A^T \mathbf v_2 = \lambda_1 \mathbf v_1^T \mathbf v_2$
- $A$ is symmetric, so
  - $\mathbf v_1^T A^T \mathbf v_2 = \mathbf v_1^T A \mathbf v_2 = \lambda_1 \mathbf v_1^T \mathbf v_2$
- we have $\mathbf v_1^T A \mathbf v_2 = \lambda_1 \mathbf v_1^T \mathbf v_2$
  - since $A \mathbf v_2 = \lambda_2 \mathbf v_2$,
  - $\lambda_2 \mathbf v_1^T \mathbf v_2 = \lambda_1 \mathbf v_1^T \mathbf v_2$
- but we assumed that $\lambda_1 \ne \lambda_2$|    |  - so the only way it can be true is when $\mathbf v_1^T \mathbf v_2 = 0$ |- thus, $\mathbf v_1 \; \bot \; \mathbf v_2$

$\square$



### Real Eigenvalues
- $A \mathbf x = \lambda \mathbf x$
- let's take a [Complex Conjugate](Complex_Conjugate): for $c = a + ib$ a conjugate is $\overline {c} = \overline{a + ib} = a - ib$
- $A$ is real, so $\overline A = A$
- thus, we have $A \overline {\mathbf x} = \overline {\lambda \mathbf x}$
- so if $A$ has eigenvalue $\lambda$ and eigenvector $\mathbf x$, then $\overline \lambda$ and $\overline {\mathbf x}$ are also eigenvalue and eigenvector - for real matrices $A$
- we want to show that $\overline \lambda = \lambda$ and $\overline {\mathbf x} = \mathbf x$, i.e. they are not complex


Let's show that: 
- Transpose $A \overline {\mathbf x} = \overline {\lambda \mathbf x}$: 
  - $\overline {\mathbf x}^T A^T = \overline {\lambda \mathbf x}^T$
- Since $A$ is symmetric, $\overline {\mathbf x}^T A = \overline {\lambda \mathbf x}^T$
  - Multiply both sides by $\mathbf x$ on the left: 
  - $\overline {\mathbf x}^T A \, \mathbf x = \overline {\lambda \mathbf x}^T \mathbf x$
- now take $A \mathbf x = \lambda \mathbf x$ and multiply both sides by $\overline {\mathbf x}^T$ on the right:
  - $\overline {\mathbf x}^T A \mathbf x = \overline {\mathbf x}^T \lambda \, \mathbf x$
- so  $\overline {\mathbf x}^T A \mathbf x = \overline {\lambda \mathbf x}^T \mathbf x$ and $\overline {\mathbf x}^T A \mathbf x = \overline {\mathbf x}^T \lambda \mathbf x$
  - they have the same right hand side
  - thus $\overline \lambda \overline {\mathbf x}^T \mathbf x = \lambda \overline {\mathbf x}^T  \mathbf x$
  - given that $\overline {\mathbf x}^T  \mathbf x \ne 0$, we divide by it and have:
- $\overline \lambda = \lambda$, or, $\lambda \in \mathbb R$


Let's have a look at $\overline {\mathbf x}^T  \mathbf x$ (when $\ne 0$):
- $\Big[ \overline x_1 \ \overline x_2 \ \cdots \ \overline x_n \Big] \begin{bmatrix}  x_1  \\ \vdots \\ x_n \end{bmatrix} = \sum \overline x_i x_i$
- for a complex number $c$, $c \cdot \overline c = (a - ib) \cdot (a + ib) = a^2 + b^2 \in \mathbb R$
- so it's a sum of real numbers|   sum of squared lengths of each component of $\mathbf x$ |- which means that the entire dot product is in $\mathbb R$ |
$\square$


### Eigenvalues are Non-Negative
- Eigenvalues are non-negative
- If $A$ is positive-definite, then all eigenvalues are positive


### [Positive-definiteness](Positive-Definite_Matrices)
A symmetric matrix is positive-definite when
- all eigenvalues of $A$ are greater than zero
- so pivots are greater then zero as well


### [Subspaces](Four_Fundamental_Subspaces)
If $A$ is symmetric,
- then its row space is the same as column space
- i.e. $C(A) = C(A^T)$


### Other properties
E.g. the identity matrix $I$: all eigenvalues $\lambda_i = 1$ and every vector is eigenvectors 



## [Spectral Theorem](Spectral_Theorem)
We can apply [Eigendecomposition](Eigendecomposition) to $A$ and get
- $A = Q \Lambda Q^T = \sum \lambda_i \mathbf q_i  \mathbf q_i^T$ - sum of [Outer Product](Outer_Product)s
- each of these outer products can be seen as a [Projection Matrix](Projection_Matrices)
- so symmetric matrix can be represented as a combination of mutually orthogonal projection matrices



## Examples
### [Gram Matrices](Gram_Matrices)
$A A^T$ and $A^T A$ Symmetric
- moreover, every symmetric matrix $B$ can be represented as $A A^T$ or $A^T A$:
- Eigendecomposition of $B = Q \Lambda Q^T = Q \sqrt{\Lambda} \sqrt{\Lambda^T} Q^T = (Q \sqrt{\Lambda}) (Q \sqrt{\Lambda})^T = A A^T$ where $A = Q \sqrt{\Lambda}$
- also [Cholesky Decomposition](Cholesky_Decomposition) would show the same
- if $B$ is positive-definite, then such $A$ is non-singular


### Others
Identity and square diagonal matrices are symmetric



## Links
- https://inst.eecs.berkeley.edu/~ee127a/book/login/l_sym_psd.html

## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://www.math.ucsd.edu/~njw/Teaching/Math271C/Lecture_03.pdf

[Category:Linear Algebra](Category_Linear_Algebra)