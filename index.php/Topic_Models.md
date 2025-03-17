---
title: Topic Models
layout: default
permalink: /index.php/Topic_Models
---

# Topic Models

{{stub}}

## Topic Models
Topic models is a probabilistic approach to [Document Clustering](Document_Clustering):
- create a probabilistic generative model for text documents
- represent corpus as a function of hidden variables 


Notation and problem:
- $D_1, \ ... \ , D_n$ are documents
- $T_1, \ ... \ , T_k$ are topics (sort of "clusters")
- each document may belong to several topics - so these "clusters" are [Fuzzy](Fuzzy_Clustering)
- probability of $D_i$ belonging to $T_j$ is $P(T_j \mid D_i)$
- but cluster membership is secondary in this problem
- the main problem is to find latent topics that generated documents - which is why it's called Topic Modeling 
- let $t_1, \ ... \ , t_d$ be $d$ terms from the lexicon
- then the probability that $t_l$ occurs in $T_j$ is $P(t_l \mid T_j)$


Thus, we need to estimate the following probabilities:
- $P(T_j \mid D_i)$ and $P(t_l \mid T_j)$
- usually parameters are learned via maximum likelihood methods like [Expectation Maximization](Expectation_Maximization)


There are two types of Topic Modeling techniques:
- [Probabilistic LSA](Probabilistic_LSA)
- [Latent Dirichlet Allocation](Latent_Dirichlet_Allocation)


## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]


[Category:Topic Models](Category_Topic_Models)
[Category:Document Clustering](Category_Document_Clustering)