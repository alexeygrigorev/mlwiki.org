---
title: Rank Correlation
layout: default
permalink: /index.php/Rank_Correlation
---

# Rank Correlation

## Rank Correlation
a ''rank correlation'' is a measure of relationship 
- between different rankings of the same variable
- of between two rankings of different ordinal variables


### Intuition
Two variables case:
- $X$ - basketball ranking of college teams
- $Y$ - football ranking of college teams
- is there a correlation between $X$ and $Y$? 
- e.g. do colleges with good football ranks tend to have good basketball ranks? 

One variable case:
- $X$ - football matches ranked by coaches 
- $Y$ - football matches ranked by sportswriters
- are these rankings similar?


## Correlation Coefficient
- A ''rank correlation coefficient'' shows the degree of similarity between two rankings
- so we want to calculate the distances between two rank vectors


## One Variable Case
### Problem
let $X = \{A, B, C, D, E \}$ - be a set of 5 objects

want to compare 
- observed ranking $r(X): [E, B, A, C, D]$
- predicted ranking $r^*(X): [B, E, C, D, A]$
- need to be able to compute distance $d(r, r^*)$ between them


### Running Example
|    |  1  |  2  |  3  |  4  |  5  |   $r$  |  $B$  |  $A$  |  $C$  |  $D$  |  $E$ ||  $r^*$ ||  $E$  |  $C$  |  $D$  |  $A$  |  $B$ |

### Spearman's Footrule
given $X = \{ x_1, ..., x_N \}$
- $d_{SF}(r, r^*) = \sum_{i=1}^{N} \big|  r(x_i) - r^*(x_i) \big|$ |- not normalized: $d_{SF}(r, r^*) \in [0, +\infty)$ 
- similar to the Manhattan distance


Example:
- $d_{SF}(r, r^*) = | 1 - 2| + |2 - 1| + |3 - 5| + |4 - 3| + |5 - 4| = 1 + 1 + 2 + 1 + 1 = 6$ |

### Spearman Distance
given $X = \{ x_1, ..., x_N \}$
- $d_{S}(r, r^*) = \sum_{i=1}^{N} \big( r(x_i) - r^*(x_i) \big)^2$
- also not normalized: $d_{SF}(r, r^*) \in [0, +\infty)$ 


Example:
- $d_{SF}(r, r^*) = | 1 - 2|^2 + |2 - 1|^2 + |3 - 5|^2 + |4 - 3|^2 + |5 - 4|^2 = 1 + 1 + 4 + 1 + 1 = 8$ |

### Spearman's $\rho$ (Rank Correlation Coefficient)
given $X = \{ x_1, ..., x_N \}$
- $\rho_S(r, r^*) = 1 - \cfrac{6 \cdot d_S(r, r^*)}{N \cdot (N^2 - 1)}$
- normalized: $\rho_S(r, r^*) \in [-1, 1]$
  - $\rho_S(r, r^*) = 1$ - identical
  - $\rho_S(r, r^*) = -1$ - inverse

Example:
- $\rho_S(r, r^*) = 1 - \cfrac{6 \cdot 5}{5 \cdot (5^2 - 1)} = 0.6$


### Kendall's Distance
It counts the pair-wise disagreement between two ranking lists, i.e. [Inversion Count](Inversion_Count)
- $d_K(r, r^*) = \Big|  \big\{ (x_i, x_j)  | r(x_i) < r(x_j) \land r^*(x_i) > r^*(x_j) \big\} \Big|$ |- so it's the # of item pairs that are inverted in the $r$ compared to $r^*$, 
- also, the ranking can be partial
- and it's not normalized

Example:
- $d_K(r, r^*) = (1+0+0+0)+(0+0+0)+(1+1)+(0)=3$
 

### Kendall's $\tau$
It normalizes the Kendall's Distance
- $\tau_K(r, r^*) = 1 - \cfrac{4 \cdot d_k(r, r^*)}{N \cdot (N - 1)}$
- $\tau_K(r, r^*) \in [-1, 1]$


Example:
- $\tau_K(r, r^*) = 1 - \cfrac{4 \cdot 3}{5 \cdot (5 - 1)} = 0.4$


### Gamma Coefficient
$\Gamma$ coefficient is based on the # of correct and incorrect rankings
- "correct": 
  - $d^+(r, r^*) = \big|  \big\{ (x_i, x_j) \ | \ r(x_i) < r(x_j) \land r^*(x_i) < r^*(x_j)  \big\} \big|$ |  - the number of items at the same relative position in raking
- "inverted" (as in Kendall's $\tau$)
  - $d^-(r, r^*) = \big|  \big\{ (x_i, x_j) \ | \ r(x_i) < r(x_j) \land r^*(x_i) > r^*(x_j)  \big\} \big|$ |  - the number of inversions
- $\Gamma(r, r^*) = \cfrac{d^+(r, r^*) - d^-(r, r^*)}{d^+(r, r^*) + d^-(r, r^*)}$
- $\Gamma(r, r^*) \in [-1, 1]$
- it's equal to $\tau_K(r, r^*)$ if the rankings are total



### Weighted Methods
The previous measures gave equal importance to all ranking positions
- i.e. differences in the first ranking positions have the same effect as for the last positions
- in many cases the closer position is to the beginning, the more important it is
- e.g. when we want to show only first 5 items, the rest after 5 are not important

Solution
- assign weight proportional to the importance
- if position is important, may assign weight s.t. they decrease with the ranking position
- $d_S(r, r^*) = \sum_{i = 1}^N w_i \cdot \big( r(x_i) - r^*(x_i) \big)^2$ with
  - $w_i = \cfrac{1}{\log r(x_i) + 1}$


### [MCDA](MCDA) Methods
Can also use Multi-Criteria Decision Aid for that
- e.g. Concordance Index from [ELECTRE](ELECTRE)


## Links
- http://theory.stanford.edu/~sergei/slides/www10-metrics.pdf

## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- http://en.wikipedia.org/wiki/Rank_correlation
- http://en.wikipedia.org/wiki/Kendall_tau_distance

[Category:Statistics](Category_Statistics)