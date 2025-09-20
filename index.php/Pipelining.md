---
layout: default
permalink: /index.php/Pipelining
tags:
- database-systems-architecture
title: Pipelining
---
## Pipelining
Sometimes the output of one [physical operator](Physical_Operators_(databases)) can be used directly as input for other operator. This technique is called ''pipelining''.
- output of an operator is stored in a buffer that serves as input for the next operator
- results are computed as early as possible - and its as soon as enough data is available
- no need to wait unit the previous operator finishes its work 
- dramatically speeds up the execution process|   | |
### Operators
Operators that usually can be pipelined
- projections
- selections
- renaming
- bag-based union
- merge-joins for which input is known to be sorted

An operator that cannot be pipelined is called ''blocking''


### Example
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/pipelining-ex.png" alt="Image">
- output from index scan on $R$ can be pipelined to filter
- filter output can be pipelined to union
- union result can be pipelined to projection
- (given we have enough memory buffers available)


## Materialization
When we cannot pipeline, we have to ''materialize'' everything. It means we have to write all the intermediate sub-results to disk. 

- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/materialization.png" alt="Image">
- also the next operator cannot start working until everything is materialized


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
