---
title: "Noise Handling (Data Mining)"
layout: default
permalink: /index.php/Noise_Handling_(Data_Mining)
---

# Noise Handling (Data Mining)

## Noise Handling (Data Mining)
Noise - a modification of the original value
- Typically very hard to detect
- Unlike [Outliers](Outliers), that are noticeable different from all other values
- Noisy data looks like real data 


Reasons for Noise:
- Faulty data collection instruments 
- people don't want to put data and put some garbage 
- e.g. age - 40 - true or false?
- Data entry or transmission problems 


### Detecting and Handling
There are several techniques 
- [Cluster Analysis](Cluster_Analysis) build clusters and then see if there are values that shouldn't belong to this cluster
- Build some model, and then run it on the original data set 
  - misclassified instances can be due to noise - are there strange? 
  - <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/noise-regression.png" alt="Image">


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))

[Category:Data Analysis](Category_Data_Analysis)
[Category:Data Mining](Category_Data_Mining)