---
layout: default
permalink: /index.php/Combinations
tags:
- combinatorics
title: Combinations
---
## Combinations
We are not always interested in the order in which elements are arranged - sometimes only the composition matters.

Combinations of size $k$ from $n$ elements are all possible selections of length $k$ composed from these elements that differ only in composition, not in the order of elements.

$C_n^k$ is the number of combinations of size $k$ that can be formed from $n$ elements.

First, we form all combinations of size $k$ from $n$ elements, and then permute the elements in each of them in all possible ways - this gives us all possible partial permutations of size $k$ from $n$ elements. From each combination, $k!$ [permutations](Permutations) can be made, hence
$k!\cdot C_n^k = A_n^k, C_n^k = \frac{A_n^k}{k!} = \frac{n!}{(n - k)! \cdot k!}$
This function coincides with the formula for the number of permutations of $k$ elements of one type and $(n-k)$ elements of a second type

$P(n, n-k) = \frac{n!}{k! \cdot (n - k)!} = C_n^k$
Let us arrange all $n$ elements in order and encode each combination as a sequence of length $n$ consisting of zeros and ones. If an element is included, we write 1; otherwise, 0.
Each combination then corresponds to a sequence of $k$ ones and $(n - k)$ zeros.

### Problem
In how many ways can 8 rooks be placed on an 8 $\times$ 8 board? (So that they may or may not attack each other.)

- We need to choose any 8 out of 64 squares.
- Therefore, $C_{64}^8 = \frac{64!}{8! \cdot 56!}$

## Combinations with Repetition
There are $n$ different types of objects. How many combinations of size $k$ can be made from them, if the order of elements in the combinations is disregarded?

### Motivating Example
A pastry shop sells 4 types of pastries: napoleon, eclairs, shortbread, and puff pastry. In how many ways can 7 pastries be purchased?

#### Method 1
- Let us encode each purchase using ones and zeros.
- First, write the number of napoleons purchased, then a zero, then the number of eclairs, a zero, shortbread, a zero, and finally puff pastries.
- We get $\underbrace{111} 0 \underbrace{1} 0 \underbrace{11} 0 \underbrace{1}$
- Different purchases correspond to distinct permutations with repetition

$P(7, 3) = \frac{10!}{7! \cdot 3!} = 120$
#### Method 2
- Arrange the pastries in each purchase in order (napoleons, eclairs, shortbread, puff pastries)
- Then number them, adding 0 to the numbers of napoleons, 1 to eclairs, 2 to shortbread, and 3 to puff pastries.
- The largest number is 7 + 3 = 10 for a puff pastry
- The smallest number is 1 + 0 = 1 for a napoleon
- No number will repeat, and each increasing sequence of 7 numbers corresponds to some purchase

For example, given the sequence (2, 3, 4, 5, 7, 8, 9). Subtract (1, 2, 3, 4, 5, 6, 7) and obtain (1, 1, 1, 1, 2, 2, 2).
That is, we have 4 eclairs (we added 1 to eclairs) and 3 shortbread (we added 2 to their numbers).

- Thus, the number of ways to buy 7 pastries equals the number of ways to choose 7 items from 10:
- Answer: $C_{10}^7 = 120$



In the general case, problems on combinations with repetition are solved in the same way.

Let us encode each combination with zeros and ones:
- for each type, write in ones how many items are included in the combination
- and separate the types with zeros


The result will have as many ones as items we need to choose, i.e. $k$, and $(n - 1)$ zeros
- $\bar{C_n^k} = P(k, n - 1) = \frac{(k + n - 1)!}{k! \cdot (n - 1)!}$
- Therefore, $\bar{C}_n^k} = C_{n + k - 1}^k$.

One can arrive at this formula using the second method as well.


### Variation
There are problems where elements of $r$ fixed types must be included, $r \leqslant n$

To solve this:
- take $r$ elements of the required types
- fill the remaining $k - r$ positions with elements belonging to all $n$ types.

The resulting formula is $\bar{C}_n^{k - r}} = C_{n + k - r - 1}^{k - r}$


## Properties of Combinations
### Property 1
$C_n^k = C_n^{n - k}$
- Obvious from the formula $C_n^k = \frac{n!}{(n - k)! \cdot k!}$
- If we replace $k$ with $(n - k)$ in the formula, then $n - k$ is replaced by $n - (n - k) = k$ - and the factors simply swap places
### Property 2
$C_n^k = C_{n - 1}^{k - 1} + C^k_{n - 1}$

- Let us form all combinations of size $k$ from $n$ elements $a_1, a_2, ..., a_n$ and split them into two groups:
  - the first group contains elements that include $a_n$
  - the second group does not contain elements that include $a_n$
- If we remove $a_n$ from the first group (since it appears everywhere, this does not affect the number of combinations), we get combinations of size $k - 1$ composed from elements $a_1, a_2, ..., a_{n - 1}$ (a total of $n - 1$ elements).
  - The number of combinations in the first group equals $C_{n - 1}^{k - 1}$
- The combinations in the second group are combinations of size $k$ composed from $n - 1$ elements $a_1, a_2, ..., a_{n - 1}$
  - The number of combinations in the second group equals $C_{n - 1}^k$
- By the [rule of sum](The_Rules_of_Sums_and_Products_(Combinatorics)), the total number of combinations is $C_{n - 1}^k + C_{n - 1}^{k - 1} = C_n^k$

### Property 3
$\sum_{k = 0}^n C_n^k = 2^n$

- $2^n$ is the number of all [partial permutations with repetition](Partial_Permutations) from elements of *two types*.
- Let us split these arrangements into $k$ groups
- In the $k$-th group, place those elements that contain $k$ elements of the first type and ($n - k$) elements of the second type
- The arrangements in the $k$-th group are all possible [permutations](Permutations) of $k$ elements of the first type and $n - k$ of the second
- The number of such permutations equals $P(k, n - k)$, and $P(k, n - k) = C_n^k$

In general form, this formula can be written as:

$\sum_{n_1 + ... + n_k = n} P(n_1, ..., n_k) = k^n$



(Properties 4 and 5 are omitted - see Vilenkin)

### Property 6
$C_n^0 - C_n^1 + ... + (-1)^n C_n^k = 0$

- $C_n^0 = C_{n - 1}^0 = 1$
- Since $C_n^1 = C_{n - 1}^0 + C_{n - 1}^1$, we have $C_{n - 1}^0 - C_n^{1} = -C_{n - 1}^2$
- Next, we have $-C_{n - 1}^2 + C_n^2 = C_{n - 1}^2$
- Eventually all terms cancel out


Some properties (especially 3 and 6) are very easily proved using the [Binomial Theorem](Binomial_Theorem)


## Pascal's Triangle
Binomial coefficients can be computed using Property 2: $C_n^k = C_{n - 1}^{k - 1} + C^k_{n - 1}$.
If we place $C_n^k$ in the middle below $C_{n - 1}^{k - 1}$ and $C^k_{n - 1}$, the numbers form a triangle

<img src="http://allmatematika.ru/images/kombib8.GIF" />


### Problem
<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/pascal-triangle-problem.png" alt="Image" />

In how many ways can one get from vertex $A$ to vertex $B$, if movement is allowed only "right" and "up"?

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/pascal-triangle-problem-solution.png" alt="Image" />

- If we write the number of ways to reach a particular node, we see Pascal's Triangle.
- Indeed, the $k$-th node in the $n$-th row can be reached either from the $(k-1)$-th or from the $k$-th node
- Therefore, the number of paths leading to this node is $C_n^k = C_{n - 1}^{k - 1} + C^k_{n - 1}$

Thus, we can formulate one of the properties of Pascal's Triangle:
Each number in the triangle equals the number of ways to reach it from the top, moving either down-right or down-left.


## See also
- [Permutations](Permutations)
- [Binomial Theorem](Binomial_Theorem)

## Sources
- Vilenkin N.Ya. Combinatorics. Moscow, Nauka, 1969.
- Genkin S.A., Itenberg I.V., Fomin D.V. Leningrad Mathematical Circles, 1994.
