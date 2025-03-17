---
title: Max Min Strategy
layout: default
permalink: /index.php/Max_Min_Strategy
---

# Max Min Strategy

## Max Min Strategy
How to choose an alternative? 
- in [Game Theory](Game_Theory)
- in [Decision Under Uncertainty](Decision_Under_Uncertainty)


Idea: Extreme Pessimism
- Base your choice on the worst situation that can happen 
- and maximize the consequences in the worst case
- $\max_{a \in A} \min_{e \in E} c(a, e)$


In other words:
- We don't know what will be the state of nature (or the strategy played by the other player)
- But since we're pessimistic, we choose the worst outcome 
- and we want to select the alternatives that are best in the worst case



### Example 1: [Decision Under Uncertainty](Decision_Under_Uncertainty)
Consider the following example:

|   $c$  |  $e_1$  |  $e_2$  |  $e_3$  |  min  |   |   $a_1$   |  40  |  70  |  -20  |  -20   |  worst case for $a_1$ ||   $a_2$   |  -10  |  40  |  100  |  -10  |  worst case for $a_2$ ||   $a_3$   |  20  |  40  |  -5  |  5  |  worst case for $a_3$ ||   |   |      |   max:   |  5  |  $\to a_3$ |

In the "min" column shows the worst cases for all alternatives
- now we select the maximal value from them 
- and base our decision on it


### Advantages and Disadvantages
Downsides
- bad use of information
  - we have a lot of information in the table, but not using only one value from each row
  - and the choice is based only on one value
- no compensation between different consequences 
  - see an example below 

No Compensation

|   $c$  |  $e_1$  |  $e_2$  |  ...  |  $e_{1000}$  |  min  |   $a$   |  -100  |  1000  |  1000  |  ...  |  1000  |  -100 ||   $b$   |  -99  |  -99  |  -99  |  ...  |  -99  |  -99 ||         |       |       |       |       |       |  '''-99'''   |
In this case we choose $b$ 
- although it's clear that $a$ is better at everything 
- it's only a little little bit worse at $e_1$


Advantages:
- no need for rich scale:
  - enough to have only an ordinal scale 
  - only need to rank the alternatives and take the worst/the best


## Max Min and Min Max
; maxmin strategy
- strategy that maximizes player's worst-case payoff
- when others want to cause the greatest harm
- i.e. it maximizes the minimal outcome
- maximin value - guaranteed minimal payoff

; minmax strategy
- of player $i$ against player $-i$
- one that minimizes the maximal value of $-i$

; minimax theorem
- in any finite 2-players zero-sum game
- each player receives a payoff that is equal to both
- his minimax and his maximin value
- 0 is a saddle point
- <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/1luv6hbhnsqr0a8bblsdadplgd.png" alt="Image">" />
- ''saddle point'' - where minimax = maximin


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- [Game Theory (coursera)](Game_Theory_(coursera))

[Category:Decision Under Uncertainty](Category_Decision_Under_Uncertainty)
[Category:Game Theory](Category_Game_Theory)