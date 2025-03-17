---
title: "Scheduler"
layout: default
permalink: /index.php/Scheduler
---

# Scheduler

## Scheduler
The ''Transaction Manager'' is a component of a [Database](Database#Classical_DBMS_Architecture) that issues read and write requests to the ''scheduler''.

The ''scheduler'' determines the order of execution of these requests
- Given some transactions,  
- Find a [conflict-serializable schedule](Serializable_Schedule) to execute them

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/transaction-manager.png" alt="Image">

Problem:
- Read/Write requests arrive continuously and the scheduler never knows the whole transaction
- it also may be a long running transaction 

$\Rightarrow$ the scheduler has to construct the schedule dynamically by
- allowing some read/write requests 
- blocking others 
- restarting some transactions when necessary
- all to ensure that the resulting schedule is conflict-serializable

There are many schedulers:

Serializable Level of Isolation
- [Lock-Based Scheduler](Lock-Based_Scheduler)
- [Timestamp-Based Scheduler](Timestamp-Based_Scheduler)
- [Validation-Based Scheduler](Validation-Based_Scheduler)


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Concurrency](Category_Concurrency)
[Category:Database Systems Architecture](Category_Database_Systems_Architecture)