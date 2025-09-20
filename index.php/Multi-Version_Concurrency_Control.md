---
layout: default
permalink: /index.php/Multi-Version_Concurrency_Control
tags:
- concurrency
- database-systems-architecture
title: Multi-Version Concurrency Control
---
## Concurrency Control
In a typical relational database when we modify a table, we put a lock - and all other clients that want to access the table are queued
- This sequential execution of tasks wastes a lot of processor's power and time: 
- under high load it may spend a lot of time trying to figure out whose turn is next

MVCC, Multi-Version Concurrency Control, is one of the [Concurrency Control](Concurrency_Control) techniques. 
- it is used to manage concurrent access to the data 
- it runs effectively even under high load, without worrying about queuing requests

<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/couchdb-concurrency.png" alt="Image">

(figure source: [http://guide.couchdb.org/draft/consistency.html#figure/3])



This is used in:
- [CouchDB](CouchDB)


## Ways to Achieve
### [B-Tree](B-Tree) Storage Engine
This way it is achieved in [CouchDB](CouchDB)

[B-Tree](B-Tree) is used everywhere, also for internal data: documents and views
- Usage of this data structure imposes an important restriction: can access only by key. 
- Reason: to be make huge performance gains 

Modification in B-Trees to support MVCC:
- reads and writes without locking the system 
- writes do not block reads 
- this is because of append-only design 


Append-only design 
- old versions are not deleted
- every time something is updated, a new node is created, and a new root as well
  - but old reads still have references to the old root,
  - so they are able to continue reading without being interrupted, 
  - i.e. have old consistent state 
- data never lost and never corrupted

Idea:
- When a new request comes, it uses the current root for querying
- If the root changes by other transaction, this request is still active and will get the old valid and consistent value


## Sources
- [CouchDB The Definitive Guide by Anderson, Lehnardt and Slater](http://guide.couchdb.org/draft)
