---
title: "Decision Under Uncertainty"
layout: default
permalink: /index.php/Decision_Under_Uncertainty
---

# Decision Under Uncertainty

## Decision Under Uncertainty
This is a tool to model [Decision Analysis](Decision_Analysis) problems. Unlike [Decision Under Risk](Decision_Under_Risk), here we cannot obtain the probability distribution of possible consequences, can only list the scenarios. 


; Decision Under Uncertainty
- it is impossible to determine with certainty the consequences of implementing an alternative - there are no probabilities 
- ''Nature'' decides what will happen 
  - we make a decision and then the Nature decides what is going to happen based on the decision
  - this is like a [two-player game](Game_Theory), where consequences of my actions are based on what the Nature decides to do 



### The Model
Based on that we define the following model:
- $A$ is a set of alternatives
  - $a \in A$ is a decision that you may take
- $E$ is a set of states of nature 
  - $e \in E$ is a decision that the Nature can take and influence the consequences of at least one alternative $a \in A$
- $X$ is a set of consequences
- $c: A \times E \mapsto X$
  - $c(a, e)$ is the consequence of implementing $a$ when the Nature decides to do $e$


### Decision Table
A finite case is usually modeled with a decision table:
- $A$ and $E$ are both finite
- $c(a_i, e_j$ - the consequence of implementing $a_i$ when $e_j$ happens

|   $c$  |  $e_1$  |  $e_2 $  |  $...$  |  $e_n$   |   $a_1$   |  $c(a_1, e_1)$  |  $c(a_1, e_2)$  |  $...$  |  $c(a_1, e_n)$ ||   $a_2$   |  $c(a_2, e_1)$  |  $c(a_2, e_2)$  |  $...$  |  $c(a_2, e_n)$ ||   $...$   |  $...$  |  $...$  |  ...  |  $...$ ||   $a_n$   |  $c(a_n, e_1)$  |  $c(a_n, e_2)$  |  $...$  |  $c(a_n, e_n)$ |
Filling this table in is already very difficult (the same is in [MCDA](MCDA) problems)


## [Dominance](Dominance)
Using the dominance principle we can remove a set of actions from $A$
- we can always remove the actions that are dominated 
- the definition is exactly the same as for [Normal Form Game](Normal_Form_Game)s 
- $a \ D \ b$ - $a$ dominates $b$

; $a \in A$ is ''efficient''
- if $a$ is not dominated by any other alternative

$A^*$ is a set of efficient solutions
- when $A$ and $E$ are finite, can define them $A^*$ as 
- $A^* = \{ a \in A \ |  \ \forall  b: \overline{b \ D \ a} \}$ |- i.e. $A^*$ is a set of alternatives that are not dominated by any other 
- $A^*$ is always not empty


Problems with Using the Dominance Principle 
- dominated solutions are sometimes also good


## Examples
### Example 1: The Omelet Problem
The Game:
- you want to cook an omelet and you have only 6 eggs 
- but you know that the last egg may be bad 
- so there are 2 states of nature: 
  - the egg is good ($e_g$) or 
  - the egg is bad ($e_b$)
- and we can implement the following actions: 
  - put the egg into the omelet without checking it ($a_b$)
  - throw the egg away without checking it ($a_t$)
  - check the egg: use an additional bowl for it ($a_c$)

|   $c$  |  $e_g$  |  $e_b$  |   $a_b$   |  O with 6 eggs  |  No O ||   $a_t$   |  O with 5 eggs  |  O with 5 eggs ||   $a_c$   |  O with 6 eggs <br> + a bowl to wash  |  O with 5 eggs <br> + a bowl to wash |
Notes:
- We don't know anything about the probability - just scenarios 
- no way to add additional information


### Example 2
In this case the consequences are real numbers: 
- $X \equiv \mathbb{R}$
- this is usually the case in such models

|   $c$  |  $e_1$  |  $e_2$  |  $e_3$   |   $a_1$   |  40  |  70  |  -20 ||   $a_2$   |  -10  |  40  |  100 ||   $a_3$   |  20  |  40  |  -5 |

## Methods
How to make a choice?
- [Max Min Strategy](Max_Min_Strategy) - extreme pessimism 
- [Max Max Strategy](Max_Max_Strategy) - extreme optimism
- [Hurwitz's Index](Hurwitz's_Index) - between the extreme pessimism and the extreme optimism
- [Min Max Regret Strategy](Min_Max_Regret_Strategy) - when we want to minimize the regret of a missed opportunity
- [Laplace Rule](Laplace_Rule) - the principle of insufficient reasoning


Note that these methods, like in [Voting Theory](Voting_Theory) (see [Voting Theory Examples](Voting_Theory_Examples))

|   $c$  |  $e_1$  |  $e_2$  |  $e_3$  |  $e_4$   |   $a$   |  2  |  2  |  0  |  1 ||   $b$   |  1  |  1  |  1  |  1 ||   $c$   |  0  |  4  |  0  |  0 ||   $d$   |  1  |  3  |  0  |  0 |
Note that in this case all the methods will give different results 
- MinMax - $b$
- MaxMax - $c$
- Laplace - $a$ 
- Savage - $d$


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Decision Under Uncertainty](Category_Decision_Under_Uncertainty)