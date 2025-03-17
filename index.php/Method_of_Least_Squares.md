---
title: Method of Least Squares
layout: default
permalink: /index.php/Method_of_Least_Squares
---

# Method of Least Squares

## Method of Least Squares
### [Linear Regression](Linear_Regression)
- Suppose we want to fit a [regression line](Linear_Regression) to our data
- We want to find the slope and intercept parameters 
- And we want to find the best fit 


Optimization
- To do that we minimize the sum of squares for differences:
- $\text{ss} = \sum_{i = 1}^{n} (y_i - b_0 - b_1 x_i)^2 $
- We want to make $\text{ss}$ as small as possible 


We need to use calculus to do that
- we find partial derivatives to find the critical (minimal in our case) value 
- $\cfrac{\partial \text{ss}}{\partial b_0} = \cfrac{\partial \text{ss}}{\partial b_1} = 0$


So after calculating that we get:
- $b_0 = \cfrac{1}{n} (\sum y_i - b_0 \sum x_i)$ for intercept
- $b_1 = \cfrac{n \sum x_i y_i - \sum x_i \sum y_i }{n \sum x_i^2 - (\sum x_i)^2}$ for slope

These values minimize the sum of square differences 


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))

[Category:Regression](Category_Regression)
[Category:Statistics](Category_Statistics)