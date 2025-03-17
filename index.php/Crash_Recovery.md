---
title: "Crash Recovery"
layout: default
permalink: /index.php/Crash_Recovery
---

# Crash Recovery

## Crash Recovery
### Failure Model
Events can be: desired (things that are supposed to happen) and undesired

Undesired events can be:
- expected - we know that they may occur so we guard against them
  - system crashes: memory lost, CPU halts, etc
- unexpected
  - everything else

### [Memory Hierarchy](Memory_Hierarchy)
Recall that 
- we may be operating on things in memory that have not been flushed to disk yet
- suppose the power is cut - this means these changes are lost  
- if only a part of transaction was written to disk - the database is left in in[consistent](Consistency_(Databases)) state

### Operations
Under this model we define the following operations:
- input($x$) load block containing $x$ into memory
- output($x$) flush the block containing $x$ to disk
- read(database object $x$, variable $t$)
  - load $x$ to memory if not already there (input($x$))
  - write value from $x$ to $t$
- write(database object $x$, variable $t$)
  - input($x$) if $x$ not in memory
  - replace value of $x$ by $t$ (in memory) - no output to disk yet
  - read and write operate on variables and buffers in memory


### Unfinished Transaction
This is the key problem we want to address 

Example
- suppose we have two database items $A$ and $B$ and constraint $A = B$ 
- $T_1 = A \leftarrow A \times 2; B \leftarrow B \times B$
- on low level:
  - (1) read($A, t$); $t \leftarrow t \times 2$;
  - (2) write($A, t$); 
  - (3) read($B, t$); $t \leftarrow t \times 2$;
  - (4) write($B, t$); 
  - (5) output($A$)
  - (6) output($B$)

suppose a crash happens between (5) and (6)
- when we get the database back to work, it's not in a consistent state:
- $A \ne B$: 
  - the new results of $A$ was written to disk and it contains 16
  - the new results of $B$ was not written to disk and it contains 8
  - the constraint is not satisfied 

Usually deal with it with [Database Transaction Log](Database_Transaction_Log) (e.g. [Undo/Redo Logging](Undo_Redo_Logging))


## See also
- [ACID](ACID): [Consistency (databases)](Consistency_(databases)) and [Durability (databases)](Durability_(databases))
- [Database Transaction Log](Database_Transaction_Log)
- [Undo/Redo Logging](Undo_Redo_Logging)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)