---
title: Inverse Matrices
layout: default
permalink: /index.php/Inverse_Matrices
---

# Inverse Matrices

## Inverse Matrices
A square $n \times n$ matrix $A$ has inverse (or $A$ is ''invertible'') if there exists $B$ s.t. $A \times B = B \times A = I_n$ 
- If $B$ exists, then it's denoted $A^{-1}$  
- $A$ in such case is called ''non-singular''
- otherwise (no $A^{-1}$ exists) $A$ is called ''singular''



There are two types of inverses:
- left and right
- $\underbrace{A \times A^{-1}}_\text{left} = I_n = \underbrace{A^{-1} \times A}_\text{right}$ 
- for square matrices left and right inverses are equal


## Finding the Inverse
### Gauss-Jordan Elimination
Suppose we have an equation $A \times A^{-1} = I$
- how can we solve it to find $A^{-1}$? Let's replace $A^{-1}$ by $X$ and solve $A \times X = I$
- $A \times X = \begin{bmatrix}
a_{11} & a_{12} \\ 
a_{21} & a_{22} \\
\end{bmatrix} \times \begin{bmatrix}
x_{11} & x_{12} \\ 
x_{21} & x_{22} \\
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\ 
0 & 1
\end{bmatrix} = I$
- one idea: Solve $n$ different [systems of linear equations](System_of_Linear_Equations)
  - $\begin{bmatrix}
a_{11} & a_{12} \\ 
a_{21} & a_{22} \\
\end{bmatrix} \times \begin{bmatrix}
x_{11} \\ 
x_{21} \\
\end{bmatrix} = \begin{bmatrix}
1 \\ 
0
\end{bmatrix}$ and 
  - $\begin{bmatrix}
a_{11} & a_{12} \\ 
a_{21} & a_{22} \\
\end{bmatrix} \times \begin{bmatrix}
x_{12} \\ 
x_{22} \\
\end{bmatrix} = \begin{bmatrix}
0 \\ 
1
\end{bmatrix}$ 
  - i.e. for $i$th system, take $i$th column of $X$ ($\mathbf x_i$) and $i$th row of $I$ ($\mathbf  e_i$)
- we have a bunch of systems like $A \mathbf x_i = \mathbf e_i$ that we know how to solve
  - so we can use [Gaussian Elimination](Gaussian_Elimination) for that 
  - we'll have several augmented matrices like $\left[ \begin{array}{cc| c} |a_{11} & a_{12} & 1 \\ 
a_{21} & a_{22} & 0 \\
\end{array} \right]$ and $\left[ \begin{array}{cc| c} |a_{11} & a_{12} & 0 \\ 
a_{21} & a_{22} & 1 \\
\end{array} \right]$ that we can solve to get $\begin{bmatrix}
x_{11} \\ 
x_{21} \\
\end{bmatrix}$ and $\begin{bmatrix}
x_{12} \\ 
x_{22} \\
\end{bmatrix}$
- but we can also put all such vectors $\mathbf x_i$ and $\mathbf e_i$ at the same time|   |  - $\left[ \begin{array}{cc|cc} |a_{11} & a_{12} & 1 & 0 \\ 
a_{21} & a_{22} & 0 & 1 \\
\end{array} \right]$


Gaussian Elimination:
- so once we have an augmented matrix $\Big[ \ A \; \Big|  \; I \ \Big] = \left[ \begin{array}{cc|cc} |a_{11} & a_{12} & 1 & 0 \\ 
a_{21} & a_{22} & 0 & 1 \\
\end{array} \right]$
- we come from $A$ to $I$  while applying the same actions to the augmented part $I$.
- at the end we should get $\Big[ \ A \; \Big|  \; I \ \Big] \to \Big[ \ I \; \Big| \; A^{-1} \ \Big]$ |

Why does it work? 
- suppose you did your elimination on $A$ alone, so you obtained $EA = I$ (assume no row exchanges)
- let's apply $E$ to augmented $\Big[ \ A \; \Big|  \; I \ \Big]$.  |- $E \times \Big[ \ A \; \Big|  \; I \ \Big] = \Big[ \ EA \; \Big| \; EI \ \Big] = \Big[ \ I \; \Big| \; E \ \Big]$ |- what is $E$? Since $EA = I$ we know that it can be only when $E = A^{-1}$
- so we finally have $\Big[ \ I \; \Big|  \; A^{-1} \ \Big]$ |

### [Cramer's Rule](Cramer's_Rule)
- We can compute the inverse of $A$ using the following formula:
- $A^{-1} = \cfrac{1}- where $| A|$ is the [Determinant](Determinant) of $A$ and $C^T$ is the [Cofactors](Cofactors) matrix |


## Properties
- $(AB)^{-1} = B^{-1} A^{-1}$ 
- $(A^{-1})^T = (A^T)^{-1}$


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- http://en.wikipedia.org/wiki/Invertible_matrix
- Курош А.Г. Курс Высшей Алгебры

[Category:Linear Algebra](Category_Linear_Algebra)