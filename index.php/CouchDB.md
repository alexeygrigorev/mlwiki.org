---
title: "CouchDB"
layout: default
permalink: /index.php/CouchDB
---

# CouchDB

This is a part of the report made for [Advanced Databases (ULB)](Advanced_Databases_(ULB)) course
- The report is available [here](http://docs.google.com/document/d/1pCfUo8TmxZkl5eFtyZGa42T5HlJJRqOBnc0TFiQAIFM/pub)


## Couch DB
Key features
- HTTP-based [REST](REST) Api
- [Distributed](Distributed_Databases), scalable and fault-tolerant
- [Document-oriented storage](Document-Oriented_Databases): the data is self-contained 
  - i.e. it contains everything it needs - like real-world document
  - not a relational model (with rigid schemata and normal forms)
  - [Traditional (Relational) DBs](Relational_Databases) require you to model the data up-front 
Schema-free design (like in CouchDB) allows to aggregate data after some fact has happened


### Documents
A document is the central data structure in CouchDB, and it uses JSON to store documents

Each document has an id, which must be unique per database. Usually the best ids are UUIDs (Universal Unique ID - random string with extremely low collision probability [http://en.wikipedia.org/wiki/Universally_unique_identifier]), but generally it can be anything 

- A good example of a document is a file for a word processor or a user profile.
- This sort of data you want to denormalize as mush as possible 
- Usually you want to fetch in one request as mush data as it makes sense to display 
- If we need to join some records, we want to precompute as much as possible and store related data together so it's retrieved at the same time. For that there's notion of ''virtual documents'' for that 



### CouchDB Locally
How CouchDB works on a single machine 

<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/couchdb-scheme.png" alt="Image">

It consists of two components: 
- HTTP REST API
- CouchDB core


## HTTP REST API Overview
- CouchDB provides [REST](REST)ful HTTP Api to interact with it (To see what's REST consult [http://en.wikipedia.org/wiki/Representational_state_transfer])
- When it's installed with default settings, it can be accessed via http://localhost:5984/


To check if it's running, send a GET request to this address :
```text only
curl -X GET http://localhost:5984/
```
('''curl''' is an unix utility for sending HTTP requests [http://curl.haxx.se/])

The database replies with the following: (if you see that, everything works)
```json
{
  "couchdb": "Welcome",
  "uuid": "2af023889ce22a70de68547c956e273a",
  "version": "1.4.0",
  "vendor": {
    "version": "1.4.0",
    "name": "The Apache Software Foundation"
  }
}
```
(here and henceforth formatted for better readability)


To get the list of all available databases, use command "_all_dbs"
```scdoc
curl -X GET http://localhost:5984/_all_dbs
```

To create a new database, issue a '''PUT''' request to database you want to create 
```scdoc
curl -X PUT http://localhost:5984/new_database
```

When an operation is successful, it replies with
```json
{"ok":true}
```


Adding
- To add new document, we issue a PUT request to url/{database_name}/{document_id}
- since the schema is not rigid, we may put there everything we want, for example 
```json
curl -X PUT http://localhost:5984/new_database/super_toaster -d '{"title":"toaster","price":"10$"}'
```
```json
{"ok":true,"id":"super_toaster","rev":"1-8f71d392bd5139ba142eb87ea52096d7"}
```
it returns id of the newly added plus revision id

To retrieve this document use the same url 
```scdoc
curl -X GET http://localhost:5984/new_database/super_toaster
```
```json
{
  "_id": "super_toaster",
  "_rev": "1-8f71d392bd5139ba142eb87ea52096d7",
  "title": "toaster",
  "price": "10$"
}
```
Note that we don't have to specify the id in the document, CouchDB takes care of adding it itself

Mechanisms behind versioning and revisions will be discussed below.


### Generating a database
- You can easily generate a lot of json data with http://json-generator.appspot.com/
- It's easy to bulk post your data to CoachDB [https://couchdb.readthedocs.org/en/latest/api/database.html#post-db-bulk-docs]

We have prepared 80k+ lines of JSON code (1500 documents) with user data to be inserted to the database (available at http://goo.gl/jkcCim)

To create this database execute the following: 
```gdscript
1. create a database "users"
curl -X PUT http://localhost:5984/users/
1. download database data into "database.json"
wget http://goo.gl/jkcCim --no-check-certificate -O test-database.json
1. use bulk post to add your data to CouchDB
curl -X POST http://localhost:5984/users/_bulk_docs -H "Content-Type:application/json" -d @test-database.json
1. at this point, CouchDB will answer with a list of newly added ids
```


### Futon
You don't have to interact with CouchDB only via HTTP requests: there is a web application for managing the database through a web browser, called Futon, which comes along with CouchDB. To access it, open your browser and go to http://localhost:5984/_utils/

<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/futon.png" alt="Image">

With Futon you can create databases and explore existing ones

To see what's inside a document, just chick on it

There are two options: 
- to see formatted version of JSON 
- or raw JSON data


## Core
Main core components:
- [B-Tree](B-Tree)-based storage engine
- [MapReduce](MapReduce) for querying (MapReduce queries are called ''views'')


### Design Documents
A ''design document'' is a special type of documents that contain application code. 
- They also live inside the database, but they are highly structured.
- These documents are very similar to usual documents: they can be replicated, have id and revision id. 


Virtual Documents
- We typically want to fetch all the data we want to display in one request, so it makes sense to store related records together, and if there is a need for joining, we want to precompute this.
- For that there's a technique called "virtual documents" which uses views to collate data together


A design document starts with a special prefix "_design/".

A design document may contain:
- [MapReduce](MapReduce) queries: "views" field
- "show" and "list" functions to render responses in other formats rather than JSON: XML, HTML, whatever you want 


### Validation
Validation is a powerful tool to ensure that only document you need/want end up in your database 
- There is a function "validate_doc_update" in a design document 
- this function must not have any side-effects, and they are run in isolation 
- it also can block invalid updated from other CouchDB instances during replication 
- This function is executed each time a document is added or updated 
  - if it raises an exception, the update is canceled, otherwise - accepted 
- Validation is optional, if there's no such function, every update will get accepted 


A design document may contain only one validation function, but if you have several design documents, all the validation function will be executed on a write request. If at least one of them decides to reject, the update is rejected. 
- NB: order of execution is not defined, so you must not make any assumptions about it 


```scdoc
function(newDoc, savedDoc, ctx) {
  // some logic 
  if (/* validation */) {
    throw({unauthorized: 'some message'})
  }
}
```


### Types
Types are needed to ensure that documents have proper type - i.e. have all required fields 
- This is a common pattern: to assign document types to records 
- It's not the part of CouchDB and it's up to user to decide whether to include type fields or not 

Consider the following validation query

```carbon
function(newDoc, oldDoc, ctx) {
  if (newDoc.type == "post") {
    // validate post
  }
  if (newDoc.type == "comment") {
    // validate comment
  }
}
```



## Queries and MapReduce
For [Relational Databases](Relational_Databases) you can issue any query, and as long as you data is structured correctly, you'll be able to get an answer. 

However, documents aren't always as structured as relations in Relational Databases, and for that we need a different approach. For CouchDB this approach is [MapReduce](MapReduce).

A user has to provide two functions that will operate on all data:
- Map - apply to each document and emit zero or more key/value pairs
- Reduce - apply reduce function to the result of Map function grouped by key
- A combination of Map and Reduce functions is called a ''view'' 

These functions provide CouchDB with great flexibility: they can adapt to various document structures. 


### Views
So a view is a combination of map and reduce functions

Views:
- allows for parallel and incremental computation of views (described below)
- since MapReduce produces key-value pairs, the results are also stored in the B-Trees 
- View results are stored in a B-Tree (like documents), but in their own file 

View functions are stored inside "views" field of a design document
- Once you create a view, you query it to get results 


### Map
- Map is applied to each document and emits zero or more key/value pairs - ''view rows''
- A map function doesn't depend on any information outside of the document, which allows CouchDB views be generated incrementally and in parallel 
- Views are stored as rows that are sorted by key in a [B-Tree](B-Tree), which makes range retrievals efficient
- When writing a map function, your goal is to build an index that stores related data recodes under nearby keys.

Incremental Computation of Map Results 
- a map function runs through all records when you first query the view 
- a call to emit creates an entry in the view results where everything is sorted by the key
- indexes for each document can be computed independently and in parallel 
- if a document is changed, the map function is run only once to recompute the key and values for this single documents 
- if a document is deleted, corresponding entries are marked ''invalid'' - and they don't show up in the results 


### Reduce
Reduce is applied after map


### Querying Views
to query a view use the following url

```scdoc
curl -X GET HOST/db/_design/{design_document}/_views/{view_name}
```

but you also can pass a ''view parameter''

```scdoc
curl -X GET HOST/db/_design/{design_document}/_views/{view_name}?key="abcd"
```

where "abcd" is the key we used in "emit" call


### Examples
Retrieve all active users that are women with more than 3 friends

```tera term macro
function(doc) {
  if (doc.isActive && doc.gender == 'female' && doc.friends.length >= 3) {
    emit(null, doc);
  }
}
```


This gives us unsorted output (it is sorted by document id, which gives us an impression that the result is not ordered)

Since the results are sorted by keys emitted by a map function, we to order the result on the last name of a user, we pass their name as the first argument of emit function

```javascript
function(doc) {
  if (doc.isActive && doc.gender == 'female' && doc.friends.length >= 3) {
    var lastName = doc.name.split(" ")[1];
    emit(lastName, doc);
  }
}
```


Consider another view:
```javascript
function(doc) {
 if (doc.isActive && doc.gender == 'female' && doc.friends.length >= 3) {
   var lastName = doc.name.split(" ")[1];
   emit(lastName, {"name": doc.name, "email": doc.email});
 }
}
```

It outputs names and emails of all active female users with at least 3 friends and sorts the result by their last names.


Suppose we want to calculate what is the average balance for all active female users with at least 3 friends. Here is our view:

```javascript
function(doc) {
 if (doc.isActive && doc.gender == 'female' && doc.friends.length >= 3) {
   var sum = doc.balance.replace(',', '').slice(1);
   emit(null, parseInt(sum));
 }
}

function(keys, values) {
 return sum(values) / values.length;
}
```


The result is only one value. It is also possible to calculate the average value per group. Say, we want to see the average salary per first letter of user’s last name

```javascript
function(doc) {
 if (doc.isActive && doc.gender == 'female' && doc.friends.length >= 3) {
   var sum = doc.balance.replace(',', '').slice(1);
   var lastName = doc.name.split(" ")[1];
   var firstLetter = lastName[0];
   emit(firstLetter , parseInt(sum));
 }
}

function(keys, values) {
 return sum(values) / values.length;
}
```


## Replication
A replication is a mechanism that allows to synchronize two or more database instances.

Reasons for doing replication:
- reliability 
- scaling
- load balancing


### [Eventual Consistency](Eventual_Consistency)
- [Distributed systems](Distributed_Databases) operate over some network, 
- and networks are often segmented (see Partition Tolerance in the [CAP Theorem](CAP_Theorem)). 
- Eventual consistency means that data will be consistent eventually, but the database is always available


### Incremental Replication
Data is kept locally
- no need for constant network access for communicating with other CouchDB instances
- synchronization happens whenever possible (when a network connection appears, etc)

Replication in CouchDB works incrementally
- only differences are replicated, not whole databases
- if something during the replication goes wrong,
- when this is fixed, next time it starts from the same moment 


Note that replication is unidirectional (from source to target)
If you want bidirectional replication, run it twice, swapping the source and the target for the second run.


Incremental Replication
- CouchDB achieves eventual consistency by Incremental Replication - this is the process when all document changes are copied periodically.
- This is called "Shared Nothing" cluster of databases with each node being independent and self-sufficient: these is no single point of connection in the system.
- Changes can be propagated in any way we like, and after replication each server can continue working independently 


This is how it works 
: <img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/couchdb-changes-propagation.png" alt="Image">
: (figure source [http://guide.couchdb.org/draft/consistency.html#figure/4])

To scale the system we just add another server


Schematically we may show replication like that:

<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/couchdb-replication.png" alt="Image">

When the replication process is run
- first, it runs the comparison between the two servers, which returns a list of changed documents
- : this includes:
  - new documents
  - changed documents
  - deleted documents
: documents that exist both on source and on target are not transfered (only differences will be moved)


Databases in CouchDB have a ''sequence number''
- it gets incremented when any change occurs 
- it remembers what change was associated with a particular sequence number

So calculating difference between source and target is efficient

If replication process is interrupted, the target database may be left in an inconsistent state.
But if you trigger the replication again, it will continue from the moment of interruption 


### Replication API
To synchronize two databases we issue a simple PUT request where we specify
- the source of the updates 
- the target 

CouchDB will figure out what are the new documents and what are the new revisions that are no the source but not yet on the targer, and will transfer it to the target 
```json
curl -X PUT http://localhost:5984/_replicate -d '{"source":"users","target":"users_replica"}'
```
The database replies with some statistics and tells if it was successful or not 

'''NB''': the request for replication will stay open till the replication process finishes, so it may take a while 


## Concurrency
In a typical relational database when we modify a table, we put a lock - and all other clients that want to access the table are queued

This sequential execution of tasks wastes a lot of processor's power and time: under high load it may spend a lot of time trying to figure out whose turn is next

MVCC, [Multi-Version Concurrency Control](Multi-Version_Concurrency_Control), is used to manage concurrent access to the data in CouchDB 

<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/couchdb-concurrency.png" alt="Image">

(figure source: [http://guide.couchdb.org/draft/consistency.html#figure/3])

This concurrency model allows CouchDB to run effectively even under high load, without worrying about queuing requests. 


### [B-Tree](B-Tree) storage engine
B-Tree (CouchDB uses a variation of a B-Tree [[http://www.scholarpedia.org/article/B-tree_and_UB-tree](http://en.wikipedia.org/wiki/B-tree]) called B+Tree [http://en.wikipedia.org/wiki/B%2B_tree])
- ''B-Tree'' is a sorted data structure that allows for searching, insertions and deletion in logarithmic time 
- Lookup is $O(\log N)$ time, and range is $O(\log N + K)$


This data structure is used everywhere, also for internal data: documents and views
- Usage of this data structure imposes an important restriction: can access only by key. 
- Reason: to be make huge performance gains 

In CouchDB the implementation is a little bit different from original B+Trees. It adds:
- Support for MVCC 
  - reads and writes without locking the system 
  - writes do not block reads 
  - this is because of append-only design 
- append-only design 
  - old versions are not deleted
  - every time something is updated, a new node is created, and a new root as well
    - but old reads still have references to the old root,
    - so they are able to continue reading without being interrupted, 
    - i.e. have old consistent state 
  - data never lost and never corrupted


## Conflicts Management
### Versioning
All documents have versions (like in version control systems such as SVN)

If you want to change a document, you create a new one and save it over the old one. After doing that there will be two versions of the same document. Since a new version is just appended to the database, the read requests don't have to be suspended. 

Once a new version is appended, all new requests are routed to this newer version


Updates in CoachDB
- load object
- change something
- save as a new revision


each revision is identified with a new "_rev" value

if you want to update or delete a document, you must specify the revision you're updating. This is to ensure that you will not overwrite some other update 

suppose you want to update a document without providing the revision id: 

```json
curl -X PUT http://localhost:5984/new_database/super_toaster -d '{"title":"toaster","price":"15$"}'
```

CouchDB responses with an error:

```json
{"error":"conflict","reason":"Document update conflict."}
```

So we add the revision id to the document we're updating: 

```json
curl -X PUT http://localhost:5984/new_database/super_toaster -d '{"title":"toaster","price":"15$","_rev":"1-8f71d392bd5139ba142eb87ea52096d7"}'
```

This time the database replies with "ok" and a new revision update:
```json
{"ok":true,"id":"super_toaster","rev":"2-9c85d3c3324c3777a4665f00330b73b5"}
```


### Conflicts
A ''conflicting'' change is a change that occurs simultaneously in two or more replicas. This happens regularly in [Distributes Databases](Distributes_Databases).

So a ''document conflict'' means that now there are two latest revisions of the same document.


CouchDB can detect a conflicting change in a document and signals it with "_conflict" flag set to true.

When there are two revisions of the same file, CouchDB has to choose one ''winning'' revision - revision that will be stored and the latest revision. However the ''loosing'' revisions aren't deleted - they are stored as well, but as previous revisions. 


CouchDB doesn't attempt to reconcile the conflicting changes: it ensures that all conflicts are detected, but it's up to the application to deal with them. Essentially this is the same mechanism used by SVN [http://en.wikipedia.org/wiki/Apache_Subversion] and other popular version control systems. 


### Conflict Resolution
Replication from $A$ to $B$ (assuming triggered replication, not continuous)
Direction $A \to B$ (not $B \to A$)

All other types of replication are reduced to these steps

1. $A$: create document $d_1$
1. trigger replication $A \to B$
1. now $B$ also has $d_1$
1. change $d_1$ on $B$ (CouchDB generates a new revision id)
1. change $d_1$ on $A$ (CouchDB also generates a new different revision id)
1. trigger replication $A \to B$
1. CouchDB detects a conflict (two conflicting revisions of the same document)
1. Application resolves the conflict:
  - it tells CouchDB which revision to keep 
  - another way: we merge two revisions, update the document and CouchDB will generate a hew revision and mark the conflict resolved

To see if we have any conflicts we may use this simple view: 

```scdoc
function(doc) {
  if (doc._conflicts) {
    emit(doc._conflicts, null)
  }
}
```

"_conflict" is an array that contains all conflicting revisions


### Choosing Winning Revision
CouchDB uses a deterministic algorithm to ensure that each CouchDB instance will come up with the same winning and loosing revision. 

Note that your application should never depend on these details and should treat the results as an  arbitrary choice rather than some deterministic algorithm. 

Algorithm
- Each revision has a revision history: a list with all previous revision IDs. 
- A version with longest revision history wins
- If the length is the same, "_rev" values are compared in ASCII sort order
: for example, "2-de..." wins over "2-7e..."

If we don't agree with CouchDB automatic choice, we delete one revision and keep another 

```scdoc
curt -X DELETE $HOST/database/document_id?rev=2-de...
```

This returns a new revision (remember that a delete is also an update)

Next, we put the values we want to keep back to the database, specifying the revision we like

```json
curl -X PUT $HOST/database/document_id -d '{..., "_rev":"2-7e..."}'
```

It also responses with a new revision ID. 

This way we resolve the conflict 

Now we need to replicate $B \to A$, so both instances are synchronized. 


### Revision ID
Let's have a look at a typical revision ID:

3-dad88c6c6a0df7f0e09e1e2d0d145eeb
- 3 - an integer, the current version number, it gets incremented with each update
- dad88c6c6a0df7f0e09e1e2d0d145eeb - md5 hash over a set of properties: JSON body, attachments, "_delete" flag


It means that:
- updates on the same document on different instances create their own independent revision IDs. 
- for two different documents with same data the right part of the revision ID will be the same:

```json
$ curl -X PUT $HOST/db/a -d '{"a":1}'
{"ok":true,"id":"a","rev":"1-23202479633c2b380f79507a776743d5"}
$ curl -X PUT $HOST/db/b -d '{"a":1}'
{"ok":true,"id":"b","rev":"1-23202479633c2b380f79507a776743d5"}
```


### Revision Tree
<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/revisions-list1.png" alt="Image">

When there is a conflict, the history branches into a tree
- each branch can extent its own history independently 
- the last documents in the tree (i.e. leaves) are the set of conflicting revisions
  - in this case these are $r_{4a}, r_{3b}, r_{2c}$

The way to resolve conflict: 
- combine all the conflicting revisions ($r_{4a}, r_{3b}, r_{2c}$) into a single document 
- replace one of them, say $r_{4a}$ with the new document. That will give us a new revision $r_{5a}$ 
- delete all the remaining of leaves: $r_{3b}, r_{2c}$
 
<img src="https://github.com/alexeygrigorev/ulb-adb-project-couchbd/raw/master/report/images/revisions-list2.png" alt="Image">

- Note that when we delete a record, another revision is added to the revision tree, and the deleted record still exists, but as "deleted" node. 
- It will be still possible to retrieve this record, but it will be marked with "_deleted" flag set to true
- Also afterwards during compaction data from non-leaf nodes will be removed
  - leaving only a chunk of metadata called ''tombstone'' plus 
  - the list of historical "_revs" is still retained in case in future you meet old database replicas 
- There also is a mechanism for "pruning" the revision tree to prevent it from growing too large 


## Misc
### Compaction
Compaction is a mechanism used to reduce disk space usage 
- by removing unused and old data from database or view index files

During the compaction of a database CouchDB 
- creates a new file with ".compact" extension and transfers only actual data into it
- when the data successfully transferred, the ".compact" file replaces the actual database file 

Old revisions are replaced with a ''tombstone'' - a small piece of metadata that will be used for conflict resolution 

To cause the compaction manually, run 

```scdoc
curl -X POST HOST/{database}/_compact
```





## Sources
- [CouchDB The Definitive Guide by Anderson, Lehnardt and Slater](http://guide.couchdb.org/draft)
- [CouchDB documentation: Replication and Conflict Model](http://docs.couchdb.org/en/latest/replication/conflicts.html)

[Category:NoSQL](Category_NoSQL)
[Category:Distributed Systems](Category_Distributed_Systems)
[Category:Databases](Category_Databases)