---
layout: default
permalink: /Text_Mining
tags:
- nlp
- data-mining
title: Text Mining
---

## Text Mining

Document Representation:
- [Vector Space Models](Vector_Space_Models) bag of words
- [Language Models](Language_Models) - as a [Probability Distribution](Probability_Distribution) over words

### Textual Data
Properties of textual data
- dimensionality is very large, but vectors are very sparse
  - e.g. vocabulary size $| V | = 10^5$, but documents may contain only 500 distinct words
  - or even less - when we consider sentences or tweets
- lexicon of document may be large, but words are typically correlated with each other 
  - so number of concepts ("principal components") is $\ll | V |$
  - want to account for that 
- number of words across different documents may wary a lot
  - so need to normalize

- Berry, Michael W., Susan T. Dumais, and Gavin W. O'Brien. "Using linear algebra for intelligent information retrieval." (1995). [http://machinelearningtext.pbworks.com/w/file/fetch/47378285/lsiPaper_ut-cs-94-270.pdf]
