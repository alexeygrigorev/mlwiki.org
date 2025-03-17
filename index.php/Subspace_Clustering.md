---
title: "Subspace Clustering"
layout: default
permalink: /index.php/Subspace_Clustering
---

# Subspace Clustering

{{stub}}

## Subspace Clustering
Textual data (esp in [Vector Space Models](Vector_Space_Models)) suffers from the [Curse of Dimensionality](Curse_of_Dimensionality)
- so need to use [Dimensionality Reduction](Dimensionality_Reduction)


But often we can use the following idea:
- correlation in high-dimensional data is usually local (esp. in [text data](Text_Mining))
- for some data items features are correlated, but for some the same features are not


Subspace clustering:
- it's the task of detecting all clusters  in all subspaces 
- a data point may belong to many different clusters - with each cluster in some subspace 



Survey paper:
- Parsons, Lance, Ehtesham Haque, and Huan Liu. "Subspace clustering for high dimensional data: a review." (2004). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.85.8962&rep=rep1&type=pdf]
- Domeniconi, Carlotta, et al. "Subspace Clustering of High Dimensional Data." SDM. Vol. 73. 2004. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.107.8676&rep=rep1&type=pdf]


There are two types of subspace clustering
- based on how they determine a measure of locality for evaluating subspaces
- bottom-up subspace search 
- top-down search


### Bottom-up Subspace Search
Use downward closure property for density to reduce the search space ([Apriori](Apriori)-style)


CLIQUE:
- Agrawal, Rakesh, et al. Automatic subspace clustering of high dimensional data for data mining applications.1998. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.407.4066&rep=rep1&type=pdf]

ENCLUS
- Cheng, Chun-Hung, Ada Waichee Fu, and Yi Zhang. "Entropy-based subspace clustering for mining numerical data." 1999. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.33.1465&rep=rep1&type=pdf]

MAFIA 
- Goil, Sanjay, Harsha Nagesh, and Alok Choudhary. "MAFIA: Efficient and scalable subspace clustering for very large data sets." 1999. [http://www.cs.upc.edu/~bejar/amlt/material_art/DM%20clustering%20goil99mafia.pdf]

CBF
- Chang, Jae-Woo, and Du-Seok Jin. "A new cell-based clustering method for large, high-dimensional data in data mining applications.", 2002. [http://www.researchgate.net/profile/Jae-Woo_Chang2/publication/221001126_A_new_cell-based_clustering_method_for_large_high-dimensional_data_in_data_mining_applications/links/02e7e519c25a68e567000000.pdf]

CLTree
- clustering via decision trees 

DOC
- Procopiuc, Cecilia M., et al. "A Monte Carlo algorithm for fast projective clustering." 2002. [http://www.cs.duke.edu/~pankaj/publications/papers/proj-cluster-sample.pdf]


### Iterative Top-Down Subspace Search
PROCLUS 
- Aggarwal, Charu C., et al. "Fast algorithms for projected clustering." 1999. [http://dbs.informatik.uni-halle.de/Lehre/Aktiv_2000/Paper/aggarwal_sigmod99.pdf]

ORCLUS
- Aggarwal, Charu C., and Philip S. Yu. Finding generalized projected clusters in high dimensional spaces. 2000. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.23.5160&rep=rep1&type=pdf]

FINDIT 
- Woo, Kyoung-Gu, et al. "FINDIT: a fast and intelligent subspace clustering algorithm using dimension voting." (2004). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.108.5164&rep=rep1&type=pdf]

$\beta$-Clusters 
- Yang, Jiong, et al. "δ-clusters: Capturing subspace correlation in a large data set." 2002. [http://ftp.it.murdoch.edu.au/units/ICT219/Papers%20for%20transfer/papers%20on%20Clustering/delta%20clusers.pdf]

COSA
- Friedman, Jerome H., and Jacqueline J. Meulman. "Clustering objects on subsets of attributes (with discussion)." (2004). [http://www.datatheory.nl/pages/Friedman%26Meulman.pdf]



## Document Subspace Clustering
Text data is very high-dimensional 
- creates problems for [Document Clustering](Document_Clustering)


Adaptive subspace iteration:
- reduce data
- identify subspaces


## Sources
- Jing, Liping. "Survey of text clustering." (2008). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.3476&rep=rep1&type=pdf]
- http://en.wikipedia.org/wiki/Clustering_high-dimensional_data

[Category:Cluster Analysis](Category_Cluster_Analysis)