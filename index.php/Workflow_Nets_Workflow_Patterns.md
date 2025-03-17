---
title: "Workflow Nets/Workflow Patterns"
layout: default
permalink: /index.php/Workflow_Nets_Workflow_Patterns
---

# Workflow Nets/Workflow Patterns

{{stub}}

## [Workflow Patterns](Workflow_Patterns) in Workflow Nets

### Sequence
First task $a$, then task $b$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-sequence.png" alt="Image">


### Parallel Split
Tasks $b$ and $c$ are processed in parallel
- this construction is also called "AND-split"
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-par-split.png" alt="Image">


### Synchronization
Do $d$ only after both $b$ and $c$ are completed 
- this is a synchronization between two parallel processes 
- this construction is also called "AND-join"
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-synch.png" alt="Image">


### Parallel Routing
A combination of Parallel Split and Synchronization
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-parallel-ex.png" alt="Image">


### Exclusive Choice
after $a$, do $b$ or $c$
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-xor.png" alt="Image">
- choice in this case depends on the results of the activity $a$
- here both '''doA''' and '''doB''' will be active, but we want to fire only one of them, based on the activity $a$ 


### Simple Merge
perform $d$ after $b$ or $c$ finishes
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-xor-merge.png" alt="Image">


### Alternative Routing
a combination of Exclusive Choice and Simple Merge
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-alt-routing.png" alt="Image">


### [Deferred Choice](Deferred_Choice)
When the choice is deferred to the point when we execute something 
- for Petri Nets, visually looks identical to Exclusive Choice
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-deferred-choice.png" alt="Image">


Deferred Choice vs Exclusive Choice
- in Exclusive Choice after execution of $a$ you already know what activity to run
- but for the deferred choice there's a race condition between the activities 


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)
[Category:Petri Nets](Category_Petri_Nets)