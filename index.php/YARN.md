---
title: "YARN"
layout: default
permalink: /index.php/YARN
---

# YARN

## YARN
YARN stands for "Yet another resource negotiator"
- it's a [Hadoop](Hadoop) cluster resource manager system 
- it's not restricted to [Hadoop MapReduce](Hadoop_MapReduce) and can run any systems, e.g. [Flink](Flink)
- it's an alternative to Hadoop TaskTracker - which is referred as "Hadoop1"
- YARN is "Hadoop2"


YARN
- so YARN is API for requesting and working with cluster resources 
- it's for frameworks, not for users


### Components
<img src="https://habrastorage.org/files/0b8/698/e0c/0b8698e0c74b46c58f8ec81ac1e8ed5d.png" alt="Image"> {{void| yarn.png}} |
It has: 
- Resource Manager: one per cluster
- Node Managers: per each node 

Roles of components:
- node managers launch and monitor containers (which are unix processes)
- a client contacts the RM and asks to run a ''master process''
- if the requirements can be satisfied, YARN finds a node manager that can run it 
- then the application master can request more containers for its processes

a resource request in YARN is a set of constraints that include: 
- memory constrain: how much memory should a container have
- CPU: how much cores
- locality constant: container should be as close to data as possible


## Job Execution
How a Job is Executed
- Let us consider how YARN executes a Hadoop MapReduce job
- <img src="https://habrastorage.org/files/de8/b3c/41e/de8b3c41e9834c6681569c30ddc72ad4.png" alt="Image"> {{void| yarn-jobexecution.png}} |
There are 5 entities 
- client - submits the job
- YARN Resource Manager - coordinates allocation of resources
- YARN Node Manager - launches and monitors containers on the machines of the cluster 
- MR Application Master - coordinates the tasks that run the MR job 
  - MR tasks and the Application Master run the container scheduled by the Resource anager 
  - it is managed by the Node Manager
- [HDFS](HDFS) for sharing job files


### Job Submission
The client submits the job
- typically done via <code>job.waitForCompletion(true)</code>
- the client also pulls the job's execution status and progress each second and reports to the user


Job Submission:
- asks the Resource Manager for a new application id - it will used as the MR Job id
- checks out the specification of the job
- computes the input splits 
- copies the job resources: jars, config, computed input split
- submits the job


### Job Initialization
- when the Resource Manager get a call to its <code>submit</code>, it passes it to YARN Scheduler
- The Scheduler allocates a container that satisfies the requirements
- the Resource Manager launches the Application Master process there
- For MapReduce, the Application Master is <code>MRAppMaster</code> class - it creates some bookkeeping classes to monitor the progress
- Then it retrieves the input splits from HDFS
- and creates map tasks for each split and reducer tasks (set with <code>setNumReduceTasks()</code>)
- each task is assigned an ID


### Task Assignment
- the Application Master request containers for all map and reduce tasks from the Resource Manager
- first, the requests are made for the map tasks
- requests for reducers aren't made until at least 5% of all map tasks are finished


Request constraints that Resource Manager has to satisfy:
- Locality constraint. Optimal case when the task is ''data local'', or at least ''rack local''
- Memory and CPU requirements. By default, each task is allocated 1024 MB and 1 CPU 


These values are configurable on per-job basis:
- <code>mapreduce.map.memory.mb</code>
- <code>mapreduce.reduce.memry.mb</code>
- <code>mapreduce.map.cpu.vcores</code>
- <code>mapreduce.reduce.cpu.vcores</code>
- they are subject to min/max constraints specified in the YARN config ({{TODO| describe them as well}}) |

### Task Execution
- a task is assigned to a container on a particular node by the Resource Manager's Scheduler
- the Application Manager starts the container by contacting the node manager 
- the task is executed by a java class <code>YarnChild</code>
- before running, it get all needed files (e.g. config, job jars, etc) from the distributed cache
- finally, it runs the tasks: first, map tasks, then - reduce tasks
- <code>YarnChild</code> runs on a separate JVM so it doesn't affect anything else 


### Job Completion
- When the last Job task is complete, the Application Master changes its status to "SUCCESSFUL"
- then <code>job.waitForCompletion(true)</code> finishes and returns <code>true</code>
- if there was an error, it returns <code>false</code>

## Source
- [Hadoop: The Definitive Guide (book)](Hadoop__The_Definitive_Guide_(book))

[Category:Distributed Systems](Category_Distributed_Systems)
[Category:Hadoop](Category_Hadoop)
[Category:Resource Management](Category_Resource_Management)
[Category:Improve Images](Category_Improve_Images)