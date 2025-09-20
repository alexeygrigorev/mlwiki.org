---
layout: default
permalink: /index.php/MapReduce_Joins
tags:
- hadoop
- mapreduce
title: MapReduce/Joins
---
## MapReduce/Joins
How to implement a Join from [Relational Algebra](Relational_Algebra) using [MapReduce](MapReduce)?

There are several types of joins:
- broadcast join
- reduce-side join


## Broadcast-Join
- when one table is small enough to fit into memory
- small one is broadcasted to each mapper and kept in memory there
- go through blocks of other one and do the join


### [Hadoop MapReduce](Hadoop_MapReduce) Implementation
- use [Distributed Cache](Hadoop_MapReduce#Distributed_Cache) for sending the same data to all the nodes
- [BookAndAuthorBroadcastJoin.java](http://github.com/alexeygrigorev/aim3/blob/master/src/main/java/de/tuberlin/dima/aim3/assignment1/BookAndAuthorBroadcastJoin.java) 




## Reduce-Side Join
- preparation step
  - each mapper tags each record to identify which entity it is
- mapper outputs (id, record) for each record
  - same keys will be copied to same reducer during shuffling
- each reducer does the join based on equal kets
- similar to [Hash Join](Physical_Operators_(databases)#(Partition)_Hash_Join) in DBMS

note
- it may lead to massive data re-distribution 
- when input is huge
- even though data may be on one node it may be moved to others
- need to take the cost of communication into account


### Example
Suppose we have the following schema: 
- Employee(name, SSN)
- Department(emplSSN, depName)

We want to have the following join: 
- $\text{Employee} \Join_\text{SSN = emplSSN} \text{Department}$

Our tagged dataset 
|  Emp  |  Sue  |  999 ||  Emp  |  Tony  |  777 ||  Dep  |  999  |  Accounts  ||  Dep  |  777  |  Sales ||  Dep  |  777  |  Marketing |

After applying map we get
|  999  |  (Emp, Sue, 999) ||  777  |  (Emp, Tony, 777) ||  999  |  (Dep, 999, Accounts) ||  777  |  (Dep, 777, Sales) ||  777  |  (Dep, 777, Marketing) |

And finally after the reduce stage we get 

|  key=999  |  [(Emp, Sue, 999), (Dep, 999, Accounts)] ||  key=777  |  [(Emp, Tony, 777), (Dep, 777, Sales), (Dep, 777, Marketing)] |


### Python Implementation
Source: [http://code.google.com/p/stolzen/source/browse/trunk/courses/coursera/Introduction%20to%20Data%20Science/assignment3/p2_join.py]

 def mapper(record):
   id = record[1]
   emit(id, record)
 
 def reducer(key, list_of_values):
   grouped = itertools.groupby(list_of_values, operator.itemgetter(0))
   g = {k: list(v) for (k, v) in grouped}
   order = g['order'][0]
 
   for line_item in g['line_item']:
     emit(order + line_item)


### Hadoop MapReduce Implementation
From [AIM3](Scalable_Data_Analytics_and_Data_Mining_AIM3_(TUB)):
- [BookAndAuthorReduceSideJoin.java](http://github.com/alexeygrigorev/aim3/blob/master/src/main/java/de/tuberlin/dima/aim3/assignment1/BookAndAuthorReduceSideJoin.java)


## High Level APIs
- High level APIs such as [Pig](Pig)/[Hive](Hive) or [Flink](Flink)/[Spark](Spark) already provide join abstractions
- so there's no need to implement them 

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Scalable Data Analytics and Data Mining AIM3 (TUB)](Scalable_Data_Analytics_and_Data_Mining_AIM3_(TUB))
