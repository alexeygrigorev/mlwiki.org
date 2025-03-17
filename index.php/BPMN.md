---
title: "BPMN"
layout: default
permalink: /index.php/BPMN
---

# BPMN

## BPMN
BPMN - Business Process Modeling Notation 
- This is a graphical language for describing business processes for [BPM](BPM)
- BPMN 2.0 is de-facto the industrial standard for [BPM](BPM)
- executable via [BPeL](BPeL) or there are tools that natively support execution of BPM


## Control Flow Syntax
Differences with [YAWL](YAWL) and [Workflow Nets](Workflow_Nets)
- no such things as places in BPML


### Activities
Activities are things that are performed as a part of the process 

They can be:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-activities.png" alt="Image">
- task: a single business action
- look: an action that repeats over time
- sub-process that contains other process inside
- and all other things 


### Gateways
Gateways are needed for routing purposes

There are the following gateways
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-gateways.png" alt="Image">
- AND-split and AND-join
- XOR-split and XOR-join
- Event-based (which is [Deferred Choice](Deferred_Choice))
- OR-split and OR-join (same semantics as in [YAWL](YAWL))


Note that activities can be connected to multiple activities without any gateways 
- but these gateways are implicitly assumed in this case 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-activities-impl-gateways.png" alt="Image">
- so be careful with the following construction:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-activities-impl-gateways-careful1.png" alt="Image">
- because it will implicitly assumed to be something like the following
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-activities-impl-gateways-careful2.png" alt="Image">


### Events
Events represent actions that take place 
- when the flow starts and ends
- when something happens on the way from start to end 
- it is also possible to add some decorations to express meaning of some events

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-events.png" alt="Image">


During the flow some exceptions can occur

There are 2 types of events for that:
- "throw" events
- "catch" events


Exceptions:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-exceptions.png" alt="Image">
- something inside a subflow can throw an exception
- and there are "guarding" listeners that are triggered when such exceptions are thrown


Consider this example:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-exceptions-ex.png" alt="Image">
- there's one throwing event that interrupts the flow 
  - ''throwing event''
  - produces some events 
  - these events are interrupting: the flow ends with such event
- and this exception is caught outside of the subflow and handled 
  - ''catching event''
  - listens for certain events
- we also have ''non-interrupting'' events - border events 
  - they are activated when something happens outside of the flow


Also note that in this example there are two blocking intermediate events
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-events-receive.png" alt="Image">
- these events stop the flow and resume when a message is received
- note that in this case such events keep tokens inside
- so we need a concept of [Cancellation Regions](Cancellation_Regions) to be able to terminate all subprocess 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-events-bullseye.png" alt="Image"> terminates all the processes and stops the flow 


Here's a list of decorations for events:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-events-all.png" alt="Image">



### Pools and Lines
Different organizations and different actors withing the organization are represented with 
- pools for organizations
- lines withing the pools for actors
- that makes it possible to show visually who is in charge of what


If a task is on a line that belongs to some actor,
- he is responsible for executing it


External actors
- it is advisable to model external actors - actors that do not execute the business process themselves (clients, etc) - with "empty" pools
- this way the interaction with them can be clearly seen
- it is good because such actors do not perform any actions, but they generate "incoming events"
- and we don't have any illusion that we have control over what the external actors 
- we interact with them only with messages 


Example:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-external.png" alt="Image">
- a student is an external actor: they generate events but do not execute any business process themselves
- student is "abstract" - there are no actions in this pool


## Approach for Building a Model
1. Decide: when does process start/end
1. Enumerate main activities & possible end-states
1. Create top-level BPMN diagram
1. Expand top-level activities to sub-processes
1. Add pools for external parties & message flow (business context)
1. Repeat 4-5 for sub-processes

Walk-through example:
- [Car Dealer Example](http://www.evernote.com/shard/s344/sh/7e4b0db5-002c-4d67-a813-6a8b8d54070b/11743304157d0e41b60ca0ed6c172ac5) (With pictures taken during the lecture)


## Examples
Example 1: 
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-ex1.png" alt="Image">


Example 2:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-exceptions-ex.png" alt="Image">


Example 3:
- booking a trip
- [YAWL](YAWL) diagram:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/yawl/yawl-travel-agency.png" alt="Image">
- converting it to BPMN:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpmn/bpmn-insurance-ex.png" alt="Image">



## Links
- Lecture notes from Evernote: [https://www.evernote.com/shard/s344/sh/9de02c1b-f96f-41ff-9095-13ae608be099/e1e4dd29c665b5f2a6f21c45ea90a467] 
- BPMN 2.0 reference card [http://www.chellar.com/AnalysisFu/images/ccp/BPMN_Poster.pdf]
- [Exercises 1](http://dl.dropboxusercontent.com/u/5119252/BPM/2013/Exercises%20BPMN.pdf) [Solutions 1](http://dl.dropboxusercontent.com/u/5119252/BPM/2013/Solution%20BPMN.pdf)
- [Exercises 2](http://dl.dropboxusercontent.com/u/5119252/BPM/2013/BPMN%20Modeling.pdf) [Solutions 2](http://dl.dropboxusercontent.com/u/5119252/BPM/2013/Solutions%20BPMN%20Modeling.pdf) ([in-class notes](http://www.evernote.com/shard/s344/sh/5c34000b-89aa-4277-93e9-54ac3ba77e98/79ca7457df8ba7aac3766ac2656d9235))



## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)