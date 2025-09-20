---
layout: default
permalink: /index.php/Relational_Databases
tags:
- data-models
- databases
- relational-databases
title: Relational Databases
---
## Relational [Data Model](Data_Model)
A relational database is a collection of ''relations''
- everything is a table 
- every row in a table has the same number of columns 
- relations are implicit: no pointers


### Structure of Data
A ''relation'' is a two-dimension table 

For example, Consider a '''Movie''' relation: 

|   Title  |  Year  |  Length  |  Genre   |  Gone with the Wind  |  1939  |  231  |  Drama  ||  Star Wars  |  1977  |  124  |  Sci-Fi |

Columns
- The columns of a relation are named by ''attributes''
- E.g.: Title, Year, etc.
- They describe the meaning of entities in columns


The name of a relation with its attributes is called ''schema''
- e.g.: Movies(Title, Year, Length, Genre)
- Note that the attributes form a set, not a list
- A database consists of one or more relations, each with a schema 
- And the set of all schemata within one database is called ''Relational DB Schema''


Rows of a relation (other than the header row - which describes the attributes) are called ''tuples''
- ("Gone with the Wind", 1939, Drama)
- We don't include the attribute names, so the order is important here 


We usually associate a ''domain'' with each attribute - a particular elementary type 
- E.g.: Movie(Title: String, Year: Integer, Length: Integer, Genre: String)


### Operations on Data
- Usually the operations are [Relational Algebra](Relational_Algebra) expressions
- SQL is usually transformed to Relational Algebra for processing 


### Constraint
One fundamental constraint in this model is ''key constraint'' 

A set of attributes form a ''key'' for a relation if there are no two tuples with the same values in for the attributes of the key

We indicate that the attributes form a key by <u>underlining</u> them:
- e.g.: Movies(<u>Title</u>, <u>Year</u>, Length, Genre)


## Modeling Relational Databases
- Conceptual level: [Entity-Relationship Model](Entity-Relationship_Model)



## Query Processing
<!-- Main: Query Processing --> How to translate a SQL query into physical query plan


## Sources
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
