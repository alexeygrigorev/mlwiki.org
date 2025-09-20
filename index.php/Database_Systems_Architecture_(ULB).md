---
layout: default
permalink: /index.php/Database_Systems_Architecture_(ULB)
tags:
- database-systems-architecture
- databases
- it4bi
title: Database Systems Architecture (ULB)
---
- The course was taken in autumn 2013 at the ULB
- Taught by Stijn Vansummeren


## Content
### [Query Processing](Query_Processing)
[Logical Query Plan](Query_Plan#Logical_Query_Plan)
- [Relational Algebra](Relational_Algebra)
- [Translating SQL to Relational Algebra](Translating_SQL_to_Relational_Algebra)
- [Logical Query Plan Optimization](Logical_Query_Plan_Optimization): Heuristics and optimization of [Conjunctive Queries](Conjunctive_Query)

[Physical Query Plan](Query_Plan#Physical_Query_Plan)
- [Physical Operators (databases)](Physical_Operators_(databases))
- [Physical Query Plan Optimization](Physical_Query_Plan_Optimization)
  - [Query Result Size Estimation](Query_Result_Size_Estimation) to estimate the result size 
  - [Join Ordering](Join_Ordering) to select the optimal way of ordering join operations
  - [Greedy Algorithm](Physical_Query_Plan_Optimization#Greedy_Algorithm) to select the optimal plan


### [Indexing](Indexing_(databases))
Simple (Conventional) Indexes
- [Dense Index](Dense_Index)
- [Sparse Index](Sparse_Index)
- [Secondary Index](Secondary_Index)

Tree-Based Indexes
- [B-Tree](B-Tree)

Hash-Based Indexes
- [Open Hashing Index](Open_Hashing_Index)
- [Extensible Hashing](Extensible_Hashing)
- [Linear Hashing](Linear_Hashing)

### [Multi-Dimensional Indexes](Multi-Dimensional_Indexes)
Conventional
- [Multiple-Key Index](Multiple-Key_Index)

Tree-Based Indexes
- [kd-Trees](kd-Trees)
- [Quad Trees](Quad_Trees)
- [R-Tree](R-Tree)

Hash-Based Indexes
- [Grid File Index](Grid_File_Index)
- [Partitioned Hash Function Index](Partitioned_Hash_Function_Index)

### Different Stuff
- [Physical Data Organization (databases)](Physical_Data_Organization_(databases))
- [Typical DB Architecture](Database#Classical_DBMS_Architecture)

### Ensuring [ACID](ACID)
; [A](Atomicity_(databases)), [C](Consistency_(databases)) and [D](Durability_(databases))
- [Crash Recovery](Crash_Recovery)
- [Database Transaction Log](Database_Transaction_Log)
  - [Undo Logging](Undo_Logging)
  - [Redo Logging](Redo_Logging)
  - [Undo/Redo Logging](Undo_Redo_Logging)
; [I](Isolation_(databases))
- [Concurrency Control](Concurrency_Control) and [Serializable Scheduling](Serializable_Scheduling)
- [Scheduler](Scheduler)s:
  - [Lock-Based Scheduler](Lock-Based_Scheduler)
  - [Timestamp-Based Scheduler](Timestamp-Based_Scheduler)
  - [Validation-Based Scheduler](Validation-Based_Scheduler)


## Info
- Course Webpage http://cs.ulb.ac.be/public/teaching/infoh417
- Dropbox folder with all the materials https://www.dropbox.com/sh/r0zvy3zaycbevx8/yLvz9YdT-f
