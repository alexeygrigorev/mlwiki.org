---
layout: default
permalink: /index.php/Two-Phase_Commit
tags:
- database-systems-architecture
- distributed-systems
title: Two-Phase Commit
---
## Two-Phase Commit
A way to ensure consistency in a [distributed system](Distributed_Databases)


## Two Phases
; Phase 1
- coordinator sends "prepare to commit" message
- subordinates make sure they can do that no matter what happens 
- write the action to a [Database Transaction Log](Database_Transaction_Log) to tolerate failures
- subordinates reply with "ready to commit" message

; Phase 2
- if all ready, send "commit"
- if anyone fails, send "abort"


## Example
<img src="https://raw.github.com/alexeygrigorev/ulb-adb-project-couchbd/master/report/images/two-phase-commit.png" alt="Image">

1. Coordinator: update
1. Coordinator: prepare to commit
1. Subordinate: write to log
1. Subordinate: say "ready"
1. Coordinator: commit


## See also
- [ACID](ACID): [Consistency (databases)](Consistency_(databases)) and [Durability (databases)](Durability_(databases))

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
