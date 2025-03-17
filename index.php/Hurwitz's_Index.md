---
title: "Hurwitz's Index"
layout: default
permalink: /index.php/Hurwitz's_Index
---

# Hurwitz's Index

## Hurwitz's Index
How to choose an alternative? 
- in [Game Theory](Game_Theory)
- in [Decision Under Uncertainty](Decision_Under_Uncertainty)


Idea: in-between the extreme pessimism and extreme optimism
- this is a "compromise" between [Max Min Strategy](Max_Min_Strategy) and [Max Max Strategy](Max_Max_Strategy)


Coefficient of Pessimism:
- define $\alpha \in [0, 1]$ as the coefficient of pessimism
- then choose the solution $a \in A$ that is the closest to 
- $\max_{a \in A} \big[ \alpha \cdot \min_{e \in E} c(a, e) + (1 - \alpha) \cdot \max_{e \in E} c (a, e)  \big]$  


### Example:
$\alpha = 0.5$

|   $c$  |  $e_1$  |  $e_2$  |  $e_3$  |  $\alpha =0.5$  |   |   $a_1$   |  40  |  70  |  -20  |  (-20 + 70) / 2  |  25 ||   $a_2$   |  -10  |  40  |  100  |  (-10 + 100) / 2  |  45 ||   $a_3$   |  20  |  40  |  -5  |  (-5 + 40) / 2  |  17.5 ||   |   |      |   max:   |  45  |  $\to a_2$ |

## Downsides
- bad use of information
  - we combine two approaches ([Max Min Strategy](Max_Min_Strategy) and [Max Max Strategy](Max_Max_Strategy)) that both suffer from bad use of information
- now the scale matters - since we multiply by $\alpha$
- how to determine and justify $\alpha$?


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Decision Under Uncertainty](Category_Decision_Under_Uncertainty)