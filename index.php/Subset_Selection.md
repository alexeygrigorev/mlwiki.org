---
layout: default
permalink: /index.php/Subset_Selection
tags:
- statistics
- machine-learning
title: Subset Selection
---

## Subset Selection
Or Wrapper approach

choose a subset of features using some learning method that will be used for building a classifier 

[Meta Learning](Meta_Learning)

- start with initial set of features 
- generate a new set by adding/removing a feature 
- then test the classifier on the validation set to see if the objective is improved or not

Usually isn't used for datasets with large dimensionality (e.g. text data) because it becomes too expensive
