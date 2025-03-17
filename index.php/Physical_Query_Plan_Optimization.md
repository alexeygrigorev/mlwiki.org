---
title: Physical Query Plan Optimization
layout: default
permalink: /index.php/Physical_Query_Plan_Optimization
---

# Physical Query Plan Optimization

## [Physical Query Plan](Query_Plan#Physical_Query_Plan) Optimization
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/query-processing-3rd.png" alt="Image">

Translating SQL to RA expression is the first step in [Query Processing](Query_Processing) Pipeline
- Input: Optimized Logical Query plan - expression in Extended [Relational Algebra](Relational_Algebra)
- Output: Optimized Physical Query Plan - expression in Relational algebra with each node assigned some [physical algorithm](Physical_Operators_(databases))


## Cost-Based Plan Selection
We need to select the optimal plan based on 
- Cost of [Physical Operators](Physical_Operators_(databases)) and 
- on [estimated cost of subqueries](Query_Result_Size_Estimation)

This is an [Optimization Problem](Optimization_Problem)
- One of the possible approaches is [Greedy Algorithms](Greedy_Algorithms)


## Greedy Algorithm
At each step we choose the operation with least local cost

Bottom-up approach:
- first assign physical operators to leaves 
- then to parents of the leaves 
- then to their parents 
- and so on
- at each step choose an operator that gives the lowest cost
- for join operators use a [gredy algorithm for join ordering](Join_Ordering#Greedy_Algorithm)

### Limitations
Doesn't take into account the properties of the output of an operator

Consider this example:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/plan-selection-bad.png" alt="Image">
- suppose optimized sort-merge join is not available - not enough memory
- so the Greedy algorithm decides to use hash-based join (recall that its output is not sorted)
- we could've taken slightly more expensive sort-merge join 
  - but instead of 3-pass duplicate elimination we'd just need one pass for $\delta$
  - which would give us overall lower total cost


## Exercises
{{ Main |  Query Plan Selection Exercises }} |

## See also
- [Query Plan](Query_Plan)
- [Physical Operators (databases)](Physical_Operators_(databases))
- [Query Result Size Estimation](Query_Result_Size_Estimation)
- [Join Ordering](Join_Ordering)
- [Pipelining](Pipelining)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))


[Category:Relational Databases](Category_Relational_Databases)
[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Optimization](Category_Optimization)
[Category:Greedy Algorithms](Category_Greedy_Algorithms)