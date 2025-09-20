---
title: "Undo/Redo Logging"
layout: default
permalink: /index.php/Undo_Redo_Logging
---

# Undo/Redo Logging

## Undo/Redo Logging
This is a [Database Transaction Log](Database_Transaction_Log) for dealing with [Crash Recovery](Crash_Recovery). 

Undo/Redo Logging is a combination of two logging approaches:
- [Undo Logging](Undo_Logging) and
- [Redo Logging](Redo_Logging)


=== Log Record === 
Each log record has the following form:
- $\langle T_i, X, v_\text{new}, v_\text{old} \rangle$
- $T_i$ - transaction identifier
- $X$ - id of database object
- $v_\text{new}$ - new value of $X$ (like in [Redo Logging](Redo_Logging))
- $v_\text{old}$ - old value of $X$ (like in [Undo Logging](Undo_Logging))


## Rules
- object $X$ can be flushed either before or after $\langle T_i, \text{commit} \rangle$ - it doesn't matter
- all the log records should be flushed before corresponding modifications are written to disk (write-ahead logging, WAL)
- flush at commit: once there's $\langle T_i, \text{commit} \rangle$, flush the log


## Non-Quiescent Checkpoint
Algorithm
- write $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ and flush the log
  - $(T_1, ..., T_k)$ - all active transactions 
- write to disk all ''dirty'' memory buffers 
  - a memory buffer is ''dirty'' if it contains a modified item
  - no matter whether it was committed or not
- write $\langle \text{end ckpt} \rangle$ and flush the log


## Recovery
The recovery procedure happens in two passes
- backwards pass 
  - undo not committed 
  - end $\to$ last valid $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$
- forwards pass 
  - redo committed but not flushed 
  - last valid $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ $\to$ end

Notation:
- let $S^+$ be all committed transactions and $S^-$ all not-committed transactions

'''Backwards Pass'''
- undo transactions $T_i \in S^-$ - ones that have not committed 
- for doing that may have to go little bit further than the last valid $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$


'''Forwards Pass'''
- redo all transactions $T_j \in S^+$ 


## Drawbacks and Benefits
- (-) requires more memory - need to store both old and new values
- (+) can flush to disk whenever we want - gives us more flexibility 


## Exercises
<!-- Main: Database Transaction Log Exercises -->

## See also
- [Crash Recovery](Crash_Recovery)
- [Undo Logging](Undo_Logging) and [Redo Logging](Redo_Logging)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)