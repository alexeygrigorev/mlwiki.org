---
title: "Cramer's Coefficient"
layout: default
permalink: /index.php/Cramer's_Coefficient
---

# Cramer's Coefficient

{{draft}}

## Cramer's Coefficient
Note about [$\chi^2$ Test of Independence](Chi-Squared_Test_of_Independence):
- when the size of a data set increases, the gap between observed and expected values also increases
- even if the distribution remains unchanged
- thus we reject the independence hypothesis as the size grows 
- Crammer's Coefficient provides a solution for that


### Definition
The Cramer's coefficient $v$
- $V = \sqrt{ \cfrac{\chi^2}{\chi^2_\text{max} } }$
- with $\chi^2_\text{max} = N \times ( \min(N, P) - 1 )$ where
  - $N$ is the number of tuples and $P$ the number of attributes 
- $V \in [0, 1]$
- 0 - maximal independence, and 1 - maximal correlation


## Example
Consider the same example as for [$\chi^2$ Test](chi-square_Test_of_Independence)

<table>
<tr>
<td>

| + Small Dataset ||   Male  |  Female  |  Total   |   Blois   |  55  |  45  |  100  ||   Tours   |  20  |  30  |  50  ||  Total  |  75  |  75  |  150  |
</td>
<td>

| + Bigger Dataset  ||   Male  |  Female  |  Total   |   Blois   |  550  |  450  |  1000  ||   Tours   |  200  |  300  |  500  ||  Total  |  750  |  750  |  1500  |
</td>
</tr>
</table>


$V = \sqrt{ 3 / 150 } = \sqrt{ 30 / 1500 } \approx 0.14 $


## [R](R)
<!-- TODO: Expand it -->
```scdoc
cv.test = function(x,y) {
  CV = sqrt(chisq.test(x, y, correct=FALSE)$statistic /
    (length(x) * (min(length(unique(x)),length(unique(y))) - 1)))
  print.noquote("Cramér V / Phi:")
  return(as.numeric(CV))
}
```

So we can get Cramer's V as

```text only
helpdata = read.csv("http://www.math.smith.edu/r/data/help.csv")
with(helpdata, cv.test(female, homeless)
```

or 

```bash
cv.test <- function(x) {
  CV <- sqrt(chisq.test(x, correct=FALSE)$statistic / (sum(x) * min(dim(x) - 1 )))

  ### The result of the Pearson chi-square (without the Yates correction) is divided by the sum of table cells and...
  ### ...multiplied by the smalles number of (row or column) cells minus 1.
  ### The $statistic sends the correct value (the X^2 only) into the sqrt function

  print.noquote("Cramér V / Phi:")
  return(as.numeric(CV))
}
```


## Links
- http://en.wikipedia.org/wiki/Phi_coefficient
- http://sas-and-r.blogspot.fr/2011/06/example-839-calculating-cramers-v.html
- http://home.hib.no/ansatte/gbj/cramer_v.htm
- http://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V
- |  !! http://stats.stackexchange.com/questions/105795/understanding-chi2-and-cram%C3%A9rs-v-results/105827#105827 | |
## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- http://en.wikipedia.org/wiki/Analysis_of_variance

[Category:Correlation](Category_Correlation)
[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)
[Category:Data Analysis](Category_Data_Analysis)