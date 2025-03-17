---
title: "T Distribution"
layout: default
permalink: /index.php/T_Distribution
---

# T Distribution

## $t$ Distribution
This is a family of Continuous [Distribution](Distribution)s
- unimodal and bell-shaped, like [Normal Distribution](Normal_Distribution)
- centered at 0
- has one parameter: degrees of freedom ($\text{df}$)


### Origin
Origin (and usage):
- arises when estimating the mean of normally distributed population when 
- sample size is small and population standard deviation is unknown 



### $t$-distribution vs [Normal](Normal_Distribution)
- for large $\text{df}$ ($\geqslant 100$) $t$-dist closely follows $N(0,1)$
- but even for $\text{df} \geqslant 30$ it's already almost indistinguishable

<img src="http://habrastorage.org/files/2d3/6f1/963/2d36f1963cc54cd5be3534c691f68c1c.gif" alt="Image">

- for $t$ tails are thicker 
  - so observations are more likely to fall beyond 2$\sigma$ from the mean (than under $N(0,1)$)
- it's good for [t-tests](t-tests): 
  - the thick tails are exactly the correction to deal with poorly estimated [Standard Error](Standard_Error)


<img src="http://habrastorage.org/files/502/05d/b61/50205db619254cd9a7eded5d7579cabe.png" alt="Image">
- here, $\text{df}$ is the lowest, and it approaches the normal curse as $\text{df}$ grows

{{ Hider |  |   title=R code to produce the figure |  |   content=
```text only
default.par = par()

x = seq(-4,4,0.1)
n = dnorm(x)

library(animation)

saveGIF({
  par(mar=c(0,0,0,0))
  
  for (i in 1:100) {
    plot(x, n, type='l', lty=2, col='grey')
    t = dt(x, df=i)
    lines(x, t, col='blue')
    text(1.5, 0.37, paste('df =', i))
    text(1.66, 0.35, format(sum(abs(n - t)))) 
  }
}, interval=0.1)

par(mar=c(0,0,0,0))
plot(x, n, type='l', lty=2, col='grey')

for (i in 1:7) {
  t = dt(x, df=i)
  lines(x, t, col=i)
}

par(default.par)
```
}}



## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://projectile.sv.cmu.edu/research/public/talks/t-test.htm

[Category:Probability](Category_Probability)
[Category:Distributions](Category_Distributions)
[Category:R](Category_R)