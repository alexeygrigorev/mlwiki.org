---
title: "Indexing (databases)"
layout: default
permalink: /index.php/Indexing_(databases)
---

# Indexing (databases)

## Motivation: Searching
Suppose we have a relation $R(A, B, C, D)$, each tuple - 32 bytes
- $128 \times 10^6$ tuples is $R$
- Block size is $B$ = 4kb
- I.e. can store 128 tuples per block, $10^6$ tuples in total

Suppose we want to find a tuple with $C = 10$


Searching in [I/O Model of Computation](I_O_Model_of_Computation)
- for each block $X \in R$
  - load $X$
  - check if there's a tuple $T \in X$ with $C = 10$
  - yes - output $T$
  - no - continue
  - release $X$ from memory

In worst case it's $10^6$ I/Os 
- suppose $10^{-3}$ seconds per I/O operation
- 16.6 minutes in total

Can we do better? 


## Indexing
An ''index'' is any [secondary memory](Secondary_Storage) data structure that
- takes a search key as input
- efficiently returns the collection of matching records


## One-Dimensional Indexes
### Conventional Indexes
- [Dense Index](Dense_Index)
- [Sparse Index](Sparse_Index)
- [Secondary Index](Secondary_Index) as a combination of both

### Tree-Based Indexes
- [B-Tree](B-Tree)

### Hash-Based Indexes
- [Open Hashing Index](Open_Hashing_Index)
- [Extensible Hashing](Extensible_Hashing)
- [Linear Hashing](Linear_Hashing)


## [Multi-Dimensional Indexes](Multi-Dimensional_Indexes)
### Conventional
- [Multiple-Key Index](Multiple-Key_Index)

### Tree-Based Indexes
- [kd-Trees](kd-Trees)
- [Quad Trees](Quad_Trees)
- [R-Tree](R-Tree)
- [Metric Trees](Metric_Trees) and [Spill-Trees](Spill-Trees) 

### Hash-Based Indexes
- [Grid File Index](Grid_File_Index)
- [Partitioned Hash Function Index](Partitioned_Hash_Function_Index)



## Clustered Index
Index can be clustered or unclustered
- When index is clustered it means the records themselves are stored in index, not pointers
- I.e. a clustered index ensures that all data is stored in some order 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-ways-to-store.png" alt="Image">
- Usually there is only one clustered index per relation (otherwise the data will be duplicated)

If an index (say, [B-Tree](B-Tree)) is not clustered, then instead of following each pointer other techniques can be used, such as [Bitmap Heap Scan](Bitmap_Heap_Scan)


## [Information Retrieval](Information_Retrieval) Indexing
Indexing can also be applied to unstructured data such as text
- [Inverted Index](Inverted_Index) builds an index from words to documents where these words are contained
- [Locality Sensitive Hashing](Locality_Sensitive_Hashing) gives an approximate answer to [KNN](KNN) queries



## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Database Indexes](Category_Database_Indexes)
[Category:Databases](Category_Databases)