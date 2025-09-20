---
layout: default
permalink: /index.php/Sample_Size_Estimation
tags:
- statistical-tests
- statistics
title: Sample Size Estimation
---
## Sample Size
When we need to estimate the size of a sample?
- For [Confidence Intervals](Confidence_Intervals) we want to know how much we need to sample to get some Margin of Error
- For [Hypothesis Testing](Hypothesis_Testing) we want to control [Type II Errors](Type_II_Errors)


## [Confidence Intervals](Confidence_Intervals)
### [Binomial Proportion Confidence Intervals](Binomial_Proportion_Confidence_Intervals)
The best $n$?
- CI for $p$
  - $\beta = z_{\alpha/2} \sqrt{p(1-p)/n}$, 
- we want margin error be $\beta = 0.03$
- for 95% CI $\alpha = 0.025$

We plug everything in and calculate
- $0.03 = 1.96 \sqrt{p(1-p)/n}$
- use $p = 0.5$ (it's the worst-case scenario)
- $n = \left(\cfrac{1.96 \cdot 0.5}{0.03}\right)^2 \approx 1067$

What if we want margin error 0.01? 
- $0.01 = 1.96 \sqrt{0.5 \cdot 0.5 / n}$ or
- $n \approx 9604 = 9 \cdot 1067$ |   | |To cut the margin error in half we need 4 times bigger sample size|   |  - So lovering the margin is expensive  |

What if we want 99% CI instead of 95%? 
- $z_{\alpha/2} = z_{0.005} \approx 2.576$
- $0.03 = 2.576 \sqrt{0.5 \cdot 0.5 / n}$
- $n \approx 1843$

For 90% CI $n \approx 753$




### [R](R)
Example 1
```scdoc
p = 0.5
ME = 0.03
z = qnorm(0.025, mean=0, sd=1, lower.tail=F)
n = z^2 * p * (1 - p) / ME^2
```


Example 2:
- What sample size is needed to attain a margin error of 0.5% for 99% CI?
```text only
p = 0.5 // worst-case estimate
ME = 0.005
cl = 0.99
al = (1 - cl) / 2

z = qnorm(al, mean=0, sd=1, lower.tail=F)
n = z^2 * p * (1 - p) / ME^2
```


## Controlling False Negatives
Sample Size controls [Type II Errors](Type_II_Errors) - False Negatives
- What sample size is good for a certain margin of error?
- recall that a margin of error the "radius" of the [Confidence Interval](Confidence_Intervals) - boundaries of the [Point Estimate](Point_Estimate)


### [$Z$ Statistics](z-tests) for Means
Suppose we want to have a 95% confidence interval
- $Z = 1.96$
- $\text{ME}_{0.95} = Z \cdot \text{SE} = 1.96 \cfrac{\sigma}{\sqrt{n}}$
- we want $\text{ME} \leqslant 4$ 
- so $1.96 \cdot \cfrac{\sigma}{\sqrt{n}} \leqslant 4$, and we want to get $n$ from this inequality
  - NOTE: need to know $\sigma$, otherwise we should use $T$ statistics instead of $Z$ and estimate $\sigma$ by $s$
- e.g. suppose that we know that the whole country $\sigma$ is 25, so it might be a good estimate for $\sigma$ within a company


We get:
- $1.96 \cdot \cfrac{\sigma}{\sqrt{n}} \approx 1.96 \cdot \cfrac{25}{\sqrt{n}}$
- $1.96 \cdot \cfrac{25}{4} \leqslant \sqrt{n}$
- $\left( 1.96 \cdot \cfrac{25}{4} \right)^2 \leqslant n$
- $150.06 \leqslant n$

$\Rightarrow$ we need $n \geqslant 151$ to have ME of 4


## Stuff
<!-- TODO: Interesting Links --> - http://www.mailund.dk/index.php/2009/07/05/false-positives-and-large-sample-sizes/


Caveat, with such a large sample size, one would expect even tiny differences in occurrence to produce "strong" significance levels. See Why does frequentist hypothesis testing become biased towards rejecting the null hypothesis with sufficiently large samples?

http://stats.stackexchange.com/questions/108911/why-does-frequentist-hypothesis-testing-become-biased-towards-rejecting-the-null/

I've seen this claim before in Karl Friston's 2012 paper in NeuroImage, where he calls it the fallacy of classical inference.



## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://en.wikipedia.org/wiki/Sample_size
