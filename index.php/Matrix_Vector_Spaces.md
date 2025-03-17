---
title: Matrix Vector Spaces
layout: default
permalink: /index.php/Matrix_Vector_Spaces
---

# Matrix Vector Spaces

## Matrix Spaces
A Matrix space is a [Vector Space](Vector_Space) where elements are matrices


E.g. Space $M$ - $3 \times 3$ matrices 
- any $3 \times 3$ matrix an element of this space $M$ ("vector" in $M$)
- we can multiply by a scalar and add two matrices - which is why we can call it "vector space"


### [Subspaces](Vector_Subspaces)
Subspaces of the matrix space should form a space on their own. 
- What are subspaces of the matrix space? 
- All upper-triangular matrices
- all symmetric matrices
- diagonal matrices (upper-triangular $\cup$ symmetric)


### [Bases](Basis_(Linear_Algebra))
What about bases for such spaces?

E.g. $M$: $3 \times 3$ matrices:
- $\begin{bmatrix}
1 & 0 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 0 \\
\end{bmatrix}, 
\begin{bmatrix}
0 & 1 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 0 \\
\end{bmatrix},
\begin{bmatrix}
0 & 0 & 1 \\ 
0 & 0 & 0 \\ 
0 & 0 & 0 \\
\end{bmatrix}, ... ,
\begin{bmatrix}
0 & 0 & 0 \\ 
0 & 0 & 0 \\ 
0 & 0 & 1 \\
\end{bmatrix}$
- $\text{dim}\big( M \big) = 9$


$S$ - subspace of $M$, symmetric $3 \times 3$ matrices 
- $\text{dim}\big( S \big) = 6$ - because only 6 elements change in this subspace 


$U$ - subspace of $M$ with upper-diagonal matrices 
- $\text{dim}\big( U\big) = 6$ as well - same reason (but have zeros for the upper corner)

$S \cup U$ - symmetric and upper-diagonal $\Rightarrow$ diagonal matrices
- $\text{dim}\big( S \cup U\big) = 3$ 

$S \cap U$
- not a subspace:
- $S$ is 6-dim, $U$ is 3-dim


$S + U$
- any matrix from $S$ plus any matrix from $U$ 
- this way we can get possible matrix
- so it's also a subspace 
- $\text{dim}\big( S + U\big) = 9$


rule:
- $\text{dim}\big( S \big) + \text{dim}\big( U \big) = \text{dim}\big( S \cap U \big) + \text{dim}\big( S + U \big)$



## [Inner Product](Inner_Product)
How do we define the inner product?
- Element-wise: $\langle A, B \rangle = \sum_{ij} a_{ij} b_{ij}$
- then the norm based on this product is $\|  A \|_F = \langle A, A \rangle$, it's called the [Frobenius Norm](Frobenius_Norm). |



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- Kalman, Dan. "A singularly valuable decomposition: the SVD of a matrix." (1996). [http://www.math.washington.edu/~morrow/498_13/svd.pdf]

[Category:Linear Algebra](Category_Linear_Algebra)
[Category:Vector Spaces](Category_Vector_Spaces)