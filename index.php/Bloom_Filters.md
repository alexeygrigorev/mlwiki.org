---
layout: default
permalink: /index.php/Bloom_Filters
tags:
- algorithms
- data-structures
title: Bloom Filters
---
## Bloom filters
Goal: fast inserts and lookups

Compared to [Hash Tables](Hash_Tables)
- pros
  - more space efficient
- cons
  - can't store associated object
  - no deletions
  - small false positive probability


## Applications
- early spell-checkers (original)
- list of forbidden passwords
- network routers
  - limited memory
  - need to be super-fast


## Implementation
Inside contains 
- array of $n$ bits
  - $\frac{n}  - in data set $S$
- $h$ - hash function $h_1..h_k$
  - $k$ - a small constant


## Operations
Insert($x$):
- for $i = 1..k$
- set $A[h_i(x)] = 1$

Lookup($x$)
- True if $A[h_i(x)] = 1$ for every $i = 1..k$


## False positives
if $x$ was inserted
- no false negatives - guaranteed to succeed

if $x$ wasn't inserted, false positives if
- all $k$ $h_i(x)$ are already set to 1 by other insertions


## See also
- [Hash Tables](Hash_Tables)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))
