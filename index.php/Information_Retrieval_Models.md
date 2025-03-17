---
title: "Information Retrieval Models"
layout: default
permalink: /index.php/Information_Retrieval_Models
---

# Information Retrieval Models

## Information Retrieval Models
General goal of an [Information Retrieval](Information_Retrieval) systems: rank relevant items much higher than non-relevant
- to do it, the items must be scored 


''Retrieval function'' is a scoring function that's used to rank documents 
- retrieval function is based on a [retrieval model](Information_Retrieval_Models)
- Retrieval Model defines the notion of relevance and makes it possible to rank the documents 


There are 5 categories of IR models
- they define the retrieval function in different ways 
- they also different in how they define/measure relevance


## Similarity-Based Models
- main assumption: relevance of a query $Q$ to the document $D$ is correlated with $\text{similarity}(Q, D)$
- i.e. the more similar a document $D$ to the query $Q$, the more relevant $Q$ to $D$ is 
- potentially can use any similarity function 


=== Algebraic Model === 
[Vector Space Model](Vector_Space_Model)s are most well-known 
- use Bag-of-Word to build a vector space
- both documents and the query are represented as vectors in this space
- each term is assigned some weight that reflects the importance of this term
- and then we use [Cosine Similarity](Cosine_Similarity) or [Inner Product](Inner_Product) to rank queries

It's a framework that defines:
- Term VSM: how documents and queries are represented (by terms they have)
- Similarity measure defined on this vector space
- also it has Document VSM: how terms are represented (terms are represented by documents where they are used) - but it's not very relevant for IR


### Set-Based
- [Boolean Model](Boolean_Model): only exact match
- satisfies all the conditions of the query 
- hard to rank
- [Extended Boolean Model](Extended_Boolean_Model): more flexible



## Probabilistic Relevance Models
[Probabilistic Retrieval Model](Probabilistic_Retrieval_Model)
- relevance = "what is the probability that document $D$ is relevant to the query $Q$?"
- Binary Independence Retrieval - classical probabilistic IR model, assumes term independence 
- it's sort of "[Naive Bayes Classifier](Naive_Bayes_Classifier)" for IR
- BM25 Ranking Function is comparable with [TF-IDF](TF-IDF) weighting performance



## Probabilistic Inference Models
### [Decision-Theoretic](Decision_Theory) Retrieval Framework
- from [Bayesian Decision Theory](Bayesian_Decision_Theory)
- general risk miminization framework for IR


### Query Likelihood Retrieval Model
Query Likelihood scoring method
- use [Statistical Language Models](Statistical_Language_Models) for [NLP](NLP)
- Ponte, Jay M., and W. Bruce Croft. "A language modeling approach to information retrieval." 1998. [http://www.cs.unibo.it/~montesi/CBD/Articoli/LanguageModelApproachIR.pdf]




## Links
- http://comminfo.rutgers.edu/~aspoerri/InfoCrystal/Ch_2.html
- http://wwwhome.cs.utwente.nl/~hiemstra/papers/IRModelsTutorial-draft.pdf


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
- Zhai, ChengXiang. "Statistical language models for information retrieval." 2008.


[Category:Information Retrieval](Category_Information_Retrieval)
[Category:NLP](Category_NLP)