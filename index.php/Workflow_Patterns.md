---
layout: default
permalink: /index.php/Workflow_Patterns
tags:
- business-process-management
title: Workflow Patterns
---
## Workflow Patterns
Workflow patterns help to express the constructions common to workflows
- http://www.workflowpatterns.com/
- here we consider control flow patterns: http://www.workflowpatterns.com/patterns/control/index.php


## Basic Control Flow Patterns
### Sequence
First task $A$, then task $B$ [http://www.workflowpatterns.com/patterns/control/basic/wcp1.php]:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-sequence.png" alt="Image">

### Parallel Split
Tasks $b$ and $c$ are processed in parallel [http://www.workflowpatterns.com/patterns/control/basic/wcp2.php]
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-par-split.png" alt="Image">


### Synchronization
Do $d$ only after both $b$ and $c$ are completed [http://www.workflowpatterns.com/patterns/control/basic/wcp3.php]
- this is a synchronization between two parallel processes 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-synch.png" alt="Image">


### Exclusive Choice
after $a$, do $b$ or $c$ [http://www.workflowpatterns.com/patterns/control/basic/wcp4.php]
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-xor.png" alt="Image">


### Simple Merge
perform $d$ after $b$ or $c$ finishes [http://www.workflowpatterns.com/patterns/control/basic/wcp5.php]
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-xor-merge.png" alt="Image">


## Advanced Branching and Synchronization Patterns
- Multiple Choice 
- Synchronized Merge 
- Multi Merge 
- [Discriminator Pattern](Discriminator_Pattern)
- Arbitrary Cycles


## Termination Patterns
- Implicit Termination



## State-Based Patterns
- [Deferred Choice](Deferred_Choice)
- Interleaved Parallel Routing
- [Milestone Pattern](Milestone_Pattern)


## Cancellation and Force Completion Patterns
- [Cancellation Region](Cancellation_Regions)
- Cancel Activity
- Cancel Case


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))
