---
title: "Data Discretization"
layout: default
permalink: /index.php/Data_Discretization
---

# Data Discretization

## Data Discretization
What if we want to [transform](Data_Transformation) a continuous attribute to a categorical?


## Equal-Width Partitioning
Also called ''distance partitioning''
- want to divide $X = (x_1, ..., x_m)$ into $N$ equal intervals
- let $A = \min X$ and $B = \max X$
- width: $W = \cfrac{B - A}{N}$
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/discretization-equal-width.png" alt="Image">
- suppose that in one such partition you have all your data
- you'll lose a lot of information
- so it's sensible to [Outliers](Outliers)


## Equal-Depth Partitioning
Also called ''frequency partitioning'' 
- Divides $X$ into $N$ intervals, 
- with each interval containing approximately same number of samples
- not sensible to outliers
- distribution of values is taken into account
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/discretization-equal-depth.png" alt="Image">


## Entropy-Based Discretization
Uses entropy to find the best way to split your data 
- find the value $\alpha$ that maximizes the [Information Gain](Information_Gain)
- split by $\alpha$
- repeat recursively until have $N$ intervals or no information gain is possible



## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Data Transformation](Category_Data_Transformation)