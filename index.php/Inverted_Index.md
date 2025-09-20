---
layout: default
permalink: /index.php/Inverted_Index
tags:
- database-indexes
- information-retrieval
title: Inverted Index
---
## Inverted Index
### Indexing for [Information Retrieval](Information_Retrieval)
In [Databases](Databases), [indexing](Indexing_(databases)) is needed to speed up queries
- want to avoid full table scan 
- same is true for [Information Retrieval](Information_Retrieval) and other [Text Mining](Text_Mining)/[NLP](NLP) tasks
- Inverted index is a way of achieving this, and it can be generalized to other forms of input, not just text


For IR
- index is a partial representation of a document that contains the most important information about the document
- usually want to find terms to index automatically 




## Inverted Index for Similarity Search
### General Idea
Idea:
- usually a document contains only a small portion of terms 
- so document vectors are very sparse
- typical distance is cosine similarity - it ignores zeros. for cosine to be non-zero, two docs need to share at least one term
- $D^T$ is the inverted index of the term-document matrix $D$


This, to find docs similar to $d$:
- for each $w_i \in d$
  - let $D_i = \text{index}[w_i] - d$ be a set of documents that contain $w_i$ (except for $d$ itself)
- then take the union of all $D_i$
- calculate similarity only with documents from this union


Can be used in [Document Clustering](Document_Clustering) to speed up similarity computation


## Implementation
### Posting List
Build a dictionary: a "posting" list
- for each word we store ids of documents that have this word
- document are sorted by ids
- <img src="<img src="http://slidewiki.org/upload/media/images/29/509.png" alt="Image">?filter=Resize-width-550" />
- source of picture: [http://slidewiki.org/print/deck/339]
- sorting - because it's easier to take union: just merge the posting list 



== Sources == 
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
- Ertöz, Levent, Michael Steinbach, and Vipin Kumar. "Finding clusters of different sizes, shapes, and densities in noisy, high dimensional data." 2003. [http://static.msi.umn.edu/rreports/2003/73.pdf]
