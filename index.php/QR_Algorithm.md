---
layout: default
permalink: /QR_Algorithm
tags:
- linear-algebra
- matrix-decomposition
title: QR Algorithm
---

## QR Algorithm
QR Algorithm is used to find [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors) of a matrix

The basic idea is to perform a [QR Decomposition](QR_Decomposition):
- writing the matrix as a product of an orthogonal matrix and an upper triangular matrix
- multiply the factors in the reverse order, and 
- iterate

It's based on the [Power Iteration](Power_Iteration) method (Simultaneous Iteration algorithm to find all eigenvalues), and also sometimes called "QR Iteration" method

Idea is to produce a set of similarity tranformations such that 
$Q_i^T A Q_i$ is progressively more upper diagonal 

## Naive QR Iteration Algorithm
Outline
- Let $T_0 = A$
- at each step perfomr decomposition $T_k = Q_k R_k $
- let $T_{k+1} = R_k Q_k$

Why does it produce eivenvalues?
- $T_k = Q_k R_k$
- $T_k Q_k = Q_k R_k Q_k$
- $Q_k^T T_k Q_k = R_k Q_k = T_{k+1}$
- $T_{k+1} = Q_k^T T_k Q_k $
- so $T_{k+1}$ and $T_k$ are [similar](Similar_Matrices), so they have the same eigenvalues
- The sequence $\{ T_k \}$ converges to the [Schur Form](Schur_Decomposition) of $A$: it's a the eigenvalues are on the diagonal

### Algorithm
So, the algorithm:

- let $T = A$
- for $k = 1, 2, ...$
  - decompose $Q_k R_k = T$
  - compute $T = R_k Q_k$
- return the diagonal elements of $T$

Possible stopping criteria:
- When elements on the diagonal stop changing
- When the matrix $T$ becomes truly upper-triangular (all elements below the main diagonal become zero)
- When elements right after below the main diagonal become zero

```python
 def lower_diag_norm(T):
     idx = np.tril_indices_from(T, k=-1)
     return (T[idx] ** 2).sum()

 def qr_algo_naive(A, iter_limit=1000):
     T = A
 
     for i in range(iter_limit):
         Q, R = np.linalg.qr(T)
         T = R.dot(Q)
         if lower_diag_norm(T) < 1e-3:
             break
 
     return np.diag(T)
```
Recovering the eigenvectors:
- The Schur Decomposition is $A = V T V^T$
- At each QR step we have the following:
  - $T_0 = A$
  - $Q_1 R_1 = T_0$ (do QR Decomposition)
  - $T_1 = Q_1 T_0 Q_1^T$
  - $Q_2 R_2 = T_1$ 
  - $T_2 = Q_2 T_1 Q_2^T = Q_2 Q_1 T_0 Q_1^T Q_2^T$
  - $Q_3 R_3 = T_2$ 
  - $T_3 = Q_3 T_2 Q_3^T = Q_3 Q_2 Q_1 T_0 Q_1^T Q_2^T Q_3^T$
  - and so on
- So to get eigenvectors, we need to accumulate the changes intriduced by each $Q_i$
  - let $V_0 = I$
  - then $V_{i + 1} = V_i Q_i$

```python
 def qr_algo_naive(A):
     T = A
     V = np.eye(A.shape[1])
 
     for not converged(T):
         Q, R = np.linalg.qr(T)
         T = R.dot(Q)
         V = V.dot(Q)
 
     return np.diag(T), V
```
There's a problem with this algorithm - it takes long to converge, so it is very expensive to use. 

## [Hessenberg Reduction](Hessenberg_Decomposition)
How to make QR decomposition faster? 
We can brign $A$ to upper Hessenberg Form - by using Householder reduction
Hessenberg form is almost upper-diagonal (has only entries below main diag), 

Hessenberg Decomposition:

$A = U H U^T$ where $U^T U = I$ and $H$ is Hessenberg 

Nice property: 

if $Q R = H$ is the $QR$ decomposition of $H$
then $RQ$ is also a Hessenberg matrix: QR step preserves the Hessenberg structure 
(if matrix is symmetric, then $H$ is tridiagonal, and likewise, the tridiagonal structure is also preserved)

So we can perfrom QR decomposition at each step a lot faster:
goes down from O(n^3) to O(n^2)
if we use QR based on [Givens Rotations](Givens_Transformation) - and zero only the elements below the main diagonal 
So only need $n$ Givens Rotations to do that 

```python
### Implementation

 def qr_algo_hessenberg(A):
     V, H = hessenberg_form(A)

     while not converged(H):
         Q, R = givens_hessenberg_QR(H)
         H = R.dot(Q)
         V = V.dot(Q)
 
     return np.diag(H), V

## Shifts and Deflation
```
Shifting: A + s I 
let \mu be the smallest ev of shifted A 
Then A + s I - \mu I = A - (\mu - s) I is singular
so \lambda = \mu - s is the eigenvalue of A, and it's the value closest to s

Ax = \lambda x
let's shift by m: 
(A + m I) x = Ax + mx = \lambda x + mx = (\lambda + m) x

for the shifted A, the eigenvalue is \lambda + m, and the eigenvector stays the same
So shifting allows to focus on eigenvalues closest to any particular value 

if A has eigenvalues \lambda_i, then A - k I has eigenvalues \lambda_i - k
Convergence is faster because if \lambda_i < \lambda_j it takes more iterations 

before shifting conv. rate is \cfrac{\lambda_i}{\lambda_j}, but after - \cfrac{\lambda_i - k}{\lambda_j - k}

good shifts - ones closest to $\lambda_n$ - smallest eigenvalue
since we don't know $\lambda_n$ in advance - we can use some estimate, e.g. Raylegh Quotent (?)

Note that because of the shifts, the order in which we get the eigenvalues may be different (see above)

Deflation 
$H$ is a Hessenberg Matrix 
<math>H = 
\begin{bmatrix} 
H_{11} & H_{12} \\
0 & H_{22} \\
\end{bmatrix}
</math>
Then we can decompose the problem into two parts and find eigenvalues 
of $H_{11}$ and $H_{22}$ separately

So once we have a zeros on the last row of our $H_i$, we can deflate and contunie with the upper part only 

Single-Shift Strategy

We don't know the exact value - but can use $h_{kk}$ which gives a good approximation 

so 

```python
for k = n, n-1, ...
m = H[k, k]
QR = H - mI
H = RQ + mI
```
repeat till H[k-1,k] becomes zero
store the eigenvalue
deflate: let H = H[:k, :k]

Recovering the eigenvectors with deflation

When we "deflate" - we move to the top left block 
but when we compute $Q$ we should not forget about the bottom left block!

Let $Q_i$ be the matrix we obtained on the step $i$ with $k-1$ rows already deflated

then let's complete $Q_i$ from $k \times k$ to $n \times n$ by adding the identity on the right bottom block:

Q_i^* = \begin{bmatrix} 
Q_i & 0 \\
0 & I \\
\end{bmatrix}

And $V$ stores the eigenvectors

Then 

V Q_i^* = 
\begin{bmatrix} 
V_{11} & V_{12} \\
V_{12} & V_{22} \\
\end{bmatrix}
\begin{bmatrix} 
Q_i & 0 \\
0 & I \\
\end{bmatrix}
= 
\begin{bmatrix} 
V_{11} Q_i & V_{12} \\
V_{12} Q_i & V_{22} \\
\end{bmatrix}

Which makes sense: because we already computed the vectors for last $n - k$ eigenvectors, so we only update the first $k$ columns

## Double-Shift Strategy
Maybe later

## Sources
- http://www.aip.de/groups/soe/local/numres/bookcpdf/c11-3.pdf
- https://www.math.kth.se/na/SF2524/matber15/qrmethod.pdf
- https://en.wikipedia.org/wiki/QR_algorithm
- [Matrix Computations (book)](Matrix_Computations_%28book%29)
