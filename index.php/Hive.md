---
title: Hive
layout: default
permalink: /index.php/Hive
---

# Hive

## Hive
Hive is a [Data Warehouse](Data_Warehousing) solution built on top of [Hadoop](Hadoop)
- Main feature - Hive QL: Declarative Query language for ad-hoc analytics


## Hive [Data Model](Data_Model)
Basic structures:
- Tables
  - like tables in RDBs
  - each table has a corresponding [HDFS](HDFS) directory
- [Partitions](Database_Partitioning)
  - each table has one or more partitions
- Buckets
  - data in each partition is divided into buckets

Data type system
- primitives
  - int, float, string, date, boolean
- collections
  - arrays and maps
  - nestable
- can define own data types


## Achitecture
<img src="https://raw.github.com/alexeygrigorev/ulb-dw-project-hadoop/master/report/images/hive-architecture.png" alt="Image">

(figure source: [http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.151.2637])

Main Components
- External Interfaces
  - CLI
  - JDBC + Thrift
  - Web
- [System Catalog](Database_System_Catalog)
  - called Metastore
  - contains schemas
  - keeps statistics - like in [DBMS](Databases)
  - enables optimization techniques (but only naive rule-based optimizations)
- Driver that manages HiveQL queries, contains 
  - optimizer
  - executor (which executes the plan in [Topological Ordering](Topological_Ordering))
- Hadoop as the execution engine


### Query Execution
- a query plan consists of several MapReduce jobs
- results of each job is stored (materialized) on [HDFS](HDFS)
- and the results are consumed by the next job in the graph
- so a job that depends on some other job must wait until it finishes
- it cannot start until all results are materialized to disk, i.e. no [Pipelining](Pipelining)|   | |
## Hive QL
Hive Query Language is a SQL-like declarative query language for ad-hoc queries 

Main Features
- it compiles into a [DAG](Graphs#Directed_Acyclic_Graph) of [MapReduce](MapReduce) jobs that are executed in [Hadoop](Hadoop)
- also can plug custom MapReduce scripts 


### Example
Suppose we have the following tables:
- status_update(user_id int, status string, ds string)
  - '''ds''' is date
- profiles(userid int, school string, gender int)


To load data into a table we use 

```scdoc
LOAD DATA LOCAL INPATH 'logs/status_updates'
INTO TABLE status_updates 
PARTITION (ds='2009-03-20')
```

In this query we want to [partition](Database_Partitioning) our table by date

#### Query 1
Compute daily statistics on how often a status is updated based on gender and school

```googlesql
FROM 
(SELECT a.status, b.school, g.gender
 FROM status_updates a JOIN profiles b
 ON (a.userid = b.userid and a.ds = '2009-03-20') subq1

-- groups by gender
INSERT OVERWRITE TABLE gender_summary -- inserts the result into another table
PARTITION (ds='2009-03-20')
SELECT subq1.gender, count(1)
GROUP BY subq1.gender

-- groups by school
INSERT OVERWRITE TABLE school_summary
PARTITION (ds='2009-03-20')
SELECT subq.school, count(1)
GROUP BY subq1.school
```

note that we have 2 operations in one query
- they are performed in a single scan

#### Query 2
suppose we want to display top 10 memes per school

```googlesql
REDUCE subq2.school, subq2.meme, subq2.cnt
-- using custom python script
USING 'top10.py' AS (school, meme, cnt)
FROM (
	SELECT subq1.school, subq1.meme, count(1) as cnt
	FROM
	(MAP b.school, a.status
		USING 'meme_extractor.py'
		AS (school, meme)
		FROM status_update a JOIN profiles b
		ON (a.userid = b.userid)) subq1
	GROUP BY subq1.school, subq1.meme
	DISTRIBURE BY school, meme
	SORT BY school, meme, cnt desc)
) subq2
```


## See also
- [Hadoop](Hadoop) and [MapReduce](MapReduce)
- [Pig](Pig)

## Sources
- Thusoo et all, Hive: A Warehousing Solution Over a Map-Reduce Framework (2009). [http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.151.2637]


[Category:Hadoop](Category_Hadoop)