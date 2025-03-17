---
title: Depth-First Search
layout: default
permalink: /index.php/Depth-First_Search
---

# Depth-First Search

## Depth-First Search
A [Graph Search](Graph_Search) algorithm:
- explore aggressively, backtrack only if needed
- uses FILO / recursion

## Algorithm
DFS(graph $G$, start vertex $s$):
- mark $s$ as explored
- for every edge $(s, v)$
  - if $v$ is unexplored
  - DFS($G$, $v$)

running time $O(n + m)$

## DFS applications
- [Connected components](Breadth-First_Search#Connected_Components) like with [Breadth-First Search](Breadth-First_Search)
- [Topological Ordering](Topological_Ordering)
- [Strongly Connected Components](Strongly_Connected_Components)

## See also
- [Graphs](Graphs)
- [Graph Search](Graph_Search) и [Breadth-First Search](Breadth-First_Search)
- [Dijkstra's Shortest Path](Dijkstra's_Shortest_Path)


## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))

[Category:Algorithms](Category_Algorithms)
[Category:Graphs](Category_Graphs)