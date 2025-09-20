---
layout: default
permalink: /index.php/Waste_Utilization_Problem
tags:
- multi-objective-optimization
title: Waste Utilization Problem
---
## Waste Utilization Problem
This is a [Multi-Objective Optimization](Multi-Objective_Optimization) Problem
- 2 cities $X$ and $Y$ produce garbage
- there are two incinerators $I_1$ and $I_2$ with come capacity
- each incinerator has some cost of utilization per unit of waste
- there are some transportation costs per unit from a city to an incinerator

How much garbage to send from $X$ and $Y$ to $I_1$ and $I_2$?


Example:
- $X$ produces 100 tons of garbage, $Y$ produces 150 tons
- transportation costs: $X \to I_1: 2, X \to I_2: 3; Y \to I_1: 3, Y \to I_2: 4$
- cost of utilization: $I_1: 2, I_2: 1$
- capacities of $I_1$ and $I_2$ are 150

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/moo/waste-utilization.png" alt="Image">

Define the following variables:
- $XI_1, XI_2$ - garbage sent from $X$ to $I_1$ and $I_2$ respectively
- $YI_1, YI_2$ - garbage sent from $Y$ to $I_1$ and $I_2$ respectively

Constraints:
- amount of produced garbage = amount of incinerated garbage
  - $XI_1 + XI_2 = 100$
  - $YI_1 + YI_2 = 150$
- $I_1$ and $I_2$ have capacity:
  - $XI_1 + YI_1 \leqslant 150$
  - $XI_2 + YI_2 \leqslant 150$
- all must be positive
  - $XI_1, XI_2, YI_1, YI_2 \geqslant 0$

So we have the following objectives:
- we want to minimize the total cost of incineration
- : $z_1 = 2 \cdot (XI_1 + YI_1) + 1 \cdot (XI_2 + YI_2)$ 
- and we want to minimize the transportation cost
- : $z_2 = 2 \cdot XI_1 + 3 \cdot YI_1 + 3 \cdot XI_2 + 4 \cdot YI_2$ 

We evaluate all feasible solutions against $z_1$ and $z_2$
- and get something similar to this 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/moo/waste-utilization-solutions.png" alt="Image">
- the Pareto-optimal solutions [dominate](Dominance) all other feasible solutions


How to select the best one?
- [Weighed Sum](Multi-Objective_Optimization_Weighed_Sum)
  - will select only 4 solutions, the rest is ignored
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/moo/waste-utilization-solutions-weighted-sum.png" alt="Image">
- [Ideal Point](Ideal_Point)
  - we find the closest point to the ideal
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/moo/ideal-point.png" alt="Image">


## Links
- Routing Optimization for Waste Management http://www.ma.iup.edu/~jchrispe/ORArticles/WasteManagement.pdf
- Ant Colony optimization for Waste Utilization problem: http://thescipub.com/pdf/10.3844/jmssp.2009.199.205 


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
