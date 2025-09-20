---
layout: default
permalink: /index.php/Multiple-Key_Index
tags:
- database-indexes
- database-systems-architecture
title: Multiple-Key Index
---
## Multiple-Key Index
This is a very simple conventional [Multi-Dimensional](Multi-Dimensional_Indexes) [Index Structure](Indexing_(databases))


### Idea
The main idea is a nested index:
- the index on indexes
- index could be anything: [B-Tree](B-Tree) or Hash-Based one-dimensional index

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/mult-key-ind-ex1.png" alt="Image">
- in this case we have a tree 
- nodes at each level of this tree are also indexes 
- so for this example we have an index on the first attribute that points to an index on 2nd attribute


### Example
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/mult-key-ind-ex2.png" alt="Image">


## Types of Queries
- partial match queries 
  - easy if first attribute is specified
  - otherwise must look through every subindex
- range queries 
  - easy - provided individual indexes support range queries 


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
