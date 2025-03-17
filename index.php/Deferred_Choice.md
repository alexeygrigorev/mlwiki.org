---
title: Deferred Choice
layout: default
permalink: /index.php/Deferred_Choice
---

# Deferred Choice

## Deferred Choice
Deferred Choice is a [workflow pattern](Workflow_Patterns). It it used to express a situation when the action you're going to take is not known till the point of executing it.

So, ''Deferred choice'': When the choice is deferred to the point when we execute something 
- for Petri Nets, visually looks identical to Exclusive Choice
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/petri-net-deferred-choice.png" alt="Image">


Deferred Choice vs Exclusive Choice
- in Exclusive Choice after execution of $a$ you already know what activity to run
- but for the deferred choice there's a race condition between the activities 


### Example
Consider a flight:
- you can either print ticket at home or check in at reception
- based on this the following procedures are different
- it's a deferred choice: the company doesn't know which option you chose


## [YAWL](YAWL)
In YAWL it's possible to tell the difference between XOR-split and Deferred choice

Consider this:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-deferred-choice.png" alt="Image">
- we start with deferred choice: 
  - both actions are enabled, and both are offered to the user 
  - and the user decides what to do next
- but XOR-split is different
  - based on some variables that were set before it (itself, not the user|  ) chooses the route |  - for example, if variable <code>dosomething</code> is set to true, we follow the top branch |

## [BPMN](BPMN)
In BMPN the deferred choice is represented by a special-purpose gateway
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-deferred-choice.png" alt="Image">


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)