---
title: Two-Phase Document Clustering
layout: default
permalink: /index.php/Two-Phase_Document_Clustering
---

# Two-Phase Document Clustering

## Two-Phase Document Clustering
How can we use [Term Clustering](Term_Clustering) for [Document Clustering](Document_Clustering)?


Two Phases
- term clustering
- document clustering


### Notation
- let $D$ be term-document matrix: rows are documents and columns are terms 
- $X = \{ \mathbf x_1 , \ ... \ , \mathbf x_n \}$ - random vectors: rows of $D$
- $Y = \{ \mathbf y_1 , \ ... \ , \mathbf y_d \}$ - random vectors: columnts of $D$


We want to partition:
- $Y$ into $l$ clusters $\hat Y = \{ \hat Y_1 , \ ... \ , \hat Y_l \}$
- $X$ into $k$ clusters $\hat X = \{ \hat X_1 , \ ... \ , \hat X_k \}$


### Problem Statement
Formally, we want to find mappings:
- $C_Y : Y \to \hat Y$ or  $\mathbf y_1 , \ ... \ , \mathbf y_d \to \hat Y_1, \ ... \ , \hat Y_l $
- $C_X : X \to \hat X$, or $\mathbf x_1 , \ ... \ , \mathbf x_n \to \hat X_1, \ ... \ , \hat X_k $



### Phase One: Term Clustering
Find word clustering s.t. 
- most of [Mutual Information](Mutual_Information) between words and documents is preserved 
- when we go from representing docs in terms of words to representing docs in terms of word clusters


Cluster:
- find clustering of $Y$ into $\hat Y$ s.t. information from $I(X; Y)$ is preserved in $I(X; \hat Y)$ as good as possible


How?
- $P(X, Y)$ always has more information than $P(X, \hat Y)$, so $I(X; \hat Y) \leqslant I(X; Y)$
- thus find such mapping $C_Y$ that minimizes $I(X; Y) - I(X; \hat Y)$
- this loss function is called "Mutual information loss"



### Phase Two: Document Clustering
Using term clusters:
- perform document clustering 
- cluster $X$ into $\hat X$ s.t. we preserve as much of $I(X; \hat Y)$ as possible in $I(\hat X ; \hat Y)$


Same here:
- minimize  $I(X; \hat Y) - I(\hat X; \hat Y)$


For details, see Slonim2000



## References
- Slonim, Noam, and Naftali Tishby. "Document clustering using word clusters via the information bottleneck method." 2000. [http://lsa3.colorado.edu/LexicalSemantics/slonim00document.pdf]

## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]

[Category:Information Theory](Category_Information_Theory)
[Category:Document Clustering](Category_Document_Clustering)