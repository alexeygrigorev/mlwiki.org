---
title: Hadoop in Data Warehousing
layout: default
permalink: /index.php/Hadoop_in_Data_Warehousing
---

# Hadoop in Data Warehousing

[Hadoop](Hadoop) for [Data Warehousing](Data_Warehouse)
- This is a part of a project for [Data Warehousing (ULB)](Data_Warehousing_(ULB)) course
- link to the final report: [report](http://alexeygrigorev.github.io/ulb-dw-project-hadoop/report/report.pdf)
- presentation: [html](http://alexeygrigorev.github.io/ulb-dw-project-hadoop/presentation/dw-presentation.html) or [slide share](http://www.slideshare.net/AlexeyGrigorev/hadoop-in-data-warehousing)


## Introduction
Today the amounts of data stored in [Data Warehouse](Data_Warehouse)s are becoming more and more enormous. While traditional ways of Data Warehousing design on top of [Relational Databases](Relational_Databases) are still popular, they fail to curb terabytes of data efficiently, which is mostly attributed to complexity of scaling relational databases. There are new emerging approaches that try to address this problem. 

One of such approaches is to use the [MapReduce](MapReduce) paradigm and [Hadoop](Hadoop) as the implementation for building large Data Warehouses over distributed network of servers that can handle huge volumes of data. Hadoop has already become a proven tool for BigData analytics and now there is a rising interest in this technology for Data Warehousing purposes .

The goal of the work is to discuss in what ways Hadoop, as a Map-Reduce framework, can be used in Data Warehouses then compare it with traditional approaches and see in which situations it should be beneficial to use Hadoop in a Data Warehousing project. Additionally we plan to see what are cases where traditional approaches should still be preferred over Hadoop. 


### Motivation
- Proven useful in Big Data challenges
- Interesting in [Business Intelligence](Business_Intelligence)
- Many companies want to integrate Hadoop into existent Data Warehousing solutions


### [Types of Data](Types_of_Data)
- Hadoop can handle Structured data (Relational), Semi-structured (XML, JSON, ...) 
- but also it's very good at unstructured and machine-generated data: Data with no [Data Model](Data_Model)
- Hadoop will help to structure large amounts of unstructured data


### Growth
Today have lots of documents
- Not all structured (Text, audio, video)
- Want to structure then
- E.g. Lots of recorded calls - we want to extract certain keywords from them

The number of structured documents is also growing rapidly
- Transactions
- etc


## Entire Data Warehouse on Hadoop
It's possible to build entire Data Warehouse on top of Hadoop
- Example: Cheetah by Turn.inc
- It's a specialized Data Warehouse 
- [Hive](Hive) is a more generic Data Warehouse solution


### Design
Virtual views
- based on Star and Snowflake schemas 
  - central Fact Table
  - connected to dimension tables via primary key and foreign key dependencies
  - they are needed for joining
- they join the fact table with its dimensions
- only views are exposed to users for querying, not the tables
- <img src="https://raw.github.com/alexeygrigorev/ulb-dw-project-hadoop/master/report/images/virt-views.png" alt="Image">


### Operations
- Filtering, Grouping and Aggregations
  - easily supported by hadoop
- joins
  - recall that [Reduce-Side Joins](MapReduce#Reduce-Side_Join) are expensive - it may lead to data re-distribution
  - it's better to denormalize dimension tables as much as possible
  - i.e. store all data in fact tables

Denormalization works well
- all dimensions are either insertion only or [Slowly Changing Dimensions](Slowly_Changing_Dimensions)


### Queries
Special-purpose QL for querying it
- Like [Pig](Pig) and [Hive](Hive) they are compiled to [MapReduce](MapReduce) jobs
- With some optimizations

Unfortunately Chetach is proprietary - wasn't able to play with it


## Hadoop and Data Warehouse
Hadoop as a Part of Data Warehouse
- they are interchangeable
- and have lots of differences
- often used side by side
- and it can help to make the costs lower

It can be
- Transitory Platform for [ETL](ETL)
- Active Storage

### Transitory platform for [ETL](ETL)
Hadoop as an [ETL](ETL) process
- this was the initial use case of Hadoop
- goal: extract value from terabytes of information
- Hadoop is rather a component in ETL tools, not an ETL tool itself
  - it's just another channel in ETL designers
  - many vendors came up with Hadoop components in their graphical languages
  - and it's possible to do [Pig](Pig) and [Hive](Hive) queries inside these channels
  - for example, Informatica can do that 


Algorithm
- load data into [Hadoop](Hadoop)
- discover something there with it
- '''E''' parse and prepare (with [MapReduce](MapReduce))
- '''T''' clean and transform to some structured format (with [MapReduce](MapReduce))
- '''L''' extract data from Hadoop and load to a Data Warehouse

Input:
- not structured provisional data
- semi-structured, unstructured or machine-generated data
- provisional - meaning analyzed or used in isolation and don't need integration
  - unlike traditional operational Data Warehousing data
- i.e. this data don't really fit into DW paradigm, but Hadoop was created to handle it


#### Text Processing
- most common use case of Hadoop (the survey)
- RDBMs not good for this|   |- no SQL functions for text processing |- text stream -> structured data

Examples
- like: finding keywords, sentiment analysis
- once refined and structured the text, can put it into DW for further analysis
- say to match sentiment with customer profile


#### Examples
Example 1
- process raw click streams
- use [Data Mining](Data_Mining) to detect patterns 
- then put all the findings into a [Data Warehouse](Data_Warehouse)

Example 2
- suppose we run a eBay-like website
- someone publishes an advertisement - it's a dress with some description
- but the description doesn't mention the color
  - user thinks it's obvious - it can be seen on the picture|   |- but we want to be able to answer queries such as "red dress" |- so we process this image to retrieve features
  - color
  - type
  - other things that might be used for search
- not possible with SQL 
- but this information can be used in out Data Warehouse as well


### Repository
Hadoop can store lots of data

It's possible to use it in 2 ways (as a storage)
- Active Storage for unstructured data
- Live Archive for "dormant" structured enterprise data


#### Active Storage
First use-case 
- storage cost: Hadoop cluster typically costs 50-100 times less than typical DB solutions (per Tb)
- data access is fast
- can use it as a long-term storage
  - not necessary to move everything to a Data Warehouse each time we need to do some analysis - can do that with Hadoop
  - but still can move some portions of processed data to a DW for BI analysis


Example
- need to capture data arriving from raw streams
- want to store reliably and cost efficiently
- put it into Hadoop


#### Enterprise Data Live Archive
Second use case: Live archive for traditional enterprise data

motivation
- 85% of tables in DW are not used 
- can transfer this "dormant" data to low cost hadoop storage
- result in extraordinary savings


### Analytical Sandboxes
Last common use case:
- Our input data is not structured
- That means we do not know yet what we want to derive from it 
- Need to play around to see what value we can extract
- And hadoop (along with [Hive](Hive) or [Pig](Pig) for ad-hoc queries) is good for it


#### How to Integrate
- step-by step recommendations
- first: use it as a big staging area
  - for mining unstructured (and structured) data
  - then execute some ETL transformations on it
- next: use as non-dimensional warehouse for raw data
- integrate more


## Conclusion
Hadoop and Data Warehouses should work together in a single information chain

Hadoop use cases:
- front end: preprocessing raw unstructured data
- front end: analytical sandbox
- back end: long-term active storage
- in-between: supplementing existent technologies with parallel processing


Data Warehousing use cases: 
- structured and integrated data for BI and OLAP


## Questions
Q: Why?
- to be able to run on commodity hardware

Q: Who should adapt this?

Q: How much data a company should have?
- when data no longer fits in MySQL or PostreSQL - it's a good point that should adopt Hadoop


## See also
- [Data Warehouse](Data_Warehouse)
- [Hadoop](Hadoop)
- [MapReduce](MapReduce)
- [Hadoop Distributed File System](Hadoop_Distributed_File_System)

## Sources
- Lee et al, Parallel Data Processing with MapReduce: A Survey [http://www.cs.arizona.edu/~bkmoon/papers/sigmodrec11.pdf]
- Ordonez et al, Relational versus non-relational database systems for data warehousing [http://www2.cs.uh.edu/~ordonez/w-2010-DOLAP-relnonrel.pdf]
- Paper by Cloudera and Teradata, Awadallah and Graham, Hadoop and the Data Warehouse: When to Use Which. [http://www.teradata.com/white-papers/Hadoop-and-the-Data-Warehouse-When-to-Use-Which/]
- Chen. Cheetah: A High Performance, Custom Data Warehouse on Top of MapReduce. [http://www.vldb.org/pvldb/vldb2010/papers/I08.pdf]
- Russom, Integrating Hadoop into Business Intelligence and Data Warehousing. [http://www.slideshare.net/emcacademics/tdwi-best-practices-report-hadoop-foro-bi-and-dw-april-2013]


[Category:Hadoop](Category_Hadoop)
[Category:Data Warehousing](Category_Data_Warehousing)