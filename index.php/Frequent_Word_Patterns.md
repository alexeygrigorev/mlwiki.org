---
title: "Frequent Word Patterns"
layout: default
permalink: /index.php/Frequent_Word_Patterns
---

# Frequent Word Patterns

{{stub}}

## Frequent Word Patterns
Frequent word patters is a technique of [Local Pattern Discovery](Local_Pattern_Discovery) applied to documents
- we can see a document as a transaction and words like items 
- then want to find frequent itemsets of words in these documents - like in [Frequent Patterns Mining](Frequent_Patterns_Mining) with [Apriori](Apriori) or [Eclat](Eclat)
- frequent itemset $\equiv$ frequent wordset



## [Document Clustering](Document_Clustering)
We can use [FPM](Frequent_Pattern_Mining) for [Term Clustering](Term_Clustering)
- cluster = all documents that contain a certain frequent term set 
- so frequent term sets describe clusters 
- note that here clustering is not strict (it's [Fuzzy Clustering](Fuzzy_Clustering)): it allows some overlap between clusters
- which is sometimes natural in text documents


Problem formalization
- let $R$ be set of chosen frequent term sets (FTS)
- $f_i$ be the # of FTSs from $R$ contained in document $d_i$
- we put a constraint on $f_i$: it must be at least one to ensure complete coverage (there should be no documents without category)
- we want: minimize the average value of $f_i - 1$


Algorithm:
- at each iteration
- pick FTS with minimal overlap with other clusters
- see more in the reference




## References
- Beil, Florian, Martin Ester, and Xiaowei Xu. "Frequent term-based text clustering." 2002. [http://www.cs.sfu.ca/~ester/papers/KDD02.Clustering.final.pdf]

## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]


[Category:Rule Mining](Category_Rule_Mining)
[Category:Cluster Analysis](Category_Cluster_Analysis)
[Category:Document Clustering](Category_Document_Clustering)