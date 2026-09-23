---
layout: default
permalink: /Temporal_Databases
tags:
- databases
title: Temporal Databases
---
## Temporal Databases
There are many applications that need temporal aspects in many domains. 

Usually they are used for:
- versioning
- specifying some periods of time
- etc


### Time and Facts
Valid time of a fact:
- when the fact is (was, will be) true in the modeled reality
- independent of the transaction time 
- can be past, present, future
- (link to Slowly Changing Dimensions)?

Transaction time of a fact:
- when the fact was recorded in a [database](Database)



### Temporal ER Diagrams
Conceptual Modeling of Temporal aspects: 
- [Temporal Entity-Relationship Model](Temporal_Entity-Relationship_Model)


### Querying
How to query a temporal database?
- [Sequenced Queries](Sequenced_Queries)


## Sources
- [Advanced Databases (ULB)](Advanced_Databases_%28ULB%29)
