---
title: Data Mining
layout: default
permalink: /index.php/Data_Mining
---

# Data Mining

## Data Mining
Data mining - methods and algorithms to explore and analyze large volumes of data

Goal: to find patterns in data that are
- valid: with some certainty 
  - e.g. everybody speaks English in Blois - not true
- novel: non obvious for a human
  - everybody speaks French in Blois - obvious 
- useful: can do something with extracted knowledge
- understandable for humans


### What is DM
What is NOT Data Mining:
- look up a phone number in a dictionary
- compute the number of customers who bought iPad in August
- can use [SQL](SQL) for that

What is Data Mining:
- What is the profile of the customers who bought iPad?
- Which customers will buy the new iPhone?
- Which customers will buy which products?


### Origins
DM is a discipline with roots from
- [Artificial Intelligence](Artificial_Intelligence)
- [Statistics](Statistics)
- [Machine Learning](Machine_Learning)
- Pattern Recognition
- Cognitive Science
- [Database Systems](Database)


### Main Focuses
DM is mostly used
- Customer Relationship Management (CRM)
  - churn scoring - predict if a customer leaves to a competitor
  - direct marketing - show ads only to whose who are interested
  - credit scoring
  - sales forecasting 
  - etc
- website/search optimization
- supply chain optimization 
- many others


## Types of Data Mining
### [Rule Mining](Rule_Mining)
[Local Pattern Discovery](Local_Pattern_Discovery)
- [Frequent Pattern Mining](Frequent_Pattern_Mining)
  - [Apriori](Apriori) and [Eclat](Eclat) algorithms for that 
- [Association Rule Mining](Association_Rule_Mining)
- [Constraint-Based Pattern Mining](Constraint-Based_Pattern_Mining)

Sequence Mining:
- [Sequential Pattern Mining](Sequential_Pattern_Mining)


### [Graph Mining](Graph_Mining)
- Social Network Mining


### Others
- [Cluster Analysis](Cluster_Analysis)
- Web Mining
- [Text Mining](Text_Mining) - part of [Natural Language Processing](Natural_Language_Processing) and [Information Retrieval](Information_Retrieval)
- [Stream Mining](Stream_Mining)
- Tree Mining
- Preference Mining


## Data Mining Process
[CRISP-DM](CRISP-DM) (CRoss Industry Standard Process for Data Mining)
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/datamining-process.png" alt="Image">


Business Understanding
- Define the success criteria 
- How to [integrate](Data_Integration) the output with existing technologies?


Data Understanding
- Collect the data from [Data Sources](Data_Sources)
- [Summarizing Data](Summarizing_Data): First Look at the Data
- [Exploratory Data Analysis](Exploratory_Data_Analysis)
- [Univariate Analysis](Univariate_Analysis) - to analyze how variable values behave in isolation
- [Bivariate Analysis](Bivariate_Analysis) - to analyze how two variables interact


Data Preparation
- Need to prepare data so it can be processed by Models
- [Data Cleaning](Data_Cleaning)
- [Data Transformation](Data_Transformation)
- [Data Reduction](Data_Reduction)


Data Modeling
- [Multivariate Linear Regression](Multivariate_Linear_Regression)
- [Logistic Regression](Logistic_Regression)
- [Decision Tree (Data Mining)](Decision_Tree_(Data_Mining))
- [SVM](SVM)
- many others 


Evaluation
- [Error Analysis](Error_Analysis)
- [Error Metrics](Error_Metrics)
- [Cross-Validation](Cross-Validation)
- [Learning Curves](Learning_Curves)
- [ROC Analysis](ROC_Analysis)



## Links
- http://en.wikipedia.org/wiki/Data_mining
- nice DM&ML slides [http://www.evernote.com/shard/s344/sh/284d7df3-ef98-41d3-9de5-9cbc4ad4b800/77713ac8ce6e2d4b52e2b5c63e7fe2f5]
- Data Mining syllabus in Boston College [http://www.evernote.com/shard/s344/sh/da3d2ca3-390f-4a0b-b443-b1773c7c24d4/9ad3c26bd0ef9e637d8bdce2011db309]
- Data Mining map by Saed Sayad [http://www.saedsayad.com/data_mining_map.htm]


## Source
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Data Mining](Category_Data_Mining)
[Category:Machine Learning](Category_Machine_Learning)