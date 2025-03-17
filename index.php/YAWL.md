---
title: YAWL
layout: default
permalink: /index.php/YAWL
---

# YAWL

## YAWL
YAWL is a graphical notation for expressing workflows, similar to [Workflow Nets](Workflow_Nets) based on [Petri Nets](Petri_Nets), but with more expressive syntax.
- YAWL is based on [Workflow Patterns](Workflow_Patterns)
- but it's developed in academic environment


It is possible to express the following constructions:
- choices
- timeouts
- etc

## Basic Syntax
Syntax in YAWL looks similar to [Petri Nets](Petri_Nets)
- but there is syntactic sugar that makes it easier and more expressive
- and there also is some relaxation of the rules

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-and-xor.png" alt="Image">

### AND
AND-split:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-and-split.png" alt="Image">

AND-join
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-and-join.png" alt="Image">
- note that the semantics of the AND-join in YAWL is the same: 
- both places need to have tokens for $d$ to fire

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-and.png" alt="Image">


### XOR
XOR-split
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-xor-split.png" alt="Image">
- need to put some code to the XOR-split node: so it will decide which way to follow
- (don't confuse with [Deferred Choice](Deferred_Choice))

XOR-join
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-xor-join.png" alt="Image">
- semantics is the same: $d$ can fire if there's a token in either place

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-xor.png" alt="Image">



### Loops
While-loop
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-while-loop.png" alt="Image">
- based on the condition in the XOR-split it either continues or stops
- it was not possible to express that in [Workflow Nets](Workflow_Nets)


Repeat-loop
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-repeat-loop.png" alt="Image">
- until the condition in the XOR-split is not satisfied, $B$ will not be enabled


### Start and Stop
There's also a special notation for start and stop places
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-start-stop.png" alt="Image">


### Transitions
Transitions in YAWL can be connected directly, without a place within them
- but there still is an implicit invisible place between such transactions
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-transitions.png" alt="Image">
- if there's a place between transitions, it means that one is done, but the other has not started


Transitions in YAWL are no longer atomic 
- in YAWL now you cannot assume that they fire immediately: they may need some time to do the task
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-transitions-2.png" alt="Image">
- so in essence, one transition in YAWL correspond to two transitions in a Petri Net and one place between them



### Exercise
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-ex-seq.png" alt="Image">
- what are the valid firing sequences? what activities can be performed in parallel?
- first, let's explicitly show the invisible places and name all the places
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-ex-seq2.png" alt="Image">
- now we can build some kind of a [Reachability Graph](Reachability_Graph) (here we don't consider places inside the transactions)
- but in this case, unlike in [Petri Nets](Petri_Nets), firing one transition can lead to several states 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-ex-seq2-rg.png" alt="Image">
- in this example firing $B$ may bring to 3 different states, depending on what arch it will take
- we see that this network in not [sound](Workflow_Soundness):
  - it has no option to complete in several cases
  - it has improper termination 
- the highlighted edges lead to the final state 
  - thus the valid firing sequences are:
  - $ABCD$
  - $ABCEFG$
  - $ABCFEG$
  - $ABCFEG$
  - $ABCCEFG$
  - $ABCCFEG$
  - note that, for instance, $ABCCEFG$ may correspond to two different paths in the reachability graph 
- based on that it's clear that $E$ and $F$ can run in parallel


## Advanced Syntax
### Cancellation Regions
{{ Main |  Cancellation Regions}} |

### OR-Split and OR-Join
#### OR-Split
OR-split is similar to XOR-split
- but instead of taking one route, it can take many 

Example
- suppose we're buying a flight ticket and offered 2 additional options: hotel and car
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-or-split.png" alt="Image">
- the branches to active depend on what exactly you have selected
- and the OR-split should be programmed to route in the needed directions
- the system can fire many tokens, but there's one restriction: there must be at least one token

Note that
- OR-split is just syntactic sugar 
- it can be expressed with AND-splits and XOR-splits
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-or-split-with-and-xor.png" alt="Image">


#### OR-Join
OR-Join is used to synchronize many incoming branches

It has the "bus driver" semantics
- OR-Join is activated only when all tokens are ready to be consumed
- a bus driver will wait for people to jump in when he sees that people are still coming


We should handle OR-joins 
- this semantics can be computationally quite expensive
- some decision properties may suddenly become unavailable
- if complicates the model


Example
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-or-join.png" alt="Image">
- if there are still tokens to arrive, the OR-join will wait for them 
- once everybody is ready - it fires

Consider the following net:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-or-join-dilemma.png" alt="Image">
- in this example none of the OR-joins can fire
- there hypothetically can be more tokens to arrive
- so they are waiting
- no [Option to Complete](Workflow_Soundness)


#### Examples
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-or-join-ex.png" alt="Image">
- case (a):
  - $C$ is enabled: it's a XOR join
  - and $D$ is enabled: it's not possible to get a token from another branch
- case (b):
  - $C$ is working, but it can be started again: it's enabled since there's another token
  - $D$ is not enabled: it will be only when $C$ finishes its work
- case (c): 
  - $A$ is already running 
  - $C$ is enabled (here it's the same situation as in the case (a))
  - but $D$ is not enabled: there's in a token inside $A$, which may arrive from the branch below
- case (d):
  - $C$ enabled 
  - but $D$ is not enabled: there's a token before $C$ that may arrive 


### Sub-Nets
To increase readability it's possible to fold some activities to one 
- this concept is called a ''sub-net''
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-subnets.png" alt="Image">
- a subnet must also be a valid net - with its own start and stop places 



## Data
It is possible to store some variables in the YAWL engine
- to keep the results of execution, etc

Data can be stored at different levels (i.e. scopes)
- process level - global
- case level - related to this particular case 
  - i.e. data for each case is different
- task level - most local 

We don't need to transfer data from activity to activity
- there's a single data storage that will keep it
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-datastorage.png" alt="Image">


## Timers
'''TODO'''


## Resource Perspective
'''TODO'''


## YAWL Option to Complete
YAWL's option to complete is different from the [option to complete](Workflow_Soundness) property of [Workflow Nets](Workflow_Nets)

YAWL-OTC:
- for every reachable marking $M$ we can reach the final marking $[o]$
- so this is a combination of Option to Complete and Proper Termination
- unfortunately YAWL-OTC is not always decidable, therefore it's sometimes still better to use the definition of the Option to (improperly) Complete 


## Examples
### Housing Agency Net
- [Housing Agency Workflow](Housing_Agency_Workflow)


### Example 2: Travel Agency
To organize a trip
- the customer request is registered
- then an employee looks for opportunities 
- the customer is contacted to find out whether he is still 
interested and whether more alternatives are desired
- if the customer selects a trip, then the trip is booked. 
- in parallel (optionally) one or two types of insurance are prepared
- two weeks before the start date the documents are sent to the customer
- it is possible that the customer cancels the trip at any time before the start date

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-travel-agency.png" alt="Image">

It is also possible to use OR-join for choosing the insurances:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-travel-agency-orjoin.png" alt="Image">


### Example 3: Homework Submission
An exercise for modeling from the resource perspective:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-assignment-submission.png" alt="Image">


### Example 4: Four Dining Philosophers
The same net as in [Petri Nets](Petri_Nets):
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-dining-philosophers.png" alt="Image">



## Links
- http://www.yawlfoundation.org/yawlbook/downloads.html
- http://yawlfoundation.org/yawldocs/GettingStartedWithYAWL.pdf

## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)