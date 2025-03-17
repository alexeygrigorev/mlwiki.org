---
title: Lift (Data Mining)
layout: default
permalink: /index.php/Lift_(Data_Mining)
---

# Lift (Data Mining)

## Lift ([Data Mining](Data_Mining))
Lift is an interestness measure used in [Rule Mining](Rule_Mining)
- for mining more relevant [association rules](Association_Rule_Mining)


Lift:
- for a rule $X \to Y$ with $\text{supp}(X) \ne 0$ and $\text{supp}(Y) \ne 0$
- $\text{lift}(X \to Y) = \cfrac{\text{supp}(X \to Y)}{\text{supp}(X) \cdot \text{supp}(Y)}$
- since $\text{conf}(X \to Y) = \cfrac{\text{supp}(X \to Y)}{\text{supp}(X)}$, can rewrite the formula as
- $\text{lift}(X \to Y) = \cfrac{\text{conf}(X \to Y)}{\text{supp}(Y)}$


### Properties
- $\text{lift}(X \to Y) \ne 0$ 
- $\text{conf}(X \to Y) \in [0, 1]$, and $\text{supp}(Y) \in [0, 1]$
- so $\text{lift}(X \to Y) \in (0, +\infty)$


### Example
Consider this dataset $D$:
- $T_1 = ABCD, T_2 = ADE, T_3 = BDE, T_4 = E$

Lift:
- $\text{lift}(A \to \varnothing) = 1 / 1 = 1$ (everything gives 0, so it's not interesting)
- $\text{lift}(A \to B) = 0.5 / 0.5 = 1$ ($A$ and $B$ are independent, so nothing interesting)
- $\text{lift}(A \to BC) = 0.5 / 0.24 = 2$
- so lift is 1 when two items are independent, and higher when there's some correlation between them


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- http://en.wikipedia.org/wiki/Lift_(data_mining)

[Category:Rule Mining](Category_Rule_Mining)