---
layout: default
permalink: /index.php/Scatter_Gather
tags:
- cluster-analysis
- document-clustering
title: Scatter/Gather
---
## Scatter/Gather
This is 
- use [Hierarchical Clustering](Hierarchical_Clustering) for seed selection, 
- k-means for clustering

Scatter/Gather is a variation of [K-Means](K-Means) used for [Document Clustering](Document_Clustering) with
- special seed selection
- usual k-means
- then several cluster refinement operations


Idea:
- use some hierarchical clustering algorithm on a sample to find good initial seeds
- use K-Means afterwards 


Notation:
- Let $k$ be the number of clusters we want to select and 
- $n$ the number of observations we want to cluster



## Seed Selection
### Buckshot
- sample $\sqrt{k \cdot n}$ observations
- use hierarchical clustering to get $k$ seeds from them 


### Fractionation
- break dataset into $n / m$ buckets of size $m > k$ each
- apply hierarchical clustering to each bucket and obtain $v$ clusters inside each bucket
- then merge all observations in these clusters (within each bucket) into one
- repeat till we have $k$ seeds 


Can do better than randomly grouping observations into buckets
- for document clustering: 
- try to group documents in such a way that documents inside buckets have common words
- e.g. sort docs by index of $j$th most common word in them, $j \approx 3$ corresponds to medium frequent word in a doc


## K-Means Step
After we did the seed selecting, we apply the usual k-means
- but, with a difference: the centroid is not a "mean" document
- centroid is a concatenation of words from all the documents in the cluster



## Cluster Refinement
After selecting seeds just do usual K-Means 
- but do some additional operations to improve quality for document clustering


Cluster refinement hypothesis:
- documents that belong to the same cluster in finer granularity will also occur in the same cluster in coarser granularity


### Split Operations
The main idea is to continue splitting after K-Means has finished
- sometimes clusters as not as granular as we'd like
- continue splitting them to refine clusters 
- don't need to apply it to all clusters - only to non-coherent ones
- it will help create more coherent clusters


Algo: 
- select a cluster to split
- apply buckshot with $k=2$ on this cluster
- re-cluster around these centers 


How to measure "coherence"?
- compute self-similarity of a cluster:
- similarity of documents to the centroid cluster
- or average pairwise similarity within the cluster
- apply split only to clusters with low self-similarity


### Join Operation
The idea:
- after K-means has finished,
- join very similar clusters into one 


How?
- compute typical words of each cluster: 
- i.e. examine most frequent words on the centroid
- two clusters are similar if there's significant overlap between words of these clusters 


## Challenges
- if there are many documents, the centroid will contain many word => leads to slowdown 
- solution: use [projection](Projection_onto_Subspaces) techniques like [PCA](PCA) 


## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Cutting, Douglass R., et al. "Scatter/gather: A cluster-based approach to browsing large document collections." 1992. [http://courses.washington.edu/info320/au11/readings/Week4.Cutting.et.al.1992.Scatter-Gather.pdf]
