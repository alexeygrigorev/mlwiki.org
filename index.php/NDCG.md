---
layout: default
permalink: /index.php/NDCG
tags:
- information-retrieval
- model-performance-evaluation
title: NDCG
---

## NDCG

Discounted cumulative gain (DCG) 
DCG measures the usefulness, or gain, of a document based on its position in the result list

Two assumptions are made in using DCG and its related measures.

1. Highly relevant documents are more useful when appearing earlier in a search engine result list (have higher ranks)
2. Highly relevant documents are more useful than marginally relevant documents, which are in turn more useful than irrelevant documents.

sum(rel[i] / log2(i) for i in range(p))
rel[i] - relevance of result i
p - rank position p

alternative: 

sum((2 ** rel[i] - 1) / log2(i + 1) for range(p))
