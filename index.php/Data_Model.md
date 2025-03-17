---
title: "Data Model"
layout: default
permalink: /index.php/Data_Model
---

# Data Model

## Data Model
A ''data model'' is a notation for describing data. 
- It makes sure that all applications see clean and organized data


It consists of 3 parts 
- Structure of Data
- Operations on Data 
- Data Constraints 


### Structure of Data
- conceptual model (schemata, etc)
- how data should be physically organized? i.e. how is it allocated in memory
  - rows and columns?
  - nodes and edges?
  - key-value pairs?
  - sequences of bytes?


=== Operations on Data === 
- what queries are efficiently supported by this organization and what are not? 

It can be
- some limited set of queries to retrieve and modify the data
- limitation is needed to be able to describe operations at a high level

Questions to consider
- how hard it is to update or add? 
- do I reorganize the data? how hard is it? 

Examples
- find the value of key $x$
- find the rows where column "Lastname" is "Johnson"
- get the next $N$ bytes


### Data Constraints
Constraints express what are the legal structured we're allowed to create 

For example
- all rows must have the same number of columns
- all values in a column must have the same type
- a child can't have two parents


## Examples
- [Relational Data Model](Relational_Databases#Relational_Data_Model)
- [Semi-Structured Data Model](Semi-Structured_Data_Model)s: [XML](XML) or JSON data models
- etc


## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom


[Category:Databases](Category_Databases)
[Category:Data Models](Category_Data_Models)