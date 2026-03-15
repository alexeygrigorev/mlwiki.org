---
layout: default
permalink: /index.php/Greatest_Common_Divisor
tags:
- algorithms
- discrete-mathematics
title: Greatest Common Divisor
---
## Greatest Common Divisor

A ''common divisor'' of numbers $a_1, a_2, ..., a_n$ is a number that divides all numbers $a_1, a_2, ..., a_n$ without remainder.

### Algorithm

1. Represent each number as a product of its prime factors and write them as powers
1. List the divisors common to all numbers
1. Choose the smallest power of each
1. Compute the result

### Example

$168 = 2^3 \cdot 3^1 \cdot 7^1$

$180 = 2^2 \cdot 3^7 \cdot 5^1$

$3014 = 2^4 \cdot 3^3 \cdot 7^1$

$GCD(168, 180, 3014) = 2^3 \cdot 3^1 = 12$

## Euclidean Algorithm

Given: numbers $m$ and $n$. Find: the greatest common divisor of these numbers.

### Algorithm

1. Divide $m$ by $n$, $r$ is the remainder
1. If $r = 0$, then $n$ is the desired value
1. If $r \neq 0$, then set $m = n$, $n = r$ and repeat until $r$ becomes zero

### Proof

'''First''', the algorithm always converges.
'''Second''', at each iteration we have:

1. $m = n \cdot q_1 + r_1$

2. $n = r_1 \cdot q_2 + r_2$

3. $r_1 = r_2 \cdot q_3 + r_3$

...

k+1. $r_{k-1} = r_k \cdot q_{k+1} + r_{k+1}$

k+2. $r_k = r_{k+1} \cdot q_{k+2} + 0$


'''At the first step''':

Suppose that $c = GCD(m, n)$.

Then
$m = c \cdot d_m$,
$n = c \cdot d_n$,
where $d_m$ and $d_n$ are some integers.

Therefore, $r_1 = m - n q_1 = c \cdot (d_m - d_n \cdot q_1$)

That is, $r_1$ is also divisible by $c$.


'''At the $i$-th step''': similarly, $r_i$ is divisible by $c$.


'''Last step''':
Since the remainder at this step is 0, we have $r_k = c = GCD(m, n)$

'''Q.E.D.'''

## Greatest Common Divisor by Subtraction

### Algorithm

1. Subtract the smaller number from the larger one
1. If the result is 0, then the numbers are equal - return one of them


Subtracting $q$ times is the same as taking the remainder of division by $q$.


## Extended Euclidean Algorithm (Bezout's Identity)

Given: numbers $m$ and $n$

Find: the GCD of $m$ and $n$, $d = GCD(m, n)$, and two numbers $a$ and $b$ such that $am + bn = d$

### Algorithm

1. Initialization:
1. : $a' = 1$, $b = 1$
1. : $a = 0$, $b' = 0$
1. : $c = m$, $d = n$
1. $c = qd + r$
1. : $q$ is the quotient, $r$ is the remainder of dividing $c$ by $d$.
1. $r = 0$? we have $am + bn = d$
1. $r \neq 0$?
1. : repeat the iteration
1. : $c = d$, $d = r$
1. : $t = a$', $a' = a$, $a = t - qa$
1. : $t = b$', $b' = b$, $b = t - qb$


Proof: see Knuth, vol. 1, p. 33

## Sources
- D. Knuth "The Art of Computer Programming", vol. 1
