---
layout: default
permalink: /index.php/MapReduce
tags:
- algorithms
- distributed-systems
- hadoop
title: MapReduce
---
## Map Reduce
Map-Reduce is a paradigm of parallel computation that initially comes from [Functional Programming](Functional_Programming)

The main characteristics
- it's scalable and fault tolerant 
- it a data processing tool that can handle parallel processing of large volumes of data
- it typically runs on a [Distributed File System](Hadoop_Distributed_File_System)

Main Idea:
- hide details of parallel execution
- allow user to focus only on data processing strategies


### Programming Model
The Map-Reduce model is simple. A programmer needs to specify two primitives:
- a Map function which produces "intermediate" result
- a Reduce function which produces the final result
- There's also a combine stage in-between 

#### Map Function
Map($[(k, v)]$) $\to [(k_2, v_2)]$
- input: a list of $(k, v)$ pairs
- the map function is applied to each pair in the input
- and it outputs a list of $(k_2, v_2)$ pairs 

#### Combine
Combine
- from a list of $(k2, v2)$ pairs form a list of $(k_2, [v_2])$ pairs
- i.e. group intermediate results by key

#### Reduce Function
Reduce($[(k_2, [v_2])]$)
- now for each combined pair we apply reduce

### Map-Reduce Job Execution
Procession
- each processing job is broken down to pieces
- each piece is given for a map task to execute
- also there are one or more reduce tasks

<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/map-reduce.png" alt="Image">

So it's performed in two steps 
- map phase 
- reduce phase

Implementation on top of [Distributed File System](Hadoop_Distributed_File_System) is little bit more complex and needs some additional logic for replicating and so on. 
- For Hadoop implementation refer to [Hadoop#Map-Reduce Job Execution](Hadoop#Map-Reduce_Job_Execution)


### Example
Word-Counting: need to calculate how many occurrences of each word there are 
- distribute all documents among $k$ computers 
- for each document return a set of (word, freq) pairs (the map phase) 
- now sum the occurrences for each word (the reduce phase)

Pseudo-code
```python
def map(String input_key, String doc):
  for each word w in doc:
    EmitIntermediate(w, 1)

def reduce(String output_key, Iterator output_vals):
  int res = 0
  for each v in output_vals:
    res += v
  Emit(res)
```


## High Level Languages
There are SQL-like languages that work on top of [Hadoop](Hadoop) and translate into a set of Map-Reduce jobs 
- [Pig](Pig)
- [Hive](Hive)


## Joins in Map-Reduce
### Broadcast-Join
- when one table is small enough to fit into memory
- small one is broadcasted to each mapper and kept in memory there
- go through blocks of other one and do the join


### Reduce-Side Join
- preparation step
  - each mapper tags each record to identify which entity it is
- mapper outputs (id, record) for each record
  - same keys will be copied to same reducer during shuffling
- each reducer does the join based on equal kets
- similar to [Hash Join](Physical_Operators_(databases)#(Partition)_Hash_Join) in DBMS

note
- it may lead to massive data re-distribution 
- when input is huge
- even though data may be on one node it may be moved to others
- need to take the cost of communication into account


#### Example
Suppose we have the following schema: 
- Employee(name, SSN)
- Department(emplSSN, depName)

We want to have the following join: 
- $\text{Employee} \Join_\text{SSN = emplSSN} \text{Department}$

Our tagged dataset 
|  Emp  |  Sue  |  999 ||  Emp  |  Tony  |  777 ||  Dep  |  999  |  Accounts  ||  Dep  |  777  |  Sales ||  Dep  |  777  |  Marketing |

After applying map we get
|  999  |  (Emp, Sue, 999) ||  777  |  (Emp, Tony, 777) ||  999  |  (Dep, 999, Accounts) ||  777  |  (Dep, 777, Sales) ||  777  |  (Dep, 777, Marketing) |

And finally after the reduce stage we get 

|  key=999  |  [(Emp, Sue, 999), (Dep, 999, Accounts)] ||  key=777  |  [(Emp, Tony, 777), (Dep, 777, Sales), (Dep, 777, Marketing)] |

For additional code refer to this [implementation in Python](http://code.google.com/p/stolzen/source/browse/trunk/courses/coursera/Introduction%20to%20Data%20Science/assignment3/p2_join.py)


## Other Map-Reduce Examples
### Matrix Multiplication
- Suppose we have two sparse matrices: $A (l \times m)$ and $B (m \times n)$
- We want to calculate $C = A \times B$

Map: 
- for each element $(i, j) \in A$
: emit $((i, k), A[i, j])$ for $k \in 1..N$
- for each element $(j, k) \in B$
: emit $((i, k), B[j, k])$ for $i \in 1..L$

Reduce: 
- key = $(i, k)$
- value = $\sum_j (A[i, j] \times B[j, k])$

[Implementation in Python](http://code.google.com/p/stolzen/source/browse/trunk/courses/coursera/Introduction%20to%20Data%20Science/assignment3/p6_matrixmult.py)


## MapReduce vs RDBMS
[RDBMS](Relational_Databases) 
- Declarative query language
- Schemas 
- Logical Data Independence
- [Indexing](Indexing_(databases)) 
- [Algebraic Optimization](Logical_Query_Plan_Optimization) 
- Caching / [Materialized Views](View_Materialization) 
- [ACID](ACID) and transactions 

MapReduce
- High Scalability 
- Fault-tolerance



## See also
- [Hadoop](Hadoop)
- [Hadoop Distributed File System](Hadoop_Distributed_File_System)

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- Lee et al, Parallel Data Processing with MapReduce: A Survey [http://www.cs.arizona.edu/~bkmoon/papers/sigmodrec11.pdf]
