---
title: Hash Function
layout: default
permalink: /index.php/Hash_Function
---

# Hash Function

## Hash Function
Performance of [Hash Tables](Hash_Tables) depends on how good a hash functions is

In chaining implementation
- insert/delete could be anywhere from $\cfrac{m}{n}$ to $m$ for $m$ objects
- $\cfrac{m}{n}$ - equally distributed
- $m$ - all in the same bucket

That means that performance depends on the choice of hash function

### Good Hash Function
So a good hash function should
- spread data out evenly
- be easy to store
- be fast to evaluate


### Bad Hash Function
Example of bad function
- given: memory locations for objects
- $h(x) = x \mod 1000$
- all odd buckets will be empty|   | |Pathological data sets
- even a super-clever hash function does not guarantee even distribution
- for every hash function there exists a pathological data set


## Collisions
A ''collision'' is
- distinct $x, y \in U$
- such that $h(x) = h(y)$

Well-known issue: [Birthday paradox](Birthday_paradox)


## See also
- [Hash Tables](Hash_Tables)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))


[Category:Algorithms](Category_Algorithms)