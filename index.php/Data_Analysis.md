---
title: Data Analysis
layout: default
permalink: /index.php/Data_Analysis
---

# Data Analysis

## Data Analysis
### Data
Data - values of qualitative or quantitative variables belonging to a set of items 
- set of items - subjects 
- variables - measurements 


### [Data Preparation](Data_Preparation)
Raw Data
- hard to use 
- complex format

Want to have Pre-Processed Data
- ready for analysis 
- each variable forms a column
- each observation forms a raw 
- each file stores about one kind of observation


## Types of Data Analysis
- Descriptive
- Exploratory
- Inferential
- Predictive
- Causal
- Mechanistic


### [Descriptive Analysis](Descriptive_Analysis)
- Goal: to describe a set of data 
- commonly applied to census data 


### [Exploratory Data Analysis](Exploratory_Data_Analysis)
- Goal: Find relationships you didn't know about
- and ideas for the following studies 
- Exploratory analyses alone should not be used for generalizing/predicting


### [Inferential Analysis](Inferential_Statistics)
- use small data sample to say something about the bigger population


[Predictive Analysis](Predictive_Analysis)
- use data on some object to predict values for another object 


Casual Analysis 
- finds out what happens to one variable if another one changes 


Mechanistic Analysis 
- understand the exact changes in other variables 



## Structure of Data Analysis
Steps:
1. Define the question (business/scientific)
  - Start with some general question
  - "Can I automatically detect messages that are SPAM"?
  - Make it concrete
  - "Can I use quantitative characteristics of emails to classify them?"
1. Obtain the data
  - What data you can access? 
  - A lot of data can be got from [Data Sources](Data_Sources) 
  - you also may buy or generate data
1. [Clean the data](Data_Cleaning) - so you can analyze it
  - Is the data you found good enough? 
  - Most often - not, so you'll have to change the data
  - may have to use [ETL](ETL)s for that and load the data into a [Data Warehouse](Data_Warehouse)
1. [Exploratory Data Analysis](Exploratory_Data_Analysis)
  - Playing with data in R
  - try different things: [Plots](Plots), [Histograms](Histograms), etc
  - learn the main characteristics: distribution, mean, medium, outliers, etc
  - [Univariate Analysis](Univariate_Analysis), [Bivariate Analysis](Bivariate_Analysis)
  - Summarizing the DAta
1. Statistical prediction/modeling
  - To answer the question you asked 
  - Should be informed by the result of the previous phase
  - Methods may depend on the questions
  - Typically [Data Mining](Data_Mining) and [Machine Learning](Machine_Learning) algorithms are used for this
  - Report all measures of uncertainty: number of mistakes you did on the [test set](Cross-Validation), etc
1. Interpret results
  - What does it mean - in plain natural language
1. Challenge results
  - What are potential failings?
  - Challenge all the steps
  - Question
    - was it right? could you have made it more specific/general?
  - Data Sources
    - was it right data? did you get the right samples? the right population?
  - Processing
    - correctly identified the variables?
  - Analysis
    - Did we pick the right model? Could the results be better with another model?
1. Synthesize/write up results
  - In plain language - using the data to answer the question
  - should read like a story
1. Create reproducible code
  - so you can share your analysis with other people



## Links
- http://projecttemplate.net/ -  a pre-organized set of files for data analysis


## Source
- [Data Analysis (coursera)](Data_Analysis_(coursera))

[Category:Data Analysis](Category_Data_Analysis)