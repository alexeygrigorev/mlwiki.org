---
title: Probabilistic LSA
layout: default
permalink: /index.php/Probabilistic_LSA
---

# Probabilistic LSA

{{stub}}

## Probabilistic LSA
This is a probabilistic extension to [Latent Semantic Analysis](Latent_Semantic_Analysis)
- it's a part of [Topic Models](Topic_Models)


### Problem
Notation and problem:
- $D_1, \ ... \ , D_n$ are documents
- $T_1, \ ... \ , T_k$ are topics (sort of "clusters")
- each document may belong to several topics - so these "clusters" are [Fuzzy](Fuzzy_Clustering)
- probability of $D_i$ belonging to $T_j$ is $P(T_j \mid D_i)$
- but cluster membership is secondary in this problem
- the main problem is to find latent topics that generated documents - which is why it's called Topic Modeling 
- let $t_1, \ ... \ , t_d$ be $d$ terms from the lexicon
- then the probability that $t_l$ occurs in $T_j$ is $P(t_l \mid T_j)$


### Learning
Thus, we need to estimate the following probabilities:
- $P(T_j \mid D_i)$ and $P(t_l \mid T_j)$
- usually parameters are learned via maximum likelihood methods like [Expectation Maximization](Expectation_Maximization)


We need to learn $P(T_j \mid D_i)$ and $P(t_l \mid T_j)$
- $P(t_l \mid D_i)$ can be expressed via them:
- $P(t_l \mid D_i) = \sum\limits_{j=1}^k p(t_l \mid T_i) \, P(T_j \mid D_i)$
- thus, for each $t_l$ and $D_i$ we can generate $n \times d$ matrix of probabilities 
- these probabilities are learned from term-document matrix $X$: $X_{il}$ is # of times $t_l$ occurred in $D_i$ 
- so we can use [Maximum Likelihood Estimator](Maximum_Likelihood_Estimator) to maximize the product of probabilities of terms we observed 


Optimization:
- we will optimize the log likelihood $\sum_{i,l} X_{il} \cdot \log P(t_l, D_i)$
- s.t. $\sum_l P(t_l \mid T_j) = 1$ for all $T_j$ and $\sum_j P(T_j \mid D_i) = 1$ for all $D_i$
- can use [Lagrange Multipliers](Lagrange_Multipliers) for this


## [Latent Dirichlet Allocation](Latent_Dirichlet_Allocation)
is an extension of Probabilistic LSA
- model term-topic probabilities and topic-document probabilities with [Dirichlet Distribution](Dirichlet_Distribution)
- so LDA is a Bayesian version of PLSA
- but LSA overfits less than PLSA because it has less parameters to fit


## References
- Hofmann, Thomas. "Probabilistic latent semantic analysis." 1999. [http://arxiv.org/ftp/arxiv/papers/1301/1301.6705.pdf]

## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]


[Category:Topic Models](Category_Topic_Models)