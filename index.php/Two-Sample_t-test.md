---
title: Two-Sample t-test
layout: default
permalink: /index.php/Two-Sample_t-test
---

# Two-Sample t-test

## Two-Sample t-test
This type of [$t$-test](t-test) is used when we want to compare the means of two different samples
- suppose that we have two samples $a$ and $b$ of sizes $n_a$ and $n_b$ resp.
- we're interested in inferring something about $\mu_a - \mu_b$ 
- [Point Estimate](Point_Estimate) in this case is $\bar{X}_a - \bar{X}_b$
- [Standard Error](Standard_Error) is $\text{SE}_{\bar{X}_a - \bar{X}_b} = \sqrt{\text{SE}_a + \text{SE}_b } = \sqrt{ s^2_a / n_a + s^2_b / n_b}$
  - because $\text{SE}^2_{\bar{X}_a - \bar{X}_b} = \text{var}[\bar{X}_a - \bar{X}_b] = \text{var}[x_a] + \text{var}[x_b] = \text{SE}^2_a + \text{SE}^2_b$


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


## Example
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

## R code
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


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm

[Category:T-Test](Category_T-Test)
[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)