---
layout: default
permalink: /index.php/Document_Classification
tags:
- classification
- machine-learning
- nlp
- supervised-learning
- text-mining
title: Document Classification
---
## Document Classification
Document/Text Classification/Categorization is an [NLP](NLP)/[Text Mining](Text_Mining) task of labeling unseen documents with categories from some predefined set
- not to be confused with [Document Clustering](Document_Clustering) - an [Unsupervised Learning](Unsupervised_Learning) technique
- typically use [Machine Learning](Machine_Learning) for classification


### Formulation
Document Classification, most general formulation:
- a task of assigning a boolean value to each pair $\langle d_j, c_i \rangle \in D \times C$
- $D$ - domain of documents
- $C = \{ c_1, \ ... \ , c_K \}$ - predefined categories
- we assign TRUE to $\langle d_j, c_i \rangle$ if document $d_j$ belongs to category $c_i$
- the task is to approximate the unknown target function $\Phi: D \times C \to \{ \text{T}, \text{F} \}$


Types 
- non overlapping categories, i.e. can assign only one label to each document. 
  - the unknown function becomes $\Phi: D \to C$
- overlapping - can assign several labels


Hard categorization vs Ranking
- instead of assigning true/false we can rank each category 



## Features
### [Vector Space Model](Vector_Space_Model)
How do we come up with features?
- text cannot be fed to the classifier directly 
- so need to do some [indexing](Information_Retrieval) to map a document $d_j$ to some representation
- for example, to [Vector Space Model](Vector_Space_Model): represent document as a vector of term weights - "features"
- $d_j = \langle w_{1j}, \ ... \ , w_{nj} \rangle$, with $w_{ij}$ telling how much term $t_i$ contributes to the semantics of document $d_j$ 


### [TF-IDF](TF-IDF)
Weights are often term frequencies or [TF-IDF](TF-IDF):
- $\text{tf-idf}(t_k, d_j) = \text{tf}(t_k, d_j) \cdot \log \cfrac{N}{\text{df}(t_k)}$
- $\text{tf}(t_k, d_j)$ term frequency: how many times term $t_k$ appeared in document $d_j$
- $\text{df}(t_k)$ document frequency: how many documents in the training set contain term $t_k$
- $N$ number of documents in the training set


Why TF-IDF is good for classification:
- the more often a term occurs in a document, the more representative it is of this document
- the more documents contain a term, the lest discriminating it becomes


### [Dimensionality Reduction](Dimensionality_Reduction)
- Given a vocabulary/term set $V$ of size $|  V |$  |- the goal is to find $V'$ s.t. $|  V' | \ll | V |$ ($V'$ is called "reduced vocabulary" or "reduced term set") |- DR techniques tend to reduce [Overfitting](Overfitting): 
  - if dimensionality of data is $| V'|$ and there are $N$ examples in the training set |  - then it's good to have $| V'| \approx N$ to avoid overfitting |

We can divide dimensionality reduction techniques by locality: 
- local dimensionality reduction
  - applied to each category $c_i$ 
  - choose a reduced set $|  V'_i | \ll | V_i |$  for each category |- global: choose $|  V' |$ using all categories  |


There are two (very different) types of dimensionality reduction
- by term selection ([Feature Selection](Feature_Selection)): select $V' \subset V$ 
- by term extraction: terms in $V'$ are not necessarily the same as in $V$ 



Usual IR and indexing techniques for reducing dimensionality are 
- [Stop Words](Stop_Words) Removal
- [Stemming](Stemming) or [Lemmatization](Lemmatization)


[Stop Words](Stop_Words) Removal
- Before indexing some ''function words'' are sometimes removed 
- for example [Stop Words](Stop_Words) - topic neutral words such as articles, prepositions, conjunctions
- cases when stop words are not removed: author identification ("the little words give authors away")


[Stemming](Stemming)
- Stemming is grouping words that share the same morphological root 
- it's controversial whether it's helpful for document classification or not
- usually it's used: it reduces the dimensionality 
- sometimes [Lemmatization](Lemmatization) is applied instead, but it's more involved



Note that DR techniques sometimes may remove important information when removing terms

How to select terms?
- [Subset Selection](Subset_Selection): usually not used because $|  V |$ is too large |- [Feature Filtering](Feature_Filtering): rank terms according to their "usefulness" and keep only some of them
- Document Frequency: Keep only terms that occur in higher number of documents
  - e.g. remove words that occur only in 3 documents or less


Term Extraction techniques:
- these techniques create "artificial" terms that aren't really terms - they are generated, and not the ones that actually occurred in the text
- The original terms don't have the optimal dimensionality for document content representation
  - because of the problems of polysemy, homonymy and synonymy 
- so we want to find better representation that doesn't suffer from these issues
- methods: 
- [Term Clustering](Term_Clustering) cluster terms and use centroids instead of words
- [Latent Semantic Analysis](Latent_Semantic_Analysis) apply [SVD](SVD) to Term-Document matrix 



## [Classification](Classification)
Good classifiers for text:
- [Naive Bayes Classifier](Naive_Bayes_Classifier)
- [Decision Tree (Data Mining)](Decision_Tree_(Data_Mining))
- [Support Vector Machines](Support_Vector_Machines)


## Evaluation
[Precision and Recall](Precision_and_Recall) metrics can be extended to [Evaluation of Multiclass Classifiers](Multi-Class_Problems)
- similar to the [One-vs-All Classification](One-vs-All_Classification) technique
- ways of averaging the results: 
  - micro: first calculate TP, FP, FN, FN for each category separately, and then use usual formulas for precision and recall
  - and macro averaging: calculate precision and recall for each category separately, and then average


[F Measure](F_Measure)
- usually is a way of combining precision and recall
- depending on how P and R were calculated, there are $F_\beta$-micro and $F_\beta$-macro measures


## Sources
- Sebastiani, Fabrizio. "Machine learning in automated text categorization." (2002). [http://arxiv.org/pdf/cs/0110053.pdf]
