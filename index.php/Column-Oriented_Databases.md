---
title: "Column-Oriented Databases"
layout: default
permalink: /index.php/Column-Oriented_Databases
---

# Column-Oriented Databases

(article needs improving)

## Column-Oriented databases

Are better for storing large amounts of data, especially when the number of columns is very large

- Sets of columns are stored together, so a particular record is actually split across several blocks
- Within each block data is stored in sorted order
- Need to maintain "join index" - to pull together different blocks that are for the same record
- These column-oriented databases are especially good for [OLAP](OLAP) 


## BigTable (HBase)
<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/Hbase.png" alt="Image">


- Tables are distributes across different servers 
- A table is broken into many ''tablets'', each containing multiple rows (''regions'' in HBase) 
- Each tablet is broken into ''column families'', each containing set of columns 
- Each column family spans multiple rows - and stored in chunks of the [Distributed File System](Distributed_File_Systems)
- Each chunk is served by a tablet server (which also takes care of replicas) 


### Search
In order to access any particular record/column, we need to know which tablet server has them 
For that purpose there is a Metadata Table which knows on what tablet server a particular record is.

Search:
- Search starts from the Root Tablet
- We want to find columns for a particular row 
- We look up the root tablet which gives us Child Tablets that contain record's data. 
- Then we get actual chunks where data is stored  



## Example
<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/col-oriented-db-example.png" alt="Image">

- The row is indexed by a key ('''transaction ID''')
- Column families have multiple columns, and columns are stored within single chunks 
- Each Column Family may be stored on different chunk servers 
- The number of column families is fixed, but the number of columns isn't - you may create as many as you want. 

- Additionally each column combination can be timestamped. 
- For example, today the region is one, but tomorrow is another, but you change it not by updating the value, but * rather by inserting a new value with the current timestamp (so versioning is done automatically) 
- Because these DBs rely on DFS - they can do large parallel reads and inserts efficiently. 
- For aggregation queries it's very fast to get results this way 


Downside 
- there is only one key - so you cannot access a record by any value other than id, there is no index for this. 
- If you really need that, you'll have to traverse all the data. 

But it can be overcome by adding a special table with indexes (it's used by Google App Engine) -- Add details? 


## Sources
- [Web Intelligence and Big Data (coursera)](Web_Intelligence_and_Big_Data_(coursera))


[Category:NoSQL](Category_NoSQL)
[Category:Databases](Category_Databases)