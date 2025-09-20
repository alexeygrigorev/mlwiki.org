---
layout: default
permalink: /index.php/Consistent_Family_of_Criteria
tags:
- multi-criteria-decision-aid
- multi-objective-optimization
title: Consistent Family of Criteria
---
## Consistent Family of Criteria
A family of criteria in an [MCDA](MCDA) problem should satisfy the following three properties: 
- Exhaustivity
- Cohesion
- Non-Redundancy

These properties together form a consistent family of criteria

### Notation
- $A = \{a, b, c, ...\}$ - set of alternatives
- $G = \{g_1, ..., g_k\}$ - set of criteria
- $a_1 \ P \ a_2$ - preference relation between two alternatives
- $a_1 \ I \ a_2$ - indifference relation between two alternatives


## Properties
### Exhaustivity
$\forall g_i$ s.t. $g_i (a) = g_i (b) \Rightarrow a \ I \ b$


### Cohesion
$\forall a, b \in A$ if
- $\exists g_i \in G: g_i(a) > g_i(b)$ and
- $\forall g_j \in A, g_j \ne g_i: g_j(a) = g_j(b)$ 
- then $a \ P \ b$

Alternative formulation:
- The [Dominance](Dominance) principle should be respected


### Non-Redundancy
$G$ is not redundant if removal of any $g_i \in G$ leads to violation of exhaustivity or cohesion


## Links
- http://www.lamsade.dauphine.fr/~bouyssou/TranspaOrbel16.pdf

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
