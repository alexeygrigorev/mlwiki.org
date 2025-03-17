---
title: Multi-Dimensional Indexes
layout: default
permalink: /index.php/Multi-Dimensional_Indexes
---

# Multi-Dimensional Indexes

## Multi-Dimensional Indexes
### Typical Applications
- Searching [Data Cube](OLAP) for [Data Warehousing](Data_Warehousing)
- [Spatial Databases](Spatial_Databases)


## Typical Queries
### Point Query
Find all values for the (multi-dimensional) search key
- for product "TV" sold in Ireland with ALL for date
- does there exist a star on coordinate (10, 3, 5)

### Partial Match Queries
Not all values of a search key are specified
- return the coordinates pf all stars with $x=5$ and $z=3$

### Range Queries (Dicing)
- return all cube cells with date $\geqslant Q_1$ and date $\leqslant Q_2$ and sales $\leqslant 100$
- return coordinates of all stars with $x \geqslant 10$ and $20 \leqslant y \leqslant 35$

### Nearest-Neighbor Queries
- return closest 3 stars to a star at (10, 15, 20) 

## Can Use One-Dimensional Indexes?
[One-Dimensional Indexes](Indexing_(databases)#One-Dimensional_Indexes) (such as [B-Tree](B-Tree))
- take one single key
- can use one key made of multiple attributes 

### [B-Tree](B-Tree)
Need to impose [lexicographical order](B-Tree#Lexicographical_Order) on keys in B-Tree to do that
- don't answer all our queries - see [B-Tree#Multiple Keys](B-Tree#Multiple_Keys)

### Hash Tables
For [Hash-Based Indexes](Indexing_(databases)#Hash-Based_Indexes) we need to compute [Hash Function](Hash_Function) for tuples
- extend hash function: $h(x, y, z) = h_1(x) + h_2(y) + h_3(z)$

Problem 
- cannot answer range queries at all 
- age < 20
- sal < 30
- age < 20 and sal < 20
- all lead to linear scan


## Types
### Other Types
- [Multiple-Key Index](Multiple-Key_Index)

### Hash-Based Multi-Dimensional Indexes
- [Grid File Index](Grid_File_Index)
- [Partitioned Hash Function Index](Partitioned_Hash_Function_Index)

### Tree-Based Multi-Dimensional Indexes
- [kd-Trees](kd-Trees)
- [Quad Trees](Quad_Trees)
- [R-Tree](R-Tree)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom


[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Database Indexes](Category_Database_Indexes)