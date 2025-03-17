---
title: "Timestamp-Based Scheduler"
layout: default
permalink: /index.php/Timestamp-Based_Scheduler
---

# Timestamp-Based Scheduler

## Timestamp-Based Scheduler
This is a [Scheduler](Scheduler) that gives [Conflict-Serializable Schedule](Serializable_Sheduling)

This scheduler is optimistic: 
- it allows any sequence of action
- periodically it checks if everything is okay. yes - continue, no - abort the transaction and restart 


Assume we execute 3 transactions $T_1, T_2, T_3$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/timestamp-scheduler.png" alt="Image">
- we allow arbitrary reordering of actions from these transactions
- but we also consistently check if the reordering is equivalent to the [serial schedule](Serializable_Scheduling) $(T_1, T_2, T_3)$
- if not - some transactions are aborted and restarted 


## Rules
Additional information:
- every transaction $T_i$ receives a timestamp $TS(T_i)$
  - $TS(T_i)$ can be either a datetime or just a value that gets incremented on each operation 
  - the higher the $TS(T_i)$, the later $T_i$ started 
- for each DB item $X$ we associate two timestamps and a boolean flag $C(X)$
  - $RT(X)$ - read time of $X$: the $TS(T)$ of the last transaction $T$ that read $X$
  - $WT(X)$ - write time of $X$: the $TS(T)$ of the last transaction $T$ that wrote $X$

Basic Rule: 
- $RT(X)$: every time $X$ is read by $T$ check if 
  - $TS(T) > RT(X)$
  - yes - update the $RT(X) \leftarrow TS(T)$
- $WT(X)$ (initially 0): on every write to $X$ by $T$ check if
  - $TS(T) > WT(X)$
  - yes - update $WT(X) \leftarrow TS(T)$
- $C(X)$
  - true if the latest transaction that wrote to $X$ has committed 
- : this is the transaction $T$ that wrote its $TS(T)$ to $WT(X)$
  - false otherwise


### Problematic Situations
#### Problematic Situation 1
suppose we have the following sequence of actions:
1. $T_\text{start},$ 
1. $U_\text{start},$
1. ${\color{blue}{U \text{ writes } X}},$ - allow this because we're optimistic 
1. ${\color{red}{T \text{ reads } X}},$  - not consistent with the serial schedule $(T, U)$ $\Rightarrow$ abort $T$
1. $...$ 

So the problem is
- $T$ starts before $U$, but $U$ writes before $T$ reads
- should be $T$ reads then $U$ writes

To avoid it we want to check if 
- $TS(T) \geqslant WT(X)$ then we grant a read request $r_T(X)$ to transaction $T$
  - i.e. we should not allow reading of things that were modified by transactions that started later than $T$
- otherwise we abort $T$


#### Problematic Situation 2
The sequence of actions:
1. $U_\text{start},$ 
1. $U \text{ writes } X,$ 
1. $T_\text{start},$
1. $T \text{ reads } X,$
1. ${\color{red}{U_\text{abort}}}, $
1. $...$

Problem:
- Actions 1-4 are consistent with the serial schedule $(U, T)$
- However $U$ aborts 
- that means that read of $X$ by $T$ was inconsistent - it will be rolled back to the old value on $U_\text{abort}$

To avoid that:
- reads to $X$ should be delayed until
- the transaction that last modified $X$ has committed 
  - i.e. the transaction with timestamp $WT(X)$
  - and we wait until $C(X)$ is set to true
- so we do not abort, just pause


#### Problematic Situation 3
Sequence of Actions:
1. $T_\text{start},$
1. $U_\text{start},$ 
1. ${\color{blue}{U \text{ reads } X}},$ - we're optimistic, so the read is successful
1. ${\color{red}{T \text{ writes } X}},$ - not consistent with the serial schedule $(T, U)$
1. $...$

The problem:
- $T$ starts before $U$, but $U$ reads before $T$ writes
- should be $T$ first writes, then $U$ reads the value written by $T$

Solution:
- a write request $w_T(X)$ should be granted if $TS(T) \geqslant RT(X)$
- i.e. if the transaction $U$ that last read $X$ was created before the current transaction $T$


#### Problematic Situation 4
1. $S_\text{start},$
1. ${\color{blue}{S \text{ read } X}},$
1. $T_\text{start},$
1. $U_\text{start},$
1. ${\color{blue}{U \text{ writes } X}},$
1. ${\color{blue}{T \text{ writes } X}},$ - note that in this case we allow $w_T(X)$ (but ignore it) since it "will" be overwritten if executed $(T, U)$
1. $T_\text{commit},$
1. ${\color{red}{U_\text{abort}}}, $
1. $...$

The problem
- we allow, but ignore write of $T$ to $X$: 
  - we know that the value stored in $X$ should be the value written by $U$
  - because in the serial schedule $(T, U)$, $U$ would execute after $T$ and overwrite the value of $X$
- but $U$ aborts afterwards
  - it means we shouldn't have ignored the write by $T$
  - and $X$ should store the value written by $T$ 

Solution:
- $w_T(X)$ is realizable by $T$ if $TS(T) \geqslant RT(X)$ and $TS(T) < WT(X)$
  - the transaction $T$ started later that the transaction $S$ that did the last read of $X$
- : $S_\text{start}, T_\text{start}, S \text{ reads } X, T \text{ writes } X$
  - and $T$ started earlier than some transaction $R$ that did the write to $X$
- : $T_\text{start}, R_\text{start}, R \text{ writes } X, T \text{ writes } X$
- if $C(X)$ is false then $T$ must be delayed till $C(X)$ becomes true
  - i.e. the transaction $R$ that last wrote $X$ has committed
- if $C(X)$ we can ignore the write

### Timestamp-Based Schedule Rules
The rules are:
- every transactin $T$ receives a timestamp $TS(T)$
- to each DB item $X$ we associate values $RT(X), WT(X), C(X)$

Suppose we have a transaction $T$ with $TS(T) = t$ 

$T$ is allowed to read $X$ if
- $t \geqslant WT(X)$
- if $C(X)$ is false, then $T$ is paused until $C(X)$ becomes true or transaction that last wrote $X$ aborts
- if $t < WT(X)$ we abort $T$ and restart it with the next available $TS(T)$

$T$ is allowed to write to $X$ if
- $RT(X) \leqslant t$ and $WT(X) \leqslant t$
- if $t < RT(X)$ then $T$ is aborted and restarted
- if $RT(X) \leqslant t < WT(X)$
  - if $C(X)$ is true we do nothing (keep the current state of $X$)
  - otherwise we pause $T$ until $C(X)$ becomes true or transaction that last wrote $X$ aborts 

These rules prevent all bad cases



## Cons and Pros
- Not very effective when we have many transactions that both read and write - in this case we have to abort and restart many transactions
- When you have few transactions that write it's very efficient - they can proceed immediately


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Concurrency](Category_Concurrency)
[Category:Database Systems Architecture](Category_Database_Systems_Architecture)