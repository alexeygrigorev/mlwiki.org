---
title: "Document-Oriented Databases"
layout: default
permalink: /index.php/Document-Oriented_Databases
---

# Document-Oriented Databases

## Document-Oriented Databases
A document-oriented database is a database designed for storing document-oriented information. Instead of records, as in traditional [Relational Databases](Relational_Databases), these databases use structured and semi-structured documents. It may be XML, JSON or any other structured format. 


### Documents
The central abstraction of these databases is documents.

A ''document'' is 
- a self-contained record: it contains everything it needs (thus, no or little need for joining with other documents)
- a semi-structured record: it is a set of values, each of which may be complex (i.e. hold other values)
- a record with no imposed structure, other then the structure of the format (XML, JSON, etc) that is used to represent the record

Documents inside such databases are not rigid: there are usually no requirements to adhere to any schema, and records are not required to have same files. 

Categorizing
- there are ways to organize records into categories (like relations in [Relational Databases](Relational_Databases))
- typical way: add ''tags'' to mark the category of a record. A tag is usually just another field that specifies the type of a record
- databases usually don't provide tools for categorizing, and it's up to users to decide whether to use tags or not



## Document-Oriented Databases
### MongoDB
- JSON (BSON) for storing documents
- [Eventual Consistency](Eventual_Consistency)

### [CouchDB](CouchDB)
- JSON for storing documents
- [Eventual Consistency](Eventual_Consistency)
- [REST](REST) Api

### OrientDB
- 

### XML Databases
Most XML databases are Document-Oriented 


## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- [Document-oriented database (wikipedia)](http://en.wikipedia.org/wiki/Document-oriented_database)

## See also
- [NoSQL](NoSQL)


[Category:Distributed Systems](Category_Distributed_Systems)
[Category:NoSQL](Category_NoSQL)
[Category:Databases](Category_Databases)