---
title: "Discriminator Pattern"
layout: default
permalink: /index.php/Discriminator_Pattern
---

# Discriminator Pattern

## Discriminator Pattern
This is a Control flow pattern in [Workflow Patterns](Workflow_Patterns). 


Suppose that
- two processes are running in parallel 
- merge is activated when one of them ends 
- the result of the other is just ignored

### Examples
Example 1:
- to speed up a query we send it to two databases 
- once the first answer arrives we proceed 
- and just ignore the second answer 



## Types
There are 6 kinds of Discriminator pattern [http://www.workflowpatterns.com/patterns/control/index.php]:
- the Structured Discriminator (WCP9), 
- the Blocking Discriminator (WCP28), 
- the Cancelling Discriminator (WCP29), 
- the Structured Partial Join (WCP30),
- the Blocking Partial Join (WCP31) and 
- the Cancelling Partial Join (WCP32).


### Canceling Discriminator
This is a discriminator that cancels the other process [http://www.workflowpatterns.com/patterns/control/new/wcp29.php]

In [YAWL](YAWL) this is achieved:
- with one Parallel Split (AND-Split)
- a [Cancellation Region](Cancellation_Regions) for the two processes 
- one Simple Merge (XOR-Join) that is also the cancel task for the cancellation region

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-dicr-canc.png" alt="Image">


What if we don't want to interrupt the 2nd activity?
- for example, in a hospital we want to do two tests 
- we start treating the patient as soon as the first result arrives
- but we cannot discard the results of the second result
- so we do the full analysis when we have both results 

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-dicr-non-canc1.png" alt="Image">
- this way we start treatment as soon as possible
- but start the full diagnosis only when the second arrive


We may as well add a timing constrain
- we wait for the result only for 24 hours 
- and then do the diagnosis based only on partial information

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-dicr-timer.png" alt="Image">

if $A$ has finish, but $B$ hasn't
- case 1:
  - timeout task times out
  - then it fires and takes token from $B$
  - and also puts a token to the input place for full diagnosis
  - full diagnosis can start
- case 2:
  - timeout starts to count down 
  - but $B$ finishes
  - full diagnosis starts 
  - it takes the token from the timeout task so it is no longer enabled




## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)