---
layout: default
permalink: /index.php/Validation-Based_Scheduler
tags:
- concurrency
- database-systems-architecture
title: Validation-Based Scheduler
---
## Validation-Based Scheduler
This is a [Scheduler](Scheduler) that gives [Conflict-Serializable Schedule](Serializable_Sheduling)

This scheduler is optimistic (similar idea to [Timestamp-Based Scheduler](Timestamp-Based_Scheduler)): 
- it allows any sequence of action
- periodically it checks if everything is okay. yes - continue, no - abort the transaction and restart 


## Rules
for every transaction $T$ we record 
- a set of database items $RS(T)$ that were read by $T$
- a set of database items $WS(T)$ that is wants to write / were written by $T$

All transactions are executed in 3 phases
- transactions are '''only allowed to read''' 
  - when an item $X$ is read by $T$, $X$ is added to $RS(T)$
- the scheduler validated the schedule based on 
  - actions read by $T$: $RT(T)$
  - actions $T$ wants to write: $WS(T)$ (but has not written yet)
- : if validation fails, $T$ is restarted
- $T$ can write all items from $WS(T)$


### Problematic Situations
#### Problematic Situation 1
Actions:
1. $U_\text{start},$
1. $T_\text{start},$
1. ${\color{red}{T \text{ reads } X}},$
1. $U_\text{validate},$
1. ${\color{red}{U \text{ writes } X}},$
1. $T_\text{validate},$
1. ...

The problem:
- $U$ should have written $X$ before $T$ reads it
- not consistent with the serial schedule $(U, T)$
- i.e. it should be $U \text{ writes } X, T \text{ reads } X$

For every transaction $T$ we records 
- $\text{START}(T)$ - the time when $T$ starts
- $\text{VAL}(T)$ - the time when $T$ validates
- $\text{FIN}(T)$ - the time when $T$ finishes

$T$ can successfully validate if 
- $RS(T)$ is disjoint with $WS(U)$: $RS(T) \cap WS(U) = \varnothing$
  - $RS(T)$ - reads by the current transactions
  - $WS(U)$ - writes by other transactions $U$
  - $U$ - all transactions that already validated, but have not finished when $T$ started
  - (i.e. those $U$ for which $\text{FIN}(U) > \text{START}(T)$)

In this problematic example we have:
- $X \in WS(U)$ - $U$ has already validated, but has not finished
- $RT(T) \cap WS(U) = \{ X \}$: $T$ read $X$ that was later modified by $Y$
- $T$ will be restarted


#### Problematic Situation 2
Actions:
1. $U_\text{validate},$
1. $T_\text{validate},$
1. ${\color{red}{T \text{ writes } X}},$
1. $U \text{ writes } X,$
1. $U_\text{finish},$
1. $...$

The problem:
- $T$ writes $X$ first - before $U$
  - not consistent with the serial schedule $(U, T)$
- should be first write by $U$, then write by $T$
- after validation they are allowed to write in any order, but we have to make sure it respects the $(U, T)$ order

$T$ can successfully validate if 
- $WS(T) \cap WS(U) = \varnothing$
  - $WS(T)$ - items that $T$ wants to write (before validation - means "it wants to write")
  - $WS(U)$ - items that $U$ writes (after validation - means either "it wants to write" or "it has written")
- should hold for all previously validated $U$ that did not finish before $T$ validated,
  - i.e. for such $U$ that $\text{FIN}(U) > \text{VAL}(T)$

In this problematic example we have:
- $WS(T) \cap WS(U) = \{ X \}$
  - $T$ wants to write $X$
  - $U$ also wants to write $X$, but $U$ was validated before $T$
- therefore $T$ is not allowed to start


### Summary
$T$ passes validation if 
- $RS(T) \cap WS(U) = \varnothing$ for all $U$ s.t. $\text{FIN}(U) > \text{START}(T)$
- $WS(T) \cap WS(U) = \varnothing$ for all $U$ s.t. $\text{FIN}(U) > \text{VAL}(T)$

Everything that doesn't pass the validation is aborted and restarted 


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
