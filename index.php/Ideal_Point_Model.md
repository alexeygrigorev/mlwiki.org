---
title: Ideal Point Model
layout: default
permalink: /index.php/Ideal_Point_Model
---

# Ideal Point Model

## Ideal Point
In a [Multi-Objective Optimization](Multi-Objective_Optimization) Problems there are a set of the "best" (Pareto-optimal) solutions. How to decide which one to take?

The ''ideal point'' (or ''datum point'') is a solution that is not feasible, but most desired:
- we take all the extreme solutions
- and take the values of criteria at which they are best
- from these criteria we form the ideal point $i$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/moo/ideal-point.png" alt="Image">

Then we use the weighted distance to compute a point which is closest to the ideal

The distance function is:
- $\min \left[ \sum_{k=1}^m w_k (z_k(x) - i_k)^p \right]^{1/p}$
- this is called the $LP$-distance function


## Exercises
### Exercise 1
Consider the following multi-criteria problem: 
- $\max X_1 + 2 X_2$
- $\max X_1$

And the following constraints:
- $X_1 \leqslant 2$
- $X_1 + X_2 \leqslant 3$
- $- X_1 + X_2 \leqslant 1 $
- $X_1 \geqslant 0, X_2 \geqslant 0$

Compute 
- the efficient solution set 
- the datum point
- find the closest points to the datum point with $L_1$ and $L_2$ distances


First we construct the solution space:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/ideal-point-ex1-solset.png" alt="Image">
- the efficient solution set is the one that maximizes everything
- we select the following points: $A(1, 2), B(2, 1), C(2, 0)$
- values that lay on line $ABC$ form the efficient set of solutions

Now we draw the criteria space 
- we build it from all possible values of the line $ABC$
- $P(X_1, X_2) \to P(X_1, X_1 + 2 X_2)$
- $A(1, 2) \to A(1, 1 + 2 \cdot 2) = A(1, 5)$ 
- $B(2, 1) \to B(4, 2)$
- $C(2, 0) \to C(2, 2)$
- the ideal point is $D$: a virtual point that would be best for both criteria
- $D(5, 2)$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/ideal-point-ex1-datum.png" alt="Image">

Now we calculate which solutions are closest to $D$:
- for $L_1$: all values on the line $AB$
- for $L_2$: the middle between $A$ and $B$


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Multi-Objective Optimization](Category_Multi-Objective_Optimization)