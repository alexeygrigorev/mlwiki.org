---
title: "One-Sample t-test"
layout: default
permalink: /index.php/One-Sample_t-test
---

# One-Sample t-test

## [One-Sample $t$-test](One-Sample_t-test)
This is a [t-test](t-test) for one variable
- it can be used to calculate a [Confidence Interval](Confidence_Intervals) for the true mean $\mu$ 
- the null value for $H_0$ might come from other research or from your knowledge 

Parameters:
- $\text{df} = n - 1$, where $n$ is the sample size 



## Examples
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


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm

[Category:T-Test](Category_T-Test)
[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)