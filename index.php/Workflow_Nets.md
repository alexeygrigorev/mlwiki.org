---
layout: default
permalink: /index.php/Workflow_Nets
tags:
- business-process-management
- petri-nets
title: Workflow Nets
---
## Workflow Nets
By workflow nets here we refer to [petri-net-based](Petri_Nets) workflows. 

So, a ''workflow net'' is a special type of a petri net that is suitable for expressing workflows 

In a workflow net:
- there's a clear start: 
  - the unique dedicated ''input place'' $i$ s.t.
  - $\bullet i = \varnothing$
  - i.e. no transition can put a token to $i$
- there's a clear end:
  - the unique dedicated ''output place'' $o$ s.t.
  - $o \bullet = \varnothing$
  - i.e. no transitions should consume tokens from $o$
- every other transition and place are on the path from $i$ to $o$ 

Markings:
- initial marking $M_0$: 
  - $M_0(i) = 1, \forall p \ne i: M_0(p) = 0$


### Examples
Not workflow nets
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/workflow-nets-notwf.png" alt="Image">
- (1): no start, no end
- (2): $b$ is not connected to the end
- (3): $d$ is also not on the path from $i$ to $o$

Workflow net:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pn/workflow-nets-ex.png" alt="Image">
- all workflow net properties are satisfied



## Soundness
<!-- Main: Workflow Soundness -->
There are situations that we want to avoid:
- unboundness 
- livelocks and deadlocks
- dead transitions

For that we define the following properties
- Option To Complete 
- Proper Termination
- No Dead Transitions


## [Workflow Patterns](Workflow_Patterns)
<!-- Main: Workflow Nets/Workflow Patterns -->

## Housing Agency Assignment
- [Housing Agency Workflow](Housing_Agency_Workflow)


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))
