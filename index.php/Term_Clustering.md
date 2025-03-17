---
title: Term Clustering
layout: default
permalink: /index.php/Term_Clustering
---

# Term Clustering

## Term Clustering
Term clustering is a dual problem of [Document Clustering](Document_Clustering)
- it's also unsupervised [Text Mining](Text_Mining) technique, but applied to terms instead of documents
- term clustering may be good technique for [Dimensionality Reduction](Dimensionality_Reduction)



Duality:
- when we use [Vector Space Models](Vector_Space_Models), e.g. Bag of Words, then we have a term-document matrix $D$
- rows of $D$ are documents, columns of $D$ are terms
- can cluster columns instead of rows|   |- clustering rows and clustering columns are very related problems  |

Term Clustering groups words with a high degree of semantic relatedness 
- so we can use clusters (centroids of terms) to represent terms 


Li Jain 1998 
- view semantic relatedness between words in terms of their co-occurrence and co-absence in the corpus


## Clustering of Terms
How to do this?
- try applying usual row clustering techniques on $D^T$


=== Frequent Termset === 
Apply [Local Pattern Discovery](Local_Pattern_Discovery) and [Frequent Patterns Mining](Frequent_Patterns_Mining) techniques for terms:
- can see a document as a transaction and words like items 
- we want to find frequent itemsets of words in these documents 
- it's called [Frequent Word Patterns](Frequent_Word_Patterns)


### [Two-Phase Document Clustering](Two-Phase_Document_Clustering)
Main idea:
- use [Mutual Information](Mutual_Information) to find best term clustering
- and then use mutual information to find best document clustering



## Simultaneous Term/Document Clustering
Simultaneous clustering of rows and columns is called [Co-Clustering](Co-Clustering)
- simplest way is to use [Non-Negative Matrix Factorization](Non-Negative_Matrix_Factorization)


## References
- Slonim, Noam, and Naftali Tishby. "Document clustering using word clusters via the information bottleneck method." 2000. [http://lsa3.colorado.edu/LexicalSemantics/slonim00document.pdf]


## Sources
- Li, Yong H., and Anil K. Jain. "Classification of text documents." (1998) [http://julio.staff.ipb.ac.id/files/2014/09/LiJ98.pdf]
- Sebastiani, Fabrizio. "Machine learning in automated text categorization." (2002). [http://arxiv.org/pdf/cs/0110053.pdf]

[Category:Cluster Analysis](Category_Cluster_Analysis)
[Category:Document Clustering](Category_Document_Clustering)