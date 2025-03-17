---
title: Binomial Proportion Tests
layout: default
permalink: /index.php/Binomial_Proportion_Tests
---

# Binomial Proportion Tests

## Binomial Proportion Tests
This is a family of [statistical tests](Hypothesis_Testing)  
- they are typically used for assessing the true proportions of the populations
- the [Sampling Distribution](Sampling_Distribution) underneath is [Binomial Distribution](Binomial_Distribution), but the tests  use $Z$-statistics and rely on [Normal Distribution](Normal_Distribution) and [Normal Approximation](Binomial_Distribution#Normal_Approximation)


### Exact Binomial Model
Not always we need to use the Normal Approximation
- sometimes we can model the null distribution directly with Binomial Model
- see [Exact Binomial Proportion Tests](Exact_Binomial_Proportion_Tests)


### Types Of Tests
- One-Sample Binomial Test - for testing if the proportion is equal to something
- Two-Sample Binomial Test - for testing the differences in proportions


## One-Sample Binomial Test
Suppose that we have a sample where outcomes are binary - e.g. only "success" and "failure"
- given the sample, we want to estimate what's the true proportion - and use [Binomial Proportion Confidence Intervals](Binomial_Proportion_Confidence_Intervals) for that
- but we can also set up a statistical test to check if the proportion is equal to some value 


So, given
- $n$ - sample size, $n_1$ - proportion of successful observations, 
- [Point Estimate](Point_Estimate) $\hat{p} = \cfrac{n_1}{n}$
- [Standard Error](Standard_Error) $\text{SE}_{\hat{p}} = \sqrt{ \cfrac{p \cdot (1 - p)}{n} } $
  - can use $p = \hat{p}$ instead of $p$ or $p = 0.5$ (it maximizes the margin of error)


Perform the test:
- $H_0: p = p_0$
- $H_A: p \ne p_0$ or $H_A: p < p_0$ or $H_A: p > p_0$
- calculate the $Z$ statistics and the $p$ value



### Conditions
- observations are independent
  - can satisfy when random-sample less than 10% of the population
- [Sampling Distribution](Sampling_Distribution) of $\hat{p}$ should be nearly Normal
- we should see at least 10 success and 10 failures in our samples ("success-failure condition")
  - enough to check that $n \cdot p_0 \geqslant 10$ and $n \cdot (1 - p_0) \geqslant 10$



### Confidence Intervals vs Proportion Tests
There's a clear parallel with [Binomial Proportion Confidence Intervals](Binomial_Proportion_Confidence_Intervals)
- if a CI includes the null value, then we fail to reject $H_0$
- otherwise we reject $H_0$ in favor of $H_A$ 



### Example 1
Newspaper collects data about support of some politician 
- there are $n = 500$ responses in the sample
- the support is estimates as $\hat{p} = 0.52$
- want to check if the true proportion is $p_0 = 0.5$ 


Verify the conditions:
- sample is random with less than 10% of the population
- $n \cdot p_0 = n \cdot (1 - p_0) = 500 \cdot 0.5 = 250 \geqslant 10$ 
- can apply the normal approximation

Test:
- $H_0: p_0 = 0.5, H_A: p_0 > 0.5$ - one-sided test
- $\text{SE}_{\hat{p}} = \sqrt{ \cfrac{0.5 \cdot (1 - 0.5)}{500} } \approx 0.022$
- $Z = \cfrac{\hat{p} - p_0}{ \text{SE}_{\hat{p}} }  = \cfrac{0.52 - 0.5}{0.022} \approx 0.89$
- <img src="http://habrastorage.org/files/56e/b12/500/56eb125008354212b8ffdfcf4e84e815.png" alt="Image">
- the $p$ value is $p = 0.1867$
- so can't reject $H_0$



### Example 2
- $n = 1046$
- 42% support the mayor 
- $p = \text{true support}$ (unknown)
- $\hat{p} = 0.42$ (estimated)

Question we want to answer:
- Is the true support less than 50% of the population? 


Our test
- $H_0: p = 0.5, H_A: p < 0.5$
- Can we reject $H_0$? 

Under $H_0$, $p = 0.5$, so
- We know that $\cfrac{\hat{p} - p}{\sqrt{p (1- p) / n }} \approx N(0, 1)$
- and it should be  $\cfrac{\hat{p} - p}{\sqrt{0.5 \cdot 0.5 / 1046}} \approx N(0, 1)$


Observed (assuming $H_0$)
- $\hat{p} - p = 0.42 - 0.5 = -0.08$


Now we calculate the $p$-value:
- $P\left(\hat{p} - p \leqslant -0.08\right)$ = 
- $P\left(\cfrac{\hat{p} - p}{\sqrt{0.5 \cdot 0.5 / 1046}} \leqslant \cfrac{- 0.08}{\sqrt{0.5 \cdot 0.5 / 1046}}\right) \approx $
- $P(N(0, 1) \leqslant -5.17) \approx 1 / 9000000$


Small|   |- The probability that (by chance we may get the sample with 0.42 support when the true level of support is 0.5) is 1 / 9000000 |- So we reject the $H_0$


### Example 3: Flipping a Beer Cap
- Suppose we flip a cap 1000 times, and the obtained proportion is $\hat{p} = 0.576$
- want to find out the real proportion. Is it $p = P(\text{Red}) = 0.5$?

The test:
- $H_0: p = 0.5, H_A: p \neq 0.5$ (2-sided)

Assuming $H_0$, the observed statistic is 
- $Z = \hat{p} - p = 0.567 - 0.5 = 0.076$


$p$-value:
- $P(| \hat{p} - p| \geqslant 0.076) =$ |- $P\left(\left|  \cfrac{\hat{p} - p}{\sqrt{0.5 \cdot 0.5 / 1000}} \right| \geqslant \left| \cfrac{0.076}{\sqrt{0.5 \cdot 0.5 /  1000}} \right|\right) \approx$ |- $P\left(| N(0, 1)| \geqslant 4.81\right) = $ |- $2 \cdot P(N(0, 1) \leqslant -4.81) \approx 1 / 661000$


Too small - so we reject the $H_0$.


### R-code (proportions)
Our test statistics is $z = \cfrac{\hat{p} - p}{\sqrt{p (1 - p) / n}}$
```scdoc
test.stat = (0.42 - 0.5) / sqrt(0.5 * 0.5 / 1046) // -5.17
pnorm(test.stat, mean=0, sd=1, lower.tail=T) // 1.17 * 10E-7
```


or, using '''binom.test''' 
```scdoc
x = round(0.42 * 1046, 0) // 439 successes
binom.test(x, 1046, p=0.5 // our H_0
           alternative="less")
// or alternative="two.sided"
```



## Two-Sample Binomial Proportion Test
Suppose we have two samples $a$ and $b$ 
- sample size: $n_a$ and $n_b$
- we calculate proportions from these samples $\hat{p}_a$ and $\hat{p}_a$
- want to see if the two samples have the same proportions or not

Test:
- $H_0: p_a = p_b$ or $H_0: p_a - p_a = 0$ - two samples have the same proportions
- $H_A: p_a \ne p_b$ or $H_A: p_b - p_b \ne 0$ - two samples have different proportions
  - could also be $H_A: p_b - p_b > 0$ or $H_A: p_b - p_b < 0$


Typical example
- calculate support of some politician in one year and later in another
- has the support grown over time? 
- has the support decreased? 
- has the support changed?


$\hat{p}_a - \hat{p}_b$ is a [Point Estimate](Point_Estimate) of $p_a - p_b$
- it's an unbiased estimate 
- if [Sampling Distribution](Sampling_Distribution)s for both $\hat{p}_a$ and $\hat{p}_b$ are nearly normal, then the difference also must be nearly normal 
- $\text{Var}(\hat{p}_a - \hat{p}_a) = \text{Var}(\hat{p}_a) + (-1)^2 \cdot \text{Var}(\hat{p}_a) = \cfrac{p_a (1 - p_a)}{n_a} + \cfrac{p_a (1 - p_a)}{n_a}$



Test statistics calculation:
- null value is typically 0 (this is the value of $p_a - p_b$ under $H_0$)
- $Z$-score: $Z = \cfrac{\text{p.e.} - \text{null value}}{\text{SE}_\text{p.e.}} = \cfrac{ \hat{p}_a - \hat{p}_b }{ \text{SE}_{\hat{p}_a - \hat{p}_b} } $ 
  - $\text{p.e.}$ is our point estimate and $\text{SE}_{\hat{p}_a - \hat{p}_b}$ is the [Standard Error](Standard_Error)


### Pooled Proportion Estimate
Under $H_0$ we assume that $p_a = p_b$ so we approximate '''both''' $p_a$ and $p_b$ by 
- $\hat{p} = \cfrac{n_a \hat{p}_a + n_b \hat{p}_b}{n_a + n_b}$
- This is called ''pooled estimate''
- $\text{SE} = \sqrt{\hat{p} (1 - \hat{p})(1/n_a + 1/n_b)}$
- Then $\cfrac{(\hat{p}_a - \hat{p}_b) - (p_a - p_b)}{\text{SE}} = \cfrac{\hat{p}_a - \hat{p}_b}{\text{SE}} \approx N(0, 1)$

And now we can compute $p$-values



### Example 1
Want to test if the drug reduces the death rate in heart attack patients 
- we set up a [Statistical Experiment](Statistical_Experiment)
- there are 1475 patients, whom we divided into two groups:
  - treatment group who receive the drug
  - control group who receive placebo

We record the following:
- $\hat{p}_c = 60/742$ - proportion of patients who died in the control group
- $\hat{p}_t = 41/733$ - proportion of patients who died in the treatment group

Test:
- $H_0: p_c = p_t$ or $H_0: p_c - p_t = 0$ - i.e. the drug doesn't work
- $H_A: p_c > p_t$ or $H_A: p_c - p_t > 0$ - i.e. the drug works



Perform the test:
- $\hat{p}_c - \hat{p}_t = 60/742 - 41/733 = 0.025$
- $\text{SE} = 0.013$
- $Z$-score: $Z = \cfrac{0.025}{0.013} = 1.92$
- for this $Z$ score we have $p = 0.027$ 
  - <img src="http://habrastorage.org/files/0cb/b90/bc0/0cbb90bc05dc43b68ca0ad0a2c7c9ea7.png" alt="Image">
  - (figure source: [OpenIntro](OpenIntro_Statistics_(book)), figure 4.22)
- with $\alpha = 0.05$, $p < \alpha$, so 
  - we reject $H_0$ in favor of $H_A$ and
  - conclude that the drug is effective


### Example 2
- poll #1: $n_1 = 1050$, $\hat{p}_1 = 0.57$
- poll #2: $n_2 = 1046$, $\hat{p}_2 = 0.42$


Was there a drop in the support? 
- Test: $H_0: p_1 = p_2, H_A: p_1 \neq p_2 $

- $\hat{p}_1 - \hat{p}_2 = 0.57 - 0.42 = 0.15$
- $\hat{p} = \cfrac{n_1 \hat{p}_1 + n_2 \hat{p}_2}{n_1 + n_2} \approx 0.495$


then $p$-value under $H_0$ is 
- $P( |  \hat{p}_1 - \hat{p}_2 | \geqslant 0.15 ) = $ |- $P( |  \cfrac{  (\hat{p}_1 - \hat{p}_2) - (p_1 - p_2)  }{\sqrt{\hat{p} (1 - \hat{p})(1/n_1 + 1/n_2)}} | \geqslant \cfrac{ 0.15 }{\sqrt{\hat{p} (1 - \hat{p})(1/n_1 + 1/n_2)}} ) \approx $ |- $P( |  N(0, 1) | \geqslant \cfrac{ 0.15 }{\sqrt{0.495 (1 - 0.495)(1/1050 + 1/1046)}} ) \approx $ |- $P( |  N(0, 1) | \geqslant 6.87 ) \approx 6 \cdot 10^{-12} $ |
Very low|   So we reject the $H_0$ and conclude that the support dropped (i.e. $p_1 \neq p_2$). | |
### Example 3
Obama support poll:
- $n_1 = 1010, \hat{p}_1 = 0.52$ (taken 12.08)
- $n_2 = 563, \hat{p}_2 = 0.48$ (taken 12.10)
- Seems that Obama's support declined over 2 years


Is that true?

We want to test if the support dropped: 
- $H_0: p_1 = p_2, H_A: p_1 \neq p_2 $
- $\hat{p}_1 - \hat{p}_2 = 0.52 - 0.48 = 0.04$

Pooled estimate:
- $\hat{p} = \cfrac{n_1 \hat{p}_1 + n_2 \hat{p}_2}{n_1 + n_2} \approx 0.506$

$p$-value (under $H_0$):
- $P(|  \hat{p}_1 - \hat{p}_2 | \geqslant 0.04 ) = $ |- $P \left( \left|  \cfrac{  (\hat{p}_1 - \hat{p}_2) - (p_1 - p_2)  }{\sqrt{\hat{p} (1 - \hat{p})(1/n_1 + 1/n_2)}} \right| \geqslant \cfrac{ 0.04 }{\sqrt{\hat{p} (1 - \hat{p})(1/n_1 + 1/n_2)}} \right) \approx $ |- $P \left( |  N(0, 1) | \geqslant \cfrac{ 0.04 }{\sqrt{0.506 (1 - 0.506)(1/1010 + 1/563)}} \right) \approx $ |- $P( |  N(0, 1) | \geqslant 1.52 ) \approx 0.129 $ |
Not so unlikely, so we cannot reject $H_0$. Perhaps no drop.


### R
```text only
n1 = 1050
n2 = 1046

phat1 = 0.57
phat2 = 0.42 

1. number of successes
x1 = round(n1 * phat1, 0)
x1 = round(n2 * phat2, 0)

prop.test(c(x1, x2), c(n1, n2), alternative="two.sided", correct=F)
```



## Links
- http://ocw.jhsph.edu/courses/methodsinbiostatisticsii/PDFs/lecture18.pdf
- http://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/binotest.htm

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://www.cliffsnotes.com/math/statistics/univariate-inferential-tests/test-for-comparing-two-proportions


[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)