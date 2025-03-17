---
title: T-tests
layout: default
permalink: /index.php/T-tests
---

# T-tests

## $t$ Tests
$t$-tests is a family of [Statistical tests](Hypothesis_Testing) that use $t$-statistics (those values come from the [$t$-distribution](t_Distribution)) to calculate $p$-values


The following tests are $t$-tests:
- one-sample $t$-test - for comparing the mean of a sample against some given mean
- two-sample $t$-test - for comparing the means of two samples
- paired $t$-test - for Matching Pairs setup
- pairwise $t$-test - for comparing the means of more than two samples


## When To Use
### Assumptions
Assumptions for $t$ tests are similar to the assumptions of the [$z$-tests](z-tests)
- Observations are independent (if less than 10% of population is sampled, then we can make sure it's satisfied)
- Sample size is sufficiently large so [C.L.T.](Central_Limit_Theorem) holds
- Moderate skew, few outliers (not too extreme)


### vs [$z$-tests](z-tests)
Sample Size
- the sample size can be smaller than for $z$-tests 
- so it can be smaller than 30 - after 30 we can safely use $z$-tests with almost the same outcomes 

$t$-distribution:
- the tails are thicker than for $N(0,1)$ and observations are more likely to fall within 2$\sigma$ from the mean
- this is exactly the correction we need to account for poorly estimated [Standard Error](Standard_Error) when the sample size is not big



## One-Sample t-test
This is a test for one variable
- it's used mainly to calculate a [Confidence Interval](Confidence_Intervals) for the true mean $\mu$ 
- the null value for $H_0$ might come from other research or from your knowledge 

Parameters:
- $\text{df} = n - 1$ with $n$ being the sample size 


### Example 1
- Sample: $n = 60, \bar{X} = 7.177, s = 2.948$
- True mean $\mu$ is unknown 

Let's run a test:
- $H_0: \mu = 0, H_A: \mu > 0$ (this is one-sided test)
- Under $H_0$, we know that $\cfrac{\bar{X} - \mu}{\sqrt{s^2 / n}} \approx t_{n - 1}$
- Observed: $\bar{X} - \mu = 7.177 - 0 = 7.177$
- How plausible is the observed value under $H_0$? 


The probability of observing this value is 
- $P(\bar{X} - \mu \geqslant 7.177) = $
  - $P\left(\cfrac{\bar{X} - \mu}{\sqrt{s^2 / n}} \geqslant \cfrac{7.177}{\sqrt{s^2 / n}}\right) \approx$
  - $P\left(t_{59} \geqslant \cfrac{7.177}{\sqrt{2.948^2 / 60}}\right) \approx$
  - $P(t_{59} \geqslant 18.86) \approx 1 / 10^{26}$

Extremely small|   So we reject $H_0$ and conclude that $\mu > 0$ | |

### Example 2
- Sample $n = 400, \bar{X} = -14.15, s = 14.13$
- Test: $H_0: \mu = 0$  vs $H_A: \mu \neq 0$ (this is a 2-sided)

We know that
- $\cfrac{\bar{X} - \mu}{\sqrt{s^2 / n}} \approx t_{n - 1} = t_{399}$


$p$-value:
- $P( |  \bar{X} - \mu | \geqslant | -14.15 - 0 |) = $ |  - $P\left( \left|  \cfrac{\bar{X} - \mu}{\sqrt{s^2 / n}} \right| \geqslant \cfrac{14.15}{\sqrt{14.13^2 / 400}}\right) \approx $ |  - $P( |  t_{399} | \geqslant 20.03 ) =$ |  - $2 \cdot P( t_{399} \leqslant -20.03) \approx$
  - $1 / 3.5 \cdot 10^{64}$


Extremely small|   Reject the $H_0$ and conclude that $\mu \neq 0$ | |
### R code
Our test statistic is $T = \cfrac{\bar{X} - \mu}{\sqrt{s^2 / n}}$.

```gdscript
xbar = mean(ch)
s2 = var(ch)
n = length(ch)
mu = 0

t = (xbar - mu) / sqrt(s2 / n) // 18.856
pt(t, df=n-1, lower.tail=F) // 5.84E-24
// so we reject
```




## Paired t-test
### Paired Data
Two set of observations are ''paired'' if each observation in one set has exactly one corresponding observation is another set. 


Examples:
- pre- and post-test scores on the same person
- measures in pairs at the same time or place 
- outcome with or without a treatment - on same subject (cross-over study)


### [R](R) Function
```carbon
library(openintro)
data(textbooks)
t.test(textbooks$diff, mu=x.bar.nul, alternative='two.sided')
```

or 

```text only
t.test(textbooks$uclaNew, textbooks$amazNew, paired=T, 
       alternative='two.sided')
```



### Example: Bookstore vs Amazon
- two samples: local bookshop and amazon 
- $\mu_\text{dif} = \mu_l - \mu_a$ - the mean of difference in the price

Test
- $H_0: \mu_\text{dif} = 0$ - there's no difference in the price
- $H_A: \mu_\text{dif} \ne 0$ - there's some difference 

Calculations
- $\bar{x}_\text{dif} = 12.76$
- Standard Error: $\text{se}_{\bar{x}_\text{dif}} = \cfrac{s_\text{dif}}{\sqrt{n_\text{dif}}} = 1.67$
- $T = \cfrac{\bar{x}_\text{dif}}{\text{se}_{\bar{x}_\text{dif}}} = \cfrac{12.76}{1.67} = 7.59$
- $p = 6 \cdot 10^{-11}$, less than $\alpha = 0.05$, so we reject $H_0$


```carbon
library(openintro)
data(textbooks)

hist(textbooks$diff, col='yellow')

n = length(textbooks$diff)
s = sd(textbooks$diff)
se = s / sqrt(n)

x.bar.nul = 0
x.bar.dif = mean(textbooks$diff)

t = (x.bar.dif - x.bar.nul) / se
t
p = pt(t, df=n-1, lower.tail=F) * 2
p
```

or 

```text only
t.test(textbooks$diff, mu=x.bar.nul, alternative='two.sided')
```


### Example 2
Let $\mu_d = \mu_0 - \mu_1$ be the difference between two methods

Our test:
- $H_0: \mu_d = 0, H_A: \mu_d \neq 0$

Say, we have:
- $\bar{X}_d = 6.854$
- $s_d = 11.056$
- $n = 398$

Test statistics:
- $\cfrac{\bar{X}_d - 0}{s_d / \sqrt{n}} = \cfrac{6.854}{11.056 / \sqrt{398}} \approx 12.37$

Then we compare it with $t_{397}$
- $p$-value is $2.9 \cdot 10^{29}$

And we conclude that the difference between the two methods is not 0



## Two-Sample t-test
This variation of $t$-test is used when we want to compare the means of two different samples
- suppose that we have two samples $a$ and $b$ of sizes $n_a$ and $n_b$ resp.
- we're interested in inferring something about $\mu_a - \mu_b$ 
- [Point Estimate](Point_Estimate) in this case is $\bar{x}_a - \bar{x}_b$
- [Standard Error](Standard_Error) is $\text{SE}_{\bar{x}_a - \bar{x}_b} = \sqrt{\text{SE}_a + \text{SE}_b } = \sqrt{ s^2_a / n_a + s^2_b / n_b}$
  - because $\text{SE}^2_{\bar{x}_a - \bar{x}_b} = \text{var}[\bar{x}_a - \bar{x}_b] = \text{var}[x_a] + \text{var}[x_b] = \text{SE}^2_a + \text{SE}^2_b$


The test is of the following form
- $H_0: \mu_a = \mu_b$, or $H_0: \mu_a - \mu_b = 0$
- $H_A: \mu_a \neq \mu_b$ or $H_A: \mu_a - \mu_b \neq 0$ (two-sided, can also be $<$ or $>$)


So, test statistics:
- $T = \cfrac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{s_1^2 / n_1 + s_2^2 / n_2}}$
- $T \approx t_{\text{df}}$
- $\text{df}$ depends on a few things, discussed below


### Welch-Satterthwaite Approximation
What is $\text{df}$ there?
- Welch-Satterthwaite Approximation for df is
- $\text{df} = \cfrac{( s_1^2 / n_1 + s_2^2 / n_2 )^2 }{ \frac{(s_1^2 / n_1)^2 }{n_1 - 1} + \frac{(s_2^2 / n_2)^2 }{n_2 - 1} }$

This can be a non-integer value, but that's fine


### Pooled Variance Estimation
- Can we "pool" the samples?
- Yes, but only under assumption that $\sigma_1^2 = \sigma_2^2$ (in other words, we assume that the variances are equal)

We can replace $s_1^2$ and $s_2^2$ by the ''pooled variance'':
- $s^2 = \cfrac{(n_1 - 1) s_1^2 + (n_2 - 1) s_2^2 }{ (n_1 - 1) + (n_2 - 1)}$
- and $\text{df} = (n_1 - 1) + (n_2 - 1) = n_1 + n_2 - 2$



### Example 1
- males: $n_1 = 281 $
- females: $n_2 = 199$
- $\bar{X}_1 = -12.9, s_1^2 = 181.5$
- $\bar{X}_2 = -17.1, s_2^2 = 231.5$
- $\bar{X}_1 - \bar{X}_2 = -12.9 + 17.1 = 4.2$

We then calculate
- $\text{df} = 200.09$
- so $T_{0.025, 200.09} = 1.97$


We have the following test
- $H_0: \mu_1 = \mu_2, H_A: \mu_1 \neq \mu_2$
- and $\bar{X}_1 - \bar{X}_2 = 4.2$


$p$-value:
- $P(|  \bar{X}_1 - \bar{X}_2 |  \geqslant  4.2 ) = $ |- $P \left( \left|  \cfrac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{s_1^2 / n_1 + s_2^2 / n_2}} \right|  \geqslant  \cfrac{4.2}{\sqrt{s_1^2 / n_1 + s_2^2 / n_2}} \right) \approx $ |- $P\left( | t_\text{df} |  \geqslant \cfrac{4.2}{\sqrt{181.5 / 281 + 231 / 119}} \right) = 0.0097$ |
pretty small, so we reject the $H_0$.


### Example 2
Life expectancy in E.Asia and Pacific vs S.Asia
- EA&P: $n_1: 30, \bar{X}_1 = 73.1, s_1^2 = 38.7$
- SA: $n_2: 8, \bar{X} = 67.0, s_2^2 = 72.5$
- $\bar{X}_1 - \bar{X}_2 = 73.1 - 67.0 = 6.1$


We then calculate
- $\text{df} = 9.09$ by Welch-Satterthwaite Approximation
- $T_{0.025, 0.09} = 2.26$


Our test:
- $H_0: \mu_0 = \mu_1, H_A: \mu_0 \neq \mu_1$

$p$-value:
- $P(|  \bar{X}_1 - \bar{X}_2 |  \geqslant  6.1 ) = $ |- $P \left( \left|  \cfrac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{\sqrt{s_1^2 / n_1 + s_2^2 / n_2}} \right|  \geqslant  \cfrac{6.1}{\sqrt{s_1^2 / n_1 + s_2^2 / n_2}} \right) \approx $ |- $P ( | t_\text{df} |  \geqslant 1.90 ) \approx 0.09$ |
Not so small - we can't reject the $H_0$, it might be true that $\mu_0 = \mu_1$


### R (Means)
```text only
male = skeletons[sex == '1', 6]
female = skeletons[sex == '2', 6]

# critical value
qt(0.025, df=200.9, lower.tail=F)
```

or 

```text only
t.test(male, female, mu=0, conf.level=0.95, alternative='two.sided')
```



## Pairwise t-test
- we have $n$ groups, $n > 2$
- we conduct a series of Two-Sample t-tests to find out which groups are different 
- e.g. in post-[ANOVA](ANOVA) analysis


### Controlling [Family-Wise Error Rate](Family-Wise_Error_Rate)
It's important to modify $\alpha$ to avoid [Type I Errors](Type_I_Errors)
- when we run many tests, it's inevitable that we make them just by chance

E.g. use [Bonferroni Correction](Bonferroni_Correction)
- use modified confidence level $\alpha^* = \alpha \cdot \cfrac{1}{K}$
- where for $k$ groups $K= \cfrac{k \cdot (k - 1)}{2}$ 


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm

[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)