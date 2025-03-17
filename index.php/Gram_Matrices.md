---
title: Gram Matrices
layout: default
permalink: /index.php/Gram_Matrices
---

# Gram Matrices

## Gram Matrices
A Gram matrix of vectors $\mathbf a_1 , \ ... \ , \mathbf a_n$ is a matrix $G$ 
- s.t. $G = \langle \mathbf a_i, \mathbf a_j \rangle$ for all $i,j$
- if vectors $\mathbf a_1 , \ ... \ , \mathbf a_n$ are columns of a matrix $A$, then 
- $G = A^T A$ 
- a Gram matrix is  [Positive Definite](Positive-Definite_Matrices) and [Symmetric](Symmetric_Matrices) 
- if vectors $\mathbf a_1 , \ ... \ , \mathbf a_n$ are the rows of $A$ ($A$ would be so-called "Data Matrix"), then $G = A A^T$, and it's called left Gram matrix


### Notation
- let $C(A)$ be the [Column Space](Column_Space) and $R(A)$ the [Row Space](Row_Space)


## [Symmetric Matrices](Symmetric_Matrices)
Let's consider a rectangular $m \times n$ matrix $A$
- $A^T A$ is always symmetric:
- $(A^T A)^T = A^T (A^T)^T = A^T A$
- $A A^T$ is also symmetric
- $(A A^T)^T = (A^T)^T A^T = A A^T$

This is used for [Singular Value Decomposition](Singular_Value_Decomposition)


## [Four Fundamental Subspaces](Four_Fundamental_Subspaces)
### [Nullspace](Nullspace)
Let $A$ be any matrix. Let's show that $N(A^T A) = N(A)$
- we will show that $\forall \mathbf x: \mathbf x \in N(A) \iff \mathbf x \in N(A^T A)$


$\mathbf x \in N(A) \Rightarrow \mathbf x \in N(A^T A)$ case
- if $\mathbf x \in N(A)$ $\Rightarrow$ 
- $A \mathbf x = \mathbf 0$ multiply by $A^T$: 
- $(A^T A) \mathbf x = \mathbf 0$
- so $\mathbf x \in N(A^T A)$ as well


$\mathbf x \in N(A^T A) \Rightarrow \mathbf x \in N(A)$ case
- $A^T A \mathbf x = \mathbf 0$, want to show that $A \mathbf x = \mathbf 0$
- can't multiply by $(A^T)^{-1}$ - it doesn't exist
- multiply by $\mathbf x^T$ instead:
- $\mathbf x^T A^T A \mathbf x = \mathbf x^T \mathbf 0 = 0$
- $(A \mathbf x)^T A \mathbf x = 0$
- $\|  A \mathbf x \|^2 = 0$ |- so the length of vector $A \mathbf x$ is 0 - it's true only when $A \mathbf x = \mathbf 0$


So $N(A) = N(A^T A)$

$\square$



### Row Space and Column Space
- we know that $C(A^T A) \subseteq C(A^T) = R(A)$ (see [Matrix Multiplication#Properties](Matrix_Multiplication#Properties))
- and $R(A^T A) \subseteq R(A)$
- $\text{rank}(A^T A) = \text{rank}(A)$ (see below)
- so $C(A^T A) = R(A^T A) = R(A)$


The same reasoning can be applied to $A A^T$:
- $C(A A^T) = R(A A^T) = C(A)$



## Other Properties
### [Rank](Rank_(Matrix))
Consequence: 
- by the [Rank-Nullity Theorem](Rank-Nullity_Theorem), we know that for $m \times n$ matrix $A$, $\text{rank }A + \text{dim } N(A) = n$
- $A^T A$ is an $n \times n$ matrix, so $\text{rank } A^T A + \text{dim } N(A^T A) = \text{rank } A^T A + \text{dim } N(A) = n$
- so $\text{rank }A = \text{rank }A^T A = n - \text{dim } N(A)$



### Invertability
Theorem: $A^T A$ is invertible if and only if $A$ has linearly independent columns
- $A$ is invertible when $A$ has independent columns
- i.e. $N(A) = \{ \mathbf 0 \}$
- so if $N(A) = \{ \mathbf 0 \}$, then $A^T A$ is square, symmetric and invertible


### [Semi-Positive Definiteness](Positive-Definite_Matrices)
Check: Let $R$ be an $n \times m$ matrix
- let $A = R^T R$, it's square and symmetric
- $A$ is PDM:
- $\mathbf v^T A \mathbf v = \mathbf v^T R^T R \, \mathbf v = (R \, \mathbf v)^T R \, \mathbf v = \|  R \, \mathbf v \|^2 > 0$  |- if $\mathbf v \ne \mathbf 0$ - and it's the case when columns of $R$ are linearly independent 
- see the theorem in [Projection onto Subspaces](Projection_onto_Subspaces#Theorem__.24A.5ET_A.24_is_Invertible)
- If some columns of $R$ are linearly dependent, then still $R^T R$ is semi-positive, with some eigenvalues equal to 0


Let's check $R R^T$:
- $\mathbf v^T R R^T \mathbf v = \|  R^T \mathbf v \|^2$ |- it's always non negative


Also can see that both $R^T R$ and $R R^T$ have non-negative eigenvalues:
- let $\mathbf v$ be eigenvector of $R^T R$ with eigenvalue $\lambda$
- then $\|  R \mathbf v \|^2 = (R \mathbf v)^2 R \mathbf v = \mathbf v^T \underbrace{R^T R \mathbf v}_{\lambda \mathbf v} = \lambda \mathbf v^T \mathbf v = \lambda \| \mathbf v \|^2$ |- so $\|  R \mathbf v \|^2 = \lambda \| \mathbf v \|^2$. Lengths are always positive, so $\lambda$ must be non-negative |- can see the same for $RR^T$: if $\mathbf u$ is its eigenvector and $\lambda$ is eigenvalue, then
- $\|  R^T \mathbf u \|^2 = \lambda \| \mathbf u \|^2$ |


## Sources
- other inner-wiki pages
- http://en.wikipedia.org/wiki/Gramian_matrix
- http://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)