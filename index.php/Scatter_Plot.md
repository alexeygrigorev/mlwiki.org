---
title: "Scatter Plot"
layout: default
permalink: /index.php/Scatter_Plot
---

# Scatter Plot

## Scatter Plot
This is a [Plot](Plot) that can be useful for [initial](Exploratory_Data_Analysis) [analysis of the data](Data_Analysis)
- it uses Cartesian coordinates to visualize relationships between variables
- So, useful for [Bivariate Analysis](Bivariate_Analysis)

```text only
plot(pData$JWMNP, pData$WAGP, pch=19, col="blue")
```
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/scatter-plot-1.png" alt="Image">



## Tips and Tricks
### More Variables
What if we want to include one more variable?
- use color coding
- e.g. can encode sex in color

```text only
plot(pData$JWMNP, pData$WAGP, pch=19, col=pData$SEX, cex=0.5)
```
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/scatter-plot-2.png" alt="Image">


### Lots of Data
How to visualize when there are many data points in your data?

```text only
x = rnorm(10000)
y = rnorm(10000)
plot(x, y, pch=19)
```

- not very visible
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/scatter-plot-a1.png" alt="Image">


#### [Sampling](Sampling)
Sample you data
- and plot just the part

```transact-sql
sampledValues = sample(1:10000, size=1000, replace=F)
plot(x[sampledValues], y[sampledValues], pch=19)
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/scatter-plot-a2.png" alt="Image">


#### Showing Density
- how to show the density of some area?
- <code>smoothScatter(x, y)</code>
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/da/smooth-scatter.png" alt="Image">


## Sources
- [Data Analysis (coursera)](Data_Analysis_(coursera))
- http://en.wikipedia.org/wiki/Scatter_plot

[Category:Plots](Category_Plots)
[Category:R](Category_R)