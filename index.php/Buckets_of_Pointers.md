---
title: Buckets of Pointers
layout: default
permalink: /index.php/Buckets_of_Pointers
---

# Buckets of Pointers

## Buckets of Pointers
We add one more level of indirection for [indexing](Indexing_(databases))
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

Good for Range Queries
- These buckets are also useful for ''Range Queries''

Suppose we have 
- relation Emp(name, dept, floor)
- name is primary key (main index)
- dept and floor are secondary keys ([Secondary Index](Secondary_Index)es on them)

Suppose we want to ask the following:
```sql
SELECT * FROM Emp where dept = 'Toy' AND floor = 2
```
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/secondary-buckets-range-q.png" alt="Image">
- need to compute the intersection of set of pointers (very fast)
- and this is before reading from disk


## See also
- [Indexing (databases)](Indexing_(databases))
- [Secondary Index](Secondary_Index)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Database Indexes](Category_Database_Indexes)