---
layout: default
permalink: /index.php/Four_Fundamental_Subspaces
tags:
- linear-algebra
title: Four Fundamental Subspaces
---
## Four Fundamental Subspaces
A matrix $A$ has four subspaces: 
- [Column Space](Column_Space) $C(A)$
- [Nullspace](Nullspace) $N(A)$
- [Row Space](Row_Space) $C(A^T)$ of $A$ is the same as Column Space of $A^T$
- Nullspace of $A^T$ (also called "Left Nullspace")


<img width="40%" src="<img src="http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/diagram0.svg" alt="Image">" />


## Some Properties
Suppose we have an $m \times n$ matrix of rank $r$ 

### [Orthogonality](Orthogonality)
- Nullspace of $A$ is orthogonal to the row space: $N(A) \; \bot \; C(A^T)$
- Left nullspace of $A$ is orthogonal to the column space:  $N(A^T) \; \bot \; C(A)$
- see the proof in [Space Orthogonality#Row space and Nullspace](Space_Orthogonality#Row_space_and_Nullspace)


### [Column Space](Column_Space)
- $\text{dim } C(A) = r$, there are $r$ pivot columns
- basis: columns of $A$ 


### [Row Space](Row_Space)
- $\text{dim } C(A^T) = r = \text{dim } C(A)$, there are $r$ pivot rows - the same dim as for Column Space
- Let $R$ be [Row Reduced Echelon Form](Row_Reduced_Echelon_Form) of $A$, then $C(A^T) = C(R^T)$
- basis: first $r$ rows of $R$


### [Nullspace](Nullspace)
- $\text{dim } N(A) = n - r$ - the number of free variables
- basis: special solutions for [$A\mathbf x = \mathbf 0$](Homogeneous_Systems_of_Linear_Equations)


### [Left Nullspace](Nullspace#Left_Nullspace)
- This is the nullspace of $A^T$ ($A^T$ is $n \times m$ matrix of rank $r$)
- $\text{dim } N(A^T) = m - r$ - there are $m$ columns, $m$ variables, and $m - r$ free variables


## [Singular Value Decomposition](Singular_Value_Decomposition)
We know how to find the basis for all the subspaces
- e.g. from using [Gaussian Elimination](Gaussian_Elimination) transform the matrix to the echelon form and find them
- but these bases are not "perfect". We want to use [Orthogonal Vectors](Orthogonal_Vectors) instead


SVD finds these bases:
- if $A V = U \Sigma$ then
- $\mathbf v_1, \ ... \ , \mathbf v_r$ is the basis for the row space $C(A^T)$
- $\mathbf v_{r+1}, \ ... \ , \mathbf v_{n}$ is the basis for the nullspace $N(A)$
- $\mathbf u_1, \ ... \ , \mathbf u_r$ is the basis for the column space $C(A)$
- $\mathbf u_{r+1}, \ ... \ , \mathbf u_{m}$ is the basis for the left nullspace $N(A^T)$


<img width="50%" src="<img src="http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/diagram3-svd.svg" alt="Image">" />




## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- The fundamental theorem of linear algebra, G. Strang [http://www.engineering.iastate.edu/~julied/classes/CE570/Notes/strangpaper.pdf]
- The Four Fundamental Subspaces: 4 Lines, G. Strang, [http://web.mit.edu/18.06/www/Essays/newpaper_ver3.pdf]
- [Seminar Hot Topics in Information Management IMSEM (TUB)](Seminar_Hot_Topics_in_Information_Management_IMSEM_(TUB))
