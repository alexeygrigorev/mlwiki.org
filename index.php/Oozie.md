---
layout: default
permalink: /index.php/Oozie
tags:
- etl
- hadoop
- workflow-management
title: Oozie
---
## Apache Oozie
[Apache Oozie](Oozie) is a workflow manager, designed especially for running [Hadoop MapReduce](Hadoop_MapReduce) jobs

It contains 2 parts:
- workflow engine: runs workflow jobs (MR, Pig, Hive)
- coordinator engine: coordinates the execution


It's a service:
- Oozie is a service that runs on the cluster 
- the client submits only workflow definitions
- so, unlike hadoop <code>JobControl</code>, it doesn't submit the tasks itself


### Workflow
A ''workflow'' is a [DAG](Graphs#Directed_Acyclic_Graph)  of ''action nodes''
and ''control-flow nodes''

Action Nodes 
- perform workflow tasks 
- e.g. running [Hadoop MapReduce](Hadoop_MapReduce), [Pig](Pig) or [Hive](Hive) jobs
- can also be an arbitrary shell script or a Java program


Control Flow Nodes
- Conditional logic (if, else, etc)
- Parallel execution 

The Oozie workflow is written in [XML](XML) using Hadoop Process Definition language

## Editors
Hue has Oozie Workflow editor - so it is possible to design workflows manually
- see http://gethue.com/new-apache-oozie-workflow-coordinator-bundle-editors/
