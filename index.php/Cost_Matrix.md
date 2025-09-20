---
layout: default
permalink: /index.php/Cost_Matrix
tags:
- classifiers
- machine-learning
- model-performance-evaluation
title: Cost Matrix
---
## Cost Matrix
Used for comparing two different models
- A ''cost matrix'' is a matrix of the following form:

|    |  $y = +$  |  $y = -$  |   $h_\theta(x) = +$  |  $C(+ | +)$  |  $C(+ | -)$ ||   $h_\theta(x) = -$  |  $C(- | +)$  |  $C(- | -)$ |

In general case:
- $C(i |  j)$  |- a cost of classifying an example of class $j$ as class $i$
- this way we can express that some mispredictions are very costly


### Example
|    |  $y = +$  |  $y = -$  |   $h_\theta(x) = +$  |  $C(+ | +) = -1$  |  $C(+ | -) = 1$ ||   $h_\theta(x) = -$  |  $C(- | +) = 100$  |  $C(- | -) = 0$ |
- we put $C(- |  +) = 100$ because in this example false negatives are very costly |
And assume we're comparing two classifiers $C_1$ and $C_2$
- below are their [Contingency Table](Contingency_Table)s

<table class="wikitable">
<tr>
<td>
| + stats of $C_1$ ||    |  $y = +$  |  $y = -$  |   $h_{C_1}(x) = +$  |  150  |  60 ||   $h_{C_1}(x) = -$  |  40  |  250 |
- $\text{acc}(C_1) = \cfrac{150+250}{150+40+60+250} = 80\%$
- $\text{cost}(C_1) = -1 \cdot 150 + 1 \cdot 60 + 100 \cdot 40 + 0 \cdot 250 = 3910$
</td>
<td>
| + stats of $C_2$ ||    |  $y = +$  |  $y = -$  |   $h_{C_2}(x) = +$  |  250  |  5 ||   $h_{C_2}(x) = -$  |  45  |  200 |
- $\text{acc}(C_2) = \cfrac{250+200}{250+45+5+200} = 90\%$
- $\text{cost}(C_2) = -1 \cdot 250 + 1 \cdot 5 + 100 \cdot 45 + 0 \cdot 200 = 4255$
</td>
</tr>
</table>

Selecting $C_1$
- because $C_1$ has lower cost: $\text{cost}(C_1) < \text{cost}(C_2)$
- even though $C_2$ has better accuracy: $\text{acc}(C_2) > \text{acc}(C_1)$ 


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
