---
title: "Bitmap Heap Scan"
layout: default
permalink: /index.php/Bitmap_Heap_Scan
---

# Bitmap Heap Scan

{{stub}}

## Bitmap Heap Scan
Index can be clustered or unclustered
- When index is clustered it means the records themselves are stored in index, not pointers
- I.e. a clustered index ensures that all data is stored in some order 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/ind/hash-ways-to-store.png" alt="Image">
- Usually there is only one clustered index per relation (otherwise the data will be duplicated)

If an index (say, [B-Tree](B-Tree)) is not clustered, 
- then instead of following each pointer 
- can use Bitmap Heap Scan


### Algorithm
- Collect all the pointers 
- Then group them by pages on disk 
- And retrieve them one-by-one 

Reasons:
- to avoid following each pointer separately 
- to make scans on clustered indexes more efficient

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Database Indexes](Category_Database_Indexes)