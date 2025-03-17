---
title: Dot Plot
layout: default
permalink: /index.php/Dot_Plot
---

# Dot Plot

## Dot Plots
This is a [Plot](Plot) that is used to show only one variable
- can say that this is one-dimensional [Scatter Plot](Scatter_Plot)


### Dot Plot
<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-1.png" alt="Image">

It also shows
- the [mean](Expected_Value) of the distribution (as the "balanced point" of this distribution)


### Stacked Dot Plot
<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-2.png" alt="Image">
- The same, but the dots are stacked on top of each other
- As the number of values grows, it becomes harder to read
- Note that this gives us the same information as [Histogram](Histogram)s - but in there, the values are binned 



## [R](R)
In R, function <code>stripchart</code> draws the dot plot

Example with <code>email50</code> data from OpenIntro:
```carbon
library(openintro)
data(email50)
```


```scdoc
stripchart(email50$num_char, pch=19, col=rgb(0, 0, 1, 0.3), 
           cex=1.5, axes=F, ylim=c(0.9, 1.5))
axis(side = 1)
m = mean(email50$num_char)
polygon(x=c(m-3, m, m+3), y=c(0.90, 0.95, 0.90), col="red")
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-r1.png" alt="Image">

Also we can add some jitter to have an idea of how many items we have in some area

```scdoc
set.seed(10)
stripchart(email50$num_char, method="jitter", 
           pch=19, col=rgb(0, 0, 1, 0.3), cex=1.5, axes=F,
           ylim=c(0.75, 1.6))
axis(side = 1)
polygon(x=c(m-3, m, m+3), y=c(0.87, 0.95, 0.87) - 0.1, col="red")
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-r2.png" alt="Image">

Or can plot it vertically 
```scdoc
stripchart(email50$num_char, method="jitter", 
           vertical=T, 
           pch=19, col=rgb(0, 0, 1, 0.3), cex=1.5)
```

To have a stacked plot, use <code>method="stack"</code>


```scdoc
stripchart(round(email50$num_char), method="stack", 
           pch=19, col=rgb(0, 0, 1, 0.5), axes=F,
           ylim=c(0.8, 1.8))
axis(side = 1)
polygon(x=c(m-3, m, m+3), y=c(0.87, 0.95, 0.87), col="red")
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-r3.png" alt="Image">

Note that it given similar information to a [Histogram](Histogram)
- but the latter is binned, and this is not (so it looks rather as a [Bar Chart](Bar_Chart))

```scdoc
t = table(round(email50$num_char))
a = rep(NA, 65)
names(a) = 0:64

for (i in names(a)) {
  a[i] = t[i]
}

a[is.na(a)] = 0
barplot(a, ylim=c(-0.4, max(a)))
polygon(x=c(m-3, m, m+3), y=c(-0.4, -0.05, -0.4), col="red")
```
<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-r3-as-hist-1.png" alt="Image">


```scdoc
hist(email50$num_char, breaks=30, col="red")
```

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/b/openintrostat/dotplot-r3-as-hist-2.png" alt="Image">

And finally, an example from [http://stackoverflow.com/a/15245023/861423]

```scdoc
set.seed(1)
A = sample(0:10, 100, replace=T)
stripchart(A, method="stack", offset=.5, at=.15, pch = 19,
           main = "Dotplot of Random Values", xlab = "Random Values")
```

<img src="http://i.stack.imgur.com/b14vG.png" alt="Image">


## See Also
- [R Visualization Snippets](R_Visualization_Snippets)

## Links and Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://www.cyclismo.org/tutorial/R/plotting.html
- http://stackoverflow.com/a/15245023/861423

[Category:Plots](Category_Plots)
[Category:R](Category_R)