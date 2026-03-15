---
layout: default
permalink: /index.php/Partial_Permutations
tags:
- combinatorics
title: Partial Permutations
---
## Partial Permutations
Given $n$ distinct objects, how many arrangements of length $k$ can be formed? Two arrangements are considered different if they differ in at least one element, or consist of the same elements but in a different order.

Such arrangements are called *partial permutations (without repetition)* and are denoted $A_n^k$.


To construct one, we need to make $k$ choices:

- at the first step we choose from $n$ objects
- at the second step -- from $n - 1$ objects (repetition is not allowed)
- at the $k$-th step -- from $n - k + 1$ objects

Thus, $A_n^k = n \cdot (n - 1) \cdot ... \cdot (n - k + 1) = \frac{n!}{(n - k)!}$
### Problem
A scientific society consists of 25 members. A president, vice-president, scientific secretary, and treasurer must be elected. In how many ways can this be done?

$A_{25}^4 = 25 \cdot 24 \cdot 23 \cdot 22 = 303 \ 600$

## Partial Permutations with Repetitions

**TODO**


## See also
- [Permutations](Permutations)

## Sources
- Vilenkin N.Ya. Combinatorics. Moscow, Nauka, 1969.
