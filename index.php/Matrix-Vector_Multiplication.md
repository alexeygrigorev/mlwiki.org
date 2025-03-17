---
title: Matrix-Vector Multiplication
layout: default
permalink: /index.php/Matrix-Vector_Multiplication
---

# Matrix-Vector Multiplication

## Matrix-Vector Multiplication
Suppose we have an $m \times n$ matrix $A$ and $n$-vector $\mathbf b$
- How to calculate $\mathbf x = A \mathbf b$?
- note that $\mathbf x \in \mathbb R^m$ 

There are two equivalent ways to do it:
- Row at a time
- Column at a time 


### Row at a Time
See $A$ as $m$ vectors along rows:

$A = \begin{bmatrix}
— \mathbf a_1 \,— \\ 
— \mathbf a_2 \,— \\ 
 ...   \\ 
— \mathbf a_m \,— 
\end{bmatrix}$

And then multiply (using [Dot Product](Dot_Product)) each row $(\mathbf a_i)^T$ with the vector $\bf x$:
- $x_i = (\mathbf a_i)^T \mathbf b$
- $\mathbf x = \begin{bmatrix}
— (\mathbf a_1)^T \mathbf b \,— \\ 
— (\mathbf a_2)^T \mathbf b \,— \\ 
 ...   \\ 
— (\mathbf a_m)^T \mathbf b \,— 
\end{bmatrix}$
- Where dot product is $\mathbf a^T \mathbf b = \sum\limits_{i=1}^m a_i b_i$


### Column at a Time
Another way to see $A$ is as $n$ vectors along columns:

$A = \begin{bmatrix}
\mathop{a_1}\limits_| ^| \ \mathop{a_2}\limits_|^| \ \cdots \  \mathop{a_n}\limits_|^|  |\end{bmatrix}$

When we multiply $A$ on a vector $\mathbf b$, it produces a [Linear Combination](Linear_Combination) of these column vectors: 

$A \mathbf b = \begin{bmatrix}
\mathop{a_1}\limits_| ^| \ \mathop{a_2}\limits_|^| \ \cdots \ \mathop{a_n}\limits_|^|  |\end{bmatrix} \mathbf b = 
  b_1 \begin{bmatrix} \mathop{a_1}\limits_| ^| \end{bmatrix}  |+ b_2 \begin{bmatrix} \mathop{a_2}\limits_| ^| \end{bmatrix} + \cdots	 |+ \ b_n \begin{bmatrix} \mathop{a_n}\limits_| ^| \end{bmatrix}$ |

### Example
$\begin{bmatrix}
2 & 5\\ 
1 & 3
\end{bmatrix} \cdot \begin{bmatrix}
1 \\
2
\end{bmatrix} $


Row at a time: 
- $[2 \ 5] \begin{bmatrix}
1 \\
2
\end{bmatrix} = 2 \cdot 1 + 5 \cdot 2 = 12$
- $[1 \ 3] \begin{bmatrix}
1 \\
2
\end{bmatrix} = 1 \cdot 1 + 3 \cdot 2 = 7$
- so $\begin{bmatrix}
2 & 5\\ 
1 & 3
\end{bmatrix} \cdot \begin{bmatrix}
1 \\
2
\end{bmatrix} = \begin{bmatrix}
12 \\
7
\end{bmatrix}$


Column at a time
- $1 \begin{bmatrix}
2 \\
1
\end{bmatrix} + 2 \begin{bmatrix}
5 \\
3
\end{bmatrix} = \begin{bmatrix}
12 \\
7
\end{bmatrix}$


### Left Vector Multiplication
A vector may be on the left of the matrix as well
- in such case $\mathbf b$ is a row vector, and thus the result $\mathbf x$ is as well a row vector
- let $\mathbf b \in \mathbb R^{m}$ and $A \in \mathbb{R}^{m \times n}$
- $\mathbf b^T A = \mathbf x^T$
- Can transpose both parts and get $A^T \mathbf b  = \mathbf x$
- and we're back to the normal column-vector case 



## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)