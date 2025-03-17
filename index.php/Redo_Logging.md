---
title: "Redo Logging"
layout: default
permalink: /index.php/Redo_Logging
---

# Redo Logging

## Redo Logging
This is a [Database Transaction Log](Database_Transaction_Log) for dealing with [Crash Recovery](Crash_Recovery)

Also called ''deferred modification'' 
- we don't record the old value, but the new value 
- instead of undoing actions, we will do them 
- $\langle T_i, \text{commit} \rangle$ record may appear earlier than the actual modification is written to disk
- but as soon as modified data is flushed, we write $\langle T_i, \text{end} \rangle$


### Example
|   Transaction $T_1$  |  Log  |  Comment  |     |  $\langle T_1, \text{start} \rangle$  |  when the transaction starts ||  read($A, t$); $t \leftarrow t \times 2$;  |    |  ||  write($A, t$)  |  $\langle T_1, A, 16 \rangle$  |  $A$'s new value is 16 ||  read($B, t$); $t \leftarrow t \times 2$;  |   |  ||  write($B, t$)  |  $\langle T_1, B, 16 \rangle$  |  $B$'s new value is 16 ||    |   $\langle T_1, \text{commit} \rangle$   |  record in log appear earlier then actual modification ||  output($A$)  |   |  ||  output($B$)  |   |  now all modifications are on disk ||    |   $\langle T_1, \text{end} \rangle$   |  transaction finishes |

## Rules
### Redo Logging Rules
- for every action we keep a redo log with new values 
- before a DB item $X$ is flushed to disk, all log records for transactions $T_i$ that have modified $X$ (including $\langle T_i, \text{commit} \rangle$) must be on disk
- flush the log on commit 
- write $\langle T_i, \text{end} \rangle$ only when all modified BD items are on disk

Note that we cannot go to the previous state with this approach: no rollback
- need to use [Undo Logging](Undo_Logging) for this or [Undo/Redo Logging](Undo_Redo_Logging)


### Redo Logging Recovery Rules
$\langle T_i, \text{commit} \rangle$ means
- user knows that the transaction was executed correctly 
- even if now some error happens we have to ensure that the DB state is the state that the user expects after the transaction happens

$\langle T_i, \text{end} \rangle$ says
- the results are on disk - no need to redo anything

Redo(log $L$)
- let $S$ be set of all transactions $T_i$ with $\langle T_i, \text{commit} \rangle \in L$ but without $\langle T_i, \text{end} \rangle$
- for each $T_i \in S$ and for each $\langle T_i, \text{commit} \rangle \in L$ in forward order (earliest $\to$ latest)
  - write($X, v$)
  - output($X$) (write and ensure the modifications appear on disk)


## Non-Quiescent Checkpoint
Idea similar to [Undo Logging](Undo_Logging#Non-Quiescent_Checkpoint), but different semantics

Algo for creating checkpoints:
- write a log records $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$
  - $T_1, ..., T_k$ are active not-committed transactions 
- flush the log
- write to disk modifications of all transactions T_i that have $\langle T_i, \text{commit} \rangle$ record, but don't have $\langle T_i, \text{end} \rangle$ records
  - it means the modifications are still in memory buffers and have not been flushed to disk yet
- one the modifications are written to disk, write $\langle \text{end ckpt} \rangle$ and flush the log


### Example
|  $\langle T_1, \text{start} \rangle$  |   |  ||  $\langle T_1, A, 5 \rangle$  |   |   ||  $\langle T_2, \text{start} \rangle$ ||  rowspan="11" bgcolor="red" | $\uparrow$ ||   ||  $\langle T_1, \text{commit} \rangle$  |  ||  $\langle T_2, B, 10 \rangle$  |  ||  bgcolor="green" | $\langle \text{start ckpt} (T_2) \rangle$ ||  $T_2$ is the only active transaction (no $\langle T_2, \text{commit} \rangle$ record) ||  $\langle T_2, C, 15 \rangle$  |  ||  $\langle T_3, \text{start} \rangle$  |  ||  $\langle T_3, D, 20 \rangle$  |  ||  $\langle T_1, \text{end} \rangle$  |  $T_1$ had $\langle T_1, \text{commit} \rangle$, but didn't have $\langle T_1, \text{end} \rangle$ when $\langle \text{start ckpt} \rangle$ was added ||  $\langle \text{end ckpt} \rangle$  |  now $T_1$ ended, it means we can end the checkpoint  ||  $\langle T_2, \text{commit} \rangle$  |  ||  $\langle T_3, \text{commit} \rangle$  |  ||  FAILURE  |   |   |

We redo all transactions that:
- were active and not-committed when the checkpoint begun
- or started later - after the checkpoint begun

In this case
- these transactions are $T_2$ and $T_3$
- i.e. we need to read the log records till we see  $\langle T_2, \text{start} \rangle$ 
  - which was before $\langle \text{start ckpt} (T_2) \rangle$
- anything else is already on disk for sure

To recover, we :
- scan backwards till we see the $\langle \text{end ckpt} \rangle$ and corresponding $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$
- then we scan a little bit more upwards till we see all records $\langle T_1, \text{start} \rangle ... \langle T_k, \text{start} \rangle$
- redo them from this point 


If we see both $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ and $\langle \text{end ckpt} \rangle$ it means
- while scanning back when see $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ after $\langle \text{end ckpt} \rangle$ it tells us that:
- all transactions $T_j$ that 
  - had committed before $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ 
  - but their modifications had not been flushed to disk (they didn't have $\langle T_j, \text{end} \rangle$ records)
  - they would write all their modifications to disk 
  - otherwise there would not be $\langle \text{end ckpt} \rangle$ record


### Example 2
|  $\langle T_1, \text{start} \rangle$  |   ||  $\langle T_1, A, 5 \rangle$  |   ||  $\langle T_2, \text{start} \rangle$ ||  rowspan="10" bgcolor="red" | $\uparrow$ ||  $\langle T_1, \text{commit} \rangle$ ||  $\langle T_2, B, 10 \rangle$ ||  bgcolor="green" | $\langle \text{start ckpt} (T_2) \rangle$ ||  $\langle T_2, C, 15 \rangle$ ||  $\langle T_3, \text{start} \rangle$ ||  $\langle T_3, D, 20 \rangle$  ||  $\langle T_1, \text{end} \rangle$ ||  $\langle \text{end ckpt} \rangle$   ||  $\langle T_2, \text{commit} \rangle$ ||  FAILURE  |  ||  $\langle T_3, \text{commit} \rangle$  |  |

This case a little bit different 
- we still have to re-do $T_2$, but not $T_3$ 
- $T_3$'s commit record is not on disk - don't need to redo it


### Example 3
If a failure occurs after $\langle \text{start ckpt} (T_2) \rangle$ but before $\langle \text{end ckpt} \rangle$  
- you'll have to redo from the previous <u>complete</u> $\langle \text{start ckpt} (...) \rangle$
- (or from the beginning of the log)

|  $\langle T_1, \text{start} \rangle$  ||  rowspan="10" bgcolor="red" | $\uparrow$ ||  $\langle T_1, A, 5 \rangle$  ||  $\langle T_2, \text{start} \rangle$ ||  $\langle T_1, \text{commit} \rangle$ ||  $\langle T_2, B, 10 \rangle$ ||  bgcolor="green" | $\langle \text{start ckpt} (T_2) \rangle$ ||  $\langle T_2, C, 15 \rangle$ ||  $\langle T_3, \text{start} \rangle$ ||  $\langle T_3, D, 20 \rangle$  ||  $\langle T_1, \text{end} \rangle$ ||  FAILURE  |  |

Note:
- for the Non-Quiescent Check Logging records $\langle T_i, \text{end} \rangle$ are redundant 
- the checkpoints give us the same information


## Drawbacks and Benefits
- (-) need to keep all modified blocks in memory until the commit happens 
- (+) good for backups: just replay the logs on another DB instance 


## Undo/Redo Logging
[Undo/Redo Logging](Undo_Redo_Logging) is the combination of [Undo Logging](Undo_Logging) and Redo Logging


## Exercises
{{ Main |  Database Transaction Log Exercises }} |

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)