---
title: NoSQL
layout: default
permalink: /index.php/NoSQL
---

# NoSQL

## [RDBMSs](Relational_Databases) / Row-Oriented databases
- Typically have strict schema
- Declarative query language SQL (excellent for ad-hoc queries, easy joins)
- Good transactions support ([ACID](ACID))
- Algebraic Optimization
- Caching / Materialized Views 
- Strong [ Consistency](Consistency_(databases))

### Downsides
- many services don't require complex ad-hoc querying
- typically choose consistency over availability (see the [CAP Theorem](CAP_Theorem))
- replication solutions are limited
  - use traditional replication algorithms to give strong consistency (like [Two-Phase Commit](Two-Phase_Commit))
  - but data is not made available until the commit finishes (and the database is back to the consistent state)
  - not an option for systems where network failures are possible|   |- as the volume of data grows, queries become inefficient - not easily scalable |  - need to wait too long for all replicas to finish with commit
- hard to load-balance

## NoSQL
### [Column-Oriented Databases](Column-Oriented_Databases)
Are better for storing large amounts of data, especially when the number of columns is very large

- Sets of columns are stored together, so a particular record is actually split across several blocks
- Within each block data is stored in sorted order
- Need to maintain "join index" - to pull together different blocks that are for the same record
- Especially good for analytical queries (such as [OLAP](OLAP))

### [Document-Oriented Databases](Document-Oriented_Databases)
Main unit of data is a document - a self-contained (typically) record with all information at hand
- no (little) need for joins

### In-Memory DBs
- Real-time transactions
- Variety of indexing
- Complex joins - still possible 
- Not for big data

### NoSQL features
- No [ACID](ACID) transactions, usually use weaker concurrency model ([BASE](BASE))
- Simpler API - usually no query language
- restricted joins (for better efficiency)
- Ability to horizontally scale "simple operations" throughput over many servers 
: simple = key lookups, read/write of one record
- Ability to replicate and partition data over many servers 
- Efficient use of distributed indexes and RAM for data storage 
- The ability to dynamically add new attributes to data records 


## Major impact systems
### Memcached
Showed that in-memory indexes can be highly scalable and it's possible to distribute and replicate objects over multiple nodes

- main-memory caching service 
: no persistence, replication or fault-tolerance 
- mature system, in wide use
- important concept: [Consistent Hashing](Consistent_Hashing)

### Dynamo
Pioneered the idea of eventual consistency as a new way to achieve higher availability and scalability :
- data fetches are not guaranteed to be up-to-date, but
- updates are guaranteed to be propagated to all nodes (eventually)
- DHT (Distributed Hash Table) with replication 
  - for $N$ replicas stores values at servers $k$, $k + 1$, ..., $k + N - 1$ 
  - [eventually consistent](Eventual_Consistency) via [vector clock](Vector_Clock) to capture causality
- Reconciliation at read time:
  - writes never fail
  - conflict resolution: last write wins or application specific
- [Configurable Consistency](Eventual_Consistency#Configurable_Consistency)


### BigTable
Showed that persistend record storage could be scaled to thousands of nodes 



## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Web Intelligence and Big Data (coursera)](Web_Intelligence_and_Big_Data_(coursera))
- Amazon's Dynamo paper [http://s3.amazonaws.com/AllThingsDistributed/sosp/amazon-dynamo-sosp2007.pdf]



[Category:NoSQL](Category_NoSQL)
[Category:Databases](Category_Databases)