---
layout: default
permalink: /index.php/Concurrency_Control
tags:
- concurrency
- database-systems-architecture
title: Concurrency Control
---
## Concurrency Control
A database typically serves multiple users at the same time 
- the goal in this case is to make an impression that everything works in [isolation](Isolation_(databases))
- Concurrency Control deals with that: it ensures that transactions have the same effect as if they were run in isolation 


## Conflicts
### Write-Read Conflict
Problem:
- one transaction $T_1$ is reading a DB item that was written by another transaction $T_2$
- without $T_2$ having completed 
- this results in Write-Read Conflict


Illustrative Example
- suppose there are two transactions $T_1$ and $T_2$
- $T_1$ transfers 100 USD from one account to another 
- $T_2$ gives 6% interest rate to all accounts

|   $T_1$  |  $T_2$  |    |  Read($A, s$)  |   |  read from $A$ to main-memory variable $s$ ||  $s \leftarrow s - 100$  |   |  withdraw 100 USD from $A$ ||  Write($A, s$)  |   |  persist the result to disk ||    |  Read($A, t$)  |   ||    |  $t \leftarrow t \times 1.06$  |  give 6% interest rate to $A$ ||    |  Write($A, t$)  |  note that at this moment the money hasn't appeared at $B$ yet ||    |  Read($B, t$)  |   ||    |  $t \leftarrow t \times 1.06$  |  give 6% interest rate to $B$ ||    |  Write($B, t$)  |   ||  Read($B, s$)  |   |   ||  $s \leftarrow s + 100$  |   |  put 100 USD to $B$ ||  Write($B, s$)  |   |  persist the result to disk |
Assume both $A$ and $B$ have 100 USD
- $A$ won't get any interest (no money at the moment of interest calculation)
- $B$ will get interest only on 100 USD instead of 200 USD

Reason: 
- two transactions interleaved, 
- it should be either 
  - first all actions of $T_1$ and then all actions of $T_2$ or
  - first all actions of $T_2$ and then all actions of $T_1$

### Write-Write Conflict
Problem:
- both transactions are just writing new values without reading the old ones 

Example
- $T_1$ puts 100 USD to both $A$ and $B$ 
- $T_2$ puts 200 USD to both $A$ and $B$ 

|   $T_1$  |  $T_2$  |  $s \leftarrow 100$  |  ||  Write($A, s$)  |  ||   |  $t \leftarrow 200$ ||   |  Write($A, t$) ||   |  $t \leftarrow 200$ ||   |  Write($B, t$) ||  $s \leftarrow 100$  |  ||  Write($B, s$)  |  |
We want the transactions to run in some sequence
- as if they were not allowed to interleave 

Not [consistent](Consistency_(databases)) state:
- $B$ has 100 USD, $A$ has 200 

Consistent state:
- both have 200 USD (first $T_1$ then $T_2$)
- both have 100 USD (first $T_2$ then $T_1$)


### Scheduling
- The [Scheduler](Scheduler) is responsible for creating an impressions that all transactions are run in isolation 


## Approaches
- [Lock-Based Scheduler](Lock-Based_Scheduler)
- [Timestamp-Based Scheduler](Timestamp-Based_Scheduler) [http://en.wikipedia.org/wiki/Timestamp-based_concurrency_control]
- [Validation-Based Scheduler](Validation-Based_Scheduler)
- [Multi-Version Concurrency Control](Multi-Version_Concurrency_Control) (MVCC) [([CouchDB](http://en.wikipedia.org/wiki/Multiversion_concurrency_control])(CouchDB)) (also "optimistic concurrency model")
- [Vector Clock](Vector_Clock) (like in Amazon Dynamo etc)


## Distributed Concurrency
- Multi-Master
- Master/Slave
- Partitioning 
- Sharding 
- Write thought Caches


## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Design Patterns for Distributed Non-relational Databases](http://www.slideshare.net/guestdfd1ec/design-patterns-for-distributed-nonrelational-databases)
- http://en.wikipedia.org/wiki/Concurrency_control
