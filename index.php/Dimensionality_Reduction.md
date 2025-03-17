---
title: "Dimensionality Reduction"
layout: default
permalink: /index.php/Dimensionality_Reduction
---

# Dimensionality Reduction

## Dimensionality Reduction
This is a technique to reduce the dimensionality of our data sets 
- we have a data set of $\{ \mathbf x_i \}$ of $\mathbf x_i \in \mathbb R^D$ with very large $D$
- the goal is to find a mapping $f: \mathbb R^D \mapsto \mathbb R^d$ s.t. $d \ll D$
- for [Visualization](Visualization) the target dimension is usually small, e.g. $d = 2$ or $d =3$


### Overfitting
- DR techniques tend to reduce [Overfitting](Overfitting): 
- if dimensionality of data is $D$ and there are $N$ examples in the training set
- then it's good to have $D \approx N$ to avoid overfitting


### Agressiveness
- Note that DR techniques sometimes may remove important information 
- Aggressiveness of reduction is $D / d$



## [Feature Selection](Feature_Selection)
### [Information Retrieval](Information_Retrieval) and [Text Mining](Text_Mining)
In IR these techniques are usually called "Term Selection" rather than "Feature selection"


Usual IR and indexing techniques for reducing dimensionality are
- [Stop Words](Stop_Words) Removal
- [Stemming](Stemming) or [Lemmatization](Lemmatization)  
- less common techniques are [Term Strength](Term_Strength) and [Term Contribution](Term_Contribution)

[Term Clustering](Term_Clustering)
- [Concept Decomposition](Concept_Decomposition) 


### General Techniques
- [Subset Selection](Subset_Selection) ("Wrapper Approach") take subset of features and see if it's better or not
- [Feature Filtering](Feature_Filtering): rank features according to some "usefulness" function
  - [Entropy-Based Ranking](Entropy-Based_Ranking)
  - [Information Gain](Information_Gain)
  - [Mutual Information](Mutual_Information)
  - [Odds Ratio](Odds_Ratio)
  - [Chi-Squared Ranking](Chi-Squared_Ranking)


## Feature Extraction
[Factor Analysis](Factor_Analysis)

Generate new features based on the original ones  


Linear 
- [Principal Component Analysis](Principal_Component_Analysis) (often done via [Eigendecomposition](Eigendecomposition) or [SVD](SVD))
- [Fisher Discriminant Analysis](Fisher_Discriminant_Analysis) (sometimes Linear Discriminant Analysis) - supervised technique for Dimensionality Reduction


Non-Linear
- [Locally Linear Embedding](Locally_Linear_Embedding)


## Links
- http://www.public.asu.edu/~jtang20/publication/feature_selection_for_classification.pdf
- http://www.public.asu.edu/~jtang20/publication/FSClustering.pdf


## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))
- [Machine Learning 1 (TUB)](Machine_Learning_1_(TUB))
- [Machine Learning 2 (TUB)](Machine_Learning_2_(TUB))
- Sebastiani, Fabrizio. "Machine learning in automated text categorization." (2002). [http://arxiv.org/pdf/cs/0110053.pdf]


[Category:Machine Learning](Category_Machine_Learning)
[Category:Dimensionality Reduction](Category_Dimensionality_Reduction)
[Category:Feature Selection](Category_Feature_Selection)