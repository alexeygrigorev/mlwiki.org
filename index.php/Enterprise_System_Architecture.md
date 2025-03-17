---
title: "Enterprise System Architecture"
layout: default
permalink: /index.php/Enterprise_System_Architecture
---

# Enterprise System Architecture

## Enterprise System Architecture
This is a motivation why workflow management systems are needed

## Evolution of Integration
### No Integration
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/esa-no-integration.png" alt="Image">

There are 3 systems:
- HR: human resources 
- POM: purchase order management
- WM: warehouse management 

No integration:
- a change in one DB is not propagated to others (automatically)
- this has to be maintained 
- suppose an address changes in HR, but the rest don't know about it
- $\Rightarrow$ [inconsistency](Consistency_(databases))


### Central ERP System
This is also called 2-tier client-server architecture 

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/esa-central-erp.png" alt="Image">
- there's a central ERP system that explicitly integrates all the data into one source 
- but there are performance issues
- and what if the ERP server goes down?


### Application Integration
There are several ways to integrate different application

#### Point-To-Point
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/esa-central-p2p.png" alt="Image">
- every system communicated with all other systems 
- $N^2$ connections for $N$ systems - a lot|   | |
#### Message-Oriented Middleware
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/esa-mom.png" alt="Image">
- each client connects to the Integration Application 
- IA dispatches the messages to the receivers 
- this approach takes away the burden of implementing all the connectors
- but it's still point-to-point: all must know about others
- $\cfrac{N \cdot (N - 1)}{2}$ connections in this scheme


#### Application Integration
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/esa-central-hub.png" alt="Image">
- now there's a hub: a centralized integration middleware: it orchestrates the flow
- the hub acts as a message broker: it defines the rules for communication and transformation
- system no longer need to know about each other 
- it's similar to emailing: no need to know about the received: where is he, whether he can read now or not, etc

The differences between it and central ERP:
- in the central ERP there's one single DB
- here each application has it's own database 


### Workflow Management Systems
There are three kind of workflow management systems:
- hard-coded workflows (process and organization specific)
- custom-made (with some generic wokrkflow but still organization specific)
- generic software with embedded workflow functionality 
  - workflow components of one particular type of systems, say ERP
- generic software focused on workflow
  - how we can connect different components from different manufactures
  - allows great flexibility 



## Sources
- [Business Process Management (ULB)](Business_Process_Management_(ULB))

[Category:Business Process Management](Category_Business_Process_Management)
[Category:Software Design](Category_Software_Design)