---
title: KNN
layout: default
permalink: /index.php/KNN
---

# KNN

{{stub}} {{draft}}

## $K$ Nearest Neighbors


KNN Graph
a graph that contains links only between $k$ closest neighborhoods 
used in 


## [Machine Learning](Machine_Learning) and [Statistics](Statistics)
Simple and popular method for many areas of machine learning, statistics and beyond


### [Regression Problem](Regression_Problem)



### [Classification Problem](Classification_Problem)



### [Cluster Analysis](Cluster_Analysis)
KNN approach is used in [SNN Clustering](SNN_Clustering)
- can use the number of shared neighbors as a similarity measure



### [Probability Density Estimation](Probability_Density_Estimation)
- If $k$th nearest neighbor is close, then the region is most likely of high density
- so the distance to $k$th neighbor gives a measure of density of a point
- can use it with [Euclidean Distance](Euclidean_Distance), [Cosine Similarity](Cosine_Similarity) or SNN Similarity (see [SNN Clustering](SNN_Clustering))



## [Curse of Dimensionality](Curse_of_Dimensionality)
Also note that for high dimensional data many distance/similarity measures become less meaningful 
- especially [Euclidean Distance](Euclidean_Distance)
- can use special functions that can handle high dimensional data: SNN Similarity (see [SNN Clustering](SNN_Clustering))


## Indexing for KNN Queries
Brute force search for $k$NN takes $O(N)$ where $N$ is the size of the database
- need to use [Multi-Dimensional Indexes](Multi-Dimensional_Indexes), for example, trees: [Kd-Trees](Kd-Trees) or [R-Tree](R-Tree)s
- however for high dimensional data tree performance degrades from $O(\log N)$ to $O(N)$
- see Weber98: all indexing techniques degrade to linear search for large dimensionality
- also can't use classical hash-based indexes (like [Linear Hashing](Linear_Hashing) or [Extensible Hashing](Extensible_Hashing)): they aim at exact match and don't handle KNN queries

Trees
- [Metric Trees](Metric_Trees)
- [Spill-Trees](Spill-Trees) gives approximate answer to KNN
- both don't work well in high dimensions, but can apply [Random Projections](Random_Projections) to make them work


Hashes:


### Dealing with High Dimensionality
How to deal with the [Curse of Dimensionality](Curse_of_Dimensionality)?

Pre-aggregating data:
- can use [Locality Sensitive Hashing](Locality_Sensitive_Hashing): probabilistic/approximate indexing techniques that return the true KNNs most of the time correctly  
- it would put data items into hash buckets, and when we look for KNN of $q$, we look into buckets where $q$ landed
- alternatively, can use [canopies](Canopy_Clustering)




## References
- Weber, Roger, Hans-Jörg Schek, and Stephen Blott. "A quantitative analysis and performance study for similarity-search methods in high-dimensional spaces." 1998. [http://www.vldb.org/conf/1998/p194.pdf]
- Nearest-Neighbor Methods in Learning and Vision: Theory and Practice [http://people.csail.mit.edu/gregory/annbook/book.html]

## Sources
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]


[Categories:Machine Learning](Categories_Machine_Learning)
[Categories:Statistics](Categories_Statistics)