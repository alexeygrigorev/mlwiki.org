---
layout: default
permalink: /index.php/Types_of_Variables
tags:
- data-analysis
- statistics
title: Types of Variables
---
## Types of Variables
When we have a table with data, rows correspond to ''observation units'' (subjects, etc.) and columns are ''variables''. 
- NB: Don't confuse with [Random Variable](Random_Variable)s from Probability Theory


There are several types of variables: 
- [Categorical Variables](Categorical_Variables) - values that can be organized into categories (not numerical)
- [Quantitative Variables](Quantitative_Variables) -  with numerical values for which arithmetic operation make sense
- ''Ordinal Variables'' - with natural order


### Problems with Variables
Also we may have
- [Outliers](Outliers) - too large or too small values, sometimes they are errors, we have to find explanation for them
  - use [Anomaly Detection](Anomaly_Detection) techniques to detect outliers
- ''Missing values'' - not present values, can bias the result
  - need [Handling Missing Values](Handling_Missing_Values) to avoid that 
- Noise - modification of the original value
  - Looks like normal input, but it's faulty
  - Very hard to detect 


## Relationships
Types of variables in the analysis: 
- outcome - the variables of our interest
- explanatory - the variables that are used to analyze and explain the outcome


### Types of Relationships
The relationships between the explanatory variable and the outcome
- ''independent'': there is no association between the variables
- ''association'': the variables are dependent, but it's not clear what kind of relationship there is
  - ''causes'': changes in the explanatory variables case the outcome to change 
  - ''reverse causation'': changes in outcome cause the explanatory variable to change
  - ''coincidence'': just pure chance
  - ''common cause'': some other variable causes both the explanatory variables and the outcome to change - see [Lurking Variables](Lurking_Variables) and [Confounding Variables](Confounding_Variables)


### Multivariate Analysis
To analyze relationships between variables there are following methods:
- [Bivariate Analysis](Bivariate_Analysis)
- e.g. [Correlation](Correlation), [Regression Analysis](Regression_Analysis), [ANOVA](ANOVA), [Statistical Test of Independence](Statistical_Test_of_Independence)
- and many others 


## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
