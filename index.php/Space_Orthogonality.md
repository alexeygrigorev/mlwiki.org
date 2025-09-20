---
layout: default
permalink: /index.php/Space_Orthogonality
tags:
- linear-algebra
title: Space Orthogonality
---
## Space Orthogonality
Two vectors [(sub)spaces](Vector_Spaces) can also be [orthogonal](Orthogonality) 


Consider two subspaces $S$ and $T$
- $S \; \bot \; T$ means that $\forall \mathbf s \in S, \forall \mathbf t \in T: \mathbf s \; \bot \; \mathbf t$
- i.e. if every vector in $T$ is [orthogonal](Vector_Orthogonality) to every vector in $S$, then $S$ and $T$ are ''orthogonal''


## Examples
### Example 1
Suppose you have two spaces: a wall and a floor. Are they orthogonal? 
- <img src="http://habrastorage.org/files/40a/44a/1b5/40a44a1b5a02484cbab4cbff0176e6f2.png" alt="Image">
- take one vector from the wall that is 45° to one of the axis. It's not orthogonal to the floor|   it's 45° |- also, there are vectors that belong to both subspaces (and not just the origin| ) - these vectors are not orthogonal  | |So, if two spaces intersect in more than just the zero-vector, then they cannot be orthogonal 


### Example 2
Two subspaces that meet in $\mathbf 0$ can be orthogonal

<img src="http://habrastorage.org/files/a8f/5a6/c88/a8f5a6c88d5641afb9845c57911c0b15.png" alt="Image">


### [Row space](Row_space) and [Nullspace](Nullspace)
Row space $C(A^T)$ and nullspace $N(A)$ are orthogonal.
- <img src="http://habrastorage.org/files/c67/a41/cc5/c67a41cc5bfb4bcaa634b1135f5d97ad.png" alt="Image">

why?

Let's consider only rows from $A$
- $\mathbf x \in N(A) \Rightarrow A \mathbf x = \mathbf 0$
- $\begin{bmatrix}
— (\text{row 1}) \,— \\ 
— (\text{row 2}) \,— \\ 
 \vdots   \\ 
— (\text{row $n$}) \,— 
\end{bmatrix} \cdot \mathbf x = \begin{bmatrix}
0 \\ 0 \\ \vdots \\ 0
\end{bmatrix}$
- or $\begin{bmatrix}
(\text{row 1})^T \mathbf x = 0 \\ 
(\text{row 2})^T \mathbf x = 0 \\ 
 \vdots   \\ 
(\text{row $n$})^T \mathbf x = 0 \\ 
\end{bmatrix}$
- so $\mathbf x$ is orthogonal to all rows in $A$ 

what else is in the row space? linear combinations of rows of $A$ 
- $c_1 \cdot \text{row 1} + \ ... \ + c_n \cdot \text{row $n$}$ what if we multiply it by $\mathbf x$?
- $(c_1 \cdot \text{row 1} + \ ... \ + c_n \cdot \text{row $n$})^T \mathbf x = (c_1 \cdot \text{row 1})^T \mathbf x + \ ... \ + (c_n \cdot  \text{row $n$})^T \mathbf x = c_1 \cdot  \underbrace{(\text{row 1})^T \mathbf x}_{0} + \ ... \ + c_n \cdot  \underbrace{(\text{row $n$})^T \mathbf x}_{0} = 0$


### [Column Space](Column_Space) and Left Nullspace

<img src="http://habrastorage.org/files/11e/4ad/d32/11e4add32dbe4ba0a4aa6ba8adb9b456.png" alt="Image">

They are orthogonal for exactly the same reason 
- just transpose $A$ and go through the same argument as for row space and nullspace


## Orthogonal Compliments
$N(A) \; \bot \; C(A^T)$ and $\text{dim} N(A) + \text{dim} C(A^T) = n$
- they add up to the whole space 
- so they are ''orthogonal compliments'' in $\mathbb R^n$


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://en.wikipedia.org/wiki/Orthogonality
