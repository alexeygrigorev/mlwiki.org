---
title: "Graph Search"
layout: default
permalink: /index.php/Graph_Search
---

# Graph Search

## Graph Search
Motivation: Given a [graph](Graphs)
- check if network is connected (get from $A$ to $B$)
- find best driving directions (shortest path)
- etc etc

Search:
- find everything findable from a given vertex $s$
- don't explore anything twice
- goal: $O(n+m)$

## Algorithm
GenericAlgorithm(graph $G$, starting vertex $s$):
- initially only $s$ is explored
- while possible
  - choose an edge $(u, v)$ with $u$ explored and $v$ unexplored
  - mark $v$ explored
- if at the end $v$ is explored, there is a path from $s$ to $v$

## Concrete algorithms
- [Breadth-First Search](Breadth-First_Search) 
- [Depth-First Search](Depth-First_Search)
- [Dijkstra's Shortest Path](Dijkstra's_Shortest_Path)

## See also
- [Graphs](Graphs)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))

[Category:Algorithms](Category_Algorithms)
[Category:Graphs](Category_Graphs)