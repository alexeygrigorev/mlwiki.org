---
title: "Cancellation Regions"
layout: default
permalink: /index.php/Cancellation_Regions
---

# Cancellation Regions

## Cancellation Regions
Consider the following scenario:
- at each point of time the user may decide to cancel the order 
- this is very difficult to express with plain [Workflow Nets](Workflow_Nets)
- therefore in [YAWL](YAWL) there is a special syntactic construction for that

### Motivation
- at the beginning we have the following
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-motiv1.png" alt="Image">
- now we need to be able to cancel the task at the bottom:
- we add a special cancel task for this that takes the token and puts it directly to the final place
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-motiv2.png" alt="Image">
- then we add more such cancel tasks
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-motiv3.png" alt="Image">
- so it quickly becomes cluttered and unreadable


### Syntax
A ''cancellation region'' consists of
- a number of tasks and places 
- transitions between tasks - recall that in YAWL they contain "hidden" places
- the cancellation task


Semantics
- upon completion of the cancellation task all tokens in the cancellation region are removed
- so it guarantees the [proper completion](Workflow_Soundness) property:
- it makes sure the unneeded tokes are removed and no other activity within the Cancellation Region is performed


Syntax:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-syntax.png" alt="Image">
- if there was something in the cancellation region when the cancellation task was activated
- it will be removed


### Usage Pattern
Typical Pattern of Usage:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-pattern.png" alt="Image">
- there's a cancellation place before the cancellation task
- when the job inside the cancellation region is done, '''close case''' takes a token away from this place
- so the cancel task is no longer active 
- but if the cancel task fires, it takes the token from the cancellation regions and finishes the case


### [Workflow Soundness](Workflow_Soundness)
In [Workflow Nets](Workflow_Nets) unboundness always means unsoundness 
- but with cancellation regions it's no longer the case 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-unboundness.png" alt="Image">
- but [Reachability Graph](Reachability_Graph) can no longer be used to decide on soundness: it's infinitely large now
- for that we use [Coverability Graph](Coverability_Graph)


## Examples
### Booking
- a flight, hotel and car can be booked in parallel. 
- if booking of all three succeeds the payment follows. 
- otherwise task cancel is executed
- cancel is delayed until all three bookings succeed/fail
- if something is already booked, nothing is reverted: it remains booked


We model it the following way:
- each option can either fail of succeed, therefore for each we have two possible output places
- the waiting is modeled with OR-Join which, because of its Bus-Driver semantics, will wait for all possible tokens to come: we connect it with all fail places
- the OR-join is the cancellation task that will put the tokens out of succeeded places on activation
- if we used XOR-join instead of OR-join, then it would fire once there's at least one token in any of the failed places
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-1.png" alt="Image">



Consider a slightly different scenario:
- cancel is not delayed until everything fails/succeeds
- if there are booking tasks that have not started yet, they are canceled as well 


The model above is changed a little bit:
- now we use XOR-join: one there's a token, it fires
- and the cancellation region is expanded to include everything after the AND-split
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-2.png" alt="Image">

Note that in this case the cancel task is itself a part of the cancellation region
- it's to ensure that all tokens are removed and cancel can never fire twice

Assume it wasn't the part of the CR
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-3-nocr.png" alt="Image">
- suppose booking of hotel and car failed 
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-3-2tok.png" alt="Image">
  - if one is fired first, then this will remove the remaining token
  - but what if both tokens are already allocated and now are in the cancel task:
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-3-2tok2.png" alt="Image">
  - it processes one token and outputs it
  - <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-cr-booking-3-2tok3.png" alt="Image">
  - but now it can fire the second time|   | |
## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)