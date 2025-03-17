---
title: Curse of Dimensionality
layout: default
permalink: /index.php/Curse_of_Dimensionality
---

# Curse of Dimensionality

## Curse of Dimensionality
In high dimensional space distances (esp. [Euclidean Distance](Euclidean_Distance)) become less meaningful
- distance between each pair of point is almost the same 
- for many data distributions and distances  


$$\lim_{d \to \infty} \frac{\text{dist}_\max - \text{dist}_\min}{\text{dist}_\min} = 0$$


- [Curse of Dimensionality](Curse_of_Dimensionality) makes similarity functions behave poorly
- [KNN](KNN) makes less sense
- distances become more uniform as dimensionality grows
- and this makes clustering difficult 

Similarity between two point of high dimensionality can be misleading
- often points may be similar even though they should belong to different clusters 


How to deal?
- [Dimensionality Reduction](Dimensionality_Reduction)
- [Subspace Clustering](Subspace_Clustering)


## Paper
- Beyer, Kevin, et al. "When is “nearest neighbor” meaningful?." 1999. [http://www.loria.fr/~berger/Enseignement/Master2/Exposes/beyer.pdf]
- Kriegel, Hans-Peter, Peer Kröger, and Arthur Zimek. "Clustering high-dimensional data: A survey on subspace clustering, pattern-based clustering, and correlation clustering." (2009) 

## Sources
- http://en.wikipedia.org/wiki/Curse_of_dimensionality
- http://en.wikipedia.org/wiki/Clustering_high-dimensional_data
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]

[Category:Distances](Category_Distances)