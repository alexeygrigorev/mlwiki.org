---
title: "Graph Kernel"
layout: default
permalink: /index.php/Graph_Kernel
---

# Graph Kernel

## [Graph](Graph) Kernel
A ''kernel'' of a graph $K \subset V$ is ($V$ - all nodes of a graph)
- $\forall a \in K, \not \exists b: a \to b$
- : no alternative $a$ inside the kernel $K$ is better than any other alternative $b$ inside $K$
- $\forall c \not \in K, \exists a \in K: a \to c$
- : each alternative $c$ outside of the kernel $K$ is worse than at least one alternative $a$ inside $K$

For the example above:
- $K = \{b, d, e\}$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/mcda/electree-graph-kernel1.png" alt="Image">

Remarks:
- If the graph has no cycles then the kernel is unique 
- Each cycle can be replaced by a single node (see [Strongly Connected Components](Strongly_Connected_Components))



## Usage
- [ELECTRE](ELECTRE) methods of [MCDA](MCDA).


## Links
- http://en.wikipedia.org/wiki/Graph_kernel
- http://jmlr.org/papers/volume11/vishwanathan10a/vishwanathan10a.pdf

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- http://web.itu.edu.tr/~topcuil/ya/MDM08Outranking.pptx
- http://electre.no.sapo.pt/MElecI2.htm


[Category:Graphs](Category_Graphs)