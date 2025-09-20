---
layout: default
permalink: /index.php/Principal_Component_Analysis
tags:
- algebra
- machine-learning
title: Principal Component Analysis
---
## Principal Component Analysis
Principal Component Analysis is the most popular and commonly used technique for [Dimensionality Reduction](Dimensionality_Reduction)

Suppose we want to reduce from 2D to 1D
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/dim-red-intuition.png" alt="Image">
- how to find the best projection line? 

We want to find a line which would give us the smallest square distance from the data points to their projection
- http://stolzen.googlecode.com/svn/trunk/courses/coursera/Machine%20Learning/figures/pca-projection-error
- the sum of squared length of projection liens is called a ''projection error''

Before running PCA it's a good idea to perform [Feature Scaling](Feature_Scaling)
- so features have zero mean and
- comparable ranges of values 

To reduce from $N$-dim to $K$-dim
- we find a direction (a vector $u^{(1)} \in \mathbb{R}^n$, say $n = 2$)
- we project the data onto this direction
- and we want the projection error to be as small as possible
- doesn't matter if $u^{(1)}$ is 



## See also
- [Dimensionality Reduction](Dimensionality_Reduction)

## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))
