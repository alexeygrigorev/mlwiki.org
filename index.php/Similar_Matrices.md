---
layout: default
permalink: /index.php/Similar_Matrices
tags:
- linear-algebra
title: Similar Matrices
---
## Similar Matrices
We say that two $n \times n$ matrices $A$ and $B$ are ''similar''
- if for some invertible $M$ we can write $B = M^{-1} A \, M$




## Families
Suppose $A$ has all its [eigenvalues](Eigenvalues_and_Eigenvectors)
- then if we [diagonalize](Eigendecomposition) $A$, we have $S^{-1} A \, S = \Lambda$
- so $A$ is similar to $\Lambda$
- Here $M = \Lambda$ 
- we may take another $M \ne \Lambda$ and will get another matrix similar to $A$ (not necessarily diagonal)


A family of similar matrices for $A$ is a set of matrices similar for $A$ for different $M$ 



## Why Similar?
What is similar about such $A$ and $B$? 
- they have the same eigenvalues|   | |Let's check it:
- let $A \mathbf x = \lambda \mathbf x$
- and $B = M^{-1} A \, M$
- then $A \mathbf x = A I \mathbf x = A M M^{-1} \mathbf x = \lambda \mathbf x$
- now let's multiply by $M^{-1}$ on the left:
- $\underbrace{M^{-1} A \, M}_{B} \, M^{-1} \mathbf x = M^{-1} \lambda \mathbf x$
- $B M^{-1} \mathbf x = M^{-1} \lambda \mathbf x$
- Let $\mathbf x^*$ be $M^{-1} \mathbf x$, so we have 
- $B \mathbf x^* = \lambda \mathbf x^*$
- so matrices $A$ and $B$ share the same eigenvalue $\lambda$, but the eigenvectors $\mathbf x \ne \mathbf x^*$



For diagonalization
- $A = S^{-1} \Lambda \, S$ eigenvalues stay the same, but eigenvectors become unit vectors 


What if for some $i \ne j$, $\lambda_i = \lambda_j$?
- there might be not enough eigenvectors to span $\mathbb R^n$
- i.e. columns of $A$ are not linearly independent


### Other Things
There are other things that make these matrices similar.

$M$ does not change:
- eigenvalues $\lambda_i$ (as discussed earlier)
- [Trace](Trace_(Matrix)) and [Determinant](Determinant) (because $\text{tr}(A) = \sum \lambda_i$ and $\text{det}(A) = \prod \lambda_i$)
- rank, and therefore number of independent eigenvectors


$M$ '''does''' change
- eivenvectors
- [Nullspace](Nullspace) and left nullspace
- [Row Space](Row_Space) and [Column Space](Column_Space)
- Singular Values (see [SVD](SVD)): they depend on $A^T A$



## Jordan Form
Suppose $A$ has a family of similar matrices
- then the Jordan Form is the most diagonal matrix of the family


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
