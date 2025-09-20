---
layout: default
permalink: /index.php/Cramer's_Rule
tags:
- linear-algebra
title: Cramer's Rule
---
## Cramer's Rule
This is a method for finding a [Matrix Inverse](Inverse_Matrices) and for solving a [System of Linear Equations](System_of_Linear_Equations).


## Finding Inverse
The formula is $A^{-1} = \cfrac{1}- $| A|$ is the [Determinant](Determinant) of $A$  |- $C$ is the [Cofactors](Cofactors) matrix of $A$ 


### $2 \times 2$ case: Motivation
Let $A$ be an $2 \times 2$ matrix
- $A = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix}$
- let's find $A^{-1}$ with Gauss-Jordan elimination (see [Inverse Matrices](Inverse_Matrices))
  - $\left[ \begin{array}{cc| cc} |a_{11} & a_{12} & 1 & 0 \\ 
a_{21} & a_{22} & 0 & 1 \\
\end{array} \right] \sim $ row 2: $\text{row $2$} - \cfrac{a_{21}}{a_{11}} \text{row $1$}$
  - $\sim \left[ \begin{array}{cc| cc} |a_{11} & a_{12} & 1 & 0 \\ 
0 & a_{22} - a_{12} \cfrac{a_{21}}{a_{11}} & - \cfrac{a_{21}}{a_{11}} & 1 \\
\end{array} \right] \sim $ now divide first row by $a_{11}$ and multiply second by $a_{11}$
  - $\sim \left[ \begin{array}{cc| cc} |1 & \cfrac{a_{12}}{a_{11}} & \cfrac{1}{a_{11}} & 0 \\ 
0 & a_{11} a_{22} - a_{12} a_{21} & - a_{21} & a_{11} \\
\end{array} \right] =$ now note that $a_{11} a_{22} - a_{12} a_{21} = |  A |$, so |  - $ = \left[ \begin{array}{cc| cc} |1 & \cfrac{a_{12}}{a_{11}} & \cfrac{1}{a_{11}} & 0 \\ 
0 & | A| & - a_{21} & a_{11} \\ |\end{array} \right] \sim $ let's divide row 2 by $| A|$ |  - $ \sim \left[ \begin{array}{cc| cc} |1 & \cfrac{a_{12}}{a_{11}} & \cfrac{1}{a_{11}} & 0 \\ 
0 & 1 & - \cfrac{a_{21}}\end{array} \right] \sim $ now for row 1: $\text{row $1$} - \cfrac{a_{12}}{a_{11}} \text{row $2$}$
  - $ \sim \left[ \begin{array}{cc| cc} |1 & 0 & \cfrac{a_{22}}0 & 1 & - \cfrac{a_{21}}\end{array} \right]$
- so $A^{-1} = \cfrac{1}a_{22} & - a_{12} \\
- a_{21} & a_{11} \\
\end{bmatrix}$
- now we can note that the [Cofactors](Cofactors) of $A$ are: $C_{11} = a_{22}, C_{12} = -a_{21}, C_{21} = - a_{12}, C_{22} = a_{11}$
- we can put all cofactors in one matrix $C = \begin{bmatrix}
C_{11} & C_{12} \\
C_{21} & C_{22} \\
\end{bmatrix} = 
\begin{bmatrix}
a_{22} & -a_{21} \\
-a_{12} & a_{11} \\
\end{bmatrix} =
\begin{bmatrix}
a_{22} & - a_{12} \\
- a_{21} & a_{11} \\
\end{bmatrix}^T$
- this is the same as in the formula for $A^{-1}$, but transposed|   |- so $A^{-1} = \cfrac{1} |

### General Case: Check
Does it always work? Let's check 
- if $A^{-1} = \cfrac{1}- or, $\underbrace{\begin{bmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{bmatrix}}_{A} 
\underbrace{\begin{bmatrix}
  C_{11} & C_{21} & \cdots & C_{n1} \\
  C_{12} & C_{22} & \cdots & C_{n2} \\
  \vdots & \vdots & \ddots & \vdots \\
  C_{1n} & C_{2n} & \cdots & C_{nn} \\
\end{bmatrix}}_{C^T} = 
\underbrace{\begin{bmatrix}
  | A| & 0 & \cdots & 0 \\ |  0 & | A| & \cdots & 0 \\ |  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & | A| \\ |\end{bmatrix}}_- so why do we have zeros off the diagonal?
  - $\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
\end{bmatrix} \begin{bmatrix}
C_{11} & C_{21} \\
C_{12} & C_{22} \\
\end{bmatrix} = 
\begin{bmatrix}
\boxed{a_{11} C_{11}} + a_{12} C_{12} & a_{11} C_{21} + a_{12} C_{22} \\
a_{21} C_{11} + a_{22} C_{12} & a_{21} C_{21} + \boxed{a_{22} C_{22}} \\
\end{bmatrix}$
  - need to check that $\text{row $i$} \times \text{cofactor of $i$} = | A|$ |  - and $\text{row $i$} \times \text{cofactors of $j$} = 0$ ($i \ne j$)
  - then we'll have $| A|$ only on the diagonal |

$\text{row $i$} \times \text{cofactors of $i$} = | A|$ |- $\text{row $i$} = \begin{bmatrix} a_{i1} & a_{i2} & \cdots & a_{in} \end{bmatrix}$
- $\text{cofactors of $i$} = \begin{bmatrix} C_{i1} \\ C_{i2} \\ \vdots \\ C_{in} \end{bmatrix}$
- so $\text{row $i$} \times \text{cofactors of $i$} = \sum\limits_k a_{ik} C_{ik}$
- note that this is the [Cofactors](Cofactors) formula for calculating the determinant|   |- thus, $\text{row $i$} \times \text{cofactors of $i$} = |A|$ |

$\text{row $i$} \times \text{cofactors of $j$} = 0$ for $i \ne j$
- let's have a look what this dot product calculates
- take row $i$ of $A$ and row $j$ of $C$ (i.e. column $j$ of $C^T$)
- $\text{row $i$} \times \text{cofactors of $j$} = \begin{bmatrix} a_{i1} & a_{i2} & \cdots & a_{in} \end{bmatrix} \begin{bmatrix} C_{j1} \\ C_{j2} \\ \vdots \\ C_{jn} \end{bmatrix} = \sum\limits_k a_{ik} C_{jk}$
- this is a cofactors formula for a new matrix $A^*$ where the row $i$ of $A$ is copied to row $j$ of $A$. So this new matrix has two equal rows, therefore $|  A^* | = 0$  |- and thus, $\text{row $i$} \times \text{cofactors of $j$} = 0$


so we showed that 
- $A \, C^T = | A| \, I$ |- therefore, $A^{-1} = \cfrac{1}

## Cramer's Rule: Solving $A \mathbf x = \mathbf b$
Now since we can find the inverse of $A^{-1}$, we can solve the system $A \mathbf x = \mathbf b$
- let $A$ be $n \times n$ invertible matrix
- we know that $A^{-1} = \cfrac{1}- let's have a look at the components of $\mathbf x$
  - $x_1 = \cfrac{ (C^T \mathbf b)_1 }  - $(C^T \mathbf b)_1  = (\text{column 1 of $C$})^T \mathbf b = C_{11} b_1 + C_{21} b_2 + \ ... $
  - any time we multiply something by cofactors, it's the same as getting a determinant of some matrix
  - in this case, we're calculating the determinant of $B_1$ - matrix $A$ with column 1 replaced with $\mathbf b$ 
  - thus, $x_1 = \cfrac  b_{1} & a_{12} & \cdots & a_{1n} \\
  b_{2} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  b_{n} & a_{n2} & \cdots & a_{nn} \\
\end{vmatrix} / \begin{vmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{vmatrix}$
- and generally, $x_i = \cfrac
This is known as the '''Cramer's Rule'''


### Efficiency
This is known as not very practical method for computing the inverse or for solving the system
- some more computationally efficient methods are [Gaussian Elimination](Gaussian_Elimination) (= [LU Decomposition](LU_Decomposition))



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- Strang, G. Introduction to linear algebra.
- http://en.wikipedia.org/wiki/Cramer%27s_rule
