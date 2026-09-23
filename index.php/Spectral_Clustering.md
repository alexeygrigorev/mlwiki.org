---
layout: default
permalink: /Spectral_Clustering
tags:
- cluster-analysis
- machine-learning
title: Spectral Clustering
---

## Spectral Clustering

[Spectral Clustering](Spectral_Clustering)
- apply [Graph Partitioning](Graph_Partitioning) but in some high-dimensional space
- usually involves computing [Singular Values and Vectors](SVD) / [Eigenvalues and Eigenvectors](Eigenvalues_and_Eigenvectors) of the graph affinity matrix
- usually has global optimum

Criteria: 
- Average Cut, 
  - Chan, Pak K., Martine DF Schlag, and Jason Y. Zien. "Spectral k-way ratio-cut partitioning and clustering." 1994. [http://homes.esat.kuleuven.be/~sdeboeck/Ratio_Cut_Partitioning.pdf]
- Average Association,
- Normalized Cut,  
  - Shi, Jianbo, and Jitendra Malik. "Normalized cuts and image segmentation." 2000. [http://repository.upenn.edu/cgi/viewcontent.cgi?article=1101&context=cis_papers]
- Min-Max Cut, 
  - Ding, Chris HQ, et al. "A min-max cut algorithm for graph partitioning and data clustering." 2001. [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.454.9484&rep=rep1&type=pdf] 
  - Ding, Chris, et al. "Spectral min-max cut for graph partitioning and data clustering." 2001. [https://publications.lbl.gov/islandora/object/ir%3A117369/datastream/PDF/download/citation.pdf]

- when applied to [documents](Document_Clustering), under certain conditions resulting eigenspaces are equivalent to semantic spaces found by [Latent Semantic Analysis](Latent_Semantic_Analysis) 
- but also like in LSA, usually found directions don't correspond to clusters directly, need to do additional clustering afterwards (e.g. by [K-Means](K-Means))
