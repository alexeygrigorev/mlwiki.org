---
title: "True Error of Model"
layout: default
permalink: /index.php/True_Error_of_Model
---

# True Error of Model

## True Error of Model
What do we do when we want to know how accurately the model ''will'' perform in practice
- need to estimate its ''true error''


### Estimating the Accuracy
Given: 
- classification model $C$ 
- dataset $S$ with $n$ examples drawn w.r.t. distribution $P$ 

Problem 
- estimate the accuracy of $C$ over future instances drawn with $P$ 
- this is called the ''true error''
- it's important to distinguish ''sample error'' and ''true error''


### Sample Error
the ''sample error'' of $C$ calculated on sample $S$ is
- the proportion of examples in $S$ that $C$ misclassified
- $\text{error}(C, S) = \cfrac{1}- $\text{acc}(C, S)  = \cfrac{1}

But usually we have training and testing sets (see [Cross-Validation](Cross-Validation))
- i.e. we have some data set $S$ (drawn from the population with distribution $P$) 
- learning set $R \subset S$,
- training set $T \subset S$,
- $R$ and $T$ are disjoint: $R \cap T = \varnothing$
- so the sample error is computed against $T$: $\text{error}(C, T)$


### True Error
the ''true error'' of $C$ w.r.t distribution $S$ on the population $D$
- is the probability to misclassify an instance drawn from $D$ at random
- $\text{error}(C, D) = \sum_{(x,y) \in D} P(x, y) \cdot \delta(C(x) \ne y)$
  - $P(x, y)$ is the probability to draw a pair $(x,y) \in D$


Estimate of $\text{error}(C, D)$
- Sample error $\text{error}(C, S)$ is just an estimate of $\text{error}(C, D)$
- since $S \subset D$, $S$ is always finite, while $D$ can be infinite 
- but this estimate is not always accurate|   (need to have more accurate estimate) | |
More accurate estimates:
- [K-Fold Cross-Validation](K-Fold_Cross-Validation)
- average over $K$ testing errors to reduce variability 


[Category:Machine Learning](Category_Machine_Learning)
[Category:Statistics](Category_Statistics)
[Category:Model Performance Evaluation](Category_Model_Performance_Evaluation)