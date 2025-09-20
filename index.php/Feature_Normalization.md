---
layout: default
permalink: /index.php/Feature_Normalization
tags:
- data-transformation
- statistics
title: Feature Normalization
---
## Data Normalization
Typically, ''normalization'' refers to
- transforming all values of some continuous variable to the same scale
- it's done at the [Data Transformation](Data_Transformation) stage

There are several approaches 
- Min-Max
- $Z$-score


## Min-Max Normalization
Min-max normalization
- normalize to scale $[\text{new_min}_A, \text{new_max}_A]$
- for each new value, calculate $v'= \cfrac{v - \text{min}_A}{\text{max}_A - \text{min}_A} \cdot (\text{new_max}_A - \text{new_min}_A) + \text{new_min}_A$
- the easiest model
- not always good - if there are [outliers](outliers) 

Example
- income range between 12K to 98K
- want to normalize to $[0.0, 1.0]$. 
- so, for 73K have $\cfrac{73-12}{98-12} \approx 0.716$


## $Z$-score Normalization
$v'= \cfrac{v - \mu_A}{\sigma_A}$
- $\mu_A$ is [Mean](Mean) of $A$ and $\sigma_A$ is [Standard Deviation](Standard_Deviation)
- less susceptible to outliers 

Example 
- Assume that $\mu = 54K$ and $\sigma = 16K$
- So 73K becomes 1.225 


## Usages
- to help [Gradient Descent](Gradient_Descent) converge faster, typically normalize to $[-1, 1]$ 


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- [Machine Learning (coursera)](Machine_Learning_(coursera))
