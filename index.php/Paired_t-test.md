---
title: Paired t-test
layout: default
permalink: /index.php/Paired_t-test
---

# Paired t-test

## Paired t-test
This variation of [t-test](t-test) is used for Paired Data

### Paired Data
Two set of observations are ''paired'' if each observation in one set has exactly one corresponding observation is another set. 


Examples:
- pre- and post-test scores on the same person
- measures in pairs at the same time or place 
- outcome with or without a treatment - on same subject (cross-over study)


### Using in [R](R)
```carbon
library(openintro)
data(textbooks)
t.test(textbooks$diff, mu=x.bar.nul, alternative='two.sided')
```

or 

```text only
t.test(textbooks$uclaNew, textbooks$amazNew, paired=T, alternative='two.sided')
```


## Examples
### Example: Bookstore vs Amazon
- two samples: local bookshop and amazon 
- $\mu_\text{dif} = \mu_l - \mu_a$ - the mean of difference in the price

Test
- $H_0: \mu_\text{dif} = 0$ - there's no difference in the price
- $H_A: \mu_\text{dif} \ne 0$ - there's some difference 

Calculations
- $\bar{X}_\text{dif} = 12.76$
- [Standard Error](Standard_Error): $\text{SE}_{\bar{X}_\text{dif}} = \cfrac{s_\text{dif}}{\sqrt{n_\text{dif}}} = 1.67$
- $T = \cfrac{\bar{X}_\text{dif}}{\text{SE}_{\bar{X}_\text{dif}}} = \cfrac{12.76}{1.67} = 7.59$
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


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm

[Category:T-Test](Category_T-Test)
[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)