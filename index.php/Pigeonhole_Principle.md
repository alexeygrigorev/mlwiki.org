---
layout: default
permalink: /index.php/Pigeonhole_Principle
tags:
- combinatorics
title: Pigeonhole Principle
---
## Pigeonhole Principle

If there are at least $N + 1$ pigeons sitting in $N$ pigeonholes, then at least one pigeonhole contains at least 2 pigeons.

This statement is known as the ''Dirichlet principle''. It is proved by contradiction: if each pigeonhole contained at most one pigeon, then $N$ pigeonholes would contain at most $N$ pigeons -- a contradiction.

A more general formulation of the principle:

If $k$ objects are placed into $n$ boxes and $k > n$, then there exists at least one box containing at least 2 objects.

## Generalized Pigeonhole Principle
If $pn + 1$ objects are placed into $n$ boxes, then at least one box will contain $p + 1$ objects.

## Problems

### Problem 1
There are 1 million fir trees in a forest and it is known that each of them has at most 600 thousand needles. Prove that there exist at least two trees with the same number of needles.

- 1,000,000 trees (objects)
- 600,001 boxes - each tree has $0 \leqslant k \leqslant 600,000$ needles
- Since there are more objects than boxes, at least one box contains more than one object.

### Problem 2
Prove that among 6 integers there exist two numbers whose difference is divisible by 5.

- 5 boxes: { 0, 1, 2, 3, 4, 5 } - remainders when dividing by 5,
- If we distribute the numbers into boxes, then one box will contain two numbers,
- Therefore, there exist at least two numbers with the same remainder when dividing by 5,
- Then the difference of these numbers is divisible by 5.

### Problem 3
Prove that for any $n \in \mathbb{N}$, $n \geqslant 1$ there exists $k \in \mathbb{N}$, consisting only of the digits 0 and 5, such that it is divisible by $n$.

- $a_1 = 50, a_2 = 5050, a_n = \underbrace{5050..50}$ ($n$ times)
- Distribute these objects into boxes $s_i \in \{0, 1, ..., n-1\}$
- Place number $a_k$ into box $s_i$ if it has remainder $i$ when divided by $n$
- If box $s_0$ contains 1 object, then the problem is solved.
- Otherwise, $n$ objects are in $n - 1$ boxes, therefore there exist two numbers with the same remainder when divided by $n$
- Since the difference of two numbers consisting of 5 and 0 also consists of 5 and 0, the difference of these two numbers is the answer.

### Problem 4
There are 40 people in a building. Does there exist a month in which at least 4 of them celebrate their birthdays?

- Boxes - months (12)
- Objects - people (40 = 12 * 3 + 4)
- There exists a box with at least 3 + 1 objects

## Sources
- Genkin S.A., Itenberg I.V., Fomin D.V. Leningrad Mathematical Circles, 1994.
- Pigeonhole Principle, http://bars-minsk.narod.ru/teachers/dirichle.html
