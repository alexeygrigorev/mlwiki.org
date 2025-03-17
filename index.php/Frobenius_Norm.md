---
title: Frobenius Norm
layout: default
permalink: /index.php/Frobenius_Norm
---

# Frobenius Norm

## Frobenius Norm
Is a norm for [Matrix Vector Spaces](Matrix_Vector_Spaces): a vector space of matrices
- Define [Inner Product](Inner_Product) element-wise: $\langle A, B \rangle = \sum_{ij} a_{ij} b_{ij}$
- then the norm based on this product is $\|  A \|_F = \langle A, A \rangle$ |- this norm is ''Frobenius Norm''


Orthogonality:
- Matrices $A$ and $B$ are orthogonal if $\langle A, B \rangle = 0$


## Norm of [Matrix Multiplication](Matrix_Multiplication)
### [Rank-1 Matrices](Outer_Product)
What about the norm of two rank-1 matrices?
- let $A = \mathbf x \mathbf y^T$ and $B = \mathbf u \mathbf v^T$ 
- then $\langle A, B \rangle = \langle \mathbf x \mathbf y^T, \mathbf u \mathbf v^T \rangle$
- $\mathbf x \mathbf y^T = \begin{bmatrix}
|  & & | \\ |\mathbf x y_1 & \cdots & \mathbf x y_n \\ 
|  & & | \\ |\end{bmatrix}$ and $\mathbf u \mathbf v^T = \begin{bmatrix}
|  & & | \\ |\mathbf u v_1 & \cdots & \mathbf u v_n \\ 
|  & & | \\ |\end{bmatrix}$
- thus, $\langle \mathbf x \mathbf y^T, \mathbf u \mathbf v^T \rangle = \sum\limits_i \langle \mathbf x y_i , \mathbf u v_i \rangle = \langle \mathbf x, \mathbf u \rangle \sum_i y_i v_i = \langle \mathbf x, \mathbf u \rangle  \langle \mathbf y, \mathbf v \rangle$


Orthogonality
- so two rank-1 matrices will be orthogonal if $\mathbf x \; \bot \; \mathbf u$ or $\mathbf y \; \bot \; \mathbf v$


### General Case
- Let $X$ and $Y$ be two matrices
- and $\mathbf x_i$ be the columns of $X$ and $\mathbf y_i^T$ be the rows of $Y$
- then norm of the multiplication is $\|  XY \|_F = \langle XY, XY \rangle = (\sum_i \mathbf x_i \mathbf y_i^T) (\sum_j \mathbf x_j \mathbf y_j^T) = \sum_{ij} \langle \mathbf x_i \mathbf x_j \rangle \langle \mathbf y_i \mathbf y_j \rangle = \sum_i \| \mathbf x_i \|^2 \| \mathbf y_i \|^2 + \sum_{i \ne j} \langle \mathbf x_i \mathbf x_j \rangle \langle \mathbf y_i \mathbf y_j \rangle$ |

if $\mathbf x_i$ are orthogonal, then
- $\|  XY \|_F = \sum_i \| \mathbf x_i \|^2 \| \mathbf y_i \|^2$ (cross terms are 0 because of orthogonality) |

if $\mathbf x_i$ are orthonormal, then
- $X$ is an [Orthogonal Matrix](Orthogonal_Matrix)
- $\|  XY \|_F = \sum_i \| \mathbf y_i \|^2 = \| Y \|^2_F$ |

Same applies if $\mathbf y_i$ are orthogonal/orthonormal 



## Norm of Matrices
### [Rank-1 Matrices](Outer_Product)
Suppose $A$ is a rank-1 matrix, i.e. $A = \mathbf x \mathbf y^T$
- $A = \mathbf x \mathbf y^T = \begin{bmatrix}
|  & & | \\ |\mathbf x y_i & \cdots & \mathbf x y_n \\
|  & & | \\ |\end{bmatrix} = 
\begin{bmatrix}
- & x_1 \mathbf y & - \\
 & \vdots &  \\
- & x_n \mathbf y & - 
\end{bmatrix} =
\begin{bmatrix}
x_1 y_1 & \cdots & x_1 y_n \\
\vdots & \ddots & \vdots \\
x_n y_1 & \cdots & x_n y_n \\
\end{bmatrix}$ 
- thus $\|  A \|^2_F = \sum_i \| y_i \mathbf x \|^2 = \sum_i \| x_i \mathbf y \|^2 = \sum_{ij} (x_i y_j)^2$ |- can simplify it further: $\|  A \|^2_F = \sum_i \| y_i \mathbf x \|^2 = \sum_i y_i^2 \| \mathbf x \|^2 = \| \mathbf x \|^2 \sum_i y_i^2 = \| \mathbf x \|^2 \| \mathbf y \|^2$ |


### General Case
- If $A$ is an $m \times n$ matrix 
- and $\mathbf a_i$ are columns of $A$ and $\mathbf r_j$ are rows of $A$, then
- $\|  A \|^2_F = \sum_{ij} A_{ij} = \sum_i \| \mathbf a_i \|^2 = \sum_j \| \mathbf r_j \|^2$ |

Using [SVD](SVD), we can find another way:
- SVD of $A$ is $A V = U \Sigma$
- then $\|  A V \|_F^2 = \| U \Sigma \|_F^2$ |- both $V$ and $U$ are orthonormal, thus by norm multiplication have 
- then $\|  A \|_F^2 = \| \Sigma \|_F^2$ |- or, $\|  A \|_F^2 = \sum_{i=1}^r \sigma_i^2$ - sum of singular values, and $\| A \|_F = \sqrt{\sum_{i=1}^r \sigma_i^2}$ |

## Properties
For any matrix $A$, $\|  A \|_F = \sqrt{\text{tr}(AA^T)} = \sqrt{\text{tr}(A^T A)}$ |- $\|  A \|_F^2 = \sum_{i=1}^n \| \mathbf a_i \|^2$ where $\mathbf a_i$ are columns of $A$  |- consider $A^T A$: on the main diagonal we have $\mathbf a_i^T \mathbf a_i = \|  \mathbf a_i \|^2$ |- so $\|  A \|_F^2 = \text{tr}(A^T A)$ |- can show the same way for rows of $A$ via $A A^T$


Can also apply SVD to show that:
- let $A = U \Sigma V^T$ be SVD of A
- then $\|  A \|_F^2 = \| \Sigma \|_F^2 = \sum\limits_{i=1}^r \sigma_i^2$ |- $\sigma_i^2$ are [Eigenvalues](Eigenvalues) of $AA^T$ and $A^TA$
- then, $\sum \sigma_i^2 = \text{tr}(A A^T) = \text{tr}(A^T A)$ 
- so it also shows that sum of eigenvalues is the trace of the matrix


## Application
This is used for [Reduced Rank Approximation](Reduced_Rank_Approximation) to show that [SVD](SVD) gives the best approximation in terms of Total Least Squares


## Sources
- Kalman, Dan. "A singularly valuable decomposition: the SVD of a matrix." (1996). [http://www.math.washington.edu/~morrow/498_13/svd.pdf]


[Category:Linear Algebra](Category_Linear_Algebra)
[Category:Vector Spaces](Category_Vector_Spaces)
[Category:Norms](Category_Norms)