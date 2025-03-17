---
title: Entropy-Based Ranking
layout: default
permalink: /index.php/Entropy-Based_Ranking
---

# Entropy-Based Ranking

## Entropy-Based Ranking


## Unsupervised Learning
Consider feature $F_i$ as  a Random Variable with a value $f_i$ 

Entropy is
- $H(F_1, \ ... \ , F_M) = - \sum_{f_1}  \ ... \ \sum_{f_M} p(f_1, \ ... \ , f_M) \log p(f_1, \ ... \ , f_M)$

When the data has well-formed clusters, the uncertainty is low so is the entropy.  
- In the real-world data, there are few cases that the clusters are well-formed.
- Two points belonging to the same cluster or 2 different clusters will contribute to the total entropy less that if they were uniformly separated. 
- Similarity $S_{ij}$ between two instances $X_i$ and $X_j$ is high if the 2 instance are very close and $S_{ij}$ is low if the 2 are far away. Entropy $H_{ij}$ will be low if $S_{ij}$ is either high or low, and $H_{ij}$ will be low otherwise.


We can measure the quality of a term $t$ by amount of [Entropy](Entropy) it removes when we prune $t$ 

$$H(t) = \sum_{i = 1}^n \sum_{j = 1}^n \Big[  S_{ij} \log S_{ij} + (1 - S_{ij}) \log (1 - S_{ij}) \Big] $$

where $S_{ij}$ is similarity between documents $i$ and $j$ when feature $f$ is removed 

$$S_{ij} = 2^{-\frac{\text{dist}(i, j)}{\text{avg.dist}}}$$

- $\text{dist}(i, j)$ distance between $i$ and $j$ when $t$ is removed 
- $\text{avg.dist}$ - average distance when 


But it's very slow: $O(n^2)$ for each $t$



## References
- Dash, Manoranjan, and Huan Liu. "Feature selection for clustering." 2000. [http://blog.finsternis.me/attachment/fk12.pdf]

## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- http://cs.gmu.edu/~carlotta/teaching/INFS-795-s05/readings/INFS795_MCayci.ppt


[Category:Dimensionality Reduction](Category_Dimensionality_Reduction)
[Category:Document Clustering](Category_Document_Clustering)