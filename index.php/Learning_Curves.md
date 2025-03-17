---
title: "Learning Curves"
layout: default
permalink: /index.php/Learning_Curves
---

# Learning Curves

## [Learning Curves](Learning_Curves)
This is a good technique (a part of [Machine Learning Diagnosis](Machine_Learning_Diagnosis))
- to sanity-check a model 
- to improve performance 

A ''learning curve'' is a plot where we have two functions of $m$ ($m$ is a set size): 
- training set error $J_{\text{train}}(\theta)$, 
- the cross-validation error $J_{\text{cv}}(\theta)$


We can artificially reduce our training set size. 
- We start from $m = 1$, then $m = 2$ and so on 

So suppose we have the following model:
- $h_{\theta}(x) = \theta_0 + \theta_1 x + \theta_2 x^2$
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-trainingset-red.png" alt="Image">
- for each $m$ we calculate $J_{\text{train}}(\theta)$ and $J_{\text{cv}}(\theta)$ and plot the values  
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-grow.png" alt="Image">
- This is the learning curve of the model


## Diagnose High Bias (Underfitting)
Suppose we want to fit a straight line to out data: 
: $h_{\theta}(x) = \theta_0 + \theta_1 x$

As $m$ increases we have pretty same line: 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-lin.png" alt="Image">

If we draw the learning curves, we'll have 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-lin2.png" alt="Image">

So we see that 
- as $m$ grows $J_{\text{cv}}(\theta) \to J_{\text{train}}(\theta)$
- and both errors are high 

$\Rightarrow$
If learning algorithm is suffering from high bias, getting more examples will not help

## Diagnose High Variance ([Overfitting](Overfitting))
Now suppose we have a model with polynomial of very high order: 
: $h_{\theta}(x) = \theta_0 + \theta_1 x + \theta_2 x^2 + ... + \theta_{100} x^{100}$

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-overfit1.png" alt="Image">
- at the beginning we very much overfit
- as we increase $m$, we still able to fit the data well


<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/learning-curves-overfit2.png" alt="Image">

So we can see that as $m$ increases,
- $J_{\text{train}}(\theta)$ increases (we have more and more data - so it's harder and harder to fit $h_{\theta}(x)$), but it increases very slowly 
- on the other hand, $J_{\text{cv}}(\theta)$ decreases, but also very very slow 
- and there's a huge gap between these 2
- to fill that gap we need many many more training examples

$\Rightarrow$ if a learning algorithm is suffering from high variance (i.e. it overfits), getting more data is likely to help




## See also
- [Machine Learning Diagnosis](Machine_Learning_Diagnosis)
- [Model Selection](Model_Selection)
- [Cross-Validation](Cross-Validation)


## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))

[Category:Machine Learning](Category_Machine_Learning)