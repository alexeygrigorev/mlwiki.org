---
title: Durability (databases)
layout: default
permalink: /index.php/Durability_(databases)
---

# Durability (databases)

## Durability
One of the [ACID](ACID) properties of transactions. It says if a transaction has committed, then it should be permanently persisted on disk, even if a crash occurs

Techniques for [Crash Recovery](Crash_Recovery) are usually [Database Transaction Log](Database_Transaction_Log)s:
- [Undo Logging](Undo_Logging)
- [Redo Logging](Redo_Logging)
- [Undo/Redo Logging](Undo_Redo_Logging)

In [Distributed Databases](Distributed_Databases) for distributed transactions there are also some protocols for ensuring durability:
- [Two-Phase Commit](Two-Phase_Commit) 

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- [Durability (database systems)](http://en.wikipedia.org/wiki/Durability_%28database_systems%29)

## See also
- [ACID](ACID)

[Category:Databases](Category_Databases)