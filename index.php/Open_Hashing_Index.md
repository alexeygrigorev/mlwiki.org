---
title: Open Hashing Index
layout: default
permalink: /index.php/Open_Hashing_Index
---

# Open Hashing Index

## Open Hashing Index
Idea: 
- apply [Open Hashing](Hash_Tables) to [Secondary Storage](Secondary_Storage) to build an [index](Indexing_(databases))

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-idea.png" alt="Image">

Given:
- We have $n$ hashing buckets (each bucket is typically one disk block)
- a [Hash Function](Hash_Function) $h$ that maps a key $k$ to a bucket: an integers $\in [0 .. n - 1]$

### Examples
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-example.png" alt="Image">
- assume we have 2 records per bucket
- hash function: $h(a) = 1, h(b) = 2, h(c) = 1, h(d) = 0$


## Storing
Two options 
- store records themselves in the buckets (clustered index) 
- store only pointers to actual records (the only option for secondary index) (unclustered index)
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-ways-to-store.png" alt="Image">
- also see ([Clustered Index](Indexing_(databases)#Clustered_Index))

Do we sort records by key withing buckets
- we may if we want faster retrieval
- and inserts and deletes are not frequent (they get slower)


## Overflow Blocks
We allow overflow blocks
- when we want to insert something, but there's no room in the bucket
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-example-overflow.png" alt="Image">


## Operations
### Lookup
- for a search key $k$ calculate $h(k)$ (apply hash function to the key)
- use the returned value to locate the bucket with our record
- if the record is not there we follow the overflow pointer
- once we've reached the end of chain and still haven't found anything - there is no such record


### Insert
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-example.png" alt="Image">
- suppose we want to insert $e, h(e) = 1$
- but bucket 1 is already full 
- we create an overflow block and put it there 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-example-overflow.png" alt="Image">

Algorithm
- calculate $h(k)$ to locate bucket $B$ to use
- if $B$ is not full, just add
- if $B$ is full, and there's an overflow block, try putting it there
- otherwise create a new overflow and store this record there

'''NB:''' performance degrades as the number of overflow blocks grows|   see [#Reorganization](#Reorganization) | |
### Deletion
- for search key $k$ calculate $h(k)$ to locate the bucket $B$
- find the record in bucket $B$
- if there not there - follow the overflow pointer
- if there - remove it
- if you're in an overflow block and this record was the last one - also remove the block 
- if not last one - you may want to shift elements from other overflow blocks


## Reorganization
Rule: we want to keep space utilization between 50% and 80%

''space utilization'' - how much space is used
- $u = \cfrac{\text{# keys used}}{\text{total # of keys}}$
- the denominator is the # of keys that we can store if we used '''only''' main buckets, without any overflow blocks 
  - e.g. 2 items per block, 3 blocks = 6 keys
- if $u < 50\%$ - lots of space wasted (many empty buckets)
- if $u > 80\%$ - significant overflow
- if we go beyond the boundaries, we need to do rehashing 

Rehashing: creating new buckets or eliminating wasted space 
- very costly 


### Other Hash-Based Indexes
To be able to better cope with growth, there are other approaches:
- Dynamic Hashing:
  - [Extensible Hashing](Extensible_Hashing)
  - [Linear Hashing](Linear_Hashing)


## See also
- [Indexing (databases)](Indexing_(databases))
- http://dblab.cs.toronto.edu/courses/443/2013/06.hash-index.html


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Data Structures](Category_Data_Structures)
[Category:Database Indexes](Category_Database_Indexes)