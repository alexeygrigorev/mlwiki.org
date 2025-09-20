---
title: "Reduced Rank Approximation"
layout: default
permalink: /index.php/Reduced_Rank_Approximation
---

# Reduced Rank Approximation

## Reduced Rank Approximation
Given an $m \times n$ matrix $A$, the goal is to describe $A$ using fewer than $m \times n$ entries
- also called '''Total Least Squares''' because we want to approximate matrix $A$ with matrix $B$ by minimizing $\|  A - B \|^2_F$ |- in the [Matrix Vector Spaces](Matrix_Vector_Spaces) with [Frobenius Norm](Frobenius_Norm)



### Redundancy of Matrix
- [rank](Rank_(Matrix)) of $A$ specifies the number of linearly independent columns/rows
- so it's a good measure of redundancy
- if the rank is low, $A$ has a lot of redundancy
- such matrices can be expressed more efficiently than just a table of entries 
- for example, [Rank One Matrices](Outer_Product) are very redundant: instead of $mn$ entries they can be represented by $m + n$ entries


## Approximation with [SVD](SVD)
### Best Approximation
Finding the approximation
- Suppose our matrix doesn't have rank-1, 
- but we want to find the best rank-1 approximation to this matrix 
- so we want to express $A$ in terms of two vectors and their [Outer Product](Outer_Product)


How do we define "best"?
- let matrix $B$ be the best rank-one approximation of $A$ if $\|  B - A \|^2$ is minimum  |- so $B$ is the best in terms of "Total Least Squares"
- norm for a matrix? Use [Frobenious Norm](Frobenious_Norm)
- so use element-wise [Inner Product](Inner_Product) $\langle A, B \rangle = \sum_{ij} a_{ij} b_{ij}$ and norm is $\|  A \|_F = \langle A, A \rangle$. |


Let's apply [SVD](SVD):
- $A = U \Sigma V^T = \sum_i \sigma_i \mathbf u_i \mathbf v_i^T$
- $\|  A \|^2_F = \sum_i \| \sigma_i \mathbf u_i \mathbf v_i^T \|^2_F$  |  - <!-- TODO: why??? prove it --> |  - the terms are orthogonal w.r.t. matrix inner product
- SVD is orthogonal decomposition into rank-1 matrices
- also because norm of rank-1 matrix is $\|  \mathbf u_i \mathbf v_i^T \|^2_F = \| \mathbf u_i  \|^2 \|\mathbf v_i  \|^2$ and $\mathbf v_i$ and $\mathbf u_i$ are orthonormal, we have  |- $\|  A \|^2_F = \sum_i \sigma_i^2$  |


### Approximation
Let's express $A$ as $A = S_k + E_k$
- where $S_k = \sum_{i = 1}^k \sigma_i \mathbf u_i \mathbf v_i^T$ - first $k$ vectors
- and $E_k = \sum_{i = k+1}^r \sigma_i \mathbf u_i \mathbf v_i^T$ - remaining $k$ vectors
- then $\|  A \|_F^2 = \| S_k \|_F^2 + \| E_k \|_F^2 $ for any $k$  |- also, $\|  S_k \|_F^2 = \sum_{i = 1}^k \sigma_i^2$ and  $\| E_k \|_F^2 = \sum_{i = k+1}^r \sigma_i^2$ |

### Rank-1 Approximation
'''Theorem'''
: The best rank-1 approximation of $A$ is $\sigma_1 \mathbf u_1 \mathbf v_1^T$

Proof
- $S_1 = \sigma_1 \mathbf u_1 \mathbf v_1^T$ and $E_1 = \sigma_2^2 + \ ... \ + \sigma_r^2$
- show that $E_1$ is the best achievable error
- let $A_1$ be any rank-1 approximation, so it's error is $\|  A - A_1 \|^2$ |- this norm is preserved under multiplication by orthogonal matrices (see [Froubenius Norm](Froubenius_Norm))
- so $\|  A - A_1 \|^2 = \| U \Sigma V^T - A_1 \|^2 = \| \Sigma V^T - U^T A_1 \|^2 = \| \Sigma - U^T A_1 V \|^2$ |- let's write $U^T A_1 V$ as $\alpha \mathbf x \mathbf y^T$ with $\alpha > 0$ and unit vectors $\mathbf x \in \mathbb R^m$ and $\mathbf y \in \mathbb R^n$ 
- so, $\|  \Sigma - U^T A_1 V \|^2_F = \| \Sigma \|^2_F - 2 \alpha \Sigma \mathbf x \mathbf y^T + \alpha^2 \| \mathbf x \mathbf y^T \|^2_F$ |- $\|  \mathbf x \mathbf y^T \|^2_F = 1$ because both $\mathbf x$ and $\mathbf y$ are unit vectors |- $\Sigma \mathbf x \mathbf y^T = \sum_{i=1}^r \sigma_i x_i y_i \leqslant \sum_{i=1}^r \sigma_i |  x_i | \, | y_i | \leqslant \sigma_1 \sum_{i=1}^r  | x_i | \, | y_i |$  |  - recall that in SVD $\sigma_1$ the biggest singular value
- let $\mathbf x^* = (| x_1|, \ ... \ , |x_r|)$ and $\mathbf y^* = (|y_1|, \ ... \ , |y_r|)$ |- so $\sum_{i=1}^r  |  x_i | \, | y_i | = \langle \mathbf x^*, \mathbf y^* \rangle$  |- by [Cauchy-Schwartz Inequality](Cauchy-Schwartz_Inequality) we have $\langle \mathbf x^*, \mathbf y^* \rangle \leqslant \|  \mathbf x^* \| \,  \| \mathbf y^* \| \leqslant \| \mathbf x \| \,  \| \mathbf y \|= 1$ |- so $\sigma_1 \langle \mathbf x^*, \mathbf y^* \rangle \leqslant \sigma_1$
- and $\Sigma \mathbf x \mathbf y^T \leqslant \sigma_1$
- $\|  \Sigma - U^T A_1 V \|^2_F = \| \Sigma \|^2_F - 2 \alpha \Sigma \mathbf x \mathbf y^T + \alpha^2 \| \mathbf x \mathbf y^T \|^2_F \geqslant \| \Sigma \|^2_F - 2 \alpha\sigma_1$ |- complete the square and get $\|  \Sigma \|^2_F - 2 \alpha\sigma_1 = \| \Sigma \|^2_F - (\alpha - \sigma_1)^2 - \sigma_1^2$ |- apparently it's maximal when $\alpha = \sigma_1$
- so $\|  \Sigma - U^T A_1 V \|^2_F \geqslant \| \Sigma \|^2_F - \sigma_1^2 = E_2$ |- the exact minimum is obtained when $\alpha = \sigma_1, \mathbf x = \mathbf e_1 \in \mathbb R^m, \mathbf y = e_1 \in \mathbb R^n$
- finally, $A_1 = \alpha (U \mathbf x) (V \mathbf y)^T = \sigma \mathbf u_1 \mathbf v_1^T$

$\square$


### Greedy Approach to Rank-$k$ Approximation
Greedy approach:
- find rank-1 $A_1$ for which $E_1 = A - A_1$ has minimal norm
- next choose rank-1 matrix $A_2$ for which $E_2 = E_1 - A_2 = E - A_1 - A_2$ has the minimal norm
  - $A_1 + A_2$ is rank-2 approximation
- at each step choose such $A_i$ that minimizes the norm of $E_i = E_{i-1} - A_i$
- after $k$ steps we have rank-$k$ approximation to $A \approx A_1 + \ ... \ + A_k$


Step 1:
- find best rank-1 approximation
- already know how to do this


Step 2:
- now $E_1 = \sum_{i=2}^r \sigma_i \mathbf u_i \mathbf v_i^T$
- and SVD of $E_1$ will give the same|    |- so the best rank-1 approximation to $E_1$ is $\sigma_2 \mathbf u_2 \mathbf v_2^T$ |

Can repeat this argument for all $E_i$


### Best Rank-$k$ Approximation
Actually, the greedy approach gives the best possible approximation

Proof: 
- Lawson, Charles L., and Richard J. Hanson. Solving least squares problems. Vol. 161. Englewood Cliffs, NJ: Prentice-hall, 1974.


## [Fourier Transformation](Fourier_Transformation) vs Reduced Rank Approximation
DFT
- it's about representing a data vector in a special orthogonal basis
- the basis is sines and cosines
- So, the Fourier Decomposition represents data as a sum of basic functions with specific amplitudes
- often there are only a few principal frequencies that account for most variability in the data
- and the rest can be discarded 

RRA with SVD
- it's the same as DFT
- but here we find the best basis ourselves with SVD
- so we can see SVD as adaptive generalization of DFT



## Sources
- Kalman, Dan. "A singularly valuable decomposition: the SVD of a matrix." (1996). [http://www.math.washington.edu/~morrow/498_13/svd.pdf]


[Category:Linear Algebra](Category_Linear_Algebra)