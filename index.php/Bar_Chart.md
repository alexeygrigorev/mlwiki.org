---
layout: default
permalink: /index.php/Bar_Chart
tags:
- plots
- r
title: Bar Chart
---
## Bar Chart
Bar Chart, or Bar Plot or Bar Graph 
- This is a [Plot](Plot) that can be useful for [Exploratory Data Analysis](Exploratory_Data_Analysis)
- It's a graphical representation of Frequency Tables
  - It shows the values of your data set with bars
  - height of the bar is proportional to the value it represents
  - so the variables you plot must be [Quantitative Variables](Quantitative_Variables)


### In [R](R)
To create a bar chart in R
- use <code>barplot</code> command

```text only
r = dnorm(seq(from=-3, to=3, length=15), mean=0, sd=1)
barplot(r, col="red")
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/barplot-normal.png" alt="Image">


## Multivariate Analysis
Bar Charts can also be used for comparing values of two and more variables
- typically, they are graphical representation of [Contingency Tables](Contingency_Tables)

There are the following types of bar charts:
- Side-by-side bar chart
  - bars are put near each other
- Stacked (Segmented) bar chart
  - shows more information than other types - the total size, the proportion, etc
- Proportional stacked bar chart
  - standardized version of the stacked bar chart
  - makes it easier to see the [Joint Distribution](Joint_Distribution) of variables


In R
```carbon
library(openintro)
data(email)

1. stacked
t = table(email$spam, email$number)
pal = c('yellow2', 'skyblue2')
barplot(t, col=pal, beside=F)

1. proportional
t.prop = rbind(t[1,] / colSums(t),
               t[2,] / colSums(t))
pal = c('yellow2', 'skyblue2')
barplot(t.prop, col=pal, beside=F)

1. side-by-side
barplot(t, col=pal, beside=T)
```

<img src="http://habrastorage.org/files/9c4/269/82b/9c426982b95f4067bd7bca7f6d8cdca0.png" alt="Image">
<img src="http://habrastorage.org/files/859/98f/418/85998f4188884e8b8904dfaab16a3067.png" alt="Image">
<img src="http://habrastorage.org/files/568/10c/d55/56810cd554124b3e90a5febbe4ee8ffd.png" alt="Image">


### [Mosaic Plot](Mosaic_Plot)s
They can represent the information about the distribution better than proportional bar charts
- they use areas to represent the distribution
- e.g. <img src="http://habrastorage.org/files/14f/ab1/399/14fab1399fb444f58e33a7032a6bef82.png" alt="Image">


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [Data Analysis (coursera)](Data_Analysis_(coursera))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://en.wikipedia.org/wiki/Bar_chart
