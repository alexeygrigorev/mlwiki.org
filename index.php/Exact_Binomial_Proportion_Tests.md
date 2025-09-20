---
layout: default
permalink: /index.php/Exact_Binomial_Proportion_Tests
tags:
- statistical-tests
- statistics
title: Exact Binomial Proportion Tests
---
## Exact Binomial Test
This is a [Statistical Test](Statistical_Test) for proportions that uses the [Binomial Distribution](Binomial_Distribution) as the null (sampling) distribution. 

It doesn't use the [Normal Approximation](Binomial_Distribution#Normal_Approximation)
- because sometimes it's possible to use the Binomial model directly 
- or because it's not possible to use the Normal Model: some conditions are not met


### Binomial Model
Recall the formula:
- $P(\text{success}) = { n \choose k } p^k (1 - p)^{n - k}$
- this is the null distribution of our test 


Test
- the tail area of the null distribution:
  - add up the probabilities (using the formula) for all $k$ that support the alternative hypothesis $H_A$
- one-sided test - use single tail area
- two-sided - compute single tail and double it



## Examples
### Example 1: Medical Consultant (One-Sample)
- medical consultant helps patients 
- he claims that with his help the ratio of complications is lower than usually 
  - (i.e. lower than 0.10)
- is it true?


We want to test a hypothesis: 
- $H_0: p_A = 0.10$ - ratio of complications without a specialist 
- $H_A: p_A < 0.10$ - specialist helps, the complications ratio is lower than usual 

Observed data:
- 3 complications in 62 cases
- $\hat{p} = 0.048$ 
- is it only due to chance? 


Normal Model
- the Success-Failure condition is not met: $p_A \cdot 62 = 0.10 \approx 6.2 < 10$
  - under $H_0$ we'd expect to see only 6.2 complications 
- thus cannot use [Normal Approximation](Binomial_Distribution#Normal_Approximation) and perform a [Binomial Proportion Test](Binomial_Proportion_Tests)


Apply the Binomial Model:
- $p\text{-val} = \sum_{j = 0}^3  { n \choose j } p^j (1 - p)^{n - j} = 0.0015 + 0.01 + 0.034 + 0.0355 = 0.121$
- we don't reject the $H_0$ at $\alpha = 0.05$

check|   sim got 0.04 | |
