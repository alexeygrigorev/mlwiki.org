---
title: Eventual Consistency
layout: default
permalink: /index.php/Eventual_Consistency
---

# Eventual Consistency

## Eventual Consistency
- In highly available systems it is very hard to keep replicas consistent, because they have to contact each other every time a write occurs (e.g. with [Two-Phase Commit](Two-Phase_Commit)) to preserve [consistency](Consistency_(databases)).
- During the time the replicas synchronize everybody should be prevented from writing 
- But that impacts availability, and to have high availability we have to sacrifice that (See the [CAP Theorem](CAP_Theorem))


Reasons for Eventual Consistency:
- need to insure high availability 
- need to always support updates (no matter what happens)


So, Eventual consistency is a [Consistency Model](Consistency_(databases)) in which
- Updates are propagated to replicas eventually, 
- not synchronously with the write 


That is, suppose we have two methods: '''put''' and '''get'''
- put call returns to the caller before the update is applied to all replicas
- but get may return no the most up-to-date object

And there are applications that can tolerate that.



## Conflict Resolution
Each modification is a new immutable version of data, which allows multiple versions to be present.
But branching of versions may happen (because of network failures, concurrent updates, etc), so there should be a way to resolve these conflicts.


Also it is important to keep the order in which updates appear 
- to capture causality between different objects: 
- we don't want to overwrite later updates by information in earlier updates when they arrive late. 
- For this mechanisms such as [Vector Clock](Vector_Clock) are used.
- when a client wants to update, it must specify the version it updates 


There are two design choices when dealing with conflicts: 
- who will handle the conflict?
- when it will be handled? 

### Who?
Data storage
- usually not a good option because it knows little about the data it stores 
- although might attempt to merge, for example, text data (like in version control systems)
- usually it means applying policies like "last write wins" to resolve conflicts

Application 
- it knows what data is stored
- so it decide how to resolve the conflict in the way best for it 

### When?
During writes 
- a write may be rejected if the storage is in conflict (while it waits for reconciliation)
- always read non-conflicting data
- (better availability for reads)

During reads
- always writable (better availability for writes)
- rejecting an update may lead to poor customer experience 
- so may read conflicting data, and ourselves have to read it back 



In many systems (Dynamo, MongoDB, [CouchDB](CouchDB)) conflicts are allowed and it is usually up to the application to resolve them, and then put the reconciled version back to the database. 


## Configurable Consistency
Suppose we have
- $R$ - minimum number of nodes that participate in a successful read
- $W$ - minimum number of nodes that participate is a successful write 
- $N$ - replication factor 


- if $R + W > N$ we can claim consistency
- but $R + W < N$ means lower latency


## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Consistency and availability in Amazon's Dynamo](http://the-paper-trail.org/blog/consistency-and-availability-in-amazons-dynamo/)
- Amazon's Dynamo paper [http://s3.amazonaws.com/AllThingsDistributed/sosp/amazon-dynamo-sosp2007.pdf]


[Category:Distributed Systems](Category_Distributed_Systems)
[Category:NoSQL](Category_NoSQL)
[Category:Databases](Category_Databases)