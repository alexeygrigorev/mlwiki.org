---
title: Secondary Index
layout: default
permalink: /index.php/Secondary_Index
---

# Secondary Index

## Secondary Index
What if we want to support efficient search by some other attribute (not one that is already indexed)
- then the file is not sequentially sorted by this other attribute (it's sorted on the pk)
- we can make a copy of the entire table - but it's too expensive

Index structures to do that are Secondary [Indexes](Indexes_(databases))

### [Sparse Index](Sparse_Index)?
Doesn't make sense
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-sparse-no-sense.png" alt="Image">
- since the file is sorted by another key

### [Dense Index](Dense_Index)?
Idea: 
- build a dense index, sort it,
- construct sparse index on it
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-dense-sparse.png" alt="Image">


## Duplicates
### Just Repeat
Suppose we use [Dense Index](Dense_Index) as our secondary index
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-dense-dups-1.png" alt="Image">
- Same is [Option 1](Dense_Index#Option_1) from [Dense Index](Dense_Index) (note that [Option 2](Dense_Index#Option_2) will not work here - file is not ordered by this key)
- 10 occurs 3 times - may lead to waste of space
- may look innocent for integers, but often keys are strings

### Variable-Length Records
Another way is to use variable-length records
- now need to store the key value only once
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-dense-dups-2.png" alt="Image">
- problem now: need to support variable-length records (which is hard)

### Buckets of Pointers
We add one more level of indirection
- we have index on buckets
- buckets are pointers to the actual tuples

So now we have
1. [Dense Index](Dense_Index) where each value is stored once
1. ''Bucket list'' where we have multiple occurrences
  - pointers to actual values 
  - should be sequential: i.e. ordered by the key
1. Actual blocks

Also saves space|   | |Example
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-level-of-ind.png" alt="Image">
- index pointers point to the first occurrence of 10
- we read buckets down till there's no 10 anymore

This idea is used in [Buckets of Pointers](Buckets_of_Pointers)


## See also
- [Indexing (databases)](Indexing_(databases))
- [Sparse Index](Sparse_Index)
- [Dense Index](Dense_Index)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Database Indexes](Category_Database_Indexes)