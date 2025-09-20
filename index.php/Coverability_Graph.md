---
layout: default
permalink: /index.php/Coverability_Graph
tags:
- business-process-management
- graphs
- petri-nets
title: Coverability Graph
---
## Coverability Graph
This is a way of representing states of workflows, similar to [Reachability Graph](Reachability_Graph)


### Motivation
Consider the following [YAWL](YAWL) flow:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-unboundness.png" alt="Image">.
- because of the [Cancellation Regions](Cancellation_Regions) the [Reachability Graph](Reachability_Graph) of this workflow becomes infinitely large
- it is possible to know when we need to stop expanding it?
  - if there was no Cancellation Region, it would be enough just to repeat it 2 times to see that there's no proper termination
  - but in this case we don't know when to stop 
- $\Rightarrow$ can no longer use it for checking for [Workflow Soundness](Workflow_Soundness)


However there is a concept of Coverability Graphs that are 
- computationally less expensive
- can still be used to decide on some properties


### Coverability
Let's consider the following [Petri Net](Petri_Nets):
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-coverability-ex.png" alt="Image">
- how we can represent $\infty$ many nodes in this reachability graph? 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-coverability-ex-reach.png" alt="Image">
- note that marking $[p_1, p_3] < [p_1]$ - strictly larger 
  - thus with marking $[p_1, p_3]$ the petri net can do all the same as $[p_1]$ plus a little bit more
- so if it's possible to get from one marking $M_1$ to another marking $M_2$ s.t. $M_2$ covers $M_1$ completely - then we have a loop 


''Coverability'':
- marking $M$ is ''coverable'' by $M'$ $\iff$
- there $\exists$ a marking $M'$ s.t. $M \to^* M'$ and $M \leqslant M'$


Let's construct the coverability graph for this example
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-coverability-ex-reach2.png" alt="Image">
- look at all the nodes that you can reach
- if you notice some marking that covers another marking, add a loop to the coverability graph
- <img src="<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-coverability-ex-с.png" alt="Image">" />
- note that this graph is finite 
- and we can see that in this graph we do have the option to complete 


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))
