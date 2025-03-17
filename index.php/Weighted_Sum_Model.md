---
title: Weighted Sum Model
layout: default
permalink: /index.php/Weighted_Sum_Model
---

# Weighted Sum Model

## Weighted Sum Model
In a [MOO](Multi-Objective_Optimization) and [MCDA](MCDA) Problems  there are a set of the "best" (Pareto-optimal) solutions. How to decide which one to take?

One possible approach is Weighted Sum

Suppose we have the following table:
- $f_1, ..., f_q$ are criteria
- $a_1, ..., a_n$ are alternatives
- each criteria is assigned some weight $w_i$

|    |  $f_1$  |  $f_2$  |  ...  |  $f_q$  |   $a_1$    |  $f_1(a_1)$  |  $f_2(a_1)$  |  ...  |  $f_q(a_1)$ ||   $a_2$    |  $f_1(a_2)$  |  $f_2(a_2)$  |  ...  |  $f_q(a_2)$ ||   ...    |  ...  |  ...  |  ...  |  ... ||   $a_n$    |  $f_1(a_n)$  |  $f_2(a_n)$  |  ...  |  $f_q(a_1)$ ||    |  $w_1$  |  $w_2$  |  ...  |  $w_q$ | |
We rank alternatives based on the following score:
- $V(a) = \sum_{i = 1}^{q} w_i f_i (a)$
- $a_i \ P \ a_j \iff V(a_i) > V(a_j)$
- $a_i$ is preferred to $a_j$ if $V(a_i) > V(a_j)$


## Downsides
This approach is very simple, but introduces some effects on the decision

### Bad Use Of Information
We consider only one aggregated value, and don't see all the data
- cannot identify weak and strong points

Example: 

|    |  $f_1$  |  $f_2$  |  $f_3$  |  $f_4$  |   $a$  |  5  |  5  |  5  |  2 ||   $b$  |  4  |  4  |  4  |  4 ||   $w$  |  0.25  |  0.25  |  0.25  |  0.25  | |- $V(a) = 4.25, V(b) = 4$
- $b$ is never the best one
- $a$ is the best almost at all criteria, except for $f_4$ (say he's in IT and this is a communication skill)
- cannot identify that by only looking at the $V(a)$ and $V(b)$ scores


### Conflicts
|    |  $f_1$  |  $f_2$  |   $a$  |  5  |  5 ||   $b$   |  10  |  0 ||   $c$   |  0  |  10 ||   $d$  |  5  |  5 ||    |  0.5  |  0.5 | |$V(a) = V(b) = V(c) = V(d) = 0.5$
- but inside they are very different|   | |
### Scale is Important
- suppose that we say that production $p$ is more important then quality $q$
- i.e. $w_p = 2/3, w_q = 1/3$
- $p$ - production per month

|    |  $p$  |  $q$  |  Score  |   $a$  |  100  |  100  |  100 ||   $b$   |  120  |  80  |  106.6 ||   $w$  |  2/3  |  1/3  |   |
In this case $b$ is better 


But suppose now we want to use $p$ - production per week
|    |  $p$  |  $q$  |  Score  |   $a$  |  25  |  100  |  50 ||   $b$   |  30  |  80  |  46 ||   $w$  |  2/3  |  1/3  |   |
Now all of a sudden $a$ becomes better 
- because the scale changed
- need normalization 


### Not All Solutions
With weighted sum not all the solutions can be found
- With weighted sum approach we cannot find all the efficient solutions just by maximizing the sum

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/weighted-sum-non-convex.png" alt="Image">
- (a) this solution can be found: this frontier is convex
- (b) cannot be found: only the convex part is discovered


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Multi-Objective Optimization](Category_Multi-Objective_Optimization)
[Category:Multi-Criteria Decision Aid](Category_Multi-Criteria_Decision_Aid)