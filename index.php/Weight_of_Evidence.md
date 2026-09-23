---
layout: default
permalink: /Weight_of_Evidence
tags:
- statistics
- machine-learning
title: Weight of Evidence
---

## Weight of Evidence

method for grouping the data in continous predictor in a way that maximizes its discriminating ability
creates model with large Lift

Idea: 
divide into subgroups s.t. the difference between target is maximized
to do it, use Information Value (IV), which is based on WoE

Need binning that maximizes IV

Entropy: $H(X) = - \sum p_i \, \log p_i$

Information Value of $X$ measuring $Y$: what's the predictive power of $X$ to $Y$ 

Example:
if $Y$ is binary
divide $X$ into 10 bins 
\text{IV}(X) = \sum_{i = 1}^{10} \big(B_i - G_i \big) \, \ln \cfrac{B_i}{G_i}

B_i - number of bad customers in bin i
G_i - number of good customers in bin i

Weight of Evidence
\text{WoE}_i = \ln \left[ \cfrac{G_i}{\sum_j G_j} / \cfrac{B_i}{\sum_j B_j} \right]

WoE - measure of strenght for grouping good and bad customers
the further WoE from 0, the better 

http://datasciencelondon.org/scoring-models-and-weight-of-evidence-woe-by-jurek-gurycz-nuno-antonio/
https://sites.google.com/site/kittipat/rtechniques/weightofevidencewoetransformation

Discretization

Optimal binning = Supervised Discretization
https://www.google.de/search?q=Supervised+Discretization 
http://www.scoringmodeling.com/rpackage/smbinning/index.php?src=dsc20150221 smbinning in R

http://robotics.stanford.edu/users/sahami/papers-dir/disc.pdf

http://kevinmeurer.com/a-simple-guide-to-entropy-based-discretization/
