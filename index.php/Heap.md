---
title: "Heap"
layout: default
permalink: /index.php/Heap
---

# Heap

## Heap
a container that have keys

key property: at every node $x$
- key[x] $\leqslant$ (or $\geqslant$) all keys of $x$'s children
- therefore, the object at root must have min (max) value

## operations
insert
- adds new object
- $O(\log n)$


extract-min(max)
- extracts min (max) from heap
- ties broken arbitrarily
- $O(\log n)$


heapify
- initialization: builds a heap


delete
- $O(\log n)$ time


## Implementation
- it's a tree with $\approx \log_2 n$ levels
- backed by array

Traversing the tree:
- $\text{parent}(i) = i / 2$
- $\text{left}(i) = 2i$
- $\text{right}(i) = 2i + 1$

insert(key $k$):
- stick $k$ at the end of last level
- bubble-up $k$ until heap property is restored

extract-min():
- delete root
- move last leaf to be new root
- bubble-down until heap property is restored
- (always swap with the smallest child)

Java implementation: 
- [Heap.java](http://code.google.com/p/codeforces-solutions-java/source/browse/trunk/codeforces-java/src/main/java/coursera/algo1/week5/Heap.java)

## Applications
- general: fast way to do repeated minimum (maximum) computations
- priority queues, "event manager"

### Heap sort
- put everythin into heap
- repeatedly extract-min until the heap is empty


### Median maintenance
- given: a sequence of numbers $x_1, ..., x_n$, one-by-one
- goal: at each time step $i$, compute the median of $\{x_1, ..., x_i\}$
- solution: 
  - create two heaps: 
    - $H_\text{low}$ (with extract-max operation), 
    - $H_\text{high}$ (extract-min)

- key idea: maintain invariant that $\approx \cfrac{i}{2}$ smallest (largest) numbers are in $H_\text{low}$ ($H_\text{high}$)
- so on $20$th step, in $H_\text{low}$ would be $10$th order statistics, and in $H_\text{high}$ - $11$th
- keep the heaps balanced|   (so they have the same number of elements) | |
Implementation: [http://code.google.com/p/codeforces-solutions-java/source/browse/trunk/codeforces-java/src/main/java/coursera/algo1/week6/NextMedian.java]


### Speeding up the [Dijkstra's algorithm](Dijkstra's_Shortest_Path)
- naive $\Theta(nm)$
- with heaps $O(m \log n)$


## See also
- [Dijkstra's Shortest Path](Dijkstra's_Shortest_Path)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))
- http://algorithms.soc.srcf.net/notes/dijkstra_with_heaps.pdf

[Category:Algorithms](Category_Algorithms)
[Category:Data Structures](Category_Data_Structures)