---
title: "Bivariate Analysis"
layout: default
permalink: /index.php/Bivariate_Analysis
---

# Bivariate Analysis

## Bivariate Analysis
Analyzes relationships between two variables 

Recall that there are the following [Types of Variables](Types_of_Variables)
- [Categorical Variables](Categorical_Variables) - values that can be organized into categories (not numerical)
- [Quantitative Variables](Quantitative_Variables) -  with numerical values for which arithmetic operation make sense

So there can be the following combinations:
- Quantitative vs Quantitative
- Quantitative vs Categorical
- Categorical vs Categorical

### Independence
typically most interesting question is:
- "Are these variables independent"?
- if they are dependent and correlated, then one variable can be redundant
- and can be [removed](Data_Reduction)


## Quantitative vs Quantitative
If two variables are numeric:
- plot a [Scatter Plot](Scatter_Plot)
- try to fit a [regression line](Linear_Regression) 
- and find [Correlation](Correlation) between them 
- or [Discretize](Data_Discretization) one of them and do [#Quantitative vs Categorical](#Quantitative_vs_Categorical) analysis


## Quantitative vs Categorical
If one is numeric, and another is categorical:
- Visualize one variable w.r.t. another
  - typically group values of numerical variable by the values of categorical
  - [Box Plot#Bivariate Analysis](Box_Plot#Bivariate_Analysis)
  - [Bar Chart#Bivariate Analysis](Bar_Chart#Bivariate_Analysis)
  - [Histogram#Bivariate Analysis](Histogram#Bivariate_Analysis)
  - [Density Plot#Bivariate Analysis](Density_Plot#Bivariate_Analysis)
- Can do [One-Way ANOVA F-Test](One-Way_ANOVA_F-Test) to see if there is any dependence between the variables


## Categorical vs Categorical
To compare two categorical variables
- start from building a [Contingency Table](Contingency_Table) to show relative frequencies of values
  - ''Marginal distribution'' - distribution of only one of the variables in a contingency table
  - ''Conditional Distribution'' - distribution within a fixed value of a second variable
  - so it's simple to see if there's any correlation between the two variables just using this matrix
- run some Tests of Independence:
  - [Chi-square Test of Independence](Chi-square_Test_of_Independence)
  - and [Cramer's Coefficient](Cramer's_Coefficient)


## Links
- http://en.wikipedia.org/wiki/Bivariate_analysis
- [Introduction to Bivariate Analysis (slides)](http://dept.stat.lsa.umich.edu/~kshedden/Courses/Stat401/Notes/401-bivariate-slides.pdf)

## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))

[Category:Data Analysis](Category_Data_Analysis)