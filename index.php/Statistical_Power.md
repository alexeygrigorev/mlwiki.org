---
title: "Statistical Power"
layout: default
permalink: /index.php/Statistical_Power
---

# Statistical Power

## Statistical Power
How to detect a false $H_0$? 
- ''The power of a test'' is the probability of making a correct decision (by rejecting the $H_0$) when the $H_0$ is false. 
- The higher the power, the more sensitive the test in detecting the false hypothesis.

How to have higher power? 
- the further the alternative value is away from the $H_0$, the higher the power
- A higher level of significance $\alpha$ gives higher power
- less variability - less power
- the larger the sample size - the greater the power

To determine the sample size needed for a study set $\alpha$ and the desired power, decide of the $H_A$, estimate $\sigma$ and calculate the sample size




### Power Of Test
Consider this test:
- $H_0$: average blood pressure of employers is the same as national average,
  - i.e. $H_0: \mu = 130$
- $H_A$: it's different
  - $H_A: \mu \ne 130$

Suppose that $H_A$ is actually true
- what is our chance to make [Type II Errors](Type_II_Errors)? - i.e. fail to reject $H_0$ when we should reject it 


Suppose that the actual average is 132: i.e. $\mu = 132$
we sample 100 individuals 
then the true sampling distribution of $\bar{x}$ is $N(132, 2.5)$
since $\text{SE} = \cfrac{25}{\sqrt{100}}$
what is the probability of successfully rejecting $H_0$?

We can divide it onto two probability questions:

- what are possible values of $\bar{x}$ sufficient to reject $H_0$? (under $H_0$|  ) |- use this hypothetical [Sampling Distribution](Sampling_Distribution) to find the probability of observing such values of $\bar{x}$ (from the 1st step) |

Step 1
The null distribution is $N(130, 2.5)$
the 2.5% tails are those with $Z = \pm 1.96$

$-1.96 = z_1 = \cfrac{x_1 - 130}{2.5}
$x_1 = 125.1$


$+1.96 = z_2 = \cfrac{x_2 - 130}{2.5}
$x_2 = 134.9$

<img src="http://habrastorage.org/files/a3a/866/c33/a3a866c339cb4a35b54543a63b0ac593.png" alt="Image">


Step 2

Now we compute the probability of rejecting $H_0$ if $\bar{x}$ actually came from $N(132, 2.5)$

$z_\text{left} = \cfrac{125.1 - 132}{2.5} = -2.76$
area: 0.003
$z_\text{right} = \cfrac{134.9 - 132}{2.5} = 1.16$
area: 0.123

<img src="http://habrastorage.org/files/aff/5d0/286/aff5d02862104e998bcab1248b983de3.png" alt="Image">

so the probability of rejecting $H_0$ if the true mean is 132 is 
0.004 + 0.123 = 0.126

This is the power of a test 
the probability of rejecting the $H_0$


The power varies depending on what we suppose the truth is 

If the power of a test is 0.979, what's the type 2 error rate? 
Type 2 error rate is the probability of failing to reject $H_0$ 
so type 2 error rate is 1 - 0.979 = 0.021


```carbon
x = seq(120, 140, 0.1)
null.mu = 130; se = 2.5
null.y = dnorm(x, mean=null.mu, sd=se)

plot(x, null.y, type='l', lty=2, bty='n',
     ylab='Probability')

x1 = 125.1; x2 = 134.9
abline(v=c(null.mu, x1, x2), lty=2)


real.mu = 132
real.y = dnorm(x, mean=real.mu, sd=se)

lines(x, real.y, col='red', lwd=2)
abline(v=real.mu, col='red', lwd=2)

x1.left = max(which(x <= x1))
polygon(x=x[c(1, 1:x1.left, x1.left)],
        y=c(0, real.y[1:x1.left], 0), 
        col=adjustcolor('red', 0.5), border=NA)

x2.left = min(which(x >= x2))
x2.right = length(x)
polygon(x=x[c(x2.left, x2.left:x2.right, x2.right)],
        y=c(0, real.y[x2.left:x2.right], 0), 
        col=adjustcolor('red', 0.5), border=NA)
```


## Power Analysis
{{ TODO |  what's that? }} |- e.g. see here [http://stats.stackexchange.com/questions/108186]
- http://www.statmethods.net/stats/power.html - in R
- http://www.marketingdistillery.com/2014/08/10/multiple-abn-tests-in-marketing-with-anova-and-r/ - sample size 


## Visualization
- http://homepage.stat.uiowa.edu/~mbognar/applets/power.html


## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))

[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)