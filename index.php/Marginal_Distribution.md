---
layout: default
permalink: /index.php/Marginal_Distribution
tags:
- statistics
- probability
- distributions
title: Marginal Distribution
---

## Marginal Distribution
*Marginal distribution* - distribution of only one of the variables in a contingency table

|  | $O_1$ | $O_2$ | $O_3$ |  |
|---|---|---|---|---|
| $M$ | $x_1$ | $x_2$ | $x_3$ | $x_1 + x_2 + x_3$ |
| $F$ | $x_4$ | $x_5$ | $x_6$ | $x_4 + x_5 + x_6$ |
|  | $x_1 + x_4$ | $x_2 + x_5$ | $x_3 + x_6$ |  |

- Last row is the marginal distributions for columns (sum for all cells in each column)
- And the last column is the marginal distribution for row (sum for all cells in each row)

Row and column proportions

The row proportions are computed
as the counts divided by their row totals. The value 149 at the intersection of spam and
none is replaced by 149/367 = 0.406, i.e. 149 divided by its row total, 367. So what does
0.406 represent? It corresponds to the proportion of spam emails in the sample that do not
have any numbers.

Table 1.35: A contingency table with row proportions for the spam and
number variables.

|  | none | small | big | Total |
|---|---|---|---|---|
| spam | 149/367 = 0.406 | 168/367 = 0.458 | 50/367 = 0.136 | 1.000 |
| not spam | 400/3554 = 0.113 | 2657/3554 = 0.748 | 495/3554 = 0.139 | 1.000 |
| Total | 549/3921 = 0.140 | 2827/3921 = 0.721 | 545/3921 = 0.139 | 1.000 |

A contingency table of the column proportions is computed in a similar way, where
each column proportion is computed as the count divided by the corresponding column
total.

|  | none | small | big | Total |
|---|---|---|---|---|
| spam | 149/549 = 0.271 | 168/2827 = 0.059 | 50/545 = 0.092 | 367/3921 = 0.094 |
| not spam | 400/549 = 0.729 | 2659/2827 = 0.941 | 495/545 = 0.908 | 3684/3921 = 0.906 |
| Total | 1.000 | 1.000 | 1.000 | 1.000 |

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_%28coursera%29)
- [OpenIntro Statistics (book)](OpenIntro_Statistics_%28book%29)
