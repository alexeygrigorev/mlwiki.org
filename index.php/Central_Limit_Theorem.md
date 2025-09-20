---
layout: default
permalink: /index.php/Central_Limit_Theorem
tags:
- probability
- r
- russian
- statistics
title: Central Limit Theorem
---
## Central Limit Theorem
C.L.T. explains why [Normal Distribution](Normal_Distribution) is so widespread 
- when values of a [Random Variable](Random_Variable) are the results of a big number of independent Random Variables with limited [Variance](Variance)s
- then the [Distribution](Distribution) of this RV is [Normal Distribution](Normal_Distribution)





## Experiments
### Sampling Distribution
C.L.T. allows us to assume that [Sampling Distribution](Sampling_Distribution)s approach Normal as the sample size grows 
- we want to show that experimentally for the SD of Mean 


Assume we want to sample from 3 distributions:
- <img src="http://habrastorage.org/files/e99/d4c/a20/e99d4ca2047b4969a9bc366507a63f8a.png" alt="Image">
- [Uniform Distribution](Uniform_Distribution) (blue line)
- [Lognormal Distribution](Lognormal_Distribution) (orange line)
- [Exponential Distribution](Exponential_Distribution) (red line)


There are 3 various degrees of skewness in these distributions

Uniform:
- <img src="http://habrastorage.org/files/15f/4dd/ff4/15f4ddff472a4335a686cfdfa5e83ead.gif" alt="Image">
- <img src="http://habrastorage.org/files/737/4d8/03c/7374d803c1fd448d9c393b907886e05f.png" alt="Image">

Lognormal:
- <img src="http://habrastorage.org/files/14a/549/77d/14a54977dcb84e5eb39f0f5868380665.gif" alt="Image">
- <img src="http://habrastorage.org/files/7cf/90d/f36/7cf90df361da48bda3ea90d1d3803421.png" alt="Image">

Exponential
- <img src="http://habrastorage.org/files/e30/f3b/352/e30f3b35268f4d61bc6f2e560430e35c.gif" alt="Image">
- <img src="http://habrastorage.org/files/42f/406/6fb/42f4066fba924f5396986fb4d23d4356.png" alt="Image">


<details>
<summary>R code of the experiment</summary>

```text only
default.par = par()

set.seed(18213)

x = seq(-0.1, 4.1, 0.1)
yn = dlnorm(x, meanlog=0.1, sdlog=0.5)
yu = dunif(x, min=0, max=4)
ye = dexp(x)

plot(x, yn, type='l', ylim=c(0, 1), col="orange", lwd=2,
     main='the distributions from which we sample')
lines(x, yu, col="blue", lwd=2)
lines(x, ye, col="red", lwd=2)

m = 3000

generate = function(m, FUN, main, xlim, ylim, breaks=13) {
  sd.x = replicate(m, mean(FUN()))
  par(mfcol=c(1,2))
  
  hist(sd.x, breaks=breaks, prob=T, main='', xlim=xlim, ylim=ylim)
  x = seq(min(sd.x), max(sd.x), 0.01)
  y = dnorm(x=x, mean=mean(sd.x), sd=sd(sd.x))
  lines(x=x, y=y, col="blue", lwd=2)
  
  dens = density(sd.x, adjust=2)
  lines(dens, col="red", lwd=2)

  qqnorm(sd.x, col="orange", pch=19, main='')
  qqline(sd.x, lwd=2)

  mtext(main, side=3, outer=TRUE, line=-3) 
  par(mfcol=c(1,1))
}

gen.uniform = function(n) {
  function() { runif(n, min=0, max=4) }
}

gen.lnorm = function(n) {
  function() { rlnorm(n, meanlog=0.1, sdlog=0.5) }
}

gen.exp = function(n) {
  function() { rexp(n) }
}

require(animation)

n.vec = c(1:20, 50)
saveGIF({
  for (n in n.vec) {
    generate(m, gen.uniform(n), 
             xlim=c(0,4), ylim=c(0, 1.4),
             paste('Uniform Distribution, sample size = ', n))
  }
}, interval=0.3)


n.vec = c(1:40, 100)
saveGIF({
  for (n in n.vec) {
    generate(m, gen.lnorm(n), 
             xlim=c(0,3), ylim=c(0, 1.8),
             paste('Lognormal Distribution, sample size = ', n))
  }
}, interval=0.3)

n.vec = c(1:50, 100)
saveGIF({ 
  for (n in n.vec) {
    generate(m, gen.exp(n), 
             xlim=c(0,3), ylim=c(0, 1.8),
             paste('Exponential Distribution, sample size = ', n))
  }
}, interval=0.3)

generate(m, gen.uniform(n), 
         xlim=c(1.5,2.5), ylim=c(0, 4),
         paste('Uniform Distribution, sample size = ', n))
generate(m, gen.lnorm(n), 
         xlim=c(1,1.5), ylim=c(0, 6),
         paste('Lognormal Distribution, sample size = ', n))
generate(m, gen.exp(n), 
         xlim=c(0.5,1.5), ylim=c(0, 4),
         paste('Exponential Distribution, sample size = ', n))

par(default.par)
```

</details>


[See also here](http://yadi.sk/i/-4wm3y_0XzkKN)
- this is taken from [OpenIntro](OpenIntro_Statistics_(book)), figure 4.20



## Теорема (Ляпунов)
Если случайная величина $X$ представляет собой сумму очень большого количества взаимно-независимых случайных величин, влияние каждой из них на всю сумму ничтожно мало, то X имеет распределение, близкое к нормальному. 

'''TODO''': доказательство

### Применение
Пусть $X_i$ - последовательность независимых случайных величин, каждая из которых имеет мат. ожидание и дисперсию:

$M(X_i) = a_i, D(X_i) = b_i^2$

- Введём обозначения 
: $S_n = X_1 + ... + X_n$
: $A_n = \sum_{i = 1}^{n} a_i$
: $B^2 = \sum_{i = 1}^{n} b_i^2$
- Тогда $F_n(X) = P\left(\frac{S_n - A_n}{B_n} < x\right)$ - функция распределения нормированной суммы



К последовательности $X_i$ применима центральная предельная теорема, если 

$\lim_{n \rightarrow \infty} P\left(\frac{S_n - A_n}{B_n} < x\right) = \frac{1}{\sqrt{2\Pi}} \int_{-\infty}^{x} e^{-z^2/2} dz
$


## See Also
- [Laws of Large Numbers](Laws_of_Large_Numbers)
- [Normal Distribution](Normal_Distribution)
- [Weak Law of Large Numbers](Weak_Law_of_Large_Numbers)

## Sources
- [Закон больших чисел на exponenta.ru](http://www.exponenta.ru/educat/class/courses/tv/theme0/10.asp)
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
