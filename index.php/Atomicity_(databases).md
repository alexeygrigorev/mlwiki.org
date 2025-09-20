---
layout: default
permalink: /index.php/Atomicity_(databases)
tags:
- databases
title: Atomicity (databases)
---
## Atomicity
''Atomicity'' is a desired property of a transaction according to [ACID](ACID)
- a transaction should be either executed completely - or not executed at all
- If it executed - it takes database from one [consistent](Consistency_(databases)) state to another
- if not executed - it takes database back to the consistent state it was before execution
- It's especially important when dealing with [Crash Recovery](Crash_Recovery)

Ways to ensure Atomicity:
- [Database Transaction Log](Database_Transaction_Log)

## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
