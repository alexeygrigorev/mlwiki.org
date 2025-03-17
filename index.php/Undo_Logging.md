---
title: Undo Logging
layout: default
permalink: /index.php/Undo_Logging
---

# Undo Logging

## Undo Logging
This is a [Database Transaction Log](Database_Transaction_Log) for dealing with [Crash Recovery](Crash_Recovery)

### Idea
Hansel and Gretel
- poor parents dropped the children in the forest
- the children trace the steps they take and recover the path back to parents 

The same in databases:
- we keep a log of things we do
- but the [Memory Hierarchy](Memory_Hierarchy) changes a little bit: 
- additionally to Main Memory and [Secondary Storage](Secondary_Storage) we now have Log

Undo Logging or ''Immediate Modification'' log
- before writing anything to disk, we record the <u>old value</u> to the log
- and only after that write 

### Example
So the way we do it is:
- we allow to modify things in memory 
- while modifying them we create corresponding records in the log that keeps the old value 
- all the log records have to already be on disk before writing database items back to disk

Example 

|   Transaction $T_1$  |  Log  |  Comment  |     |  $\langle T_1, \text{start} \rangle$  |  when the transaction starts ||  read($A, t$); $t \leftarrow t \times 2$;  |    |  ||  write($A, t$)  |  $\langle T_1, A, 8 \rangle$  |  now it's allowed to output($A$) ||  read($B, t$); $t \leftarrow t \times 2$;  |   |  ||  write($B, t$)  |  $\langle T_1, B, 8 \rangle$  |  now it's allowed to output($B$) ||  output($A$)  |   |  ||  output($B$)  |   |  now all modifications are on disk ||    |   $\langle T_1, \text{commit} \rangle$   |  transaction has finished |

The log record's form is:
- $\langle \text{transaction id}, \text{DB item}, \text{old value} \rangle$
- $\langle T_1, B, 8 \rangle$ means $T_1$ made modification to database item $B$ and the old value is 8
- $\langle T_1, \text{commit} \rangle$ means $T_1$ has successfully completed and it everything has been written to disk


### Complications
- Logs are as well first written to memory and then to disk 
- we cannot flush logs to disk on every action - it would result in too much I/O

Bad States we want to avoid:
- A database item is modified on disk, but no corresponding log record is not yet written
- The entire log is on disk (including $\langle T, \text{commit} \rangle$ record) but new values themselves are not


## Rules
### Undo Logging Rules
- for every action generate an undo log record with the old value
- before element $X$ is modified on disk, we write all log records that belong to $X$ to disk
  - this is called ''Write-Ahead Logging'': 
  - before writing a new value, write all corresponding log records
- before you write '''commit''' to logs, all modifications should be already flushed on disk


### Undo Logging Recovery Rules
How to [recover from failures](Crash_Recovery) with Undo Logging:
- we undo the failed transactions 
- i.e. we put the database in the state it was prior this transaction

Recover(log $L$)
- for every transaction $T_i$ that has a $\langle T_i, \text{start} \rangle$ record in the log
  - if there's already $\langle T_i, \text{commit} \rangle$ or $\langle T_i, \text{abort} \rangle$
    - do nothing
  - otherwise - rollback:
  - for all $\langle T_i, X, v \rangle \in L$
    - write($X, v$)
    - output($X$)
  - write $\langle T_i, \text{abort} \rangle$ to $L$

$\langle T_i, \text{abort} \rangle$ record "commits" the abort of transaction
- to avoid the situation when in the middle of abortion the power was cut again
- it says if we undid a transaction successfully we never have to do it again

If during rollback the power was cut again - it's not really a problem 
- we will just overwrite the old value again - and that's it
- writing the old value twice it's the same as writing it once (it's idempotent) 
- this way you're guaranteed to bet back to a consistent state 

Problem:
- what if a transaction changes a value of some variable several times? 
- in this case we should recover only the first one and ignore the rest

Recover(log $L$)
- let $S^*$ be all set of transactions $T_i$ with $\langle T_i, \text{start} \rangle \in L$
- (1) let $S$ be all transaction $T_i \in S^*$ without $\langle T_i, \text{commit} \rangle \in L$ or $\langle T_i, \text{abort} \rangle \in L$
- (2) for each $\langle T_i, X, v \rangle \in \text{reverse}(L)$ (reverse order: latest $\to$ earliest)
  - if $T_i \in S$:
    - write($X, v$)
    - output($X$)
- (3) for each $T_i \in S$
  - write $\langle T_i, \text{abort} \rangle$ to $L$


## Several Transactions
Note that there can be several transactions that are happening at the same time.
- Can writes of $\langle T_i, \text{abort} \rangle$ records to log be done in any order? 

### Example
- $T_1$ and $T_2$ both write $A$, $T_1$ before $T_2$ 
- suppose that both $T_1$ and $T_2$ are rolled back

Suppose we undo both, but write only $\langle T_1, \text{abort} \rangle$ (power was cut when writing $\langle T_2, \text{abort} \rangle$) 
- undoing something 2 times is not a problem, but here we have two transactions
- recall that $\langle T_1, \text{abort} \rangle$ means the value on disk is the value $A$ had prior to $T_1$
- we have undone $T_1$ and now trying to undo $T_2$ 
- this will rollback to value that was there prior to $T_2$, overwriting value that was prior to $T_1$ 
- (That actually could be the value written by $T_1$ which we rolled back)
- '''BAD STATE''' 

If we write $\langle T_2, \text{abort} \rangle$, but not $\langle T_1, \text{abort} \rangle$
- no problems in this case 

$\Rightarrow$
- we must write the abort record in the reversed order of starting times of transactions
- i.e. latest to start - the first to be undone, and its $\langle \text{abort} \rangle$ record should appear first in the log


## Checkpoints
If we keep track on everything we do we'll quickly run out of log space
- we can free some space by truncating the log
- are there parts of the log we know for sure are not needed anymore and can be safely discarded? 

Need to be careful:
- just anything before a $\langle T_i, \text{commit} \rangle$? 
- will not work in case of multiple transactions:
- one transaction could commit, but before this commit there may be records of another transaction that has not committed yet - we'd need to undo them as well


### Stop the World
The simplest way

Periodically do the following
- do not accept any transactions (say "stop" to everybody)
- wait until all running transactions finish
- flush their modification to disk (as well as their commit record)
- commit all log records to disk
- write a $\langle \text{ckpt} \rangle$ - checkpoint record - to logs
- now can resume accepting all transactions again


Example
|  $\langle T_1, \text{start} \rangle$  ||  rowspan="8" bgcolor="green" style="text-align: center;" |  this can <br> be removed <br> from logs  ||  $\langle T_1, A, 5 \rangle$ ||  $\langle T_2, \text{start} \rangle$ ||  $\langle T_2, B, 10 \rangle$ ||  $\langle T_2, C, 15 \rangle$ ||  $\langle T_1, D, 20 \rangle$ ||  $\langle T_1, \text{commit} \rangle$ ||  $\langle T_2, \text{commit} \rangle$ ||  bgcolor="green" | $\langle \text{ckpt} \rangle$  ||  bgcolor="green" | ||  $\langle T_3, \text{start} \rangle$ ||  rowspan="3" style="text-align: center;" | undoing only <br> this part ||  $\langle T_3, E, 25 \rangle$ ||  $\langle T_3, F, 30 \rangle$ ||  FAILURE  |  |

Rollback:
- If a failure occurs we know that it's enough just to get back to the latest successful checkpoint
- everything started before the checkpoint had been committed 

Problem:
- we're shutting down the system while doing the checkpoint
- especially bad when the number of transactions is very high
- we'd like to avoid that 


### Non-Quiescent Checkpoint
This is a more complex technique
- allow  new transactions to enter the system during the checkpoint 

Algorithm: 
- write to log
  - $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$
  - where $T_1, ..., T_k$ is the list of all active transactions that have not committed yet (and therefore not flushed their results to disk)
- wait until all $T_1, ..., T_k$ commit or abort 
  - and there should the corresponding records in the log 
  - don't prohibit other transactions to start
- when all $T_1, ..., T_k$ have finished
  - write $\langle \text{end ckpt} \rangle$ to log on dist


Idea:
- to undo we scan backwards until we see the end checkpoint ($\langle \text{end ckpt} \rangle$)
- at this point we know that all transaction that were active when the checkpoint started had committed 
- so everything before $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$ is already committed - no need to consider them 
- also: every $\langle \text{start ckpt} \rangle$ should have corresponding $\langle \text{end ckpt} \rangle$


So rollback:
- undo till the latest start checkpoint  $\langle \text{start ckpt} (T_1, ..., T_k) \rangle$


#### Example 1

|  $\langle T_1, \text{start} \rangle$   ||  rowspan="4" bgcolor="red" | can truncate this part ||  $\langle T_1, A, 5 \rangle$ ||  $\langle T_2, \text{start} \rangle$ ||  $\langle T_2, B, 10 \rangle$ ||  bgcolor="green" | $\langle \text{start ckpt} (T_1, T_2) \rangle$  ||  bgcolor="green" | $T_1$ and $T_2$ are active ||  $\langle T_2, C, 15 \rangle$  ||  rowspan="8" | undoing <br> only this part <br><br> note that $T_3$ started <br> after checkpoint ||  $\langle T_3, \text{start} \rangle$  ||  $\langle T_1, D, 20 \rangle$  ||  $\langle T_1, \text{commit} \rangle$ ||  $\langle T_3, E, 25 \rangle$ ||  $\langle T_2, \text{commit} \rangle$ ||  $\langle \text{end ckpt} \rangle$ ||  $\langle T_3, F, 30 \rangle$ ||  FAILURE  |  |
In this case 
- we undo only $T_3$ 
- $T_1$ and $T_2$ are not undone - we see their commit records


#### Example 2: Failure during checkpoint
|  $\langle T_1, \text{start} \rangle$  ||  rowspan="10" bgcolor="red" style="text-align: center;" | $\uparrow$ <br> undo to <br> last <br> complete <br> checkpoint <br><br> only <br> not committed  <br> transactions <br> ($T_2$) ||  $\langle T_1, A, 5 \rangle$ ||  $\langle T_2, \text{start} \rangle$ ||  $\langle T_2, B, 10 \rangle$ ||  $\langle \text{start ckpt} (T_1, T_2) \rangle$ ||  $\langle T_2, C, 15 \rangle$ ||  $\langle T_3, \text{start} \rangle$ ||  $\langle T_1, D, 20 \rangle$ ||  $\langle T_1, \text{commit} \rangle$ ||  $\langle T_3, E, 25 \rangle$ ||  FAILURE  |  (before $\text{ckpt}$) |

In this case:
- haven't seen $\langle T_3, \text{commit} \rangle$ - undoing $T_3$
- also have to undo $T_2$
- don't have to undo $T_1$ - it's committed
- when going back, cannot stop at $\langle \text{start ckpt} (T_1, T_2) \rangle$:
  - still have to undo all active transactions from the list that haven't committed yet
  - the list is $(T_1, T_2)$, $T_1$ has committed - i.e. undoing only $T_2$
- so it may be enough to go up until you see that all not-committed transactions start 
  - but it can be as far as the last completed checkpoint
  - at this point you're certain that you've undone everything


## Drawbacks and Benefits
- (+) don't need much memory for logging - keep as much as you can, flush when there's no memory
- (-) not good for backups - it goes back it time, not forward 
  - backup with such logging approach: stop the world and do the backup
  - [Redo Logging](Redo_Logging) is another alternative without this drawback


## Undo/Redo Logging
[Undo/Redo Logging](Undo_Redo_Logging) is the combination of Undo Logging and [Redo Logging](Redo_Logging)


## Exercises
{{ Main |  Database Transaction Log Exercises }} |

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)