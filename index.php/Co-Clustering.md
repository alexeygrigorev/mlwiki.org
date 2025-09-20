---
layout: default
permalink: /index.php/Co-Clustering
tags:
- document-clustering
title: Co-Clustering
---
{{stub}}

## Co-Clustering
Co-clustering is a set of techniques in [Cluster Analysis](Cluster_Analysis)
- given some matrix $A$ we want to cluster rows of $A$ and columns of $A$ simultaneously 
- this is a common task for ''dyadic'' data matrices such as [term-document matrices](Vector_Space_Models) or [user-item matrices](Collaborative_Filtering)


Co-clustering is also called bi-clustering 
- let $A$ be  $m \times n$ matrix, 
- goal is to generate biclusters/co-clusters: a subset of rows which exhibit similar behavior across a subset of columns, or vice versa.



Co-clustering is defined as two map functions:
- rows -> row cluster indexes
- columns -> column cluster indexes 
- these map functions are learned simultaneously
- Unlike [Two-Phase Document Clustering](Two-Phase_Document_Clustering) where we first cluster columns and then we use this to cluster rows


### [Subspace Clustering](Subspace_Clustering)
Can use subspace clustering for co-clustering
- subspace clustering $\approx$ local feature selection



## [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization)
One way of doing Co-Clustering is via NMF:
- let $A = UV^T$ where $U$ is $m \times k$ and $V$ is $n \times k$
- then rows of $U$ may correspond to clusters of rows, and rows of $V$ to clusters of columns



## References
- Dhillon, Inderjit S. "Co-clustering documents and words using bipartite spectral graph partitioning." 2001. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.20.9634&rep=rep1&type=pdf]
- Dhillon, Inderjit S., Subramanyam Mallela, and Dharmendra S. Modha. "Information-theoretic co-clustering." 2003. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.6173&rep=rep1&type=pdf]
- Li, Tao, Sheng Ma, and Mitsunori Ogihara. "Document clustering via adaptive subspace iteration."  2004. [http://users.cs.fiu.edu/~taoli/pub/sigir04-p218-li.pdf]

## Sources
- http://en.wikipedia.org/wiki/Biclustering
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
