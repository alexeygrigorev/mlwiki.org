---
title: "CURE Clustering"
layout: default
permalink: /index.php/CURE_Clustering
---

# CURE Clustering

{{ stub }}

## CURE Algorithm for Clustering
Use a set of representative points to find non-global clusters 
- these points capture the geometry and shape of clusters 

{{ TODO |  see [Scalable Data Analytics and Data Mining AIM3 (TUB)](Scalable_Data_Analytics_and_Data_Mining_AIM3_(TUB)) lectures }} |

Choose points
- 2 farthest away points
- 3 and so on - furthest away from previous ones
- this procedure guarantees that the points are well distributed 

Then shrink the points towards the centroids by factor of $\alpha$ 


CURE eliminates outliers by discarding small slowly growing clusters 
- but it has a notion of center - not all shapes has natural center


== References == 
- Guha, Sudipto, Rajeev Rastogi, and Kyuseok Shim. "Cure: an efficient clustering algorithm for large databases." (2001) [http://www.cs.sfu.ca/CourseCentral/459/han/papers/guha98.pdf]

## Sources
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
- http://en.wikipedia.org/wiki/CURE_data_clustering_algorithm

[Category:Cluster Analysis](Category_Cluster_Analysis)