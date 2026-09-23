---
layout: default
permalink: /QR_Algorithm_Improvements
tags:
- linear-algebra
- matrix-decomposition
title: QR Algorithm Improvements
---

## QR Algorithm Improvements

Working smarter helps, though.
you know that the dominant eigenvector is orthogonal to the others, so you could use the power method (or the inverse power method) twice, forcing the two vectors to be orthogonal at each step of the way. This will guarantee they do not converge to the same vector. If this
approach converges to anything, it probably converges to the dominant and “next-dominant” eigenvectors and their associated eigenvalues.

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

http://www.aip.de/groups/soe/local/numres/bookcpdf/c11-3.pdf
