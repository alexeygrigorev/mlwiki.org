---
layout: default
permalink: /index.php/Non-Discriminating_Criteria
tags:
- multi-criteria-decision-aid
title: Non-Discriminating Criteria
---
## Non-Discriminating Criteria
In [MCDA](MCDA) a criterion is non-discriminating if for all alternatives we have the same evaluation

For example,

|    |  $f_1$  |  $f_2$  |  ...  |  $f_k$  |  ...  |  $f_q$  |  $a_1$   |  $f_1(a_1)$  |  $f_2(a_1)$  |  ...  |  $\alpha$  |  ...  |  $f_q(a_1)$ ||  $a_2$   |  $f_1(a_2)$  |  $f_2(a_2)$  |  ...  |  $\alpha$  |  ...  |  $f_q(a_2)$ ||  ...   |  ...  |  ...  |  ...  |  ...  |  ...  |  ... ||  $a_n$   |  $f_1(a_n)$  |  $f_2(a_n)$  |  ...  |  $\alpha$  |  ...  |  $f_q(a_n)$ |

$f_k$ is non-discriminating criterion because for all alternatives it evaluates to $\alpha$
- this criteria is meaningless 
- we want to delete it
- but we must be careful: because it may lead to [Rank Reversal](Rank_Reversal) for some [MCDA](MCDA) methods
- for [PROMETHEE](PROMETHEE) it will not: we can safely remove such criteria 


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
