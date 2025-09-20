---
layout: default
permalink: /index.php/Z-tests
tags:
- r
- statistical-tests
- statistics
title: Z-tests
---
## $Z$ Tests
This is a family of [statistical tests](Hypothesis_Testing) that use [Normal Model](Normal_Distribution) to compute test statistics 
- most of the time $Z$ tests are restricted versions of [$t$-tests](t-tests), so it's more advisable to use $t$ tests, especially because for larger degrees of freedom [$t$-distribution](t_Distribution) is very close to Normal


The following are $z$ tests
- one-sample $z$-test - for comparing the mean of a sample against some given mean
- paired $z$-test - for Matching Pairs setup
- two-sample $z$-test - for comparing the means of two samples



## Assumptions
- Observations are independent (if less than 10% of population is sampled, then we can make sure it's satisfied)
- Sample size is sufficiently large so [C.L.T.](Central_Limit_Theorem) holds
- Moderate skew, few outliers (not too extreme)

If these assumptions are hold, then we can use the $z$ statistics 
- if sample size is smaller, then it's better to use [$t$-tests](t-tests)
- if the distribution has skews and outliers, use simulations <!-- TODO: add link --> |- but in any case the observations have to be independent |

## One-Sample $z$ Test
### Example 1: One-Sided
Assume we have the following
- <img src="http://habrastorage.org/files/9d6/bf3/a36/9d6bf3a3673e4ca9a37fe1e94a481b29.png" alt="Image">
- source: [OpenIntro](OpenIntro_Statistics_(book)), figure 4.14

Sample: 110 students, conditions are met:
- less than 10% of all students are sampled,
- sufficiently large $\geqslant 30$
- only a couple of outliers, which is acceptable for sample size $n=110$


So we can apply the Normal Model and do the following test:
- $H_0: \mu = 7$ - students sleep only 7 hours on avg, $H_A: \mu > 7$ students sleep more than 7 hours on avg


Calculate 
- the sample mean: $\bar{x} = 7.42$
- the [Standard Error](Standard_Error): $\text{SE}_{\bar{x}} = \cfrac{s_x}{\sqrt{n}} = \cfrac{1.75}{110} = 0.17$

$Z$ score:
- then compute the $Z$ score: $Z = \cfrac{x - \text{null value}}{\text{SE}_{\bar{x}}} = \cfrac{7.42 - 7}{0.17} = 2.47$
- then calculate the $p$-value for this test statistics 
  - $p = 0.007$
  - <img src="http://habrastorage.org/files/4c3/5c0/ae1/4c35c0ae1faf403cbb35255a3bd20544.png" alt="Image">
  - source: [OpenIntro](OpenIntro_Statistics_(book)), figure 4.15


so, under $H_0$ the probability of observing such $\bar{x}$ is just $p = 0.007$
- our level of significance is $\alpha 0.05$, we compare $\alpha$ and $p$: 
- $p =  0.007 < 0.05 = \alpha$,
- $\Rightarrow$ we reject $H_0$ in favor of $H_A$: what we observe is so unusual under $H_0$ which casts a doubt on $H_0$ and provides strong evidence to $H_A$
- so we reject $H_0$ and conclude that on average students sleep more than 7 hours


## Other $z$-tests
### Paired $z$-test
Analogously to Paired $t$-test, we can use $z$ statistics to analyze matched pairs data, provided that the sample size is sufficiently large 

Example:
- two samples: local bookshop and amazon 
- $\mu_\text{dif} = \mu_l - \mu_a$ - the mean of difference in the price
- $H_0: \mu_\text{dif} = 0$ - there's no difference in the price
- $H_A: \mu_\text{dif} \ne 0$ - there's some difference 
- $\bar{x}_\text{dif} = 12.76$
- Standard Error: $\text{se}_{\bar{x}_\text{dif}} = \cfrac{s_\text{dif}}{\sqrt{n_\text{dif}}} = 1.67$
- $Z = \cfrac{\bar{x}_\text{dif}}{\text{se}_{\bar{x}_\text{dif}}} = \cfrac{12.76}{1.67} = 7.59$
- this is too large $z$ score, but let's calculate the $p$-value
- $p = 0.00004$, less than $\alpha = 0.05$, so we reject $H_0$


```carbon
library(openintro)
data(textbooks)

hist(textbooks$diff, col='yellow')

n = length(textbooks$diff)
s = sd(textbooks$diff)
se = s / sqrt(n)

x.bar.nul = 0
x.bar.dif = mean(textbooks$diff)

z = (x.bar.dif - x.bar.nul) / se
z

p = pnorm(z, mean=x.bar.nul, sd=se, lower.tail=F) * 2
p
```




## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm
