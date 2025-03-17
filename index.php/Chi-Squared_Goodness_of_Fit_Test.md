---
title: "Chi-Squared Goodness of Fit Test"
layout: default
permalink: /index.php/Chi-Squared_Goodness_of_Fit_Test
---

# Chi-Squared Goodness of Fit Test

## Chi-Squared Goodness of Fit Test
This is one of [$\chi^2$ tests](Chi-Squared_Tests)
- one-way table tests - for testing [Frequency Tables](Frequency_Tables), this one
- two-way table tests - for testing [Contingency Tables](Contingency_Tables), [Chi-Squared Test of Independence](Chi-Squared_Test_of_Independence)


### $\chi^2$ One-Way Table Test
This is a method for assessing a null model when the data is binned 

Used when:
- given a sample of cases that can be classified into several groups, determine if the sample is representative of the general population 
- evaluate is the data resemble some distribution, e.g. normal or geometric ("Goodness Of Fit")


### Idea
Goodness of Fit test:
- suppose we have a variable with $n$ modalities 
  - it can be a categorical variable with $n$ groups
  - or numerical data binned into $n$ bins
  - or even discrete numerical data with not many distinct values
- suppose that we have some observed values $O_i$, for each bin $i$ 
- also for each bin $i$, values $E_i$ represent values expected under $H_0$
- are the observed values statistically different from expected? 


### Test
- $H_0$: the observed values do not differ from given distribution
- $H_A$: the observed values are statistically different from expected


### Test Statistics $X^2$
- for each group $i$ we calculate the squared difference between observed and expected
- this difference is normalized with standard error for each group

Values:
- $O_i$ - observed count 
- $E_i$ - count expected under $H_0$


Test statistics
- we can think of it as calculating $n$ $Z$ statistics (standardized differences) and sum them up:
- $Z_i = \cfrac{O_i - E_i}{\text{SE}_i}$, each $Z_i$ follows the [Normal Model](Normal_Distribution)
  - note that $\text{SE}_i$ is a sampling distribution under $H_0$, i.e. 
  - $\text{SE}_i = \sqrt{ E_i }$
- Since we want to minimize the squared error, we calculate 
  - $X^2 = \sum_{i=1}^{k} Z^2_i = \sum_{i=1}^{k} \cfrac{(O_i - E_i)^2}{ E_i }$
- it's called Pearson's cumulative test stat
- it follows $\chi^2$ distribution with $k - 1$ degrees of freedom, where $k$ is the number of categories 


### $p$-values
- typically need only upper-tail values 
- because the larger values correspond to stronger evidence against $H_0$

<img src="http://habrastorage.org/files/3d7/3c4/567/3d73c4567229481585119a0829fd4165.png" alt="Image">


### Conditions
- The observations must be independent 
- Sample size should be big enough, so we should have at least 5 at each cell of the expected count table
- $\text{df} \geqslant 2$



## Examples
### Example: County Jurors
- suppose we have a set of 275 jurors from a small county
- they are categorized with their racial group 
- are they representing the population of eligible jurors or there's some racial bias?
- (source: [OpenIntro](OpenIntro_Statistics_(book)), table 6.5)


|   Race  |  White  |  Black  |  Hispanic  |  Other  |  Total  |   County   |  205  |  26  |  25  |  19  ||   275  |   Ratio   |  0.75  |  0.09  |  0.09  |  0.07 ||   1.00  |   Population Ratio   |  0.72  |  0.07  |  0.12  |  0.09 | ||   1.00   | |
- It doesn't look like it's precisely representative 
- might it be solely due to chance or there's some bias? 


Expected values
- What we do is to create another table, where we add expected 
- Expected numbers represent the values we expect to see if the sample set was entirely representative


|   Race  |  White  |  Black  |  Hispanic  |  Other  |  Total  |   Observed   |  205  |  26  |  25  |  19  ||   275  |   Expected  |  198  |  19.25  |  33  |  24.75 ||   275 | |
And now we calculate the squared difference between observed and expected values for each category:


Test:
- $H_0$: the jurors are random sample, there is no racial bias and the observed counts reflect natural sampling variability
- $H_A$: there's racial bias in the selection 


Calculation:
- $X^2 = \cfrac{(205 - 198)^2}{198} +  \cfrac{(26 - 19.25)^2}{19.25} +  \cfrac{(25 - 33)^2}{33} +  \cfrac{(19 - 24.75)^2}{24.75} \approx 5.8$ 
- <img src="http://habrastorage.org/files/be8/8a1/b89/be88a1b895de4380963547530e9c6899.png" alt="Image">
- $p$-values is quite big: 0.11 - so we can't reject $H_0$


R code 
Manual:
```text only
obs = c(205, 26, 25, 19)
exp = c(198, 19.25, 33, 24.75)

x2 = sum( (obs-exp)^2 / exp )

x = seq(0, 10, 0.01)
y = dchisq(x, df=length(obs) - 1)
plot(x, y, type='l', bty='n', ylab='probability', xlab='x value')

x.min = min(which(x >= x2))
x.max = length(x)
polygon(x=x[c(x.min, x.min:x.max, x.max)],
        y=c(0, y[x.min:x.max], 0), 
        col='orange')

pchisq(x2, df=length(obs) - 1, lower.tail=F)
```



=== Example: Trading === 
- Suppose that we have some data from some stock exchange 
- we want to test if stock activity on one day is independent from previous day
- the data is taken [http://research.stlouisfed.org/fred2/series/SP500/downloaddata] for 2004-08-04	 to 2014-07-01
- example motivated by an example from [OpenIntro](OpenIntro_Statistics_(book)) 


Idea
- If the change in the price was positive, we say that that stock was up ($U$), otherwise we say it was down $D$)
- if the days are really independent, then the number of days before seeing $U$ should follow [Geometric Distribution](Geometric_Distribution). 
- How many days should we wait until seeing $U$?


|   Days  |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7+  |   Expected   |  540.5  |  270.25  |  135.13  |  67.56  |  33.78  |  16.89  |  8.45  |  7.39 ||   Actual |  |  450.0  |  298.00  |  150.00  |  85.00  |  53.00  |  22.00  |  13.00  |  10.00 |

<img src="http://habrastorage.org/files/6a9/7b6/ace/6a97b6acefca4480a96660a7dd0ac6f4.png" alt="Image">


Test:
- $H_0$: stock marked days are independent from each other
  - i.e. we assume that the number of days before seeing $U$ follows geometric distribution
- $H_A$: not independent 


Calculations:
- calculate $X^2 = \sum_{i=0}^{7} \cfrac{(O_i - E_i)^2}{E_i} \approx 43.04$
- $k = 8$, $\text{df} = 8 - 1 = 7$,
- calculate the $p$ value: $p \approx 10^{-6}$
- so we reject $H_0$ and conclude that the market days are not independent from each other


<img src="http://habrastorage.org/files/bb9/c3c/ba9/bb9c3cba91844b3facdf9e0d37e35bc2.png" alt="Image">


{{ Hider |  |   title=R code |  |   content=
```text only
sp500 = read.csv('http://goo.gl/lv268V')
values = as.numeric( as.character(sp500$VALUE) )
change = as.factor(values > 0)
levels(change) = c('D', 'U')

change = change[complete.cases(change)]

y = rep(0, length(change))
y[change == 'U'] = 1
y = c(0, y, 0)
wz = which(y == 0)
streak = diff(wz) - 1

1. chi^2 test
act = table(streak)

n = length(streak)
k = length(act)
exp = n / (2 ^ (1:k))

barplot(rbind(exp, act), beside=T, col=c('skyblue', 'orange'))
legend('topright', c('expected', 'actual'), bty='n', pch=15, 
       col=c('skyblue', 'orange'))

x2 = sum( (act - exp)^2 / exp )

pchisq(x2, df=k - 1, lower.tail=F)
c(x2=x2, theoretic=qchisq(0.95, df=k - 1))

1. let's merge the data for 7,8 and 9 days 
streak[streak >= 7] = 7
streaks = as.factor(streak)
levels(streaks)[8] = '7+'

act = table(streaks)
exp.n = c(exp[1:7], sum(exp[8:10]))
barplot(rbind(exp.n, act), beside=T, col=c('skyblue', 'orange'))
legend('topright', c('expected', 'actual'), bty='n', pch=15, 
       col=c('skyblue', 'orange'))

k = length(act)
x2 = sum( (act - exp.n)^2 / exp.n )

pchisq(x2, df=k - 1, lower.tail=F)
c(x2=x2, theoretic=qchisq(0.95, df=k - 1))
```
}}



## Links
- http://en.wikipedia.org/wiki/Goodness_of_fit#Pearson.27s_chi-squared_test

## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- https://onlinecourses.science.psu.edu/stat504/node/61


[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:R](Category_R)