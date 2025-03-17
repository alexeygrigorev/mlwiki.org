---
title: Tokenization
layout: default
permalink: /index.php/Tokenization
---

# Tokenization

## Tokenization
Tokenization is a part of [NLP Pipeline](NLP_Pipeline) and it's common in almost any [NLP](NLP) or [Information Retrieval](Information_Retrieval) task


Tokenization can be of two types:
- Decompose text into sentences 
- Decompose sentences into tokens


## Word Split
Usual tokenization is given a text, split it s.t. individual words can be accessed 

For example
- "The quick brown fox jumps over the lazy dog" -> 
- ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

Need to be careful with special cases:
- Numbers
- Los Angeles - may be one token, not two
- Punctuation is important:
- email@gmail.com - dot inside email
- U.S.A. - watch out for dots inside the token 
- Mr. Durand - one person
- see also [Text Normalization](Text_Normalization)


In some languages it's difficult
- e.g. German, Chinese 


## Sentence Split
Main challenge: distinguish between full stop dot and dot in abbreviations



## [NLP Pipeline](NLP_Pipeline)
- Tokenization is usually the very first step in NLP and IR applications 
- Then it can be followed by 
- [Stop Word Removal](Stop_Words)
- [Lemmatization](Lemmatization)
- building a [Vector Space Model](Vector_Space_Model) or [Inverted Index](Inverted_Index)
- etc


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))

[Category:Information Retrieval](Category_Information_Retrieval)
[Category:NLP](Category_NLP)