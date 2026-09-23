---
layout: default
permalink: /index.php/Schur_Decomposition
tags:
- linear-algebra
- matrix-decomposition
title: Schur Decomposition
---

## Schur Decomposition
Schur Decomposition (or "Schur Triangulation") is a matrix decomposition technique:
- it decomposes a matrix $A = QTQ^T$ where
- $Q$ is orthogonal, i.e. $Q^T Q = I$ 
- $T$ is upper diagonal
- $T$ is called the *Schur Form* of $A$: it is upper triangular and has eivenvalues on the main diagonal 
- $Q$'s columns contain the eigenvectors of $A$ 

Schur Form $T$
- we can write it down as $T = D + N$ where
- $D$ is diagonal with eigenvalues on the diagonal and 
- $T$ is strictuly upper triangular 

[Symmetric Matrices](Symmetric_Matrices)
- if $A$ is symmetric, then $T$ is zero and there's only the $D$ component
- then we have the [Eigendecomposition](Eigendecomposition)

Computing Schur Decomposition:
- [QR Algorithm](QR_Algorithm) is an iterative algorithm that does that
