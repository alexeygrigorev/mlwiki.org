---
title: Replication
layout: default
permalink: /index.php/Replication
---

# Replication

## Replication
Replication is a process of updating the same information stored in [Distributed Databases](Distributed_Databases)
- so all servers have the up-to-date information

Strategies
- synchronized copies 
  - costly, often unnecessary
  - use [Two-Phase Commit](Two-Phase_Commit) or similar strategies
  - i.e. need asynchronous techniques for this 


## Asynchronous Replication
### Asymmetric Replication
Main idea:
- one primary copy where all changes are performed
- several secondary copies that do not accept writes - only reads 
- secondary copies are updated asynchronously with the primary one 

Modules
- capture module: monitors changes made to the primary copy
- application module: propagates changes to the secondary copies


### Symmetric Replication
- all copies accept updates 
- each can have both capture and application modules
- but simultaneous updates may cause loss of [consistency](Consistency_(databases))
  - i.e. the copies may be inconsistent during some period of time 
- this leans to another notion of consistency: [Eventual Consistency](Eventual_Consistency)


Examples
- withdrawal in an ATM 
  - not instant - it takes some time for changes to propagate to every database 
  - so it's not consistent during some period of time until changes are eventually propagated
  - <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ulb/adb/ad-replication-2.png" alt="Image">
- suppose we have a network
  - and in for one server the net goes down
  - this branch still continue working with database: updates are performed locally
  - when the network is restored, the changes are propagated
  - <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ulb/adb/ad-replication.png" alt="Image">


## Ways of Replicating
### Replication with Triggers
In [Active Databases](Active_Databases) this can be done with triggers
- so we accumulate positive and negative changes into <code>PosDelta</code> and <code>NegDelta</code>
- then these deltas are applied to the secondary copies 


```sql
CREATE RULE Capture1 ON Primary
WHEN INSERTED
THEN INSERT INTO PosDelta (SELECT * FROM INSERTED)

CREATE RULE Capture2 ON Primary
WHEN DELETED
THEN INSERT INTO NegDelta (SELECT * FROM DELETED)

CREATE RULE Capture3 ON Primary
WHEN UPDATED
THEN INSERT INTO PosDelta (SELECT * FROM INSERTED);
	INSERT INTO NegDelta (SELECT * FROM DELETED);
```



### Replication with Logs
[Redo Logging](Redo_Logging) or [Undo/Redo Logging](Undo_Redo_Logging) mechanisms can be used to do that
- keep track on all committed changes
- eventually apply them to the secondary copies


## Sources
- [Advanced Databases (ULB)](Advanced_Databases_(ULB))

[Category:Distributed Systems](Category_Distributed_Systems)
[Category:Databases](Category_Databases)