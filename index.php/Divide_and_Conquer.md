---
title: "Divide and Conquer"
layout: default
permalink: /index.php/Divide_and_Conquer
---

# Divide and Conquer

## Divide and Conquer
A computational paradigm, the main idea of which is to split a problem into subproblems until they are small enough to solve them easily

Idea:
- Divide into small subproblems
- Conquer using recursion
- Combine

## Examples
### Sorting
This paradigm is used in 2 quite popular sorting algorithms:
- [Merge Sort](Merge_Sort)
- [Quick Sort](Quick_Sort)

### Multiplication
grade-school multiplication method
- $\Theta(n^2)$

recursive way:
- $x \times y = 10^n ac + 10^{\frac{n}{2}} (ab + bc) + bd$
- $T(n)$ - max number of operations
- base case: $T(1) \leqslant c$ - constant
- general case: $T(n) \leqslant 4T(\frac{n}{2}) + O(n)$
- 4 recursive calls, $O(n)$ - addition

Gauss recursive algorithm:
- (1) $ac$, (2) $bd$, $(a+b)(c+d)$ (3)
- $ad + bc = (a+b)(c+d) - ac - bd$
- base case: $T(1) \leqslant c$
- gen case: $T(n) \leqslant 3T(\frac{n}{2}) + O(n)$
- 3 recursive calls instead of 4



## The Master Method
The way of estimating running time of D&Q algorithms

- $T(n) = aT(\frac{n}{b}) + O(n^d)$
  - $a$ - number of recursive calls ($>= 1$)
  - $b$ - shrinkage factor ($> 1$)
  - $d$ - running time done outside of recursive calls
- $T =$ 
  - $O(n^d \log n)$ if $a = b^d$ (case 1)
  - $O(n^d)$ if $a < b^d$ (case 2)
  - $O(n ^ {\log_b a})$ if $a > b^d$ (case 3)

### Examples
[Merge Sort](Merge_Sort)
- $a = 2$, $b = 2$, $d = 1$
- $b^d = 2$; case 1
- $T(n) \leqslant O(n^d \log n) = O(n \log n)$


Binary Search
- $a = 1$, $b = 2$, $d = 0$; case 1
- $ T(n) = O(log n)$


Recursive integer multiplication
- $a = 4$, $b = 2$, $d = 1$
- $b^d = 2 < a$, case 3
- $T(n) = O(n ^ {\log_b a}) = O(n^2)$
- same as a grade-school algo


Gauss recursive integer multiplication
- $a = 3$, $b = 2$, $c = 1$
- $a > b^d$; case 3
- $T(n) = O(n ^ {\log_2 3}) \approx O(n^{1.59})$
- better than $O(n^2)$

### Idea behind proof
Suppose
- $a$ - rate of subproblem proliferation ("force of Evil") - $\text{RSP}$
- $b^d$ - rate of work shrinkage ("force of Good") - $\text{RWS}$

Then if
- $\text{RSP} < \text{RWS}$
  - the amount of work decreases with the recursion level j
  - of the same magnitude
  - expect $O(n^d \log n)$
- $\text{RSP} > \text{RWS}$
  - amount of work increases at level j
  - RSP outdoes PWS, most of the work is at the root
  - expect $O(n^d)$
- $\text{RSP} = \text{RWS}$
  - amount of work is the same at every level
  - $O(\# \text{leaves})$


## See also
- [Merge Sort](Merge_Sort)
- [Quick Sort](Quick_Sort)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))

[Category:Algorithms](Category_Algorithms)