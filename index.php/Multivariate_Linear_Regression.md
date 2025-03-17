---
title: "Multivariate Linear Regression"
layout: default
permalink: /index.php/Multivariate_Linear_Regression
---

# Multivariate Linear Regression

## [Linear Regression](Linear_Regression)
[Linear Regression](Linear_Regression) - main article about univariative linear regression

## Multiple Features
- suppose we have several features 
- and we want to use them all to predict $Y$


For example, we want to predict a house's price
- $y$ - price (dependent)
- $x_1$ - # of bedrooms
- $x_2$ - # of floors 
- $x_3$ - age
- $x_4$ - size


let's use the following notation 
- $n$ - number of features 
- $m$ - number of examples 
- $x^{(i)}$ - a vector all features of the $i$th training set, $x^{(i)} \in \mathbb{R}$
- $x_j^{(i)}$ - $j$th element of $i$th training example 

e.g. 
: $x^{(2)} = (x_1^{(2)}, x_2^{(2)}, x_3^{(2)}, x_4^{(2)})$ - vector of all features from the second row 


- Recall that for [one variable](Linear_Regression) we have
: $h_{\theta}(x) = \theta_0 + \theta_1 x$
- now we have 
: $h_{\theta}(x) = \theta_0 + \theta_1 x_1 + ... + \theta_n x_n$


let $x_0 = 1$ (i.e. all $x_0^{(i)} = 1$) - so-called zeroth feature - always 1 (our slope)


So now we can view $x^{(i)}$ as $n+1$ vector: $x^{(i)} \in \mathbb{R}^{n + 1}$, 
$x = 
\left[
\begin{matrix}
x_0 \\ \vdots \\ x_n
\end{matrix}
\right]$
and 
$\theta = 
\left[
\begin{matrix}
\theta_0 \\ \vdots \\ \theta_n
\end{matrix}
\right] 
\in \mathbb{R}^{n+1}$

And $h_{\theta}(x) = \theta_0 x_0 + \theta_1 x_1 + ... + \theta_n x_n = \theta^{T} x$
(which is $[\theta_0 ... \theta_n] \cdot \left[
\begin{matrix}
x_0 \\ \vdots \\ x_n
\end{matrix}
\right]$ )

This is called ''multivariate linear regression''


## Polynomial Regression
- Suppose we want to fit not just features, but their combinations
- For example, we have two features: height and width, and we want to use them both to fit one parameter $\theta$
  - So we write: 
  - $h(x) = \theta_0 + \theta_1 x = \theta_0 + \theta_1 \cdot \text{height} \cdot \text{width}$
  - ($x = \text{height} \cdot \text{width}$)

Next, suppose we have the following relationship between data 
: <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/regression-poly.png" alt="Image">
- we may try to use 
- $\theta_0 + \theta_1 x + \theta_2 x^2 $
- or even 
- $\theta_0 + \theta_1 x + \theta_2 x^2 +  \theta_3 x^3 $
- So we have 3 features instead of one: $x$, $x^2$ and $x^3$|    |- Don't forget to normalize them - it's important because all these features have different scales |

## Computing Coefficients
### [Gradient Descent](Gradient_Descent) for Multivariate Linear Regression
{{Main |  Gradient Descent#Multivariate Linear Regression}} |
### [Normal Equation](Normal_Equation)
{{Main |  Normal Equation}} |This is another way of computing coefficients for multivariate regression 


## Linear Regression Assumptions
- https://en.wikipedia.org/wiki/Ordinary_least_squares#Assumptions
- http://stats.stackexchange.com/questions/55113/where-do-the-assumptions-for-linear-regression-come-from
- http://people.duke.edu/~rnau/testing.htm
- http://www.statisticssolutions.com/assumptions-of-linear-regression/
- http://pareonline.net/getvn.asp?n=2&v=8
- http://stats.stackexchange.com/questions/16381/what-is-a-complete-list-of-the-usual-assumptions-for-linear-regression


## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))

[Category:Regression](Category_Regression)
[Category:Statistics](Category_Statistics)
[Category:Machine Learning](Category_Machine_Learning)