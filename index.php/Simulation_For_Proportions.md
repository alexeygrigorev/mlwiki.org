---
layout: default
permalink: /index.php/Simulation_For_Proportions
tags:
- r
- simulations
- statistical-tests
- statistics
title: Simulation For Proportions
---
## Simulation For Proportions
Sometimes [Statistical Inference](Statistical_Inference) can be done without applying theoretical models, but instead with using brute force: generating the data ourselves.


Consider Proportions test 
- there are a set of assumptions that have to be met to use the [Normal Approximation](Binomial_Distribution#Normal_Approximation)
- what if one of them is not met, e.g. Success-Failure condition?
- use [Exact Binomial Proportion Tests](Exact_Binomial_Proportion_Tests) - apply the Binomial Model directly
- or simulate draws from the binomial model and obtain the [Sampling Distribution](Sampling_Distribution) (or the null distribution)




## One-Sample Test
It's the same as One-Sample test for the normal approximation models:
- we have a sample and want to check if the true proportion parameter agree with some hypothetical parameter $p_0$
- and then we want to check if the data we observed align with this hypothesis

Test
- $H_0: p = p_0$
- $H_A: p \ne p_0$ or $H_A: p < p_0$ or * $H_A: p > p_0$ 
- $p$ - the true proportion, $p_0$ - the null value 


But instead of using some theoretical model, 
- we ourselves generate the null distribution 
- and then see how unusual the observed value is w.r.t. the generated null distr.


### Example
Consider the following example: 
- medical consultant helps patients 
- he claims that with his help the ratio of complications is lower than usually 
  - (i.e. lower than 0.10)
- is it true?


We want to test a hypothesis: 
- $H_0: p_A = 0.10$ - ratio of complications without a specialist 
- $H_A: p_A < 0.10$ - specialist helps, the complications ratio is lower than usual 
- note that we can't really check the claim because we have [Observational Studies](Observational_Studies) - to really check the claim we need to conduct a [Statistical Experiment](Statistical_Experiment)

Observed data:
- 3 complications in 62 cases
- $\hat{p} = 0.048$ 
- is it only due to chance? 


Normal Model
- the Success-Failure condition is not met: $p_A \cdot 62 = 0.10 \approx 6.2 < 10$
  - under $H_0$ we'd expect to see only 6.2 complications 
- thus cannot use [Normal Approximation](Binomial_Distribution#Normal_Approximation) and perform a [Binomial Proportion Test](Binomial_Proportion_Tests)


What we can do? 
- There is still a way to evaluate the $p$-value for this $p_A = 0.10$ - via simulations
- Simulate many draws from the population and build a Sampling Distribution (under $H_0$)
- then compute the probability of observing such  $\hat{p}$ in this distribution


Test
- Assume that the help of the specialist gives nothing
- i.e. 10% of cases will still have complications 
- under this assumptions we try to simulate 62 clients 


Simulation
- repeat many times (e.g. 5-10k) to build a [Sampling Distribution](Sampling_Distribution)
  - draw a sample from the [Binomial Distribution](Binomial_Distribution) with $p=0.10$ and $n=62$
  - calculate $\hat{p}_\text{sim}$ from this sample
- draw a histogram 
- and shade bars that support the $H_A$ - ones with $hat{p}_\text{sim} < 0.048$
- the shaded area represents the $p$-value - the probability of observing such small $\hat{p}$ only due to chance 



This is the histogram of the Sampling Distribution we obtained:
- <img src="http://habrastorage.org/files/3d9/618/2be/3d96182be8a746c29217bee8274b6c33.png" alt="Image">


From 10k draws 487 turned out to be below $\hat{p}$
- which means $p$-value is $487/10000 = 0.0487 < 0.05$
- so we reject $H_0$ in favor of $H_A$ and conclude that there's indeed some relation between the participation of the consultant and the complications ratio


R code:

```text only
n = 62
p = 0.10
m = 10000

set.seed(31313)
samp.dist = rbinom(n=m, size=n, prob=p) / n

p.hat = 0.048
sum(samp.dist <= p.hat) 
p.val = sum(samp.dist <= p.hat) / length(samp.dist)
p.val

ac = cut(samp.dist, breaks=18)
means = tapply(samp.dist, ac, mean)
levels(ac) = round(means, digits=3)

tbl = table(ac) / length(samp.dist)
tbl
cl = rep('grey', length(tbl))
cl[1:4] = 'black'

barplot(tbl, col=cl, las=2)
```



## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
