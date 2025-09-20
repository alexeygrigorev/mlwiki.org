---
layout: default
permalink: /index.php/Box_Plot
tags:
- plots
- r
title: Box Plot
---
## Box Plot
Box Plot
- This is a [Plot](Plot) that can be useful for [Exploratory Data Analysis](Exploratory_Data_Analysis)
- This plot is a visualization of [Summary Statistics](Summary_Statistics)
- it's "a convenient way of graphically depicting groups of numerical data through their quartiles"


General idea:
- What is [Distribution](Distribution) of data? 
  - is it compact? symmetric?
- Are there [Outliers](Outliers)?


<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/boxplot.png" alt="Image">
- IQR = Q3 - Q1 - the length of the box
- whiskers (fences) capture data outside of the box


```text only
boxplot(..., range=0, ...)
boxplot(..., horizontal=T, ...) // horizontal boxplot
```

<code>range=0</code> means that it will show usual box plot.


### Modified Box Plot
''Modified box plot'' can be used to show [Outliers](Outliers)

- IQR (''Inter Quartile Range'') - difference between 3rd and 1st quartile 
- ''Inner fences'' - the values that are 1.5 times the IQR beyond the 1st and 3rd quartile 
- Lower inner fence = 1st quartile - (1.5 x IQR)
- Upper inner fence = 3rd quartile + (1.5 x IQR)
- observations beyond the whiskers (fences) are outliers and marked with dots 


<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/boxplot-modified.png" alt="Image">

In R
- by default <code>boxplot</code> shows modified box plot
- <code>IQR(data)</code> shows the IQR


## [Bivariate Analysis](Bivariate_Analysis)
We can calculate [all 5 number](Summary_Statistics) values for all quantitative variables associated with a specific category.
- And for each category get a box plot 
- With box plots, we also can see how two values interact 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/boxplot-bivariate.png" alt="Image">


### R
```text only
boxplot(d$a ~ as.factor(d$f))
```
- it will show separate boxplot of values in $a$ for each values of $f$ 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/boxplot-bivariate-r.png" alt="Image">

```gdscript
boxplot(d$a ~ as.factor(d$f), col=c("blue","orange"), names=c("yes","no"), varwidth=T)
```
- if we want to show how much data is there for each factor, 
- we can make the with of the boxes proportional to the volume of data
- using <code>varwidth=T</code>
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/boxplot-bivariate-r2.png" alt="Image">


## Box Plot with Other [Plot](Plot)s
Box plots are nice to combine with other plots
- for example, with a [Scatter Plot](Scatter_Plot) 
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/scatter-plot-with-boxplot.png" alt="Image"> [http://www.statmethods.net/advgraphs/layout.html]
- [This](R_Visualization_Snippets#Scatter_Plot_and_Box_Plots) is the R snipped to produce this figure


## See Also
- [R Visualization Snippets](R_Visualization_Snippets)

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- [Data Analysis (coursera)](Data_Analysis_(coursera))
- http://en.wikipedia.org/wiki/Box_plot
