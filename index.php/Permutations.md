---
layout: default
permalink: /index.php/Permutations
tags:
- combinatorics
title: Permutations
---
## Permutations
If we take [partial permutations](Partial_Permutations) that include all $n$ elements, then they can only differ in order.

*Permutations of $n$ elements* are partial permutations without repetition of $n$ elements that include all elements.

They are denoted $P_n = A_n^n = n \cdot (n - 1) \cdot ... \cdot 2 \cdot 1 = n!$
### Problems
In how many ways can 8 rooks be placed on a chessboard so that none of them attacks another?

In such an arrangement, each row and each column contains exactly one rook.
- $a_1$ - the square number on the first row
- $a_2$ - the square number on the second row
- ...
- $a_8$ - the square number on the eighth row

- $(a_1, ..., a_8)$ is a permutation of $(1, ..., 8)$
- $P_8 = 8!= 40320$

## Permutations with Repetitions
In permutations above we rearranged elements that are all distinct. If some of the elements are identical, then we get fewer permutations -- some permutations coincide with each other.

Suppose we have $n$ elements of $k$ distinct types. How many permutations can be made from $n_1$ elements of the first type, $n_2$ elements of the second type, ..., $n_k$ elements of the $k$-th type?

The number of elements in each permutation is $n = n_1 + n_2 + ... + n_k$.
If all elements were distinct, we would have $n!$ permutations.
But because some elements are identical, we get fewer permutations.


Consider the permutation

$\underbrace{aa \ .. \ a}_{n_1} \ \underbrace{bb \ .. \ b}_{n_2} \ ... \ \underbrace{xx \ .. \ x}_{n_k}$

- Elements of the first type can be rearranged among themselves in $n_1!$ ways, but since these elements are identical, the permutation does not change.
- Permutations of the first, second, ..., $k$-th types can be performed independently of each other. Therefore, by the multiplication rule, the elements of this permutation can be rearranged among themselves in $n_1!\cdot n_2! \cdot ... \cdot n_k!$ ways without changing the permutation.
- Therefore, $P(n_1, n_2, ..., n_k) = \frac{n!}{n_1! n_2! ... n_k!}$
### Problem

How many permutations can be made from the letters of the word "Mississippi"?

$P(4, 4, 2, 1) = \frac{11!}{4! \cdot 4! \cdot 2! \cdot 1!} = 34650$
## Sources
- Vilenkin N.Ya. Combinatorics. Moscow, Nauka, 1969.
