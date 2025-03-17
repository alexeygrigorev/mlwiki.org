---
title: "DBSCAN"
layout: default
permalink: /index.php/DBSCAN
---

# DBSCAN

{{ stub  }}

## DBSCAN
It's a density-based clustering algorithm


Density associated with a point is obtained by counting the number of points in a region of specified radius $\epsilon$ around each point 
- points with density $\geqslant \text{min_pts}$ are considered as "core points"
- noise and non-core points are discarded 
- clusters are formed around the core points 
- if two core points are within a radius $\epsilon$, then they belong to the same cluster



Disadvantages
- can find clusters of different shapes, but can't find clusters of different densities


## Extensions
### [SNN Clustering](SNN_Clustering)
- an extension of DBSCAN that words better for high-dimensional data
- also can find clusters of different density


## References
- Ester, Martin, et al. "A density-based algorithm for discovering clusters in large spatial databases with noise." 1996. [http://www.aaai.org/Papers/KDD/1996/KDD96-037]

## Sources
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]

[Category:Cluster Analysis](Category_Cluster_Analysis)