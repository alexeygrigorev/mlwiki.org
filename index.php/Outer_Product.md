---
title: "Outer Product"
layout: default
permalink: /index.php/Outer_Product
---

# Outer Product

## Rank One Matrices
Suppose we have two vectors $\mathbf u \in \mathbb R^m$ and $\mathbf v \in \mathbb R^n$. Then multiplication $\mathbf u \times \mathbf v^T$ gives us a matrix $A = \mathbf u \cdot \mathbf v^T$, $A \in \mathbb R^{m \times n}$
- This multiplication produces [rank](Rank_(Matrix))-1 matrices


### Rank 1 Matrices
$\mathbf u \times \mathbf v^T = \begin{bmatrix}
a \\ b \\ c
\end{bmatrix} \big[1 \ 2 \big] = \begin{bmatrix}
1a & 2a \\ 
1b & 2b \\ 
1c & 2c
\end{bmatrix}$


## Subspaces
This matrix $A$ is a special matrix: 
- all these rows lie on the same line
- all these columns are same directions 

[Subspaces](Four_Fundamental_Subspaces):
- [Row Space](Row_Space): all combinations of $\mathbf v$ 
- [Column Space](Column_Space): all combinations of  $\mathbf u$


== [Projection Matrices](Projection_Matrices) == 
Suppose we want to project to a line $\mathbf u$ 
- then the Projection Matrix $P$ is $P = \cfrac{\mathbf u \mathbf u^T}{\|  \mathbf u\|^2} = \mathbf u \mathbf u^T$ |- if $\mathbf u$ is a unit vector, e.g. $\|  \mathbf u \|^2 = 1$ |- then the projection matrix is just an outer product of $\mathbf u$ with itself


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)