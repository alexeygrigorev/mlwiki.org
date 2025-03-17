---
title: Histogram
layout: default
permalink: /index.php/Histogram
---

# Histogram

## Histogram
''Histogram'' is a graphical representation of the [Distribution](Distribution) of data
- Bins: the intervals used in a histogram. The data must be separated into mutually exclusive and exhaustive bins
- Cutpoints: the values that define the beginning and the end of the bins
- Frequency: the count of the number of the data values in each bin
- The peaks in the distribution are called ''modes''
- so the variables you plot must be [Quantitative Variables](Quantitative_Variables)

[Probability Density Function](Probability_Density_Function)
- with histogram you estimate the [Probability Density Function](Probability_Density_Function) of the underlying variable 
- Alternative - [Density Plot](Density_Plot) that use [Kernel](Kernel)s to smooth the plots 


```text only
hist(d$age, col="blue")
```
- Params
  - <code>breaks=100</code> - how many bars in the histogram
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/hist-one.png" alt="Image">
- here we have 19 bins, and two modes 



## [Bivariate Analysis](Bivariate_Analysis)
It can also be useful for [Exploratory Data Analysis](Exploratory_Data_Analysis) of two variables 

Consider this example
- we have two classes of customers: $A$ and $B$
- and we want to build a model that can distinguish them
- so we can create a histogram that shows the distribution of age w.r.t. to class attribute
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/hist-bivariate.png" alt="Image">
- can see that age and class are not independent: there is strong correlation between them:
  - if age is lower then some value (say 30), all belong to class $A$ 
  - if greater than other value - all always belong to class $B$ 
- can learn that just using a simple histogram 


## Cumulative Histogram
Usual histogram estimates the [Probability Density Function](Probability_Density_Function)
- Cumulative Histogram will show the [Cumulative Distribution Function](Cumulative_Distribution_Function)


## See Also
- [Density Plot](Density_Plot)

## Sources
- [Data Analysis (coursera)](Data_Analysis_(coursera))
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))

[Category:Plots](Category_Plots)
[Category:R](Category_R)