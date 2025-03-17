---
title: K-Medoids
layout: default
permalink: /index.php/K-Medoids
---

# K-Medoids

## K-Medoids
K-Medoids is a variation of [K-Means](K-Means) clustering algorithm 


Algorithm:
- use a set of points from the original data set as anchors ("medoids")
- then build clusters around them 
- each item is assigned to its closest representation from the data set 
- iterative approach 


Objective 
- $J$: average similarity of each item to its centroid


Disadvantages 
- require many iterations to converge
- so it's slow: it's slow to compute $J$
- doesn't always work well for sparse data
  - e.g. for text, not many docs have lots of terms in common
  - so similarities between such pairs are small and noisy
  - a single medoid may not contain all needed information to build a cluster around it



## Sources
- http://en.wikipedia.org/wiki/K-medoids
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]

[Category:Cluster Analysis](Category_Cluster_Analysis)