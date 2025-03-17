---
title: "Stemming"
layout: default
permalink: /index.php/Stemming
---

# Stemming

## Stemming
Stemming is a part of [NLP Pipeline](NLP_Pipeline) useful in [Text Mining](Text_Mining) and [Information Retrieval](Information_Retrieval)
- ''stemming'' is an algorithm that extract the morphological root of a word 


Usage:
- it's a part of [Text Normalization](Text_Normalization) step: 
- it helps reducing the size of [Inverted Index](Inverted_Index) and the dimensionality of [Vector Space Model](Vector_Space_Model)
- it can be seen as a [Dimensionality Reduction](Dimensionality_Reduction) technique for textual data



## Algorithms
Need to reduce words to a stem (root) form
- use language-dependent rules
- usually they are in a form of [Automaton](Deterministic_Finite_Automate) that gradually reduces a token to its stem
- for example, there's a Porter Algorithm and Snowball Stemmer
 

### Porter Stemmer
It's a bunch of rules for reducing a word:
- sses -> es
- ies -> i
- ational -> ate
- tional -> tion
- s -> $\varnothing$
- when conflicts, the longest rule wins

Example
- economy, economic, economical, economically, economics, economize => econom
- automates, automatic, automation => automat


### Snowball Stemmer
Better stemmer than Porter


## Programming
### Python / NLTK
```python
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
stem = snowball_stemmer.stem(unigram)
```


## Downsides
- often does wrong replacement and bad reduction
- e.g. universe -> univers, university -> univers: different words, same stem
- in applications where it's important to distinguish between these words, use [Lemmatization](Lemmatization) instead (although it's more computationally expensive)


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))

[Category:Information Retrieval](Category_Information_Retrieval)
[Category:NLP](Category_NLP)