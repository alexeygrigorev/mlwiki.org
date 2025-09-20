---
layout: default
permalink: /index.php/Query_Plan
tags:
- database-systems-architecture
- relational-databases
title: Query Plan
---
## Logical Query Plan
In [Relational Databases](Relational_Databases), Logical Query Plan - intermediate code in the [Query Processing](Query_Processing) pipeline (typically a [Relational Algebra](Relational_Algebra) expression)
- Essentially it's an execution tree
- We evaluate it bottom-up
- Usually need to [optimize it](Logical_Query_Plan_Optimization) before executing  to make the execution faster


### Example
Suppose we have a Relational Algebra expression:
- $\pi_{A, B} \big(\sigma_{A = 5}(R) \cup (S \Join T) \big)$
- this defines the following execution tree 
: <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/logical-query-plan-ex.png" alt="Image">


## Physical Query Plan
A ''Physical Query Plan'' is the same as Logical Query Plan, but with [specific algorithms](Physical_Operators_(databases)) assigned to each operation (node of the tree)
- I.e. it defines how exactly a query will be executed
- [Query Result Size Estimation](Query_Result_Size_Estimation) to estimate the size of [physical operator's](Physical_Operators_(databases)) output  
- [Physical Query Plan Optimization](Physical_Query_Plan_Optimization) to select the best plan


Questions to consider
- What algorithms are available to do selections, joins, projections? These algorithms are called [physical operators](Physical_Operators_(databases)) 
- each physical operator has an associated cost - number of I/O operations (in [I/O Model of Computation](I_O_Model_of_Computation))
- It also highly depends on [how data is stored](Physical_Data_Organization_(databases))

### Example
We just assign some operation to each node: 
: <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/plan-selection-bad.png" alt="Image">


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
