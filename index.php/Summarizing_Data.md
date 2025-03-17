---
title: Summarizing Data
layout: default
permalink: /index.php/Summarizing_Data
---

# Summarizing Data

## Summarizing Data
Before we do any [Data Analysis](Data_Analysis), need to see if data is good 

Why?
- Data too big to look at 
- Need to find problems before analyzing


Problems:
- Missing values
- Values outside of expected ranges
- Values that seem to be in the wrong units
- Mislabeled variables/columns
- Variables that are the wrong class


## Summarizing Data in R
[Summary Statistics](Summary_Statistics)
- <code>summary(x)</code> - summarizes all quantitative and qualitative  variables
- <code>quantile(x)</code> - range of variables

<code>sapply(x[1, ], class)</code>
- calls <code>class</code> for every element of the 1st row
- tells if data was loaded properly

<code>names(x)</code>
- columns' names

Sizes:
- <code>dim(x)</code> - size of the dataset
- same as <code>nrow(x)</code> and <code>ncol(x)</code>
- length(x) and unique(x)

tables
- <code>table(x)</code> - unique + counter
- <code>table(x, y)</code> - two-dimensional table


logical tests
- any(x > 10) - are there any TRUEs?
- all(x > 10) - are all trues?
- which(x > 10) - which elements are TRUEs?
- which(is.na(x)) - which are NAs
- use <code>|  </code> not, <code>&</code> and, <code>|</code> or:  |  - <code>which(| is.na(x) & x > 10)</code> |- <code>sum(is.na(x))</code> - how many NAs |

summarizing by columns or rows
- <code>rowSums</code>, <code>rowMeans</code>
- <code>colSums</code>, <code>colMeans</code>


## Source
- [Data Analysis (coursera)](Data_Analysis_(coursera))

[Category:R](Category_R)
[Category:Data Analysis](Category_Data_Analysis)