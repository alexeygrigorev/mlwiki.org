---
layout: default
permalink: /index.php/Min_Max_Regret_Strategy
tags:
- decision-under-uncertainty
- game-theory
title: Min Max Regret Strategy
---
## Min Max Regret Strategy
How to choose an alternative? 
- in [Game Theory](Game_Theory)
- in [Decision Under Uncertainty](Decision_Under_Uncertainty)

This principle is also called the Savage's Opportunity Loss principle. 


Idea:
- instead of calculating the maximal gain (like in [Max Max Strategy](Max_Max_Strategy)) or maximal loss ([Max Min Strategy](Max_Min_Strategy)) we calculate the regret
- use this measure to decide which option to choose
- we don't want to experience a lot of regret, so we will minimize the maximal regret we have 
- so it's similar to  [Max Min Strategy](Max_Min_Strategy), but instead of utility we use regret


Regret
  - ''regret'' is a measure that shows how we regret choosing some alternative $a$ to another alternative $a^*$ after $e \in E$ happens
- imagine that $e$ happens and the best alternative in this case is $a^*$
- but we chose $a$
- so our regret is $c(e, a^*) - c(e, a)$
- it we chose $a^*$ then our regret is 0


So define regret as 
: $R(a, c) = max_{b \in A} \big[ c(b, e) - c(a, e) \big]$


We choose such $a \in A$ that:
- $\min_{a \in A} \max_{e \in E} R(a, e)$


Remarks
- it must be meaningful to make differences for calculating regret
- so the scale should be numerical, not ordinal 


### Example
Suppose we have the following matrix:

|   $c$  |  $e_1$  |  $e_2$  |  $e_3$  |   $a_1$   |  40  |  70  |  -20 ||   $a_2$   |  -10  |  40  |  100 ||   $a_3$   |  20  |  40  |  -5 |

- if $e_1$ happens, the regret of choosing $a_1$ is 0 
  - $a_1$ is the best for $e_1$
- if $e_1$ happens, the regret of choosing $a_2$ is 50
  - 40-(-10) = 50 
  - the best value for $e_1$ is the value for $a_1$, which is 40

So this way we compute a regret matrix:

|   $R$  |  $e_1$  |  $e_2$  |  $e_3$  |  max   |   $a_1$   |  0  |  0  |  120  |  120 ||   $a_2$   |  50  |  30  |  0  |  <font color="blue">50</font> ||   $a_3$   |  20  |  30  |  105  |  105 |

In this case the alternative $a_2$ minimizes the maximal possible regret, so we choose it 


## Manipulation
This method does not satisfy the principle of [Independence to Third Alternatives](Independence_to_Third_Alternatives) from the [Voting Theory](Voting_Theory)
- adding or removing alternatives may alter the choice in unpredicted ways

Example 

|  |     |   $c$  |  $e_1$  |  $e_2$ |      |  $a_1$ |   | 8  |  0 |      |   $a_2$ |   | 2  |  4 |  |  |     |   $R$  |  $e_1$  |  $e_2$  |  max |      |  $a_1$ |   | 0  |  4  |  <font color="blue">4</font> |      |   $a_2$ |   | 6  |  0  |  6 |  
Now $a_1$ wins - so we choose it


But what if we add a third alternative?

|  |     |   $c$  |  $e_1$  |  $e_2$ |      |  $a_1$ |   | 8  |  0 |      |   $a_2$ |   | 2  |  4 |      |   $a_3$ |   | 1  |  7 |  |  |     |   $R$  |  $e_1$  |  $e_2$  |  max |      |  $a_1$ |   | 0  |  7  |  7 |      |   $a_2$ |   | 6  |  3  |  <font color="blue">6</font> |      |   $a_3$ |   | 7  |  0  |  7 |  
But now $a_2$ wins|   | |
## [Expected Opportunity Lost](Expected_Opportunity_Lost)
Similar idea:
- we calculate the expected value on the regret table


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
