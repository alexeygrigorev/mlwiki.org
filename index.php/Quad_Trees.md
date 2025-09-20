---
layout: default
permalink: /index.php/Quad_Trees
tags:
- database-indexes
- database-systems-architecture
title: Quad Trees
---
## Quad Trees
This is [Tree-Based](Binary_Search_Trees) [Multi-Dimensional](Multi-Dimensional_Indexes) [Index Structure](Indexing_(databases)) 

Idea:
- for $k$-dimensional space 
- each node corresponds to a $k$-dimensional cube
- for 2D it's a square region


### Building
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/quad-tree-1.png" alt="Image">

Algorithm
- if a number of points in a cube is larger that can fit in a block
- then we create an interior node 
- and divide the cube recursively (i.e. we create 4 children for each quadrant)
- otherwise we create a leaf block

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/quad-tree-repr.png" alt="Image">


## Operations
Lookups, Insertions and Deletions are very similar to [kd-Trees](kd-Trees)


## See also
- [Binary Search Trees](Binary_Search_Trees)
- [kd-Trees](kd-Trees)
- [R-Tree](R-Tree)
- [Multi-Dimensional Indexes](Multi-Dimensional_Indexes)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
