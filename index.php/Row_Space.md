---
title: Row Space
layout: default
permalink: /index.php/Row_Space
---

# Row Space

## Row Space
This is one of the [Four Fundamental Subspaces](Four_Fundamental_Subspaces)

A ''Row Space'' $C(A^T)$ of a matrix $A$ is all linear combinations of rows of $A$, or all combinations of columns of $A^T$


Row Space
- $\text{dim } C(A^T) = r = \text{dim } C(A)$, there are $r$ pivot rows - the same dim as for Column Space
- basis: maximal system of linearly independent vectors from $A^T$ 
- when we get [Row Reduced Echelon Form](Row_Reduced_Echelon_Form) $R$ by applying [Gaussian Elimination](Gaussian_Elimination) to $A$, the column space changes, so $C(A) \ne C(R)$
- but because we did row operations the row space should remain the same: it changed only the column space
- so $C(A^T) = C(R^T)$
- alternatively, we can take first $r$ rows of $R$ for the basis 


Why the row space remains the same? 
- all the operations were performed on rows - and we  allowed to do only linear combinations 
- so each linear operation gives us rows from the same space 
- we may change the basis, but the space remains the same 
- and cleanest form of the row space is the rows from $R$ 


## See Also
- [Four Fundamental Subspaces](Four_Fundamental_Subspaces)


## Sources
- [Linear Algebra MIT 18.06 (OCW)](Linear_Algebra_MIT_18.06_(OCW))

[Category:Linear Algebra](Category_Linear_Algebra)