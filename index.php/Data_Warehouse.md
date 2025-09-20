---
layout: default
permalink: /index.php/Data_Warehouse
tags:
- data-warehousing
title: Data Warehouse
---
## Data Warehouse
### Definition
A data warehouse is a storage with the following four characteristics: it's subject-oriented, integrated, time-variant and non-volatile.

#### Subject-Oriented
- A data warehouse is organized around a particular subject area.
- For example, around "sales". 

#### Integrated
- Data comes from different sources and is integrated into one.
- Integrated also implies consistency
- For example, in source A and source B products have different identifiers, but in a data warehouse data from all sources have adhere to the same way of identifying.
- Another example: date may be stored in different format, but it's converted to the single common format in a data warehouse

#### Time-Variant
- It keeps historical data.
- We can retrieve 3-month-old data, 6-month, one year and even older data from a data warehouse. 
- In contrast to a [transactional system](OLTP), where typically only the most recent data is kept.
- For example, in OLTP system we have the most recent address of a customer, while in a data warehouse we keep all the history (see [Slowly Changing Dimensions](Slowly_Changing_Dimensions))

#### Non-volatile
- Once we put data into a data warehouse, we never change it. 
- If it's there - it's there forever.

### Alternative Definition
A Data Warehousing is a platform for supplying clean, standardized, dimensional, aggregated data


### Goal
The main role of data warehouses is to support decision making process.
- i.e. answer essential business questions


### Features
Best for most BI deliverables
- reports
- performance management metrics
- operational [Business Intelligence](Business_Intelligence) data
- [OLAP](OLAP) cubes

Other systems, like [Hadoop](Hadoop), are not good at this.


## Data Warehouses on Top of [Relational Databases](Relational_Databases)
Usually DWs are built on RBDs
- this structure dominates in data warehousing
- so far it's best technology to manage and analyze DWs
  - very mature here

RDBMSs are likely to remain standard in Data Warehousing worlds
- it's unlikely that they will be replaced by [MapReduce](MapReduce) or [Hadoop](Hadoop) 


### Language
For Data Warehousing purposes we can use 
- standard SQL (joins, group by, etc)
- ROLAP - SQL extensions for [OLAP](OLAP) (group by cube, ect)
- Queries are ad-hoc


### Performance
Data Warehouses (especially expensive solutions) are very effective performance-wise.

There are a lot of techniques for speeding up query executions
- [Materialized Views](View_Materialization)
- [Multi-Dimensional Indexes](Multi-Dimensional_Indexes), Cube indexes, etc
- [Cost-Based Optimization](Physical_Query_Plan_Optimization) based on [database statistics](Database_System_Catalog)
- parallel procession of structured data


### Disadvantages
Nowadays there are lots of not structured data 
- RDBs not flexible enough to manage and analyze that
- possible solutions: [Column-Oriented Databases](Column-Oriented_Databases) or [MapReduce](MapReduce) (with [Hadoop](Hadoop) as implementation)

Difficult to integrate [Data Mining](Data_Mining) Algorithms
- Data Mining typically happens outside of [RDBs](Relational_Databases)

It's costly 
- costly to run scalable parallel RDBs
- need expensive specialized hardware (like IBMs Aster)

Amounts of Data
- new data arrive to fast to process


## See Also
- [Hadoop](Hadoop)
- http://it.toolbox.com/wiki/index.php/Data_Warehouse_Fundamentals

## Sources
- [Data Warehousing (ULB)](Data_Warehousing_(ULB))
- [Data Warehouse definition](http://www.1keydata.com/datawarehousing/data-warehouse-definition.html)
- Ordonez et al, Relational versus non-relational database systems for data warehousing [http://www2.cs.uh.edu/~ordonez/co_research_proceedings.html]
- Paper by Cloudera and Teradata, Awadallah and Graham, Hadoop and the Data Warehouse: When to Use Which. [http://www.teradata.com/white-papers/Hadoop-and-the-Data-Warehouse-When-to-Use-Which/]
