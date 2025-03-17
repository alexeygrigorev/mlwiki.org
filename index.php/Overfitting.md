---
title: Overfitting
layout: default
permalink: /index.php/Overfitting
---

# Overfitting

## Overfitting
''Overfitting'' (or  ''high variance'') - if we have too many features, the learning hypothesis may 
- fit the training set very well (with cost function $J(\theta) \approx 0$), 
- but fail to generalize to new examples (predict for new data)


## Generalization Error
### [Cross-Validation](Cross-Validation)
Best way to see if you overfit:
- split data in training and test set
- train the model on training set
- evaluate the model on the training set
- evaluate the model on the test set
- generalization error: difference between them, measures the ability to generalize


It's clear that a model overfits when we plot the generalization error
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/ds/overfitting.png" alt="Image">
- we have low error on the training data, but high on the testing data
- may perform [Machine Learning Diagnosis](Machine_Learning_Diagnosis) to see that


### High Variance vs High Bias
Generalization error can be decomposed into bias and variance 
- bias: tendency to constantly learn the same wrong thing 
- variance: tendency to learn random things irrespective to the input data

Dart throwing illustration:
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/ds/high-variance-bias.png" alt="Image">


### Underfitting
- high bias, low variance
- you're always missing in the same way

example:
- predict always the same
- very insensible to the data 
- the variance is very low|   (0) |- but it has high bias - it's wrong |


## Examples
### [Multivariate Linear Regression](Multivariate_Linear_Regression)
Suppose we have a set of data 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/overfit-dataset-lin.png" alt="Image">
- We can fit the following [Multivariate Linear Regression](Multivariate_Linear_Regression) model
- linear: $\theta_0 + \theta_1 x$, likely to underfit (high bias)
- quadratic: $\theta_0 + \theta_1 x + \theta_2 x^2 $
- extreme: $\theta_0 + \theta_1 x + \theta_2 x^2 +  \theta_3 x^3 +  \theta_4 x^4 $
: <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/overfit-dataset-lin-ex.png" alt="Image">


### [Logistic Regression](Logistic_Regression)
Same applies for [Logistic Regression](Logistic_Regression)
- Suppose we have the following set
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/overfit-dataset.png" alt="Image">
- We may underfit with just a line
  - $g(\theta_0 + \theta_1 x_1 + \theta_2 x_2)$
- We may perform just right, but missing some positive examples
  - $g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_2^2 + \theta_5 x_1 x_2)$
- Or we may overfit using high-polynomial model
  - $g(\theta_0 + \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_2^2 + \theta_5 x_1 x_2 + \theta_6 x_1^2 x_2 + \theta_7 x_1 x_2^2 + \theta_8 x_1^2 x_2^2 + \theta_9 x_1^3 + ...)$
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/overfitting-logreg-ex.png" alt="Image">


The problem with it
- overly high polynomial 
- it can fit anything|   |- it overfits - results in high variance |

## Diagnosing
### How to Diagnose the Problem
To identify overfitting we can use [Machine Learning Diagnosis](Machine_Learning_Diagnosis):
- [Cross-Validation](Cross-Validation)
- and [Learning Curves](Learning_Curves)


### How to Address the Problem
- plotting - doesn't work with many features
- reducing the number of features
  - manually select features to keep 
  - [Model Selection](Model_Selection) algorithm (chooses good features by itself)
  - but it may turn out that some of the features we want to throw away are significant
  - [Principal Component Analysis](Principal_Component_Analysis)
- [Regularization](Regularization)
  - keep all the features but reduce the magnitude of parameters
- [Cross-Validation](Cross-Validation)
  - test your hypotheses on cross-validation set 



## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- Domingos, Pedro. "A few useful things to know about machine learning." [http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf]

[Category:Machine Learning](Category_Machine_Learning)
[Category:Model Performance Evaluation](Category_Model_Performance_Evaluation)