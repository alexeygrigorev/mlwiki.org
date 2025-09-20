---
layout: default
permalink: /index.php/Q-Q_Plot
tags:
- data-analysis
- plots
- r
title: Q-Q Plot
---
## Q-Q Plot
### Probability Plot
A Probability plot is a technique for comparing two data sets
- e.g. two empirical observations
- or empirical set vs theoretical set

Commonly used:
- P-P plot, "Probability-Probability" or "Percent-Percent" plot;
- Q-Q plot, "Quantile-Quantile" plot, which is more commonly used.


### Normal Probability Plot
It's a special case of Q-Q plots:
- a Q-Q plot against the standard normal distribution;


The normal probability plot is formed by:
- Vertical axis: Ordered response values
- Horizontal axis: Normal order statistic medians or means (see rankit [https://en.wikipedia.org/wiki/Rankit])


Constructing 
1. order the observations 
1. determine the percentile for each
1. identify the $z$-score for each percentile 
1. create a [Scatterplot](Scatterplot)
  - observation (vertical) vs
  - $z$-score (horizontal)


if the data is normally distributed, $z$-scores on the horizontal axis should approximately correspond to their percentiles


## [R](R)
### Example 1
Evaluating the [Normal Distribution](Normal_Distribution) (see [http://rpubs.com/agrigorev/21480])

```gdscript
load(url("http://www.openintro.org/stat/data/bdims.RData"))
fdims = subset(bdims, bdims$sex == 0)

qqnorm(fdims$hgt, col="orange", pch=19)
qqline(fdims$hgt, lwd=2)
```

<img src="http://habrastorage.org/files/fb0/7c2/422/fb07c242281d4b25911459e38f3f1d58.png" alt="Image">

Does it look similar to real [Normal Distribution](Normal_Distribution)?
- it does
- let's simulate the normal distribution and compare 

```text only
set.seed(123)
sim.norm = rnorm(n=length(fdims$hgt), mean=mean(fdims$hgt), sd=sd(fdims$hgt))
qqnorm(sim.norm, col="orange", pch=19, main="Normal Q-Q Plot of simulated data")
qqline(sim.norm, lwd=2)
```

<img src="http://habrastorage.org/files/471/d9f/11a/471d9f11a690436f96f56ad0c4c544c4.png" alt="Image">


Can try to plot several simulations 

```tera term macro
qqnormsim = function(dat, dim=c(2,2)) {
  par(mfrow=dim)
  qqnorm(dat, main="Normal QQ Plot (Data)")
  qqline(dat)
  for (i in 1:(prod(dim) - 1)) {
    simnorm <- rnorm(n=length(dat), mean=mean(dat), sd=sd(dat))
    qqnorm(simnorm, main = "Normal QQ Plot (Sim)")
    qqline(simnorm)
  }
  par(mfrow=c(1, 1))
}
qqnormsim(fdims$hgt)
```

<img src="http://habrastorage.org/files/828/0c1/c21/8280c1c21ec94cd69916fc92d26dfe3b.png" alt="Image">

Looks like it's indeed normal


### Example 2
(Same data set as in example 1)

Let's take a look at another dataset

```text only
hist(fdims$wgt)
```

<img src="http://habrastorage.org/files/600/799/aa1/600799aa1fd24b03beed1d063fd7cb0f.png" alt="Image">

Looks a bit skewed 

```text only
qqnorm(fdims$wgt, col="orange", pch=19)
qqline(fdims$wgt, lwd=2)
```

<img src="http://habrastorage.org/files/fba/bb4/94c/fbabb494c4554aa8b9c88d58b0ae0213.png" alt="Image">

```text only
qqnormsim(fdims$wgt)
```

<img src="http://habrastorage.org/files/5ca/bf6/072/5cabf607296141b5b4297fe749f1bbd2.png" alt="Image">

Most likely not normal 


## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- https://en.wikipedia.org/wiki/Q-Q_plot
- https://en.wikipedia.org/wiki/Normal_probability_plot
