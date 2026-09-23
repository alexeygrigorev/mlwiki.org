---
layout: default
permalink: /Binomial_Theorem
tags:
- combinatorics
- shad
title: Binomial Theorem
---
## Binomial Theorem

Consider the power $(a + x)^n$
- $(a + x)^2 = a^2 + 2xa + x^2 = aa + ax + xa + xx$
- $(a + x)^3 = aaa + aax + axa + axx + xaa + xax + xxa + xxx$

These formulas contain all [permutations with repetitions](Permutations) of the symbols $x$ and $a$
- $(a + x)^n$ is the same thing: it contains all possible permutations of $a$ and $x$ of length $n$


Let us find how many terms there are that contain $k$ symbols $x$ and $n - k$ symbols $a$
- $P(k, n - k) = C_n^k = \frac{n!}{k! \cdot (n - k)!}$ (the number of permutations with repetitions for two groups equals the number of [combinations](Combinations) of size $k$ out of $n$)
- i.e. we take the term $x^k \cdot a^{n - k}$ with the coefficient $C_n^k$ and get
- $(a + x)^n = C_n^0 a^n + C_n^1 a^{n-1} x + ... + C_n^k a^{n-k} x^k + ... + C_n^n x^n$

This formula is known as the *Binomial Theorem*


### General case
For $(x_1 + ... + x_m)^n$ the coefficient of $x_1^{k_1} \cdot x_2^{k_2} \cdot ... \cdot x_m^{k_m}$ is $P(k_1, k_2, ..., k_m)$.


## Proof of the [Properties of Combinations](Combinations#properties-of-combinations)
Call a function of the form $(1 + x)^n$ a *generating function*

$(1 + x)^n = C_n^0 + C_n^1 x + ... + C_n^k x^k + ... + C_n^n x^n$.

With this formula it is easy to prove the properties of combinations, in particular property 3 and property 6

Property 3: $\sum_{k = 0}^n C_n^k = 2^n$
- Let $x$ in the generating function be 1. Then
- $2^n = C_n^0 + C_n^1 + ... + C_n^k + ... + C_n^n$.


Property 6: $C_n^0 - C_n^1 + ... + (-1)^n C_n^k = 0$
- Let $x = -1$. Then
- $0 = C_n^0 - C_n^1 + ... + (-1)^n C_n^k$.


## See also
- [Combinations](Combinations)

## Sources
- Vilenkin N.Ya., Combinatorics. Moscow: Nauka, 1969. (in Russian)
