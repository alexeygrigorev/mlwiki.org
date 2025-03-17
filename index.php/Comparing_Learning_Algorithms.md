---
title: Comparing Learning Algorithms
layout: default
permalink: /index.php/Comparing_Learning_Algorithms
---

# Comparing Learning Algorithms

## Comparing Learning Algorithms
### Comparing Classifiers
A lot of things
- [Contingency Table](Contingency_Table)s
- [Cost Matrix](Cost_Matrix)
- best accuracy or $F_1$-score (see [Evaluation of Binary Classifiers](Evaluation_of_Binary_Classifiers)) 
- best [True Error of Model](True_Error_of_Model)
- best [Cumulative Gain Chart](Cumulative_Gain_Chart)
- other things


### Comparing Algorithms
What if we want to compare 
- two learning algorithms $A_1$ and $A_2$
- not just two specific classifiers $C_1$ and $C_2$


We want to measure the expected error 
- for $R \subset D$ where $D$ is the population, we want to measure
- $E \Big[ \text{error} \big(A_1(R), D \big) - \text{error} \big(A_2(R), D \big) \Big]$
  - with $\text{error} \big(A_1(R), D \big)$ being the [true error](True_Error_of_Model)


How to estimate it?
- average result over many different training sets 
- ideally all of these sets must be independent from each other 
- but usually use [K-Fold Cross-Validation](K-Fold_Cross-Validation)


### $K$-Fold Cross-Validation
Estimation:
- given a data set $S$
- for $k = 1..K$,
  - let $T_k$ be the training set,
  - and $R_k = S - T_k$
  - train $C_1 = A_1(R_k)$ and $C_2 = A_2(R_k)$
  - let $\delta_k = \text{error}(C_1, T_k) - \text{error}(C_2, T_k)$
- let $\delta^* = \cfrac{1}{K} \sum_{k = 1}^K \delta_k$
  - this is the estimate of the expected error $E \Big[ \text{error} \big(A_1(R), D \big) - \text{error} \big(A_2(R), D \big) \Big]$


### $K$-Fold CV Paired [$t$-Test](t-Test)
Let's conduct a [Statistical Tests of Significance](Statistical_Tests_of_Significance):
- assume (under the null hypothesis) that $A_1$ and $A_2$ have equal expected accuracy
- $t = \cfrac{\delta^*}{\sigma}$ follows the [Student distribution](Student_distribution) with $K-1$ degrees of freedom
  - $\delta^* = \cfrac{1}{K} \sum_{k = 1}^K \delta_k$ - the estimate of the expected error
  - $\sigma = \sqrt{ \cfrac{1}{K \cdot (K - 1)} \sum_{k = 1}^K (\delta_k - \delta^*)^2 }$ 

Test:
- the hypothesis $H_A$: $A_1$ and $A_2$ have equal expected error rate
- $H_A$ is accepted with $N = (1 - \alpha)\%$ confidence 
- if $|  t | < t_{1 - \alpha / 2, K - 1}$ |  - $t_{1 - \alpha / 2, K - 1}$ is the $1 - \alpha / 2$ percentile of  the [Student distribution](Student_distribution) with $K-1$ degrees of freedom


## Examples
### Example 1

|   $k$  |  1  |  2  |  3  |  4  |  5  |   $\text{error}(A_1, T_k)$   |  0.12  |  0.15  |  0.14  |  0.16  |  0.11 ||   $\text{error}(A_2, T_k)$   |  0.13  |  0.16  |  0.13  |  0.14  |  0.17 ||   $\delta_k$   |  -0.01  |  -0.01  |  0.01  |  0.02  |  -0.06 ||   $(\delta_k - \delta^*)^2$ with $\delta^* = -0.01$   |  0.0000  |  0.0000  |  0.0004  |  0.0009  |  0.0025 ||   $\cfrac{\delta^*}{\sigma} $  |   -0.73  |   |   |   |    |
So,
- $\left|  \cfrac{\delta^*}{\sigma} \right| = 0.73$ and $t_{97.5, 4} = 2.77$ |- the hypothesis $H_A$ is accepted with 95% confidence	


### Example 2
- given two algorithms $A_1$ and $A_2$
- 10 rounds are performed

| + Obtained error rates ||   $k$  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |   $A_1$  |  0.305  |  0.322  |  0.207  |  0.206  |  0.31  |  0.41  |  0.277  |  0.26  |  0.215  |  0.26 ||   $A_2$  |  0.224  |  0.145  |  0.224  |  0.196  |  0.207  |  0.204  |  0.221  |  0.194  |  0.162  |  0.35 |
So we calculate and obtain the following table 

|   $k$  |  $A_1$  |  $A_2$  |  $\delta_k$  |  $(\delta_k - \delta^*)^2$  |  1  |  0.305  |  0.224  |  0.081  |  0.00027225 ||  2  |  0.322  |  0.145  |  0.177  |  0.01265625 ||  3  |  0.207  |  0.224  |  -0.017  |  0.00664225 ||  4  |  0.206  |  0.196  |  0.01  |  0.00297025 ||  5  |  0.31  |  0.207  |  0.103  |  0.00148225 ||  6  |  0.41  |  0.204  |  0.206  |  0.02002225 ||  7  |  0.277  |  0.221  |  0.056  |  0.00007225 ||  8  |  0.26  |  0.194  |  0.066  |  0.00000225 ||  9  |  0.215  |  0.162  |  0.053  |  0.00013225 ||  10  |  0.26  |  0.35  |  -0.09  |  0.02387025 ||   colspan="3" | $\delta^* = \cfrac{1}{10} \sum \delta_k =$   |  0.0645  |    ||   colspan="4" | $\sigma^2 = \cfrac{1}{9 \cdot 10} \sum (\delta_k – \delta^*)^2 =$   |  0.0007569167 |
$t = \cfrac{\delta^*}{\sigma^2} \approx 2.34$
- we have 9 degrees of freedom
- for confidence level $\alpha = 0.05$ $\Rightarrow$ need to look for $1 - \alpha/2 = 0.975/%$ percentile
- Calculate the $t$-value: $t_{9, 0.975} = 2.26$
- $t = 2.34 \geqslant 2.26 = t_{9, 0.975}$
- $\Rightarrow$ the hypothesis that $A_1$ and $A_2$ have the same error rate is rejected 




## See Also
- [Cross-Validation](Cross-Validation)

## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Machine Learning](Category_Machine_Learning)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:Model Performance Evaluation](Category_Model_Performance_Evaluation)