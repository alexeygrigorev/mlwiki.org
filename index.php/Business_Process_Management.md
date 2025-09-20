---
layout: default
permalink: /index.php/Business_Process_Management
tags:
- business-process-management
title: Business Process Management
---
## Business Process Management
a ''business process'' consists of a set of activities that are performed in coordination in an organization and technical environment
- these process jointly implement some ''business goal''
- (Weske, 2007)

Motivation:
- [Enterprise System Architecture](Enterprise_System_Architecture) - why BPM systems are needed



### Example: IT4BI
Consider a process of IT4BI admission

Activities:
- Receive an application
- Assign an identifier
- Evaluate an application
- Request for more information
- Select candidates
- Communicate the results 
- Send rankings to the European Commission
- Send invitations - for visas
- Admission to the University
- and many others

This is a business process 


### BPM: Managing Business Processes
How to model BPs?
- [Petri Nets](Petri_Nets) and [Workflow Nets](Workflow_Nets) - basis, originally for modeling concurrent systems
- [YAWL](YAWL) - academic 
- [BPMN](BPMN) - the de-facto standard


### BPM Lifecycle
BPM is more than just modeling: 
- [Process Mining](Process_Mining) - to discover existing processes in a company 
- Process Analysis - in the model correct or not, is the process consistent with the model? (see [Process Conformance](Process_Conformance)) 
- Process Enacting - putting a model into software
- Process Monitoring - how much time each task takes?
- Process Simulation - after creating a model we try to see what would happen if we used it


<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ulb/bpm/bpm-lifecycle.png" alt="Image">

$(1) \to (2) \to (3) \to (4) \to (1)$
- is a BPM lifecycle


### [Process Mining](Process_Mining)
Process Mining is about discovering the existent process and creating a model from it

There are several process mining algorithms. For example,
- [Alpha Algorithm](Alpha_Algorithm)
- [Genetic Process Miner](Genetic_Process_Miner)
- and others 


## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))
