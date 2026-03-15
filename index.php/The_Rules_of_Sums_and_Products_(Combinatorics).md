---
layout: default
permalink: /index.php/The_Rules_of_Sums_and_Products_(Combinatorics)
tags:
- combinatorics
title: The Rules of Sums and Products (Combinatorics)
---
## The Rule of Sum
If element $a$ can be chosen in $m$ ways, and element $b$ in $n$ ways, then the choice "either $a$ or $b$" can be made in $m + n$ ways.

### Generalized Rule of Sum
If some ways of choosing element $a$ coincide with ways of choosing element $b$, then such a selection can be made in $m + n - k$ ways, where $k$ is the number of coinciding ways for $a$ and $b$.

## The Rule of Product
If element $a$ can be chosen in $m$ ways, and element $b$ in $n$ ways, then the pair $(a, b)$ can be chosen in $m \cdot n$ ways. (The pair $(a, b)$ is different from the pair $(b, a)$).


## Problems

### Problem 1
An alphabet has 33 letters. How many 5-letter words can be formed such that no two consecutive letters are the same?

- The first letter can be chosen in 33 ways
- Each subsequent letter can be chosen in only 32 ways, since no two consecutive letters can be identical.
- Answer: 33 * 32 * 32 * 32 * 32

### Problem 2
In how many ways can a white and a black rook be placed on an 8 * 8 chessboard so that they do not attack each other?

- 64 - the first rook can be placed on any square
- 49 - rook 1 attacks 14 squares and stands on one, so 64 - 15 squares remain
- Answer: 64 * 49

### Problem 3
In how many ways can 2 kings be placed on an 8 * 8 chessboard?

Consider several cases:
- If the king is in a corner, it attacks 3 squares and stands on one - 60 squares remain for the second;
- If the king is on the edge of the board but not in a corner (24 squares), it attacks 5 squares and stands on one - 58 squares remain;
- If it is not on the edge (36 squares), it attacks 8 squares and stands on one - 55 squares remain.

Answer: 4 * 60 + 24 * 58 + 36 * 55

## Sources

- Vilenkin N.Ya. Combinatorics. Moscow, Nauka, 1969.
- Genkin S.A., Itenberg I.V., Fomin D.V. Leningrad Mathematical Circles, 1994.
- Vilenkin N.Ya., Combinatorics. Article in "Kvant" journal, issue 1, 1971.  http://kvant.mccme.ru/1971/01/kombinatorika.htm
