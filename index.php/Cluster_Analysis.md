---
layout: default
permalink: /index.php/Cluster_Analysis
tags:
- cluster-analysis
- machine-learning
- unsupervised-learning
title: Cluster Analysis
---
## Cluster Analysis
Clustering is about finding groups of similar objects in the data

How do we define similar? 
- we measure with some similarity/distance function 


Application of Clustering
- Customer Segmentation
- Clustering for Classification
- Collaborative Filtering
- Visualization
- Document organization and indexing 



[Similarity measures](Similarity_Functions) and [Distances](Distance_Functions):
- [Euclidean Distance](Euclidean_Distance)
- [Jaccard Coefficient](Jaccard_Coefficient)
- [Dot Product](Dot_Product)
- [Cosine Similarity](Cosine_Similarity)



## One-Sided Clustering
### Partitioning Clustering
Idea: 
- decompose dataset into $k$ disjoint classes 
- s.t. each item belongs to exactly one class 


Algorithms:
- [K-Means](K-Means) and variants like [K-Medoids](K-Medoids)
- [CURE Clustering](CURE_Clustering)


### [Hierarchical Clustering](Hierarchical_Clustering)
Idea:
- build a tree

Main approaches:
- [Agglomerative Clustering](Agglomerative_Clustering)
  - at the beginning everything is a cluster on its own
  - merge till have one big cluster
- [Divisive Clustering](Divisive_Clustering)
  - at the beginning everything belongs to one big cluster
  - split clusters until everything is a cluster on its own


Others:
- [Chameleon Clustering](Chameleon_Clustering)


### Density-Based
Cluster neighborhood groups based on some density conditions
- [DBSCAN](DBSCAN)
- [SNN Clustering](SNN_Clustering) extension of DBSCAN with notion of similarity based on [$k$-nearest neighbors](KNN)


### Grid-Based
Partition space into finite number of cells and perform clustering there



## Other Types
### Graph-Based Clustering
apply [Graph Partitioning](Graph_Partitioning) Algorithms: 
- identify clusters by cutting edges from the graph 
- s.t. the sum of cuts is minimal 
- for example, [Minimal Cut Algorithm](Minimal_Cut_Algorithm)

Algorithms:
- [Chameleon Clustering](Chameleon_Clustering)


[Spectral Clustering](Spectral_Clustering)
- apply [Graph Partitioning](Graph_Partitioning) but in some high-dimensional space
- usually involves computing [Singular Values and Vectors](SVD) / [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors) of the graph affinity matrix
- usually has global optimum
- criteria: Average Cut, Average Association, Normalized Cut, Min-Max Cut
- when applied to [documents](Document_Clustering), under certain conditions resulting eigenspaces are equivalent to semantic spaces found by [Latent Semantic Analysis](Latent_Semantic_Analysis) 
- but also like in LSA, usually found directions don't correspond to clusters directly, need to do additional clustering afterwards (e.g. by [K-Means](K-Means))


Link-Based Clustering
- can use Web-graph techniques 
- [PageRang](PageRang) and [HITS](HITS) are used for Ranking
- see Oikonomakou2010


### [Neural Networks](Neural_Networks) Based
Called [Self-Organized Maps](Self-Organized_Maps)

Build a Neural Network with 2 layers:
- input layers: $n$ input nodes 
- output: $k$ nodes: decision regions


Objective we want to maximize:
- within-region similarities of items 


References:
- https://en.wikipedia.org/wiki/Self-organizing_map



### [Fuzzy Clustering](Fuzzy_Clustering)
sometimes also called "Soft Clustering"
- Usually clustering is "exclusive": the clustering algorithms assigns each object strictly to cluster
- but we can remove this restriction and modify the membership function s.t. an object can belong to several clusters
- so In this type of clustering a data point may belong to several clusters


Membership function
- computes for each object and for each cluster returns the degree of membership
- modification of K-Means: [Fuzzy C-Means](Fuzzy_C-Means)
- degree of membership to the cluster in C-Means depends on the distance from the document to the cluster centroid


Others:
- clustering via [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization) can be fuzzy
- also, Looney, Carl G. "A fuzzy clustering and fuzzy merging algorithm." 1999. [https://www.researchgate.net/publication/2467319_A_Fuzzy_Clustering_and_Fuzzy_Merging_Algorithm]



### [Probabilistic Clustering](Probabilistic_Clustering)
Membership function outputs probabilities of an item belonging to a cluster


Algorithms:
- [Finite Mixture Modeling](Finite_Mixture_Modeling)
- [Expectation Maximization](Expectation_Maximization) (with [Gaussian Mixture Models](Gaussian_Mixture_Models))



### [Co-Clustering](Co-Clustering)
One-sided clustering is clustering only rows of data matrix $D$
- co-clustering: clustering both rows and columns at the same time


Algorithms
- clustering via [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization) can be viewed as clustering both columns and rows


### [Subspace Clustering](Subspace_Clustering)
Subspace clustering:
- it's the task of detecting all clusters  in all subspaces 
- a data point may belong to many different clusters - with each cluster in some subspace 



## Sources
- http://en.wikipedia.org/wiki/Cluster_analysis
- Jing, Liping. "Survey of text clustering." (2008). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.3476&rep=rep1&type=pdf]
- Oikonomakou, Nora, and Michalis Vazirgiannis. "A review of web document clustering approaches." Data mining and knowledge discovery handbook. 2010. [https://scholar.google.com/scholar?cluster=1261203777431390097&hl=ru&as_sdt=0,5]
- Xu, Wei, Xin Liu, and Yihong Gong. "Document clustering based on non-negative matrix factorization." 2003. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.117.2293&rep=rep1&type=pdf]
