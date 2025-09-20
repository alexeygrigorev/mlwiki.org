---
layout: default
permalink: /index.php/TF-IDF
tags:
- information-retrieval
- nlp
title: TF-IDF
---
## TF-IDF
It's a family of weighting schemes for the [Vector Space Model](Vector_Space_Model) in [Information Retrieval](Information_Retrieval) and [Text Mining](Text_Mining)


### [Vector Space Model](Vector_Space_Model)
Suppose we have 
- a collection of documents $\mathcal D = \{ d_1, \ ... \ , d_N \}$ with $N$ documents
- the vocabulary $V = \{ w_1, \ ... \ , w_M \}$ consisting of $M$ words
- then each document is represented by $d = (x_1, x_2, \ ... \ , x_M)$ where $x_i$ is the weight assigned to the word $w_i$ in the document $d \in \mathcal D$
- let $D$ be a matrix with rows indexed by documents and columns indexed by words. $D$ is called a Document-Term matrix



## Term Weighing Systems
Weights can be:
- binary: 1 if term is present and 0 if not
- term frequency (TF): frequency of each word in a document
- document frequency (DF): words that are used more in the collections have more weight
- TF-IDF: combination of sublinear TF and inverse document frequency


### Term Frequency
Term Frequency (TF)
- local frequency of a word in the document
- i.e. the word is weighed by how many times it occurs in the document
- $\text{tf}(w, d) = \big|  \{ w' \in d  \ : \ w' = w \} \big|$ where $w$ is a word and $d = \{ w_1, \ ... \ , w_m \}$ is a document  |

Sublinear TF:
- sometimes a word is used too often so we want to reduce its influence compared to other less frequently used words
- for that we can use some sublinear function, e.g. 
- $\log \text{tf}(w, d)$ or $\sqrt{\text{tf}(w, d)}$



### Document Frequency
Document Frequency (DF)
- global frequency of a word in the document collection
- it's the number of documents that contain the word:
- $\text{df}(w, \mathcal D) = \big|  \{ d \in \mathcal D \ : \  w \in d \} \big|$ where $w$ is a word and $\mathcal D = \{ d_1, \ ... \ , d_N \}$ is the document corpus |

Inverse Document Frequency (IDF)
- more often we're interested in words that are rare across the document collections
- they tend to be domain specific and are usually more relevant for retrieving this document
- so we should give them more weight than to high-frequency words 
- thus, $\text{idf}(w, \mathcal D) = \log \cfrac{ | \mathcal D| + 1 }{\text{df}(w, \mathcal D)}$  |- also can be some [Entropy](Entropy)-based measure


### Good Weighting System
The main function of a weighting scheme is to enhance IR effectiveness 
- want to retrieve items relevant to the users 
- and non-relevant items should be rejected


Effectiveness of an IR system is measures via [Precision and Recall](Precision_and_Recall)
- precision $P$: % of retrieved items that are relevant
- recall $R$: % of relevant items retrieved 
- want both $P$ and $R$ be good 
- $R$ is best served by broad high-frequency items: such terms are frequent and are likely to contain relevant documents
- $P$ best served by narrow and specific terms: the ones with "discriminating power"
- we can't achieve both, so need to compromise: use terms broad enough to get good $R$, but without producing very low $P$ 


Suggestions:
- TF should be good for getting high frequency words
- but using just TF is not good: if high frequency words are contained in many documents, all of them will be retrieved, thus affecting precision
- thus need a collection dependent factor that favors terms that are contained in fewer documents: IDF
- IDF varies inversely with the # of documents and the number of documents containing them


'''Term discrimination''' considerations:
- best terms are the ones that can distinguish individual documents from the test 
- so best terms should have high TF but low IDF => so we can combine them and use TF $\times$ IDF



### TF-IDF Scheme
When weighting we want to get:
- domain specific words
- words that are frequent in the document 
- this can be done by combining TF and IDF:
- use sub-linear TF to avoid the dominating effect of words that occur very frequently 
- use IDF to reduce weights of terms that occur more frequently to ensure that document matching is done with more discriminative words 
- as the result, terms appearing too rarely or too frequently are ranked low


Intuition:
- the more often a term occurs in a document, the more representative it is of this document
- the more documents contain a term, the lest discriminating it becomes


So, we can combine then my multiplying:
- $\text{tf-idf}(w, d \mid \mathcal D) = (1 + \log \text{tf}(w, d)) \cdot \log \cfrac- this is often used in [Text Mining](Text_Mining), but in [Information Retrieval](Information_Retrieval) there can be other components in the TF-IDF


### Normalization
In systems where vectors have very different lengths a third component of a weight can be useful: 
- Term normalization component


Why? 
- if we have a short document $d$, then for corresponding vector $d$, $\|  d \|$ is small |- if we have a large doc with many words, then $\|  d \|$ is big |- so for larger documents the chances of matching are higher => so larger documents have higher chances of being retrieved just because they are larger


Normalization Factor
- Thus, we need to incorporate the normalization factor $\cfrac{d}{\|  d \- It's also called "Cosine Normalization": we normalize weights s.t. they have a unit length |- then for a document vector $d$ and a query vector $q$, $\|  d \| = 1$ and $\| q \| = 1$ |- if we do this, the [Inner Product](Inner_Product) is the same as [Cosine Similarity](Cosine_Similarity): $d^T q = \text{cosine}(d, q)$ 



### Pivoted Length Normalization Function
In Information Retrieval more involved variants of TF-IDF give better performance
- they account for TF, IDF and also document length
- but it's still a TF-IDF variation


for example,
- $$\text{tf-idf}(d, q \mid \mathcal D) = \sum_{w \in q, d} = \cfrac{1 + \ln \big(1 + \ln \text{tf}(w, d) \big)}{(1 - s) + s \cdot \|  d \| / \| \bar d \- where $s$ - some parameter |- $\|  d \|$ is the length of document $d$, i.e. how many words are in $d$ |- $\|  \bar d \|$ is the average document length |


## Critique
- TF-IDF is just a bunch of heuristics
- they don't have sound theoretical properties (in contrast to [Probabilistic Retrieval Model](Probabilistic_Retrieval_Model)s)


## [Smoothing](Smoothing_for_Language_Models) vs TF-IDF
Smoothing and TF-IDF are connected
- also see probabilistic justification for TF-IDF in 
- Hiemstra, Djoerd. "A probabilistic justification for using tf×idf term weighting in information retrieval." 2000. [http://doc.utwente.nl/66959/1/ijodl.pdf]
- see [Smoothing for Language Models#Smoothing vs TF-IDF](Smoothing_for_Language_Models#Smoothing_vs_TF-IDF)



## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
- Zhai, ChengXiang. "Statistical language models for information retrieval." 2008.
- Salton, Gerard, and Christopher Buckley. "Term-weighting approaches in automatic text retrieval." 1988. [http://www.cs.odu.edu/~jbollen/spring03_IR/readings/article1-29-03.pdf]
