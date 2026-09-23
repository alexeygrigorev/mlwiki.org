---
layout: default
permalink: /index.php/Conditional_Distribution
tags:
- statistics
- probability
- distributions
title: Conditional Distribution
---

## Conditional Distribution
*Conditional Distribution* of a [categorical variable](Categorical_Variables) is its distribution within a fixed value of a second variable

### [Contingency Table](Contingency_Table)
Consider this [Contingency Table](Contingency_Table)

|  | $O_1$ | $O_2$ | $O_3$ |  |
|---|---|---|---|---|
| $M$ | $x_1$ | $x_2$ | $x_3$ | $x_1 + x_2 + x_3$ |
| $F$ | $x_4$ | $x_5$ | $x_6$ | $x_4 + x_5 + x_6$ |
|  | $x_1 + x_4$ | $x_2 + x_5$ | $x_3 + x_6$ |  |

For this table
- given the first variable is $M$
- the conditional distribution is just for $O_1 + O_2 + O_3$
- it and can be calculated from the contingency table. 

### Example
| Handedness/Sex | Male | Female | Total |
|---|---|---|---|
| Right | 43 | 44 | 87 |
| Left | 9 | 4 | 13 |
| Total | 52 | 48 | 100 |

Conditional distribution of sex given handedness (handedness is fixed):

|  | Male | Female |
|---|---|---|
| Right | 43/87 = 0.49 | 44/87 = 0.51 |
| Left | 9/13 = 0.69 | 4/13 = 0.31 |

Note that sum of all values for one fixed variable should be 1

## Simpson's paradox
*Simpson's paradox* is when the conditional distributions within subgroups can difer from condition distributions for combined observations. 

Main cause:
- 3rd lurking variable which influences the study

Age vs Marital Status

|  | Single | Married | Widowed | Divorced | TOTAL |
|---|---|---|---|---|---|
| < 20 years old | 100% | 0% | 0% | 0% | 15% |
| Between 20 and 64 | 32% | 59% | 2% | 7% | 65% |
| $\geqslant$ 65 years old | 8% | 54% | 35% | 4% | 20% |
| TOTAL | 46% | 43% | 7% | 5% | 100% |

possible to detect if correlation exists between the age and the marital status
if some strong correlation exists it can be possible to remove one of these attributes when building a model 

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_%28coursera%29)
- [OpenIntro Statistics (book)](OpenIntro_Statistics_%28book%29)
- Stat Inference!
