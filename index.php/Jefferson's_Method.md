---
layout: default
permalink: /index.php/Jefferson's_Method
tags:
- voting-theory
title: Jefferson's Method
---
## Jefferson's Method
This is a [Parliamentary Allocation](Parliamentary_Allocation) method.

The task is:
- given 
  - $p_i$ - the number of voters in favor of party $i$ 
  - $N$ - total number of parties, $i \in \{ 1, 2, ..., N\} \equiv P$
  - $n$ - total number of voters
  - the quota of $i$ is $q_i = S \cdot \cfrac{p_i}{n}$. Note that $q_i$ is a read number, not integer
- allocate $S$ seats in parliament
  - $(s_1, ..., s_N)$ s.t. $\sum s_i = S$
  - $s_i$ must be an integer

The main idea of this method is to satisfy the following constraint:
- $s_i \ne 0, \cfrac{p_i}{s_i} \geqslant \cfrac{p_j}{s_j + 1}$


If this constraint is not respected, we have:
- $\cfrac{p_i}{s_i} < \cfrac{p_j}{s_j + 1}$
- but party $P_j$ won't be happy about it: they may need more people to allocate one seat than $P_i$


So we give a place to a party $i$ with maximal $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$ score


Meaning:
- suppose $S=10, p_1 = 6373, q_1 = 6.4$
- allocate $s_1 = 6$ seats to $P_1$ 
- $\cfrac{p_1}{s_1 + 1}$ means "to get one additional seat they need 910 people in the worst case"


### Example 1
$S = 10$

|         |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$  |  $P_1$  |  6373  |  6.373  |  6  |  6  |  <u>910.42</u>  ||  $P_2$  |  2505  |  2.505  |  2  |  2  |  835 ||  $P_3$  |  602  |  0.602   |  0  |  0  |  602 ||  $P_4$  |  520  |  0.520   |  0  |  0  |  502  ||         |       |          |  8   |  8 |      |
$P_1$ has the highest $\cfrac{p_1}{\lfloor s_1 \rfloor + 1}$ score
- so allocating additional seat to them
- note that we need to re-calculate the value $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$ for $P_1$ after we allocate the seat to them


|         |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i $ |  $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$  |  $P_1$  |  6373  |  6.373  |  6  |  <font color="red">7</font>  |  796 ||  $P_2$  |  2505  |  2.505  |  2  |  2  |  <u>835</u> ||  $P_3$  |  602  |  0.602   |  0  |  0  |  602 ||  $P_4$  |  520  |  0.520   |  0  |  0  |  502  ||         |       |          |  8   |  9  |      |
$P_2$ has the highest score now
- so allocating the 10th seat to them


### Example 2
$S = 10$

|         |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$  |  $P_1$  |  6373  |  6.4  |  6  |  6  |  <u>910.42</u> ||  $P_2$  |  2505  |  2.505  |  2  |  2  |  768.33 ||  $P_3$  |  702  |  0.602   |  0  |  0  |  702 ||  $P_4$  |  620  |  0.520   |  0  |  0  |  620  ||         |       |          |  8   |  8  |      |
Give the seat to $P_1$, recalculate the score:

|         |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $\cfrac{p_i}{\lfloor s_i \rfloor + 1}$  |  $P_1$  |  6373  |  6.4  |  6  |  7  |  <u>796.6</u> ||  $P_2$  |  2505  |  2.505  |  2  |  2  |  768.33 ||  $P_3$  |  702  |  0.602   |  0  |  0  |  702 ||  $P_4$  |  620  |  0.520   |  0  |  0  |  620  ||         |       |          |  8   |  9  |      |
Again allocate the seat to $P_1$

|         |  $p_i$  |  $q_i$  |  $\lfloor q_i \rfloor$  |  $s_i$  |  $P_1$  |  6373  |  6.4  |  6  |  7 ||  $P_2$  |  2505  |  2.505  |  2  |  2 ||  $P_3$  |  702  |  0.602   |  0  |  0 ||  $P_4$  |  620  |  0.520   |  0  |  0 ||         |       |          |  8   |  10 |
This shows that the method is still not perfect.



## Properties
### Consistency
Show that 
- $\forall i, j \in P: p_i < p_j \Rightarrow s_i \leqslant s_j$

Solution
- Jefferson Rule is: $\cfrac{p_i}{s_i} \geqslant \cfrac{p_j}{s_j + 1}$
- or $\cfrac{p_i}{p_j} \geqslant \cfrac{s_i}{s_j + 1}$
- $\cfrac{p_i}{p_j} < 1$ always (by the hypothesis $p_i < p_j$)
- thus, $\cfrac{s_i}{s_j + 1} < 1$ or $s_i < s_j + 1$


### [Monotonicity](Monotonicity)
Also respected



## Links
- http://www.math.colostate.edu/~spriggs/m130/apportionment2.pdf

## See also
- [Hamilton's Method](Hamilton's_Method)

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
