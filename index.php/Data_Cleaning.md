---
layout: default
permalink: /index.php/Data_Cleaning
tags:
- data-cleaning
title: Data Cleaning
---
## Data Cleaning
There can be several problems with data 
- Missing values - NAs, NULLs, empty or blank values
- Outliers - extreme values
- Noise in data - modifications of the original value, hard to detect
- Duplicates 


## Main Problems and Tools
### [Handling Missing Values](Handling_Missing_Values)
There are several approaches
- radical: ignore row/column
- fill with default value or mean 
- build a [Machine Learning](Machine_Learning) model to predict missing values


### Outliers Detection
Outliers are extreme values in the data
- can influence your models, e.g. [Linear Regression](Linear_Regression)
- so it's a good idea to detect them
- use [Anomaly Detection](Anomaly_Detection) techniques for that


### [Handling Noise](Noise_Handling_(Data_Mining))
noise - modification of an original value
- very hard to detect - because noisy data looks like real data


### [Duplicate Detection](Duplicate_Detection)
Duplicate Data: major issue when you merge data from different sources


## See Also
- [Data Transformation](Data_Transformation)

## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
