---
layout: default
permalink: /index.php/Contingency_Table
tags:
- statistics
title: Contingency Table
---

## Contingency Table
### Frequency Tables
Frequency tables show distribution just for one table 

| none | small | big | Total |
|---|---|---|---|
| 549 | 2827 | 545 | 3921 |

When we replace counts with rations, we get a Relative Frequency Table:

If we replaced the counts with percentages or proportions, he table would be called a relative frequency table.

| none | small | big | Total |
|---|---|---|---|
| 549 / 3921 | 2827 / 3921 | 545 / 3921 | 1 |

### Contingency Tables
A contingency table is a table that summarizes data for two [Categorical Variables](Categorical_Variables)
- It describes the [Joint Distribution](Joint_Distribution) of these variables 

E.g. consider 
- Spam = { Spam, Not Spam } and 
- Number = { none, small, big }

|  | none | small | big | Total |
|---|---|---|---|---|
| spam | 149 | 168 | 50 | 367 |
| not spam | 400 | 2659 | 495 | 3554 |
| Total | 549 | 2827 | 545 | 3921 |

In R a contingency table can be obtained by table command 
```r
table(var1, var2)
```

So, a contingency table of 2 categorical variables is a table that shows the frequency of observations for the two variables as a combination.

## 2x2 Contingency Tables Analysis
Confusion Matrix? 
http://stats.stackexchange.com/questions/107895/proper-analyses-for-2x2-contingency-tables

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_%28coursera%29)
- [OpenIntro Statistics (book)](OpenIntro_Statistics_%28book%29)
