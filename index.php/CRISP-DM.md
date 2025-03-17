---
title: CRISP-DM
layout: default
permalink: /index.php/CRISP-DM
---

# CRISP-DM

## Data Mining Process
CRISP-DM [http://en.wikipedia.org/wiki/Cross_Industry_Standard_Process_for_Data_Mining]
- CRISP-DM (CRoss Industry Standard Process for Data Mining)
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/datamining-process.png" alt="Image">
- there are 6 steps 

CRISP-DM: four levels of abstraction 
- Phases 
  - Example: Data Preparation 
- Generic Tasks 
  - A stable, general and complete set of tasks 
  - Example: [Data Cleaning ](Data_Cleaning_)
- Specialized Task
  - A specific task that belongs to a generic task 
  - Example: Missing Value Handling 
- Process Instance 
  - How a specific task is carried out?
  - Example: The mean value for numeric attributes and the most frequent for categorical attributes


### Business Understanding
Main Objectives 
- Define the success criteria 
- Forms of output?
- How to integrate the output with existing technologies?


### Data Understanding
Main Objectives 
- Collect the data
  - What are the data sources? 
  - a lot of links at [Data Sources](Data_Sources)
- [Summarizing Data](Summarizing_Data): First Look at the Data
- [Exploratory Data Analysis](Exploratory_Data_Analysis)
  - building simple data [Plots](Plots) ([Histogram](Histogram)s, etc)
  - to help to understand the [Distribution](Distribution) of data
- [Univariate Analysis](Univariate_Analysis) - to analyze how variable values behave in isolation
- [Bivariate Analysis](Bivariate_Analysis) - to analyze how two variables interact


### Data Preparation
Need to prepare data so it can be processed by Models
- [Data Cleaning](Data_Cleaning) - [Handling Noise](Handling_Noise), [Anomaly Detection](Anomaly_Detection), [Duplicate Detection](Duplicate_Detection), etc
- [Data Transformation](Data_Transformation) - [Data Normalization](Data_Normalization), [Data Discretization](Data_Discretization)
- [Data Reduction](Data_Reduction)


### Modeling
Prediction Tasks 
- models to predict unknown or future values
- Classification Models: predict a categorical value
- Regression Models: predict a continuous value

Description Tasks
- Goal: find patterns / clusters that describe a data set 
- [Cluster Analysis](Cluster_Analysis): find clusters in data
- Extraction of local patterns: find local properties in a data set 


### Evaluation
Main Questions 
- How to evaluate a method? - [Error Analysis](Error_Analysis)
- How to compare different models that solve same problem? - [Cross-Validation](Cross-Validation) and 

Objective Measures:
- Error rate of a classifier - [Error Metrics](Error_Metrics)
- Conference of associative rules 

Subjective Measures:
- [Visualization](Visualization)


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Data Mining](Category_Data_Mining)