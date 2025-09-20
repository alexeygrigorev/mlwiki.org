---
layout: default
permalink: /index.php/Standard_Error
tags:
- statistics
title: Standard Error
---
## Sampling Distribution
### Parameter Estimation
Goal of [Inferential Statistics](Inferential_Statistics) - to make conclusion about the whole population based on a sample
- So we estimate the parameters based on sampled data 
  - if the estimate is just one number, we call it a [Point Estimate](Point_Estimate)
- And with different samples (from the same population) we get different estimates of the same parameter - so we have ''variability'' (''sampling variability'') in estimates 
- The probability distribution of the parameter estimate is called ''Sampling Distribution'' 


### Sampling Distribution
The sampling distribution represents the distribution of point estimates based on samples of fixed size from the same population
- we can think that a particular [Point Estimate](Point_Estimate) is drawn from the sampling distribution
- and [Standard Error](Standard_Error) is the measure of variability (e.g. how uncertain we are about our estimate)


## Examples
### Example 1
- Suppose we flip a coin 10 times and count the number of heads
- Our parameter of interest is $p = p(\text{heads})$
- $\hat{p}$ - estimate of $p$
  - $\hat{p} = \cfrac{\text{# of heads}}{\text{total # of flips}}$
  - i.e. $\hat{p}$ is calculated from data

```text only
set.seed(134)
rbinom(10, size=10, prob=0.5)
```

We get different results each time:

|   Trial  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |   Outcome   |  4  |  6  |  7  |  4  |  5  |  3  |  4  |  6  |  3  |  6 |

Since we know that theoretically this [Random Variable](Random_Variable) follows [Binomial Distribution](Binomial_Distribution), we can model the sampling distribution as

```text only
d = dbinom(1:10, size=10, prob=0.5)
bp = barplot(d)
axis(side=1, at=bp[1:10], labels=1:10)
```

<img src="http://habrastorage.org/files/b39/001/83f/b3900183fe9f478fadf895deed1d0d56.png" alt="Image">


This sampling distribution is used for [Binomial Proportion Confidence Intervals](Binomial_Proportion_Confidence_Intervals) and for [Binomial Proportion Test](Binomial_Proportion_Test)
- note that as the sample size grows it becomes more reasonable to use the [Normal Approximation](Binomial_Distribution#Normal_Approximation) 



### Example 2
```gdscript
load(url('http://s3.amazonaws.com/assets.datacamp.com/course/dasi/ames.RData'))
area = ames$Gr.Liv.Area
sample_means50 = rep(NA, 5000)
 
for (i in 1:5000) {
  samp = sample(area, 50)
  sample_means50[i] = mean(samp)
}

hist(sample_means50, breaks=13, probability=T, col='orange',
     xlab='point estimates of mean', main='Sampling distribuion of mean')
```

<img src="http://habrastorage.org/files/d9a/06a/02d/d9a06a02d0944fb495c81c29daa29047.png" alt="Image">


### Example: Running Mean
There's another example that shows that the more data we have, the more accurate our point estimates are
- A ''running mean'' (or '[Moving Average](Moving_Average)') is a sequence of means, where each following mean uses one extra observation
- If we take the moving average from 1 data point and keep including next ones, it approaches the "true mean"

<img src="http://habrastorage.org/files/454/073/b0a/454073b0ac4149c789916b3dba2c61c6.png" alt="Image">


<details><summary>R code to produce the figure</summary>

```carbon
library(openintro)
data(run10Samp)
time = run10Samp$time
avg = sapply(X=1:100, FUN=function(x) { mean(time[1:x]) })
plot(x=1:100, y=avg, type='l', col='blue',
     ylab='running mean', xlab='sample size', bty='n')
abline(h=mean(time), lty=2, col='grey')
```

</details>


So it illustrates that the more sample size is, the better we can estimate the parameter



## Typical Sampling Distributions
- [Normal Distribution](Normal_Distribution) for this
- [t Distribution](t_Distribution) for that


## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- DataCamp, Lab 3A - Sampling distributions [http://rpubs.com/agrigorev/21595]
- https://en.wikipedia.org/wiki/Sampling_distribution
