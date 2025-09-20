---
layout: default
permalink: /index.php/Breadth-First_Search
tags:
- algorithms
- graphs
title: Breadth-First Search
---
## Breadth-First Search
A [Graph Search](Graph_Search) algorithm:
- explores [Graphs](Graphs) in "layers"
- uses FIFO (i.e. a queue)

## Basic Algorithm
BFS(graph $G$, start vertex $s$):
- [all nodes are initially unexplored]
- mark $s$ as explored
- $Q$ = queue, initialized with $s$
- while $Q$ is not empty
  - remove $v$ from $Q$
  - for each edge $(v, w)$
    - if $w$ unexplored
    - mark $w$ as explored
    - add $w$ to $Q$

running time $O(m + n)$

## Applications
### Shortest Path
Goal: compute $\text{dist}(v)$ - the fewest number of edges on the path from $s$ to $v$ (in unweighted graph)

Extra code:
- in initialization:
  - $\text{dist}(v)$:
    - $0$ if $v = s$
    - $\infty$ if $v \ne s$
- when considering edge(v, w):
  - if $w$ unexplored
  - set $\text{dist}(w) = \text{dist}(v) + 1$


### Connected Components
Goal: compute all connected components of an undirected graph.

why?
- is network connected?
- graph visualization
- clustering (quick and dirty)

ConnectedComponents(graph $G$):
- for $i$ = 1 to $n$
- if $i$ not exploted
  - BFS($G$, $i$)

Running time also $O(n + m)$

## See also
- [Graphs](Graphs)
- [Graph Search](Graph_Search) и [Depth-First Search](Depth-First_Search)
- [Dijkstra's Shortest Path](Dijkstra's_Shortest_Path)


## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))
