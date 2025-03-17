---
title: Multiple Comparisons Tests
layout: default
permalink: /index.php/Multiple_Comparisons_Tests
---

# Multiple Comparisons Tests

## Multiple Comparisons Tests

{{stub}}


## Family-Wise Error Rate
### Controlling FWER
- suppose we run many tests at the same time 
- we perform a [Pairwise t-test](Pairwise_t-test) and want to compare 10 samples
- thus we need to make about $\sum_{i=1}^{10} i = 45$ comparisons
- the chances hight that among the 45 tests a couple of them will incorrectly reject $H_0$ - i.e. they will make Type 1 Error about 5% of the time at $\alpha = 0.05%$
- the solution: to modify the significance level - run the tests at significance level $\alpha^* < \alpha$


## Corrections
### Bonferroni Correction
use $\alpha^* = \alpha \cdot \cfrac{1}{K}$
- where $K$ is the number of tests to run 
- in a pairwise test of $k$ samples,  $K= \cfrac{k \cdot (k - 1)}{2}$



## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://en.wikipedia.org/wiki/Familywise_error_rate


[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)