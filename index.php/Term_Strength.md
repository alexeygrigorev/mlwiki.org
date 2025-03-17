---
title: "Term Strength"
layout: default
permalink: /index.php/Term_Strength
---

# Term Strength

## Term Strength
Term Strength is a technique for [Feature Selection](Feature_Selection) in [Text Mining](Text_Mining)
- it doesn't need a pre-defined list of [Stop Words](Stop_Words) - it discovers them automatically
- so it's a technique for vocabulary reduction in text retrieval 
- this method estimates term importance based on how often a term appears in "related" documents

 
''Strength'' of a term $t$ 
- measures how informative a word is for identifying two related documents
- $s(t) = P(t \in y \mid t \in x)$
- for two related documents $x, y$ what's the probability that $t$ belongs to $y$ given it belongs to $x$?
- estimate $s(t)$ on training data using [Maximum Likelihood Estimation](Maximum_Likelihood_Estimation)


What does it mean "related"?
- if we know the labels of these documents, then related are those that belong to the same category
- what about [Unsupervised Learning](Unsupervised_Learning)?



## [Document Clustering](Document_Clustering)
Can we use this for unsupervised learning?

How to find such $x$ and $y$?
- manual or with user feedback - not practical

Can we automate it?

Yes (Wilbur1992):
- use [Cosine Similarity](Cosine_Similarity) to find most related documents 
- set some threshold $t$ and let all pairs with cosine $> t$ be related 

Then we can estimate $s(t)$ using [Maximum Likelihood Estimation](Maximum_Likelihood_Estimation) for [Multinomial Distribution](Multinomial_Distribution)
$$\hat s(t) = \cfrac{\text{# of pairs where $t$ occurs both in $x$ and $y$}}{\text{# of pairs where $t$ occurs in $x$}}$$



## Pruning
Let expected strength be $z = \mathbb E_t [s(t)]$ 
- we estimate $z$ as $\hat z = \cfrac{1}- let $\sigma = \text{sd}\big( s(t) \big)$ - how much $s(t)$ varies
- we prune term $t$ if $s(t) \leqslant 2 \sigma \, z$



## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Wilbur, W. John, and Karl Sirotkin. "The automatic identification of stop words." 1992. [https://www.researchgate.net/publication/247786801_The_automatic_identification_of_stop_words]


[Category:Feature Selection](Category_Feature_Selection)
[Category:Information Retrieval](Category_Information_Retrieval)