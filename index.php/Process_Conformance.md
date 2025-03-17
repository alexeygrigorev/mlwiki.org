---
title: Process Conformance
layout: default
permalink: /index.php/Process_Conformance
---

# Process Conformance

## Workflow Conformance Checking
This procedure gives the answer on the following questions
- does our model conform to what actually happens? 
- does what actually happens conform to the model?
- should we change our workflow to better fit the reality?


So it's 
- what actually happens vs
- what we think happens

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pm/conformance-checking.png" alt="Image">


### Play In
Suppose we have some logs that were captured during the process execution
- we can '''play in''' these sequences of actions on the model 
- and see if any of them fails 
- if yes - then we have no conformance 

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pm/play-in.png" alt="Image">

This is very helpful in
- finding tasks that are not automated and performed outside of the engine
- (sometimes we turn off the workflow engine and add some exceptional cases manually)
- are there lots of these exceptions? then we should add them to the model 


### Simulation (Play Out)
We can try to simulate the execution of our model 
- to see what can change if we add or remove something
- are there any bottlenecks that have appeared after the change?

To do this we need to define the environment of execution
- need to have the process itself
- for each activity
  - times and priorities 
  - statistics on how often a certain branch is followed
- frequency of incoming cases 
- the number of resources that can handle the cases


So given the statistics
- a some kind of random walk process is executed
- it basically traverses the [Reachability Graph](Reachability_Graph) of a model
- and emulates the delays, etc

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pm/play-out.png" alt="Image">

After the execution we can see:
- avg execution time
- resource utilization
- etc


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)