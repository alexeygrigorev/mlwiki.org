---
title: Hadoop Distributed File System
layout: default
permalink: /index.php/Hadoop_Distributed_File_System
---

# Hadoop Distributed File System

## Distributed File Systems
Typically [MapReduce](MapReduce) I/O operations are performed on distribute file systems.  

One such file system is HDFS - [Hadoop](Hadoop) Distribute File System
- ''Name Node'' - the node that orchestrates the process of data distributing and knows where everything is stored

Large files are typically distributed in chunks 64 mb each, and they are stored in data nodes. Each chuck is replicated (typically stored on 3 servers)


### Hadoop DFS
- block-structured file system managed by a single master node 
- MR runs on some underlying storage for reading and writing
- such storage may be distributes
- chunk-based distributed file system
- gives fault tolerance by data partitioning and replication


#### not a DBS|   |- no indexing |- no random access to files
- no SQL
- if you need DB capabilities on top of HDFS use HBase


## Maintaining Consistency
How to maintain [consistency](Consistency_(databases)) across all these replicas? 

### Reading
When a client needs to read data, it needs to know where this piece of data is:
; a "read" command is issued with an offset - how many bytes the client wants to read 
# The '''name node''' knows where every chunk of data is kept, so the clients read the metadata from it. 
# After getting the metadata, the client reads the data from the '''data node''' (so there's no centralized bottleneck - all reads are in parallel) 

In case the client fails to read a chunk of data, it asks the '''name node''' where the next replica is - and tries again


### Writing
We need to make sure that all the replicas contain the same data (i.e. they are consistent) 
# One replica is considered "main", and the master knows which one. 
# Client sends the data to be written to all replicas 
: it's written to the main one and propagated to the rest 

- So it supports parallel reads and writes from a large number of processors 
- The reads are arbitrary and random access, but the writes are best when they are added to the end (i.e. appended) 
- Because the architecture relies on the main replica for deciding the order in which multiple append requests are processed, the data is always consistent


<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/DFS.png" alt="Image">


## Sources
- [Web Intelligence and Big Data (coursera)](Web_Intelligence_and_Big_Data_(coursera))


[Category:Distributed Systems](Category_Distributed_Systems)
[Category:Hadoop](Category_Hadoop)