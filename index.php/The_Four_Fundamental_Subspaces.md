---
layout: default
permalink: /index.php/The_Four_Fundamental_Subspaces
tags:
- linear-algebra
title: The Four Fundamental Subspaces
---

## The Four Fundamental Subspaces


This is a first blog post in the series ["Fundamental Theorem of Linear Algebra"](http://www.itshared.org/2015/06/the-fundamental-theorem-of-linear.html), where we are working through Gilbert Strang's paper ["The fundamental theorem of linear algebra"](https://scholar.google.com/scholar?cluster=7422674465482742075&hl=ru&as_sdt=0,5) published by American Mathematical Monthly in 1993. 

In this post, we will go through the first two parts of the Fundamental Theorem: the **dimensionality** and the **orthogonality** of the Fundamental Subspaces.  

![](http://habrastorage.org/files/3b0/9ba/cea/3b09bacea4eb4987a900c4ab7d65114f.png)
<small>Original Strang's Diagram from the paper.</small>

But first, let's start with defining the notation we will use. Greek lower case letter $\alpha, \beta, \ ...$ are used for scalars, bold letters $\mathbf b, \mathbf x, \ ...$ – vectors, lowercase indexed letters $x_1, x_2, \ ...$ – components of vectors, capital letters $A$ – matrices, indexed bold letters $\mathbf a_1, \mathbf a_2, \ ... \ , \mathbf r_1, \mathbf r_2, \ ...$ –
columns or rows of a matrix. $\mathbf 0$ is a vector of appropriate dimensionality with $0$ in each component.

## Fundamental subspaces

A *vector space* is a set where we have addition and scalar multiplication operators (refer to [wikipedia](http://en.wikipedia.org/wiki/Vector_space) for more details). A *subspace* is a subset of some vector space such that it's closed under addition and scalar multiplication, i.e. given some subspace $S$, if $\mathbf x, \mathbf y \in S$ then for any $\alpha, \beta \in \mathbb R$, $(\alpha \mathbf x + \beta \mathbf y) \in S$.

Let $A$ be a matrix with $m$ rows and $n$ columns. Then there are four fundamental subspaces for $A$:

- $C(A)$: the *column space* of $A$, it contains all linear combinations of the columns of $A$
- $C(A^T)$: the *row space* of $A$, it contains all linear combinations of the rows of $A$ (or, columns of $A^T$)
- $N(A)$: the *nullspace* of $A$, it contains all solutions to the system $A \mathbf x = \mathbf 0$
- $N(A^T)$: the *left nullspace* of $A$, it contains all solutions to the system $A^T \mathbf y = \mathbf 0$.

**Example**. Consider a system with $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{bmatrix}$ and $\mathbf b = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$.

The column space $C(A)$ is formed by all linear combinations of columns of $A$: i.e. it is $\alpha_1 \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} + \alpha_2 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \alpha_3 \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix}$ with all possible choices of $(\alpha_1, \alpha_2, \alpha_3)$.

The row space $C(A^T)$ is formed by linear combinations of rows of $A$: $\beta_1 \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} + \beta_2 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \beta_3 \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$ for all possible choices of $(\beta_1, \beta_2, \beta_3)$. 

We will see examples for $N(A)$ and $N(A^T)$ a bit later.

Dimensionality
--------------

The first part of the theorem talks about the dimensionality of these subspaces. It states the following:

- $\operatorname{dim} C(A) = \operatorname{dim} C(A^T) = r$, where $r$ is the rank of $A$,
- $\operatorname{dim} C(A^T) + \operatorname{dim} N(A) = n$ and
- $\operatorname{dim} C(A) + \operatorname{dim} N(A^T) = m$

It means that 

- $\operatorname{dim} C(A) = \operatorname{dim} C(A^T) = r$,
- $\operatorname{dim} N(A) = n - r$ and
- $\operatorname{dim} N(A^T) = m - r$

How can we see that? 

Let's continue with the example and find the nullspace of $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{bmatrix}$.

First, we notice that the third row of $A$ is a sum of the first one and the second one. Thus, the dimensionality of the row space $C(A^T)$ is 2, and it means that the dimensionality of the nullpace $N(A)$ must be $m - r = 3-2=1$. 

Let's check it: apply [Gaussian elimination](http://en.wikipedia.org/wiki/Gaussian_elimination) to transform $A$ to the [Row-Reduced Echelon Form](http://en.wikipedia.org/wiki/Row_echelon_form) ("RREF" for short).

A matrix is in the echelon form when the leading zero elements of each row form a "staircase":

![](http://habrastorage.org/files/fd6/13b/c5b/fd613bc5b9354ddd8856d5ee1a30cfeb.png)

The first non-zero element of each row is called *pivot*, and the corresponding columns are called *pivot columns*. In RREF, the pivot elements must be equal to $1$ and all other elements of the pivot column must be equal to $0$. Other non-pivot columns are called *free columns*. 

RREF is typically obtained via Gaussian Elimination: you can subtract a multiple of a row from any other row and also you can multiply any row by a scalar until your matrix is in RREF.

If you have Matlab, you can calculate RREF as follows: 

	R = rref(A)

Let's get back to our matrix $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{bmatrix}$ and its RREF is $R = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$

There are two pivot variables, let's these variables $x_1$ and $x_2$. Also, there is one free variable $x_3$ that doesn’t have a pivot: it has $0$ on this position. 

The free variable can take any value, for example, we can assign $x_3 = 1$, so the solution to $A \mathbf x = \mathbf 0$ is $x_n = \begin{bmatrix} x_1 \\ x_2 \\ 1 \end{bmatrix}$. Now we solve  the system and obtain $x_1 = 1, x_2 = -2$, so the solution is $x_n = \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$. 

There is nothing special about the choice $x_3 = 1$, so instead we can choose $x_3 = \alpha$, and obtain $x_n = \begin{bmatrix} \alpha \\ -2 \alpha \\ \alpha \end{bmatrix} = \alpha \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$. All possible choices of $\alpha$ form the nullspace $N(A)$.

So the nullspace of $A$ is a line.

Orthogonality
-------------

The second part of the theorem says that the row space $C(A^T)$ and the nullspace $N(A)$ of $A$ are orthogonal and that the column space $C(A)$ and the left nullspace $N(A^T)$ are also orthogonal.

Two vectors are *orthogonal* if their dot product is $0$. If all vectors of one subspace are orthogonal to all vectors of another subspace, these subspaces are called *orthogonal*.

It is easy to see:

- Consider the system $A \mathbf x = \mathbf 0$
- Let's write $A$ as rows: $$\begin{bmatrix} — (\text{row 1}) \,— \\  — (\text{row 2}) \,— \\ 
 \vdots   \\
— (\text{row $n$}) \,— 
\end{bmatrix} \cdot \mathbf x = \begin{bmatrix}
0 \\ 0 \\ \vdots \\ 0
\end{bmatrix}$$
- You can convince yourself that it's the same as writing $$\begin{bmatrix}
(\text{row 1})^T \mathbf x = 0 \\ 
(\text{row 2})^T \mathbf x = 0 \\ 
 \vdots   \\ 
(\text{row $n$})^T \mathbf x = 0 \\ 
\end{bmatrix}$$
- Thus every row of $A$ is orthogonal to this $\mathbf x$. 
- Since$A \mathbf x = \mathbf 0$, this $\mathbf x$ belongs to the nullspace $N(A)$, and it means that every $\mathbf x \in N(A)$ is orthogonal to any row of $A$.
- Now let's consider some linear combinations of rows, e.g. $\big( \alpha (\text{row 1}) + \beta (\text{row 2}) \big)^T \mathbf x$, then $\alpha (\text{row 1})^T \mathbf x + \beta (\text{row 2})^T \mathbf x = \alpha \mathbf 0 + \beta \mathbf 0 = \mathbf 0$
- So any linear combination of rows of $A$ (i.e. any vector from the row space $C(A^T)$) is orthogonal to any vector from the nullspace $N(A)$.
- It means that $C(A^T)$ and $N(A)$ are orthogonal.

The same is true for $C(A)$ and $N(A^T)$: all we have to do is to transpose the matrix $A$ and come to the same conclusion.

&nbsp;

If two spaces are orthogonal and they together span the entire vector space, they are called *orthogonal complements*. $C(A^T)$ and $N(A)$ are
orthogonal complements, and the same is true for $C(A)$ and $N(A^T)$. We can illustrate this with a picture: 

![](http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/diagram0.svg)

On the left part of the diagram we have the row space $C(A^T)$ and the nullspace $N(A)$. They are orthogonal, meet only in the origin, and they together span the space $\mathbb R^n$. On the right we have $C(A)$ and $N(A^T)$: they are also orthogonal and they together span $\mathbb R^m$.

## Solution to $A \mathbf x = \mathbf b$

Now we can use the first two parts of the theorem and develop some intuition about the system $A \mathbf x = \mathbf b$ and the crucial role the subspaces play in it. 

Row Space Solution
---------------

The *general* solution to the system is $\mathbf x = \mathbf x_p + \mathbf x_n$, where $\mathbf x_p$ is some solution to the system, and $\mathbf x_n$ is the *homogenous* (nullspace) solution to $A \mathbf x = \mathbf 0$. It works because $A \mathbf x = A (\mathbf x_p + \mathbf x_n) = A \mathbf x_p + A \mathbf x_n = \mathbf b + \mathbf 0 = \mathbf b$.

Since $C(A^T)$ and $N(A)$ are orthogonal complements, they span the entire space $\mathbb R^n$ and every vector $\mathbf x$ from $\mathbb R^n$ can be expressed as $\mathbf x = \mathbf x_r + \mathbf x_n$ such that $\mathbf x_r$ is from the row space $C(A^T)$ and $\mathbf x_n$ is from the nullspace $N(A)$.

There are many possible choices of $\mathbf x_p$, but among them only one of them belongs to the row space. We call it the *row space solution* $\mathbf x_r$ to the system.

But sometimes there is no solution. A solution exists only if the right-side $\mathbf b$ belongs to the column space $C(A)$, i.e. when $\mathbf b$ is a linear combination of columns of $A$.

Let's put it more formally: if $\mathbf a_i$ are the columns of $A$, i.e. $A = \left[ \mathop{\mathbf a_1}\limits_|^| \, \mathop{\mathbf a_2}\limits_|^| \ \cdots \  \mathop{\mathbf a_n}\limits_|^| \right]$, then the solution exists if we can find coefficients $(x_1 , \ ... \ , x_n)$ such that $x_1 \mathbf a_1 + x_2 \mathbf a_2 + \ ... \ + x_n \mathbf a_n = \mathbf b$. If we can, then they form a solution $\mathbf x = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix}$. 

You can convince yourself that writing $x_1 \mathbf a_1 + x_2 \mathbf a_2 + \ ... \ + x_n \mathbf a_n = \mathbf b$ is the same as writing $A \mathbf x = \mathbf b$.

We can illustrate this with a diagram:

![](http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/diagram1.svg)

In this diagram $\mathbf b$ is in the column space  $C(A)$, so there is a solution $\mathbf x$ to the system $A \mathbf x = \mathbf b$. This solution $\mathbf x$ can be expressed as $\mathbf x_r + \mathbf x_n$ such that $\mathbf x_r$ belongs to the row space $C(A^T)$ and $\mathbf x_n$ is from the nullspace $N(A)$. We know that $A \mathbf x_r = \mathbf b$ and $A \mathbf x = \mathbf b$, and we can show that with arrows from $\mathbf x_r$  and $\mathbf x$ to $\mathbf b$.

Let's get back to our example: consider a system $A \mathbf x = \mathbf b$ with $A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{bmatrix}$ and $\mathbf b = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$.

We already know that the column space is $\alpha_1 \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} + \alpha_2 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \alpha_3 \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix}$. Now to check if the system has a solution, we need to show that $\mathbf b \in C(A)$. Or, in other words, we need to show that it is possible to find such $\mathbf x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$ that $x_1 \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} + x_2 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + x_3 \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$.

In this example it is possible: $x_1 = -1, x_2 = 1$ and $x_3 = 0$. So we have  $-1 \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} + 1 \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + 0 \begin{bmatrix} 1 \\ 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$.

Not only have we established that $\mathbf b \in C(A)$, but also found a solution $\mathbf x_p = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$. This solution is not necessarily the row space solution, i.e. it may not belong to the row space $C(A^T)$.

The nullspace $N(A)$ contains all the solutions to $A \mathbf x = \mathbf 0$. We already know how to find the nullspace solution, and for this example it's $x_n = \begin{bmatrix} \alpha \\ -2 \alpha \\ \alpha \end{bmatrix} = \alpha \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$. 

The complete solution $\mathbf x$ is a sum of some solution $\mathbf x_p $ and the homogenous solutions $\mathbf x_n$:
$\mathbf x = \mathbf x_p + \mathbf x_n = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} + \alpha \begin{bmatrix} 1 \\ -2 \\ 1 \end{bmatrix}$. Note that the set of all solutions $\mathbf x$ is just a shifted nullspace $N(A)$.

We can illustrate it with following picture:

![](http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/row-space-x-special3.svg)

Because the rank of $A$ is two, the row space $C(A^T)$ contains only two linearly independent vectors, so it is a plane in $\mathbb R^3$ formed by two rows $\mathbf r_1$ and $\mathbf r_2$. The row space solution $\mathbf x_r$ also belongs to $C(A^T)$, but the solution $\mathbf x_p = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$ does not. 

Also, maybe this animation will be helpful:

<video poster="//i.imgur.com/R8QFjOKh.jpg" preload="auto" autoplay="autoplay" muted="muted" loop="loop" webkit-playsinline>
<source src="//i.imgur.com/R8QFjOK.webm" type="video/webm">
<source src="//i.imgur.com/R8QFjOK.mp4" type="video/mp4">
</video>

Click [here](http://i.imgur.com/R8QFjOK.gifv) if it doesn't play.

Here we draw the row space, the nullspace and the solution set, and we just rotate it to see what's going on (otherwise it's hard to understand a 3D picture in 2D). Here the plane is the row space, the black dashed line is the nullspace, and the red dashed line is the solution set. We see that the solution space and the row space intersect in one special point, and this point is the special solution $\mathbb x_r$.

Let's freeze it and look at one particular angle:

![](http://alexeygrigorev.com/projects/imsem-ws14-lina/img-svg/3dpic-31.svg)

In this 2D projection we don't see the row space altogether, so it looks like its two basis vectors are lying on the line. Then we have the nullspace, which is orthogonal to the row space, with one basis vector. Finally, we have a solution set (dotted red line) and one particular solution (the red arrow). The row space solution $\mathbf x_r$ is on the intersection between the solution set and the row space (the black arrow). 

You are probably wondering how we can obtain the row space solution $\mathbf x_r$. To do this, at first we need to recognize that it’s a projection of $\mathbf x_p$ onto the row space $C(A^T)$. We will see how to find this projection in the next post of this series: "The Least Squares: The Projection onto Subspaces". <!-- [The Least Squares: The Projection onto Subspaces](http://www.itshared.org/2015/06/the-least-squares-projection-onto.html). -->
