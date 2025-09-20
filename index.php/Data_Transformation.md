---
layout: default
permalink: /index.php/Data_Transformation
tags:
- data-transformation
title: Data Transformation
---
## Data Transformation
Main Tasks 
- [Data Normalization](Data_Normalization) to normalize all data values to the same scale
- [Data Discretization](Data_Discretization) to convert numerical attributes to categorical
- Aggregation - to pre-aggregate the data so it's on the needed level of granularity
- Generalization 


## [Data Warehousing](Data_Warehousing)
Data Transformation is the first part of [ETL](ETL)
- also you typically [integrate data](Data_Integration) from different sources
- so also need to apply some transformations

### Data Aggregation
With [OLAP](OLAP) operations (in the context of a data cube) 
- Use the highest level / smallest representation which is enough to solve the task
- Example: use the total number of products sold by category and month, rather by product-id and day


### Data Generalization
By replacing low-level values by higher level abstractions 
- By replacing a complete postal address of a customer by a zip-code 
- By replacing the age of a customer by a value in { young, middleaged, senior } 


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
