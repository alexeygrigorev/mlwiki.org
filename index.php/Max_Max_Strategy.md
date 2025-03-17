---
title: "Max Max Strategy"
layout: default
permalink: /index.php/Max_Max_Strategy
---

# Max Max Strategy

## Max Max
How to choose an alternative? 
- in [Game Theory](Game_Theory)
- in [Decision Under Uncertainty](Decision_Under_Uncertainty)


Idea: Extreme Optimism
- the opposite of [Max Min Strategy](Max_Min_Strategy)
- Base your choice on the best situation that can happen 
- and maximize the consequences in the best case
- $\max_{a \in A} \max_{e \in E} c(a, e)$


### Example: [Decision Under Uncertainty](Decision_Under_Uncertainty)
|   $c$  |  $e_1$  |  $e_2$  |  $e_3$  |  max  |   |   $a_1$   |  40  |  70  |  -20  |  70   |  best case for $a_1$ ||   $a_2$   |  -10  |  40  |  100  |  <font color="red">100</font>  |  best case for $a_2$ ||   $a_3$   |  20  |  40  |  -5  |  40  |  best case for $a_3$ ||   |   |      |   max   |  100  |  $\to a_2$ |

### Advantages and Disadvantages
Same as for [Max Min Strategy](Max_Min_Strategy)

Downsides
- bad use of information
- no compensation between different consequences 

Advantages:
- no need for rich scale, ordinal scale is enough


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Decision Under Uncertainty](Category_Decision_Under_Uncertainty)
[Category:Game Theory](Category_Game_Theory)