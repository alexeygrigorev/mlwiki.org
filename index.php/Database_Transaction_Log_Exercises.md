---
layout: default
permalink: /index.php/Database_Transaction_Log_Exercises
tags:
- database-systems-architecture
title: Database Transaction Log Exercises
---
## Database Transaction Log Exercises
Exercises [and solutions [https://www.dropbox.com/s/tcbmgtqtiffdjrg/lect8-ex-crash-recovery-sol.pdf](http://www.dropbox.com/s/remf9pcuw94qvow/lect8-ex-crash-recovery.pdf])

Materials:
- [Undo Logging](Undo_Logging)
- [Redo Logging](Redo_Logging)
- [Undo/Redo Logging](Undo_Redo_Logging)


## Exercise 1
Consider the following log:
- $\langle T, \text{start} \rangle; \langle T, A, 10 \rangle; \langle T, B, 20 \rangle; \langle T, \text{commit} \rangle$ 
- and events: Output($A$), Output($B$), Flush-Log($A$), Flush-Log($B$), Commit
- what sequences of events are valid for this log? 

### Undo Logging
According [Undo Logging#Undo Logging Rules](Undo_Logging#Undo_Logging_Rules), we have the following constraints (< = "occurs before")
- Flush-Log($A$) < Output($A$) and Flush-Log($B$) < Output($B$)
  - should always flush before writing the modified item to disk
- Flush-Log($A$) < Flush-Log($B$) < Commit
  - assume DB items are flushed on disk in the order they are created $\to$ flushing logs for $A$ before logs for $B$ 
  - both have to be flushed before we write the commit record
- Output($A$) < Commit and Output($B$) < Commit
  - should write the modified database element to disk before the commit

Hence, the following sequences are legal:
- Flush-Log($A$), Output($A$), Flush-Log($B$), Output($B$), Commit
- Flush-Log($A$), Flush-Log($B$), Output($A$), Output($B$), Commit
- Flush-Log($A$), Flush-Log($B$), Output($B$), Output($A$), Commit


### Redo Logging
According [Redo Logging#Redo Logging Rules](Redo_Logging#Redo_Logging_Rules), we have the following constraints (< = "occurs before")
- Flush-Log($A$) < Output($A$) and Flush-Log($B$) < Output($B$)
  - same as for Undo Logging: should always flush before writing the modified item to disk
- Flush-Log($A$) < Flush-Log($B$) < Commit
  - same as for Undo Logging: assume DB items are flushed on disk in the order they are created
  - both have to be flushed before we write the commit record
- Commit < Output($A$) and Commit < Output($B$)
  - in contract to Undo Logging: can write modifications on disk only after the commit record was flushed 

Hence, the following sequences are legal:
- Flush-Log($A$), Flush-Log($B$), Commit, Output($A$), Output($B$)
- Flush-Log($A$), Flush-Log($B$), Commit, Output($B$), Output($A$)


### Undo/Redo Logging
According [Undo/Redo Logging#Rules](Undo_Redo_Logging#Rules), we have the following constraints (< = "occurs before")
- Flush-Log($A$), Output($A$) and Flush-Log($B$), Output($B$)
  - log records should appear before a database item is modified on disk
- Flush-Log($A$) < Flush-Log($B$) < Commit
  - logs must be flushed before the commit record

This gives mush more sequences 
- Flush-Log($A$); Output($A$); Flush-Log($B$); Output($B$); Commit
- Flush-Log($A$); Flush-Log($B$); Output($A$); Output($B$); Commit
- Flush-Log($A$); Flush-Log($B$); Output($B$); Output($A$); Commit
- Flush-Log($A$); Flush-Log($B$); Commit; Output($A$); Output($B$)
- Flush-Log($A$); Flush-Log($B$); Commit; Output($B$); Output($A$)
- Flush-Log($A$); Output($A$); Flush-Log($B$); Commit; Output($B$)
- Flush-Log($A$); Flush-Log($B$); Output($A$); Commit; Output($B$)
- Flush-Log($A$); Flush-Log($B$); Output($B$); Commit; Output($A$)


## Exercise 2.1
Events
- Start transaction $T$
- $T$ modifies $A \leftarrow 11$ (was 10)
- Start transaction $U$
- Failure occurs

Questions:
- what values might have changed?
- how to recover?


### Undo Logging
Log 
: $\langle T, \text{start} \rangle$
: $\langle T, A, 10 \rangle$
: $\langle U, \text{start} \rangle$
: FAILURE

$A$ might have changed its value

Recall the rule: 
- scan backwards from the end to the beginning
- undo things that have not committed

Recovering (while scanning backwards):
1. see $\langle U, \text{start} \rangle$
  - we've successfully undone it 
  - so write $\langle U, \text{abort} \rangle$
1. see the modification $\langle T, A, 10 \rangle$
  - write 10 to $A$ (rewriting the old value back) 
1. see $\langle T, \text{start} \rangle$
  - we've successfully undone it 
  - so write $\langle T, \text{abort} \rangle$


### Redo Logging
Log 
: $\langle T, \text{start} \rangle$
: $\langle T, A, 11 \rangle$
: $\langle U, \text{start} \rangle$
: FAILURE

$A$ cannot have changed its value - the crash occurred
- no commit record $\langle T, \text{commit} \rangle$ was written to disk
- no need to redo it

Recall the rule: 
- scan from the beginning to the end
- redo things that have committed but were not flushed to disk

Recovering (while scanning forwards):
1. see $\langle T, \text{start} \rangle$
  - write $\langle T, \text{abort} \rangle$
1. see the modification $\langle T, A, 11 \rangle$
  - do nothing - it has not changed the value on disk 
1. see $\langle U, \text{start} \rangle$
  - write $\langle U, \text{abort} \rangle$


### Undo/Redo Logging
Log
: $\langle T, \text{start} \rangle$
: $\langle T, A, 10, 11 \rangle$
: $\langle U, \text{start} \rangle$
: FAILURE

$A$ might have changed its value 
- recover in the same way as for Undo Logging

Recovering (while scanning backwards):
1. see $\langle U, \text{start} \rangle$
  - we've successfully undone it 
  - so write $\langle U, \text{abort} \rangle$
1. see the modification $\langle T, A, 10, 11 \rangle$
  - write 10 to $A$ (rewriting the old value back) 
1. see $\langle T, \text{start} \rangle$
  - we've successfully undone it 
  - so write $\langle T, \text{abort} \rangle$


## Exercise 2.2
Events
- Start transaction $T$
- $A \leftarrow 11$ (was 10) by $T$
- Start transaction $U$
- $B \leftarrow 21$ (was 20) by $U$
- $C \leftarrow 31$ (was 30) by $T$
- $D \leftarrow 41$ (was 40) by $U$
- $U$ commits 
- Failure occurs

Questions:
- what values might have changed?
- how to recover?


### Undo Logging
Log
: $\langle T, \text{start} \rangle$
: $\langle T, A, 10 \rangle$
: $\langle U, \text{start} \rangle$
: $\langle U, B, 20 \rangle$
: $\langle T, C, 30 \rangle$
: $\langle U, D, 40 \rangle$
: $\langle U, \text{commit} \rangle$
: FAILURE

Only transaction $T$ has to be undone
- $U$ committed

Changed values:
- $A$ and $C$ might have changed the values (don't see $\langle T, \text{commit} \rangle$)
- $B$ and $D$ have changed the values (see $\langle U, \text{commit} \rangle$)


Recovering (while scanning backwards):
1. see $\langle U, \text{commit} \rangle$
  - ignoring changes of $U$ altogether 
1. see $\langle U, D, 40 \rangle$
  - skipping it
1. see $\langle T, C, 30 \rangle$
  - write value 30 back to $C$
1. see $\langle U, B, 20 \rangle$ and $\langle U, \text{start} \rangle$
  - skipping it
1. see $\langle T, A, 10 \rangle$
  - write value 10 back to $C$
1. see $\langle T, \text{start} \rangle$
  - we've successfully undone it 
  - so write $\langle T, \text{abort} \rangle$


### Redo Logging
Log
: $\langle T, \text{start} \rangle$
: $\langle T, A, 11 \rangle$
: $\langle U, \text{start} \rangle$
: $\langle U, B, 21 \rangle$
: $\langle T, C, 31 \rangle$
: $\langle U, D, 41 \rangle$
: $\langle U, \text{commit} \rangle$
: FAILURE

Need to redo only transaction $U$
- only $U$ has a commit record $\langle U, \text{commit} \rangle$ 
- $T$ has not committed - no need to redo it 

Changed values 
- $A$ and $C$ have not changed ($T$ has not committed)
- $B$ and $D$ might have changed ($U$ has committed)

Recovering (while scanning forwards):
1. $\langle T, \text{start} \rangle$
  - we know that we ignore changes of $T$ - ignoring it
1. $\langle T, A, 11 \rangle$
  - skipping
1. $\langle U, \text{start} \rangle$
1. $\langle U, B, 21 \rangle$
  - writing 21 to $B$ 
1. $\langle T, C, 31 \rangle$
  - skipping
1. $\langle U, D, 41 \rangle$
  - writing 41 to $D$ 
1. $\langle U, \text{commit} \rangle$
1. write $\langle T, \text{abort} \rangle$ to log
  - don't write $\langle U, \text{abort} \rangle$ to log


### Undo/Redo Logging
Log
: $\langle T, \text{start} \rangle$
: $\langle T, A, 10, 11 \rangle$
: $\langle U, \text{start} \rangle$
: $\langle U, B, 20, 21 \rangle$
: $\langle T, C, 30, 31 \rangle$
: $\langle U, D, 40, 41 \rangle$
: $\langle U, \text{commit} \rangle$
: FAILURE


Changed values:
- everything might have changed 
  - we don't know whether it was before or after the commit when the database elements were supposed to be modified
  - so need to undo all not-committed transactions
  - and redo all committed transactions
- all $A$, $B$, $C$, $D$ might have changed their values


- $U$ must be redone (it has the commit record $\langle U, \text{commit} \rangle$)
- $T$ must be undone (it doesn't have a commit record $\langle T, \text{commit} \rangle$)


'''Recovering:'''

forwards (redoing) - same as for Redo Logging:
- ignoring changes of $T$
- write 21 to $B$ 
- write 41 to $D$

backwards (undoing) - same as for Undo Logging
- ignore changes of $U$ 
- write 30 to $C$
- write 10 to $A$ 
- write $\langle T, \text{abort} \rangle$ to log


## Exercise 3
Question
- for a given log, where a $\langle \text{end ckpt} \rangle$ can be added?
- what happens if a crash occurs?


### Undo Logging
Consider this log
: $\langle S, \text{start}  \rangle$
: $\langle S, A, 60 \rangle$
: $\langle S, \text{commit} \rangle$
: $\langle T, \text{start}  \rangle$
: $\langle T, A, 10 \rangle$
: $\langle \text{start ckpt} \rangle$ 
:* here it should identify the active transactions 
:* hence it's $\langle \text{start ckpt} (T) \rangle$ ($S$ already committed)
:* we can add $\langle \text{end ckpt} \rangle$ only once $T$ commits 
: $\langle U, \text{start} \rangle$
: $\langle U, B, 20 \rangle$
: $\langle T, C, 30 \rangle$
: $\langle V, \text{start}  \rangle$
: $\langle U, D, 40 \rangle$
: $\langle V, F, 70 \rangle$
: $\langle U, \text{commit} \rangle$
: $\langle T, E, 50 \rangle$
: $\langle T, \text{commit} \rangle$
:* since $T$ has committed, here can add $\langle \text{end ckpt} \rangle$
: $\langle V, B, 80 \rangle$
: $\langle V, \text{commit}  \rangle$


Recovery:
- depends on whether we first meet $\langle \text{end ckpt} \rangle$ or $\langle \text{start ckpt} \rangle$ 
- if $\langle \text{end ckpt} \rangle$ - go backwards till $\langle \text{start ckpt} (T) \rangle$
- if $\langle \text{start ckpt} (T) \rangle$ - then go backwards till $\langle T, \text{start}  \rangle$ ($T$ was the only active transaction when the checkpoint started)


### Redo Logging
Consider this log
: $\langle S, \text{start}  \rangle$
: $\langle S, A, 61 \rangle$
: $\langle S, \text{commit} \rangle$
: $\langle T, \text{start}  \rangle$
: $\langle T, A, 11 \rangle$
: $\langle \text{start ckpt} \rangle$ 
:* we keep that on the transactions that have committed at this point, but have not yet flushed the modifications to disk:  we wait until they do that 
:* only after that we end the checkpoint (put $\langle \text{end ckpt} \rangle$)
:* The only transaction that has committed is $S$, so the $\langle \text{end ckpt} \rangle$ can occur anywhere after this record: we cannot predict when exactly the dirty blocks will be written to disk 
:* the log record actually is $\langle \text{start ckpt} (T) \rangle$  since $T$ is the only active transaction at this point
: $\langle U, \text{start} \rangle$
: $\langle U, B, 21 \rangle$
: $\langle T, C, 31 \rangle$
: $\langle V, \text{start}  \rangle$
: $\langle U, D, 41 \rangle$
: $\langle V, F, 71 \rangle$
: $\langle U, \text{commit} \rangle$
: $\langle T, E, 51 \rangle$
: $\langle T, \text{commit} \rangle$
: $\langle V, B, 81 \rangle$
: $\langle V, \text{commit}  \rangle$

Recovery
- also depends when the crash occurs 
- $\langle \text{end ckpt} \rangle$ is last, then we know that $S$ was written fully 
  - transactions that we active at start or started later must be redone
  - these transactions are $T$, $U$ and $V$
- $\langle \text{start ckpt} (S) \rangle$ is last - need to go to the previous checkpoint end


### Undo/Redo Logging
For this we do the same reasoning as for Redo Logging

: $\langle S, \text{start}  \rangle$
: $\langle S, A, 60, 61 \rangle$
: $\langle S, \text{commit} \rangle$
: $\langle T, \text{start}  \rangle$
: $\langle T, A, 10, 11 \rangle$
: $\langle \text{start ckpt} \rangle$ 
:* again cannot predict where exactly to put $\langle \text{end ckpt} \rangle$
:* it will be written once $S$ flushes its modifications to disk
: $\langle U, \text{start} \rangle$
: $\langle U, B, 20, 21 \rangle$
: $\langle T, C, 30, 31 \rangle$
: $\langle V, \text{start}  \rangle$
: $\langle U, D, 40, 41 \rangle$
: $\langle V, F, 70, 71 \rangle$
: $\langle U, \text{commit} \rangle$
: $\langle T, E, 50, 51 \rangle$
: $\langle T, \text{commit} \rangle$
: $\langle V, B, 80, 81 \rangle$
: $\langle V, \text{commit}  \rangle$

Recovery
- if last is $\langle \text{end ckpt} \rangle$
  - all dirty blocks were written to disk
  - need to redo only active transactions from the moment when $\langle \text{start ckpt} \rangle$ occurred (i.e. $T$)
  - for that may need to go further - to $\langle T, \text{start}  \rangle$
- if last is $\langle \text{start ckpt} (T) \rangle$
  - go back to the previously successfully completed checkpoint (or the beginning of the log)


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
