---
title: Probabilistic Retrieval Model
layout: default
permalink: /index.php/Probabilistic_Retrieval_Model
---

# Probabilistic Retrieval Model

## Probabilistic Retrieval Model
### Probabilistic Ranking Principle
Due to Robertson 1977
- relevance = "what is the probability that document $D$ is relevant to the query $Q$?"


### Assumptions
- '''ranking assumption''': usefulness of a relevant document depends on the number of relevant documents the user has already seen
  - the more documents we see - the less useful they are 
- '''independence assumption''': relevance of $D_i$ to $Q$ is independent to other documents $D_j$ from the collection
  - therefore we can apply it for each document separately



## Relevance Function
- $R = \{ r, \lnot r \}$ a binary random variable that indicates relevance
- let $r$ represent the event that $D$ is relevant 
- $\lnot r$ represent the event that $D$ is not relevant 


We need estimate the probability of relevance of a document $D$ w.r.t a query $Q$ 
- Need to find:
- $P(R = r \mid D, Q)$ - prob that $D$ is relevant to $Q$
- $P(R = \lnot r \mid D, Q)$ - prob that $D$ is not relevant to $Q$
- So we need to estimate (learn) $P(R \mid D, Q)$



### [Descriptive Model](Descriptive_Models) Approach
Sometimes referred as a "[Machine Learning](Machine_Learning)" approach

It then becomes a Classification Problem:
- can learn $P(R \mid D, Q)$ with a [Descriptive Model](Descriptive_Models)
- $R$ depends on features that characterize the relationships between $D$ and $Q$ 
- for example, # of matched terms

Suppose 
- we have $k$ features $F_i(Q, D)$
- $f$ is a function with parameter $\Lambda$ s.t. $f(F_1, \ ... \ , F_k, \Lambda) = P(R \mid D, Q)$ 
- then can fit $f$ with some ML algorithm e.g. [OLS Regression](OLS_Regression), [Logistic Regression](Logistic_Regression) or [Kernel Ridge Regression](Kernel_Ridge_Regression)


Comments:
- will have to spend a lot of time engineering good features
- also model has to learn to rank rather than just classify
- but sometimes it will work even better than [Vector Space Model](Vector_Space_Model)s
- such models can use scores from other IR techniques and combine them + use some extra ones


Literature:
- Joachims, Thorsten, et al. "Learning to rank for information retrieval." 2007. [http://www.sigir.org/files/forum/2007D/2007d_sigirforum_joachims.pdf]
- Liu, Tie-Yan. "Learning to rank for information retrieval." 2009. [http://didawikinf.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/ir/ir13/1_-_learning_to_rank.pdf]



### [Generative Models](Generative_Models) Approach
Can use the [Bayes Rule](Bayes_Rule) to infer the probabilities
- $P(R = r \mid D, Q) = \cfrac{P(D, Q \mid R = r) \, P(R = r)}{P(D, Q)}$
- $P(R = \lnot r \mid D, Q) = \cfrac{P(D, Q \mid R = \lnot r) \, P(R = \lnot r)}{P(D, Q)}$
- and then compare $P(R = r \mid D, Q)$ and $P(R = \lnot r \mid D, Q)$

Interpretation:
- $P(D, Q \mid R = r)$ probability that if we know that a relevant document is retrieved, it's $D$
- $P(R = r)$ probability of retrieving a relevant document
- $P(D, Q)$ probability of retrieving $D$ and issuing $Q$


Log [Odds Ratio](Odds_Ratio):
- it's the same as using Odds ratio:
- if $\cfrac{P(R = r \mid D, Q)}{P(R = \lnot  \mid D, Q)} > 1$ or $\log \cfrac{P(R = r \mid D, Q)}{P(R = \lnot \mid D, Q)} > 0$ then $D$ is relevant w.r.t $Q$ 
- so again the formulated the problem as two-category [Document Classification](Document_Classification)
- but we're more interested in the scores rather than class outcome




## Binary Independence Retrieval Model
BIR Model: 
- classical probabilistic IR Model 
- assumes that terms are independent: it's a "[Naive Bayes Classifier](Naive_Bayes_Classifier)" for IR


Documents are represented by binary vectors 
- if a term is present in a document, it's 1, otherwise it's 0
- $T = \{T_i \}$ with $T_i = 1$ if $w_i$ is present in the document $D$ 


### Ranking
Can rank using log odds:
- use $s(Q, D) = \log \cfrac{P(R = r \mid D, Q)}{P(R = \lnot r \mid D, Q)} = \log \cfrac{P(D, Q \mid R = r) \, P(R = r)}{P(D, Q \mid R = \lnot r) \, P(R = \lnot r)}$
- $P(R = r)$ and $P(R = \lnot r)$ are just constants and will not change relative positions of documents in the rating, so let's remove them:
- $s(Q, D) = \log \cfrac{P(D, Q \mid R = r)}{P(D, Q \mid R = \lnot r)}$
- by independence have:
- $s(Q, D) = \log \cfrac{\prod P(T_i \mid Q, R = r)}{\prod P(T_i \mid Q, R = \lnot r)} = \log \prod \cfrac{P(T_i \mid Q, R = r)}{P(T_i \mid Q, R = \lnot r)} = \sum \log \cfrac{P(T_i \mid Q, R = r)}{P(T_i \mid Q, R = \lnot r)}$
- can sum only over words present in the query:
- $s(Q, D) = \sum\limits_{i \in Q} \log \cfrac{P(T_i \mid Q, R = r)}{P(T_i \mid Q, R = \lnot r)}$
- now let $p_i = P(T_1 = 1 \mid Q, R = r)$ and $q_i = P(T_1 = 1 \mid Q, R = \lnot r)$. then 
- $s(Q, D) = \sum\limits_{i \in Q \cap D} \log \cfrac{p_i \, (1 - q_i)}{(1 - p_i) \, q_i}$
- let $c_i = \log \cfrac{p_i \, (1 - q_i)}{(1 - p_i) \, q_i}$, so we have 
- $s(Q, D) = \sum\limits_{i \in Q \cap D} c_i$



Comments:
- here we take into account only presence/absence of words 
- we don't care about frequency 
- we assume a [Multiple Bernoulli Event Model](Binomial_Distribution): $P(T_i = 1 \mid Q, R) + P(T_i = 0 \mid Q, R) = 0$


### Estimation of Probabilities
How to estimate $p_i$ and $q_i$? 

Robertson / Sparck Jones Formula
- based on the training IR test corpus 
- and also can be account relevance feedback


Notation
- given a query $Q$ and a corpus $C$ 
- let $N$ be the number of documents in the corpus
- let $R$ be the number of documents relevant to $Q$ 
- $n_i$ # of docs that have term $w_i$
- $r_i$ # of relevant docs that have term $w_i$ 


Then:
- $p_i = \cfrac{r_i + \lambda}{R + 2 \lambda}$ 
- $q_i = \cfrac{n_i - r_i + \lambda}{N - R + 2 \lambda}$
- here we add some distortion value $\lambda$ (can be e.g. $\lambda = 0.5$) to avoid getting logs with 0
- It's [Laplace Smoothing](Laplace_Smoothing)



## BM25 Retrieval Function
{{ Stub }}

Use 2-Poisson Mixture Model with a Term Frequency formula

BM25:
- $\text{tf}(t, D)$ - how many times $t$ occurs in document $D$
- $\text{df}(t \mid C)$ - how many documents in the corpus $C$ contain $t$ 
- $$\text{bm25}(Q, D \mid C) = \sum_{t \in Q, D} \ln \cfrac- where $|  D |$ the length of $D$ and $| \bar D |$ is the average length of a document in $C$  |- params: $t_1 \in [1, 2]$, $b = 0.75$ and $k_3 \in [0, 1000]$
- Note that BM25 formula is very similar to [TF-IDF](TF-IDF)s


See 
- Robertson, Stephen E., and Steve Walker. "Some simple effective approximations to the 2-poisson model for probabilistic weighted retrieval." 1994. [http://nclt.computing.dcu.ie/~gjones/Teaching/CA437/p232.pdf]



## Other Probabilistic Models
- [Statistical Language Models](Statistical_Language_Models)
- [Bayesian Networks](Bayesian_Networks)


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
- Zhai, ChengXiang. "Statistical language models for information retrieval." 2008.

[Category:Information Retrieval](Category_Information_Retrieval)
[Category:Probabilistic Models](Category_Probabilistic_Models)