---
title: "Graphs"
layout: default
permalink: /index.php/Graphs
---

# Graphs

## Graphs

Consist of:
- vertices aka nodes ($V$)
- $n$ = number of vertices
- edges ($E$) = pair of vertices
- $m$ - number of edges

- can be ''undirected'' <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/29btqo4e5smcg6v9l29a0k7i8u.png" alt="Image">" \>
- or ''directed'' <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/37ijdgf2d7dri4jkv2fpbrouea.png" alt="Image">" \>


## Directed Acyclic Graph
This is a special kind of graph where
- there are no cycles
- and it is directed

These graphs can be [sorted topologically](Topological_Ordering)


## Representation
### adjacency matrix
- $n \times n$ matrix where 
- $A_{i,j} = 1$ if $G$ has $(i, j)$ edge
- or $+1$/$-1$ if directed
- or weight if weighted
- space required $\Theta(n^2)$

### adjacency list
- array of vertices
- array of edges for each vertex
- space required $\Theta(n + m)$

## Implementation
Adjacency list:
```java
public class Graph {
    private int n;
    private final List<List<Integer>> adj;

    public Graph(int n) {
        this.n = n;
        this.adj = createAdjacentList(n);
    }

    private static List<List<Integer>> createAdjacentList(int n) {
        List<List<Integer>> res = new ArrayList<List<Integer>>(n);

        int i = 0;
        while (i < n) {
            res.add(new LinkedList<Integer>());
            i++;
        }

        return res;
    }

    public void addEdge(int v, int u) {
        adj.get(v).add(u);
    }

    public Iterable<Integer> adjacent(int v) {
        return adj.get(v);
    }

    public int getN() {
        return n;
    }
}
```


## See also
- [Minimal Cut Problem](Minimal_Cut_Problem)
- [Graph Search](Graph_Search) ([Breadth-First Search](Breadth-First_Search) и [Depth-First Search](Depth-First_Search))
- [Dijkstra's Shortest Path](Dijkstra's_Shortest_Path)
- [Topological Ordering](Topological_Ordering)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))

[Category:Algorithms](Category_Algorithms)
[Category:Graphs](Category_Graphs)