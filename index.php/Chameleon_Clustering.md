---
layout: default
permalink: /index.php/Chameleon_Clustering
tags:
- cluster-analysis
title: Chameleon Clustering
---
<!-- stub -->

## Chameleon Clustering
Combines initial partition of data with hierarchical clustering techniques 
it modifies clusters dynamically

Step1: 
- Generate a [KNN](KNN) graph
- because it's local, it reduces influence of noise and outliers
- provides automatic adjustment for densities


Step2:
- use METIS: a graph partitioning algorithm 
- get equally-sized groups of well-connected vertices 
- this produces "sub-clusters" - something that is a part of true clusters


Step3:
- recombine sub-clusters 
- combine two clusters if
  - they are relatively close
  - they are relatively interconnected 
- so they are merged only if the new cluster will be similar to the original ones 
- i.e. when "self-similarity" is preserved (similar to the join operation in [Scatter/Gather](Scatter_Gather))


But 
- [Curse of Dimensionality](Curse_of_Dimensionality) makes similarity functions behave poorly
- distances become more uniform as dimensionality grows
- and this makes clustering difficult 

Similarity between two point of high dimensionality can be misleading
- often points may be similar even though they should belong to different clusters 


Solutions:
- [ROCK Clustering](ROCK_Clustering)
- [SNN Clustering](SNN_Clustering): also use [KNN](KNN)


== References == 
- Karypis, George, Eui-Hong Han, and Vipin Kumar. "Chameleon: Hierarchical clustering using dynamic modeling." (1999). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.44.5847&rep=rep1&type=pdf]

## Sources
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
