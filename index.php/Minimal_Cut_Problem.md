---
title: "Minimal Cut Problem"
layout: default
permalink: /index.php/Minimal_Cut_Problem
---

# Minimal Cut Problem

## Minimal Cut Problem
A ''cut'' in a [graph](Graphs) is a partition of vertices $V$ into two non-empty subsets $A$ and $B$

<img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/31fvn7e3gpg82523n3cguh1sua.png" alt="Image">" \>

A ''crossing edges'' is an edge that
- has one end point in each of $(A, B)$
- has tail in $A$, head in $B$ (directed)
- if head in $B$, tail in $A$ - not a crossing edge

## The problem
- input: indirect [graph](Graphs) $G = (V, E)$ with parallel edges allowed
- goal: compute a cut with fewer number of crossing edges (the min cut)

Eg:

<img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/44dvh9gbo78ljnt0tmds5rv618.png" alt="Image">" \>

## Applications
- identify weakness/bottlenecks
- detect communities
- image segregation

## Random Contraction Algorithm

MinCut algo:
- while there are more than 2 vertices
- pick a remaining edge $(u, v)$ at random
- merge (contract) $u$ and $v$ into a single vertex
- remove self-loogs
- return 2 final vertices


Example:
- step 1 <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/3lf26679cst0jm7hsug5h1hef2.png" alt="Image">" \>
- step 2 <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/3rdg1jgvkna7mtb0gnu00vbkdg.png" alt="Image">" \>
- step 3 <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/7j8r5op0949ctu5jmq03c1uf0m.png" alt="Image">" \>
- result <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/5eoumts8f24v0ifjebqgjsumjr.png" alt="Image">" \>

Example 2:
- <img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/15f4s9iuk97l9qvnt171bqc904.png" alt="Image">" \>

It can find something other than a minimal cut|   |- the probability of success is just $\cfrac{1}{n^2}$|  |- solution: repeated trials |- try $N$ times and remember the smallest cut found


How many trials we need?
- probability that all trials fail is $(1 - \cfrac{1}{n^2}) ^ N$
- if $N = n^2 \log n$, $Pr[\text{all fail}] = \frac{1}{n}$
- running time: $\Omega(n^2 m)$
- TODO: link to proof


### Implementation
```java
public class MinCutProblem {
    private UndirectedGraph graph;
    private UndirectedGraph initialGraphCopy;
    private int best;

    public void run() {
        graph = readGraph();
        initialGraphCopy = graph.copy();
        best = Integer.MAX_VALUE;

        int trials = 25;

        while (trials > 0) {
            iteration();
            graph = initialGraphCopy.copy();
            trials--;
        }

        out.println(best);
    }

    private void iteration() {
        while (graph.getN() > 2) {
            Pair<Integer, Integer> randomVertex = graph.randomEdge();
            graph.contract(randomVertex.getLeft(), randomVertex.getRight());
        }

        Map<Integer, List<Integer>> adjacencyList = graph.adjacencyList();

        Iterator<Entry<Integer, List<Integer>>> iterator = adjacencyList.entrySet().iterator();
        List<Integer> first = iterator.next().getValue();
        List<Integer> second = iterator.next().getValue();

        if (best > first.size()) {
            best = first.size();
        }
    }
}
```

```java
public class UndirectedGraph {
    private int n;
    private final Map<Integer, List<Integer>> adj;
    private final Random random = new Random();

    public UndirectedGraph(int n) {
        this.n = n;
        this.adj = createAdjacentList(n);
    }

    private static Map<Integer, List<Integer>> createAdjacentList(int n) {
        Map<Integer, List<Integer>> res = new LinkedHashMap<Integer, List<Integer>>();

        int i = 0;
        while (i < n) {
            res.put(i, new ArrayList<Integer>());
            i++;
        }

        return res;
    }

    private UndirectedGraph(UndirectedGraph copy) {
        this.n = copy.n;
        this.adj = new LinkedHashMap<Integer, List<Integer>>();
        
        for (Entry<Integer, List<Integer>> entry : copy.adj.entrySet()) {
            adj.put(entry.getKey(), new ArrayList<Integer>(entry.getValue()));
        }
    }
    
    public UndirectedGraph copy() {
        return new UndirectedGraph(this);
    }

    public void contract(int v, int u) {
        List<Integer> newList = new ArrayList<Integer>();

        for (int fromFirst : adj.get(v)) {
            if (fromFirst |  = u) { |                newList.add(fromFirst); |            }
        }

        for (int fromSecond : adj.get(u)) {
            if (fromSecond |  = v) { |                newList.add(fromSecond); |            }
        }

        adj.remove(v);
        adj.remove(u);
        n--;

        // updating the graph so 'u' now will point to 'v'
        for (Entry<Integer, List<Integer>> entry : adj.entrySet()) {
            List<Integer> row = entry.getValue();
            for (int i = 0; i < row.size(); i++) {
                if (row.get(i).intValue() == u) {
                    row.set(i, v);
                }
            }
        }

        // and keeping only 'v'
        adj.put(v, newList);
    }

    public void addEdge(int v, int u) {
        adj.get(v).add(u);
    }

    public Iterable<Integer> adjacentTo(int v) {
        if (|  adj.containsKey(v)) { |            throw new IllegalArgumentException(v + " is already removed"); |        }
        return adj.get(v);
    }

    // TODO may be implemented more efficiently
    public Pair<Integer, Integer> randomEdge() {
        int[] available = new int[n];

        int j = 0;
        for (Entry<Integer, List<Integer>> entry : adj.entrySet()) {
            if (|  entry.getValue().isEmpty()) { |                available[j] = entry.getKey(); |                j++;
            }
        }

        int vertexU = available[random.nextInt(j)];
        List<Integer> edges = adj.get(vertexU);
        int vertexV = edges.get(random.nextInt(edges.size()));
        return Pair.of(vertexU, vertexV);
    }

    public Map<Integer, List<Integer>> adjacencyList() {
        return ImmutableMap.copyOf(adj);
    }
    
    public int getN() {
        return n;
    }
}
```

## See also
- [Graphs](Graphs)

## Sources
- [Algorithms Design and Analysis Part 1 (coursera)](Algorithms_Design_and_Analysis_Part_1_(coursera))

[Category:Algorithms](Category_Algorithms)
[Category:Graphs](Category_Graphs)