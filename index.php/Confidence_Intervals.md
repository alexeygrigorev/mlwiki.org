---
title: "Confidence Intervals"
layout: default
permalink: /index.php/Confidence_Intervals
---

# Confidence Intervals

## Confidence Intervals
In [Inferential Statistics](Inferential_Statistics) we estimate a parameter of the population based on sample
- [Point Estimate](Point_Estimate) is just one single plausible value
- it's a good idea to expand it a bit and build a confidence interval around the point estimate
- and use [Standard Error](Standard_Error) as a measure of uncertainty in the Point Estimate to find this interval


Main idea - the CI should include the real parameter 


### Confidence Level
The degree of confidence at which we're sure the interval will span the true parameter is ''Confidence level''
- e.g. 95% confidence interval contains the estimated parameter with probability 0.95 - i.e. in 1 case out of 20 it will miss the real parameter


The idea of [Sampling Distribution](Sampling_Distribution) is important here
- we use it to calculate percentiles of the possible values, if the SD was centered at our point estimate
- so the SI should span the true value


Example
- we want to estimate the mean
- suppose we happen to know the sampling distribution: it's $N(\mu = 10, \sigma = 3.3)$
  - it's centered around the proportion mean $\mu$
  - and the [Standard Error](Standard_Error) is 3.3
- we draw a Point Estimate from the sampling distribution
  - we get $\bar{X} = 5.5$
- Assuming that the SD is centered around 5.5, we compute 95% CI
  - $z$-value is 1.96, so the interval is (-0.97 11.97)
- it includes the true value $\mu=10$


<img src="http://habrastorage.org/files/a76/ac7/b68/a76ac7b689e64323af65a6d4d0df5f9c.png" alt="Image">

{{ Hider |  |   title=R code |  |   content=
```carbon
x = seq(-10, 25, 0.3)
m = 10
se = 3.3

plot(x, dnorm(x, mean=m, sd=se), type='l', bty='n', lty=2, ylab='')
abline(v=m, lty=2)

m.observed = 5.5
abline(v=m.observed, col='red')
dy = dnorm(x, mean=5.5, sd=se)
lines(x, y=dy, col='red')

lo = m.observed - 1.96 * se
hi = m.observed + 1.96 * se
c(lo, hi)

x1 = min(which(x >= lo)); x2 = max(which(x <= hi)) 

polygon(x[c(x1, x1:x2, x2)],
        c(0, dy[x1:x2], 0), col=adjustcolor('red', 0.4), border=NA)

par(xpd=NA)

text(m, 0.13, m)
text(m.observed, 0.13, m.observed)

arrows(x0=lo, y0=0.02, x1=hi, y1=0.02, code=3, length=0.15)
text(m.observed, 0.02-0.005, 'confidence interval', cex=0.7)

par(xpd=FALSE)
```
}} 


A confidence interval consists of two parts
- left part - ''lower bound''
- right part - ''upper bound ''


"95% confident" means that if we took many many samples from the SD and build a CI from each, then about 95% of these CIs should contain the actual parameter being estimated (e.g. $p$ for binom, $\mu$ for mean)


<img src="http://habrastorage.org/files/2ab/3aa/77c/2ab3aa77ce294aa691b07d98778052f1.png" alt="Image">

So we see indeed that sometimes the CI doesn't include the true value
but we're 95% confident that a CI calculated from one sample will include it 



{{ Hider |  |   title=R code to produce the figure |  |   content=
```gdscript
load(url('http://s3.amazonaws.com/assets.datacamp.com/course/dasi/ames.RData'))
population = ames$Gr.Liv.Area

set.seed(1237)
n = 50
sampl = replicate(51, sample(population, n))
sampl.sd = apply(sampl, MARGIN=2, sd)
sampl.m  = apply(sampl, MARGIN=2, mean)

me = 1.96 * sampl.sd / sqrt(n)

plot_ci(sampl.m - me, sampl.m + me, mean(population))
```
}}


### Margin Of Error
If the [Sampling Distribution](Sampling_Distribution) is symmetric (e.g. [Normal Distribution](Normal_Distribution) or [t-Distribution](t-Distribution)) we can calculate the CI bounds by adding and subtracting the ''margin of error'' 
- '''margin of error''' is typically percentile ($z$ or $t$ score) multiplied by [Standard Error](Standard_Error)


### Critical Value
Critical Value shows the level of confidence in our interval
- for $\alpha = 0.025$ CI is 90%


### Types
Main types:
- [Binomial Proportion Confidence Intervals](Binomial_Proportion_Confidence_Intervals)
- [Confidence Intervals for Means](Confidence_Intervals_for_Means)


### [Statistical Simulation](Statistical_Simulation)
Not always it's possible to calculate everything with traditional methods 
- but when we know the truth and can control it, we can simulate and build the [Sampling Distribution](Sampling_Distribution), this way getting the CIs
- also, [Bootstrapping](Bootstrapping) (a [Resampling](Resampling) method) is a powerful strategy for calculating CIs 



## Extra Stuff
### Robustness
A method  for constructing CIs is ''robust'' if
- the resulting CIs include the theoretical parameter approximately the percentage claimed by the confidence level
- even if not all necessary conditions for the CIs are satisfied

[$t$-distribution](t-distribution) is very robust and works well for the [Normal Distribution](Normal_Distribution) as well as for skewed distributions


### Relationship with [Hypothesis Testing](Statistical_Tests_of_Significance)
{{Main |  Confidence Intervals and Statistical Tests}} |

### Additional Resources
- [applet](http://www.rossmanchance.com/applets/NewConfsim/Confsim.html) for simulating CIs 
- [another applet](http://www.utstat.utoronto.ca/alisong/moocapplets/ci_creation_applet)


## See Also
- [Sampling Distribution](Sampling_Distribution)
- [Inferential Statistics](Inferential_Statistics)
- [Hypothesis Testing](Hypothesis_Testing)

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- https://en.wikipedia.org/wiki/Confidence_interval



[Category:Statistics](Category_Statistics)
[Category:R](Category_R)