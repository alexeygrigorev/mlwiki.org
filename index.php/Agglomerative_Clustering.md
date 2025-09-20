---
layout: default
permalink: /index.php/Agglomerative_Clustering
tags:
- cluster-analysis
title: Agglomerative Clustering
---
<!-- stub -->

## Agglomerative Clustering
General concept: merge items into clusters based on distance/similarity 
- usually based on best pairwise similarity

Typical steps:
- at the beginning each document is a cluster on its own
- then we compute similarity between all pairs of clusters and store the results in a similarity matrix 
- merge two most similar clusters 
- update the similarity matrix 
- repeat until everything belongs to the same cluster 



## Linkage Types
How to join two clusters?
- Single Linkage (SLINK)
- Complete Linkage (CLINK)
- Group-Average Linkage


Suppose we have clusters $A, B, C, ...$ that we want to merge 

<!-- TODO: need more mathematical definitions -->

### Single Linkage
Merge two groups $A$ and $B$ based on their closest pair 


Implementation:
- compute all similarity pairs
- sort them in order of decrease
- process pairs in this order


advantage: 
- efficient to implement 
- equivalent to a Spanning Tree algo on the complete graph of pair-wise distances <!-- TODO: Link to Algo 2 from Coursera -->
- can use Prim's Spanning Tree algo |

Drawbacks 
- encourages chaining
  - similarity is usually not transitive: 
  - i.e. if $A$ is similar to $B$, and $B$ is similar to $C$, it doesn't mean that $A$ must be similar to $C$
  - but single linkage encourages grouping through transitivity chains


References:
- Sibson, Robin. "SLINK: an optimally efficient algorithm for the single-link cluster method." 1973. [http://www.cs.ucsb.edu/~veronika/MAE/SLINK_sibson.pdf]



### Complete Linkage
Worst-case similarity:
- avoids chaining altogether
- but it's very expensive computationally


References:
- Defays, Daniel. "An efficient algorithm for a complete link method." 1977. [http://comjnl.oxfordjournals.org/content/20/4/364.short]


### Group-Average Linkage
similarity between groups $A$ and $B$ are calculated as average similarity between each $a \in A$ and $b \in B$


- It's way slower than single linkage,
- but it's more robust: it doesn't show the chaining behavior


Speeding up:
- can approximate it by using the distance between centroids: mean doc in $A$ and mean doc in $B$ 



### Ward's Method
Merge the pair of clusters that minimizes the total within-group error (sum of squares) between each document and centroid 


Result:
- spherical tightly bound clusters 
- less sensitive to outliers

References:
- El-Hamdouchi, Abdelmoula, and Peter Willett. "Hierarchic document classification using Ward's clustering method." 1986. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.91.7722&rep=rep1&type=pdf]



### Pros and Cons
- Single-link algorithms are best for capturing clusters of different sizes and shapes 
- but it's also sensitive to noise 
- complete link and group average are not affected by noise, but have a bias towards finding global patterns

Computational complexity:
- only Single-Link is computationally possible for large datasets, but it doesn't give good results because uses too little information



## References
- Rasmussen, Edie M. "Clustering Algorithms." Information retrieval: data structures & algorithms 1992. [http://orion.lcg.ufrj.br/Dr.Dobbs/books/book5/chap16.htm]
- Voorhees, Ellen M. "Implementing agglomerative hierarchic clustering algorithms for use in document retrieval." 1986. [https://ecommons.library.cornell.edu/handle/1813/6605]


## Sources
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
- Oikonomakou, Nora, and Michalis Vazirgiannis. "A review of web document clustering approaches." Data mining and knowledge discovery handbook. 2010. [https://scholar.google.com/scholar?cluster=1261203777431390097&hl=ru&as_sdt=0,5]
