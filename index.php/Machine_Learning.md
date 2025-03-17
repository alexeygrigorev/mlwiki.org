---
title: "Machine Learning"
layout: default
permalink: /index.php/Machine_Learning
---

# Machine Learning

## Machine Learning
''Machine Learning'' - field of study that gives computers the ability to learn without being explicitly programmed

A computer is said to ''learn'' from experience $E$ with respect to some task $T$ and some performance measure $P$
- if it's performance of $T$,
- as measured by $P$,
- improves with experience $E$


E.g. email filtering:
- $T$: classifying email as spam/not spam
- $E$: watching you label as spam/not spam 
- $P$: the number of emails correctly classified as spam/not spam


Examples of Machine Learning: 
- db-mining
  - web-data clicks, etc
- automation
  - autonomous helicopter 
  - NLP
  - Computer Vision
- self-customizing software
  - amazon, netflix, etc
- understanding human learning


## Supervised Learning
"right answers" are given 
- i.e. the algoritm takes a training set $\{(x^{(i)}, y^{(i)})\}$
- and then predicts a value for / classifies a data example $x$


### Regression
''Regression'' - predict: continuous values 

Examples:
- You have a large inventory of identical items 
- You want to predict how many of these items will sell over the next 3 months


Main tool
- [Linear Regression](Linear_Regression)


### Classification
''Classification'' - assigning to a group (0, 1) etc: discrete values

$y \in \{0, 1\}$ - ''binary classification problem'' 
- 0 - negative class, connected with absence of smth (not spam)
- 1 - positive class, connected with presence of smth (spam)

Tools:
- [Logistic Regression](Logistic_Regression)
- [Neural Networks](Neural_Networks)
- [Support Vector Machines](Support_Vector_Machines)


## Unsupervised Learning
- just given the data, no labels 
- can we find a structure in the data? 
- we don't tell the algorithm what are the categories 

i.e. we're given only $\{x^{(i)}\}$, no $y^{(i)}$s

applications
- news segregation
- social network analysis
- clustering 
- market segregation

### [Clustering](Clustering)
The goal is to automatically group the data into coherent subsets (or ''clusters'')
- [K-Means](K-Means)




## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))

[Category:Machine Learning](Category_Machine_Learning)