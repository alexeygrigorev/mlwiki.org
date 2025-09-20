---
layout: default
permalink: /index.php/CAP_Theorem
tags:
- databases
- distributed-systems
- nosql
title: CAP Theorem
---
## CAP Theorem
'''CAP''' stands for ['''C'''onsistency](Consistency_(databases)), '''A'''vailability and '''P'''artition tolerance

### [Consistency](Consistency_(databases))
In a consistent system values of any objects don't contradict each other
- Do all applications see the same data? 

### Availability
An available system is always usable
- If some nodes fail, does everything still works? 

### Partition Tolerance
If two parts of your system cannot communicate to each other, can they proceed on their own? 
- if not - sacrifice availability 
- if yes - you need to sacrifice consistency 

If a system is partition-tolerant, then it can continue to operate even in presence of failures


'''Theorem:''' It is impossible to implement a [distributed system](Distributed_Databases) which will have all three mentioned properties. Only 2 of the 3 is possible to achieve


## Choices
- Consequently, one of the 3 must be abandoned
- Different databases choose different options:


<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/cap-triangle.png" alt="Image">


## Consistency and Availability
- But no Partition tolerance
- This is typically preferred by [RDBMSs](Relational_Databases) - which is why they usually don't offer scalability
- Easy to achieve [ACID](ACID) under C+A
- Need special algorithms to ensure consistency (like [Two-Phase Commit](Two-Phase_Commit))

## [Consistency](Consistency_(databases)) and Partition tolerance
- But no availability
- HBase chooses consistency and partitioning (no availability)

## Availability and Partition tolerance
- but no consistency|   Instead, they usually have [Eventual Consistency](Eventual_Consistency) |- historical example: DNS |- databases: Memcache, [CouchDB](CouchDB)

## See also
- [Consistency (databases)](Consistency_(databases))
- [BASE](BASE)
- [Eventual Consistency](Eventual_Consistency)

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
