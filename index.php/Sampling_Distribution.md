---
title: Sampling Distribution
layout: default
permalink: /index.php/Sampling_Distribution
---

# Sampling Distribution

## Estimation
Our goal is to be able to estimate theoretical parameters with a data sample. 

Example:
- we want to estimate the probability of getting heads in coin flipping [experiment](Experiments)
- flip a coin 10 times, 
- count number of heads 

Experiment:
- Our parameter of interest is $p = p(\text{heads})$
- Data: result of 10 coin flips
- $\hat{p}$ - estimate of $p$
: $\hat{p} = \cfrac{\text{# of heads}}{\text{total # of flips}}$
: i.e. $\hat{p}$ is calculated from data


## Sampling Distribution
- if we repeat over and over again, each time we will probably have different estimates of $\hat{p}$
- so there is a ''variability'' in the estimate
- this is called ''sampling variability'', and it occurs because of the randomness in our data


The probability distribution of all the possible values of an estimator is it's ''sampling distribution''.


### Unbiased estimation
In our coin flipping example
- a flip follows the [Bernoulli Distribution](Bernoulli_Distribution) with $p = 1/2$
: $X \sim \text{Bernoulli}(0.5)$
- and $E(X) = 0.5$


For the entire experiment:
- 10 coin flips = 10 Bernoulli experiments with outcomes $X_1, ..., X_{10}$
- so, $\hat{p} = \cfrac{X_1 + ... + X_{10}}{10} = \bar{X}$
- thus, $E(\hat{p}) = p$ since $E(X_i) = p$ and $E(\bar{X}) = \cfrac{10 p}{10}  = p$
- and $\hat{p}$ is called ''unbiased estimator''


A statistic used to estimate a parameter is ''unbiased'' if the expected value of its sampling distribution is equal to the value of the parameter being estimated


### Variance estimation
- For one observation $X \sim \text{Bernoulli}(p)$, variance $\text{Var}(X)$ is:
: $\text{Var}(X) = \sum_{x} (x - E(X))^2 p(X) = (1 - p)^2 p + (0 - p)^2 (1 - p) = p - p^2 = p(1 - p)$
- For $n$ observations $X_1, ..., X_{n}$ with $\hat{p} = E(X)$
: since $\text{Var}(\bar{X}) = \cfrac{\sum X_i}{n}$,
: $\text{Var}(\hat{p}) = \cfrac{p(1 - p)}{n}$ and $\text{sd}(\hat{p}) = \sqrt{\cfrac{p(1-p)}{n}}$,
So we get more and more precise answers over time 


And by the [Central Limit Theorem](Central_Limit_Theorem), for large $n$ the sampling distribution is approximately 

$N\left(p, \cfrac{p(1-p)}{n}\right)$


## Theoretical World Model
In the [Normal Distribution](Normal_Distribution) we have  $N(\mu, \sigma^2)$, and we're interested in $\mu$
- Say we have $n$ data values $X_1, ..., X_n$ from independent observations 
- Estimator of $\mu$ is $\bar{X} = \cfrac{X_1 + ... + X_n}{n}$
- So $E(\bar{X}) = \mu$, and $\bar{X}$ - unbiased estimator of $\mu$
- Variance of $\bar{X}$ is $\text{Var}(\bar{X}) = \cfrac{\sigma^2}{n}$ and $\text{sd}(\bar{X}) = \cfrac{\sigma}{\sqrt{n}}$
- And by the [Central Limit Theorem](Центральная_предельная_теорема) we have $\bar{X} \sim N(\mu, \cfrac{\sigma^2}{n})$


So, 
- distribution of $\hat{p} \sim N\left(p, \cfrac{p(1-p)}{n}\right)$
- distribution of $\bar{X} \sim N\left(\mu, \cfrac{\sigma^2}{n}\right)$


For data, unbiased variance is 
- $\text{Var}(X) = \cfrac{1}{n-1} \sum (X_i - \bar{X})^2$ (unbiased)
- not $\text{Var}(X) = \cfrac{1}{n} \sum (X_i - \bar{X})^2$ (biased)


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))


[Category:Statistics](Category_Statistics)
[Category:Probability](Category_Probability)