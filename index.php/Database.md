---
title: Database
layout: default
permalink: /index.php/Database
---

# Database

## Databases
A database
- is a collection of information that is organized to afford efficient retrieval 
- this collection exists over a long period of time

Data in a database should be self-describing and have a schema 

What problems databases solve? 
- Sharing 
: should support concurrent access between multiple readers and writers 
- [Data Model](Data_Model) Enforcement
: should make sure all applications see clean and organized data
- Scale (see [Secondary Storage](Secondary_Storage))
: should work with datasets too large to fit into main memory
- Flexibility
: should allow using the data in new unexpected ways 


## DBMS
- usually the term database refers to a collection of data that is managed by a ''DBMS'' - a tool for managing large amounts of data

A Database Management System (DBMS) is expected to (by [Data Model](Data_Model) Enforcement)
- allow users to create DBs and specify the schema - logical structure of the data 
: (using DDL - data definition language)
- allows to query and modify the data with some query language or data manipulation language
- support storing very large amounts of data 
- etc


## Classical DBMS Architecture
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/db-architecture.png" alt="Image">


### Recovery Manager
deals with [Crash Recovery](Crash_Recovery)
- Ensures that Database can be put back into a consistent state after a crush
- Uses [Database Transaction Log](Database_Transaction_Log)s for that

### [Concurrency Control](Concurrency_Control)
- ''Transaction Manager'' is responsible for receiving read and write requests (SQL is eventually translated to them)
- it has a [Scheduler](Scheduler): a component  that schedules commands in some sequence thus creating an impression that all users work in [isolation](Isolation_(databases))



### Query Evaluation Engine
Responsible for [Query Processing](Query_Processing)
- Transforms SQL to [Relational Algebra](Relational_Algebra) (see [Translating SQL to Relational Algebra](Translating_SQL_to_Relational_Algebra))
- [Optimizes RA expressions](Logical_Query_Plan_Optimization)
- Creates [Physical Query Plan](Query_Plan#Physical_Query_Plan) from Logical Query Plan using [physical operators](Physical_Operators_(databases))
- [Physical Query Plan Optimization](Physical_Query_Plan_Optimization) is used for finding the cheapest physical query plan


### File & Access Methods
- Provides Wrapper Around Buffer Manager
- here [B-Tree](B-Tree) and other [Indexes](Indexing_(databases)) are implemented


### Buffer Manager
''Buffer Manager'' is mediator between [external storage](Secondary_Storage) and main memory (see [Memory Hierarchy](Memory_Hierarchy))

Main Responsibility: Partitioning main memory into buffers
- it maintains a ''buffer pool''
- it's a collection of memory slots (called ''buffers'')
- a ''buffer'' is a page-sized regions into which disk blocks are transferred 
- disk blocks are brought into memory per request
  - sometimes it may allocate more blocks when asked - in anticipation that some blocks will be needed

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/db-architecture-buffermanager.png" alt="Image">

A ''replacement policy'' decides which block gets evicted when the buffer pool is full
- popular policies" FIFO, Least Recently Used, Clock, etc

Blocks Management
- Higher levels don't care care if a block in memory or not
  - BM loads it if it's not 
  - BM doesn't load if it's already there
  - if no empty buffers, but need to load something, it uses the replacing policy
- Higher levels also inform when a block is no longer needed 
  - so BM can reuse the space
- ''pinned block'' - block that should remain in the memory because it's still needed 
  - ''pinning'' - making a block pinned
  - ''unpinning'' - telling BM that a block is no longer needed
- if a block is modified, BM makes sure the changes are propagated to dosk


### Disk Space Manager
sometimes also ''Storage Manager''
- controls where the data in main memory or on disk is stored 
- keeps track on locations of data requested by buffer manager  
- deals with requests from upper layers to allocate, deallocate, read and write blocks 
- hides details of underlaying hardware and OS 
- typically uses functionality provided by OS



## Stored Information
- data - content of the DS
- metadata - DB schema that describes the DB
- [log records](Database_Transaction_Log) - information about recent changes to the database 
- Statistics - sizes, values, relation to other components of DB, stored in [Database System Catalog](Database_System_Catalog)
- [Indexes](Indexing_(databases)) to support efficient access to data


## Databases
- [Relational Databases](Relational_Databases)
- [NoSQL](NoSQL)
  - [Column-Oriented Databases](Column-Oriented_Databases)
  - [Document-Oriented Databases](Document-Oriented_Databases) ([CouchDB](CouchDB))


## Sources
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))

[Category:Databases](Category_Databases)