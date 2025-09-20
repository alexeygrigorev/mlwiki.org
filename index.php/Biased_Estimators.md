---
title: "Biased Estimators"
layout: default
permalink: /index.php/Biased_Estimators
---

# Biased Estimators

## Biased Estimators
A [Point Estimate](Point_Estimate) is [''biased''](Bias) if
- the [Sampling Distribution](Sampling_Distribution) of some parameter being estimated is not centered around the true parameter value
- otherwise a Point Estimate is ''unbiased''


[Bias](Bias) of an estimate is the expected difference between the estimated value and the true value


## Unbiased Estimation
A statistic used to estimate a parameter is ''unbiased'' if the expected value of its sampling distribution is equal to the value of the parameter being estimated


### Proportion
In our coin flipping example
- a flip follows the [Bernoulli Distribution](Bernoulli_Distribution) with $p = 1/2$
  - $X \sim \text{Bernoulli}(0.5)$
- and $E(X) = 0.5$


For the entire experiment:
- 10 coin flips = 10 Bernoulli experiments with outcomes $X_1, ..., X_{10}$
- so, $\hat{p} = \cfrac{X_1 + ... + X_{10}}{10} = \bar{X}$
- thus, $E(\hat{p}) = p$ since $E(X_i) = p$ and $E(\bar{X}) = \cfrac{10 p}{10}  = p$
- and $\hat{p}$ is called ''unbiased estimator''


## Biased Estimation


### [Standard Deviation](Standard_Deviation)
Standard Deviation is biased estimate of the true standard deviation of the proportion
- so we typically use the sample standard deviation, which is 
  - $s = \cfrac{1}{n-1} \sum_{i=1}^n x_i $


Can simulate it to see that it's true
- suppose that we have the following population
  - <img src="http://habrastorage.org/files/d6f/7d4/88b/d6f7d488b10e4e819d77def52d4bd26d.png" alt="Image">
- we sample with sample size 25 many times (e.g. 5000) 
  - each time calculate biased std as well as corrected std
- then plot the sampling distributions
  - <img src="http://habrastorage.org/files/a33/440/4ea/a334404ea02a4ffd877dc57c7f0636b9.png" alt="Image">
  - we see that the corrected std is closer to the real population std
  - note that the real population std should not be corrected

<details>
<summary>R simulation</summary>

```r
sd.population = function(x) {
  n = length(x)
  m = mean(x)
  sqrt(sum((x - m) ^ 2) / n)
}

population = unlist(sapply(X=1:7, FUN=function(x) { rep(x, choose(8, x)) }))
pop = table(population)
b = barplot(pop)
text(x=b, y=pop-4, pop)

set.seed(1231)
sample.1 = rep(NA, 5000)
sample.2 = rep(NA, 5000)

size = 25

for (i in 1:5000) {
  s = sample(population, size)
  sample.1[i] = sd(s)
  sample.2[i] = sd.population(s)
}

true.pop = sd.population(population)
biased.center = mean(sample.2)
center = mean(sample.1)

c(true.pop, center, biased.center)
c(abs(true.pop - center), abs(true.pop - biased.center))

x = seq(0, 3, 0.1)

hist(sample.1, col=adjustcolor('blue', 1/4), breaks=35,
     probability=T, xlim=c(0.8, 1.9),
     main='Sampling Distributions of STD functions',
     xlab='Estimated Value')
abline(v=center, col='blue')
xspline(x=x, y=dnorm(x, mean=center, sd=sd(sample.1)), 
        lwd=1, shape=1, lty=2, border="blue")

hist(sample.2, col=adjustcolor('red', 1/4), probability=T,
     breaks=35, add=T)
abline(v=biased.center, col='red')
xspline(x=x, y=dnorm(x, mean=biased.center, sd=sd(sample.2)), 
        lwd=1, shape=1, lty=2, border="red")

abline(v=true.pop)
```
</details>



## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- https://en.wikipedia.org/wiki/Bias_of_an_estimator

[Category:Statistics](Category_Statistics)
[Category:R](Category_R)