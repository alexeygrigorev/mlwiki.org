---
layout: default
permalink: /index.php/Grid_File_Index
tags:
- database-indexes
- database-systems-architecture
title: Grid File Index
---
## Grid File Index
This is [Hash-Based](Hash_Function) [Multi-Dimensional](Multi-Dimensional_Indexes) [Index Structure](Indexing_(databases)) 

## Main Idea
In each dimension, using ''Grid Lines'', we divide our key space into ''stripes''
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/grid-files-ex1.png" alt="Image">
- lines divide the space into subspaces that are large enough to store ''one block''
- if needed, overflow blocks may be used 

### Representation
Each stripe points to some block on [disk](Secondary_Storage)
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/grid-files-repr.png" alt="Image">
- note that we have two empty buckets there, and don't have any pointers to actual blocks
- may allow for overflow blocks


## Operations
### Lookup
- need to know values for each grid line 
- so it's different from just applying a Hash Function
- we look at each component of the tuple and determine the position in the grid
- may add single-dimension index (such as [B-Tree](B-Tree)) for coordinates of each line to speed up finding the proper coordinate

### Insert
- Locate the needed bucket 
- if there is room - insert
- no room - two options
  - Overflow blocks
  - Split by creating new grid lines (hard)

Splitting
- causes additional problems:
- content of blocks is linked across dimensions
- so adding a grid line will split all the buckets along this line
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/grid-files-split.png" alt="Image">
- for $n$ dimensions we may choose which dimension to split
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/grid-files-split-ndim.png" alt="Image">

### Delete
- Find the corresponding bucket
- delete the record
- reorganize if needed 


## Summary
Recall [the typical of queries](Multi-Dimensional_Indexes#Typical_Queries) we want to answer for [Multi-Dimensional Indexes](Multi-Dimensional_Indexes)
- (+) good support for 
  - point queries
  - partial match queries (we know where to look to needed data)
  - range queries
- (+) reasonable support for 
  - nearest neighbor queries (first look withing the bucket, then neighbor buckets and so on)
- (-) downsides 
  - many empty buckets when data is not uniformly distributed
  - need to have a good algorithm that splits the space 


## See also
- [Partitioned Hash Function Index](Partitioned_Hash_Function_Index)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
