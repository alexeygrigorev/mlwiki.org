---
title: "Gaussian Elimination"
layout: default
permalink: /index.php/Gaussian_Elimination
---

# Gaussian Elimination

## Gaussian Elimination
Gaussian Elimination or Row Reduction is a method for solving a [System of Linear Equations](System_of_Linear_Equations)
- it corresponds to elimination of variables in the system 
- if a matrix $A$ that we reduce is non-singular and invertible, then we always have a solution
- a by-product of Gaussian Elimination is [LU Factorization](LU_Factorization)


### Row Elimination
- First, do the forward elimination to reduce the matrix to triangular 
- Then we do the back-substitution to find the solution
- When we multiply a row on some constant $c$ and subtract from any other row, we get an equivalent system


## Elimination by Example
We have the following system with 3 equations and 3 unknowns:

$\left\{\begin{array}{l}
x + 2y + z = 2\\ 
3x + 8y + z = 12 \\ 
4y + z = 2
\end{array}\right.$

Matrix form:
- $\underbrace{\begin{bmatrix}
1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}}_{A} \cdot \underbrace{\begin{bmatrix}
x \\ y \\ z
\end{bmatrix}}_{\mathbf x} = 
\underbrace{\begin{bmatrix}
2 \\ 12 \\ 2
\end{bmatrix}}_{\mathbf b}$



### Forward elimination
So, first let's see how elimination works 
- i.e. concentrate only on the matrix $A$
- $A = \begin{bmatrix}
1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}$


Let's proceed
- at each step
  - multiply the $i$th equation by the right number and subtract it from the equations below
  - s.t. there's 0 for the first column in all other rows
  - so we want to knock out the $x_i$ part of the equation, or "eliminate" $x_i$
- $\begin{bmatrix}
\boxed 1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}$. $\boxed 1$ is the 1st pivot 
- step 2.1: clean cell $a_{21}$:
  - $\begin{bmatrix}
\boxed 1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix} \sim \begin{bmatrix}
\boxed 1 & 2 & 1\\ 
0 & 2 & -2\\ 
0 & 4 & 1
\end{bmatrix}$ 
- multiplying row 1 by 3 will knock out $x$ from the 2nd equation
- step 3.1: clean cell $a_{21}$
  - already 0, continuing
- $\begin{bmatrix}
\boxed 1 & 2 & 1\\ 
0 & \boxed 2 & -2\\ 
0 & 4 & 1
\end{bmatrix}$, $\boxed 2$ is the 2nd pivot
- step 3.2
  - $\begin{bmatrix}
\boxed 1 & 2 & 1\\ 
0 & \boxed 2 & -2\\ 
0 & 4 & 1
\end{bmatrix} \sim \begin{bmatrix}
\boxed 1 & 2 & 1\\ 
0 & \boxed 2 & -2\\ 
0 & 0 & \boxed 5
\end{bmatrix}$
- $\begin{bmatrix}
\boxed 1 & 2 & 1\\ 
0 & \boxed 2 & -2\\ 
0 & 0 & \boxed 5
\end{bmatrix}$, $\boxed 5$ - it's 3rd pivot


The matrix is now in the upper-triangular form $U$


### When Does if Fails?
Not always we are able to do the forward elimination

0 at a Pivot position:
- suppose the first pivot is 0:
- $\begin{bmatrix}
\boxed 0 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}$
- But here it doesn't mean that we can't solve the system: we can switch the rows and continue:
- $\begin{bmatrix}
\boxed 3 & 8 & 1\\ 
0 & 2 & 1\\ 
0 & 4 & 1
\end{bmatrix}$
- so, if there's a 0 at the pivot position, try to exchange rows
- if there's no rows with non-zero values at the pivot position - the elimination fails
  - there's no solution to the system


=== Augmented Matrix === 
But we shouldn't forget about $\mathbf b$|   |- $A$ augmented is $\begin{bmatrix} |\mathop{a_1}\limits_| ^| \mathop{a_2}\limits_|^|  ...  \mathop{a_n}\limits_|^| \ \Bigg| \ \mathop{\mathbf b}\limits_|^|  |\end{bmatrix}$: matrix $A$ with column $\mathbf b$ stacked to the right
- $A$ augmented: $\left[\begin{array}{ccc| c} |1 & 2 & 1 & 2\\ 
3 & 8 & 1 & 12\\ 
0 & 4 & 1 & 2
\end{array}\right]$
- the right part $\mathbf b$ also changes as we go through elimination
- $\left[\begin{array}{ccc| c} |1 & 2 & 1 & 2\\ 
3 & 8 & 1 & 12\\ 
0 & 4 & 1 & 2
\end{array}\right] \to \left[\begin{array}{ccc| c} |1 & 2 & 1 & 2\\ 
0 & 2 & -6 & 6\\ 
0 & 4 & 1 & 2
\end{array}\right] \to \left[\begin{array}{ccc| c} |1 & 2 & 1 & 2\\ 
0 & 2 & -6 & 6\\ 
0 & 0 & 5 & -10
\end{array}\right]$
- let $\mathbf c$ be the result of applying elimination to $\mathbf b$


### Back Substitution
After we forward-eliminated variables of augmented $A$, we can do back substitution:
- Our matrix is 
$\left[\begin{array}{ccc| c} |1 & 2 & 1 & 2\\ 
0 & 2 & -6 & 6\\ 
0 & 0 & 5 & -10
\end{array}\right]$
- It means that our system is 


$\left\{\begin{array}{rl}
x + 2y + z & = 2\\ 
2y - 2z & = 6 \\ 
5z & = -10
\end{array}\right.$

Now we just go backwards and solve: first for $z$, then for $y$, and finally for $x$
- we get $z = -2, y = -1, x =2$
- it's easy to solve because the matrix is triangular


### Elimination: Matrix Form
We can write these elimination steps in matrix form
- $\begin{bmatrix}
1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}$
- the first step of the elimination was to take first and last rows unchanged, and subtract 3 times 1st row from the second. 
- Can we write it with [Matrix Multiplication](Matrix_Multiplication)?
  - $\begin{bmatrix}
1 & 0 & 0\\ 
? & ? & ?\\ 
0 & 0 & 1
\end{bmatrix} \times \begin{bmatrix}
1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix}$
  - The first and last rows remain unchanged - hence we have $\begin{bmatrix}
1\\ 
?\\ 
0
\end{bmatrix}$ and $\begin{bmatrix}
0\\ 
?\\ 
1
\end{bmatrix}$
  - what should we put instead of $[? \ ? \ ?]$ so multiplication takes us from one matrix to another?
  - $\begin{bmatrix}
1 & 0 & 0\\ 
\boxed{-3} & 1 & 0\\ 
0 & 0 & 1
\end{bmatrix}$
  - we want to subtract 3 times row 1 from row 2:
  - $\begin{bmatrix}
1 & 0 & 0\\ 
\boxed{-3} & 1 & 0\\ 
0 & 0 & 1
\end{bmatrix} \times \begin{bmatrix}
1 & 2 & 1\\ 
3 & 8 & 1\\ 
0 & 4 & 1
\end{bmatrix} = \begin{bmatrix}
1 & 2 & 1\\ 
0 & 2 & -2\\ 
0 & 4 & 1
\end{bmatrix}$
- let $E_{21}$ be the matrix that's used for step 2,1 of the elimination
  - $E_{21} A = \begin{bmatrix}
1 & 2 & 1\\ 
0 & 2 & -2\\ 
0 & 4 & 1
\end{bmatrix}$
- we continue this way until we transform $A$ to $U$
  - so we have $E_{21} (E_{21} A) = U$ 
  - or $\underbrace{(E_{21} E_{21})}_E A = EA = U $ 
  - This a part of [$LU$ Factorization](LU_Factorization)


What if we need to exchange rows? 
- use a [Permutation Matrix](Permutation_Matrices)|   |- in this case the correct solution is $E (PA) = U$ |


## See Also
- [Inverse Matrices#Gauss-Jordan Elimination](Inverse_Matrices#Gauss-Jordan_Elimination)
- [LU Factorization](LU_Factorization)

## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))
- Курош А.Г. Курс Высшей Алгебры

[Category:Linear Algebra](Category_Linear_Algebra)