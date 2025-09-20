---
layout: default
permalink: /index.php/Entity-Relationship_Model
tags:
- databases
- relational-databases
title: Entity-Relationship Model
---
## Entity-Relationship Model
An entity–relationship model (ER model) is a [Data Model](Data_Model) for describing a [Database](Database) in an abstract way at a conceptual level. 

A database can be modeled as 
- a collection of entities plus
- the relationships between the entities 


### Definitions
''Entity'' is an object that exists and is distinguishable from other objects
- e.g. a company, an event, a person
- entities have attributes 

An ''entity set'' is a set of entities of the same type that share the same properties 
- set of all people, companies, events

A ''relationship'' is an association between several entities 
- for example "student" entity -- advisor (relationship) -- "instructor" entity

A relationship set is a set of relations between two specific entities 
- e.g. (studentId, instructorId) $\in$ advisor


An entity is represented by a set of ''attributes'' 
- an attribute is a descriptive property that all members of this entity set have 
- e.g. <code>instructor=(ID, name, street, city, salary)</code>
- <code>course=(ID, title, credits)</code>

''Domain'' is a set of permitted values for each attribute


Types of attributes:
- simple or composite 
- single-valued or multi-valued
- derived (computed from other values)
  - e.g. age given the date of birth
- composite attributes consist of other attributes (that also in turn may be composite)


; Keys
A ''super key'' of an entity set is a set of one or more attributes 
- these attributes must uniquely identity each entity

A ''candidate key'' of an entity set is a minimal possible super key
- e.g. id of an instructor
- although there could be several candidate keys, one must be selected to be a ''primary key'' 

''Relationships primary keys''
- The combination of primary keys for entities that participate in a relationship form a primary key for that relationship
- e.g. (s_id, i_id) is a superkey for advisor



## E-R Diagrams
### Basic Notation
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example1.png" alt="Image">
- rectangles represent entity sets 
  - attributes are listed inside
  - primary key attributes are underlined 
- diamonds represent relationship sets 
  - a relationship set may have attributes 

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example2.png" alt="Image">
- complex attributes are shown with indent 
- <code>{}</code> is used to show multivalued attributes 
- <code>()</code> shows that an attribute is derived


<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-3.png" alt="Image">
- directed line shows relationship with cardinality "one"
- undirected line - cardinality "many"
- alternatively, we can use cardinality limits 


<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-4.png" alt="Image">
- this is called "total participation"
  - indicated by a double line 
  - means: every entity set participates in at least one relationship
- opposite is "partial participation"
  - some entities may not participate in any relationship


### Weak Entity Sets
An entity set that does not have a primary key is a ''weak entity set''
- the existence of a weak entity set depends of ''identifying entity set''
- it must relate to the identifying entity set via a total one-to-many relationship set

''Discriminator (or partial key)'' of a weak entity set
- this is the set of attributes that distinguishes an entity among another entities 

So the primary key of such entities is formed by:
- the primary key of the strong entity (on which the weak one depends)
- the discriminator of the weak entity

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-5.png" alt="Image">
- discriminator is underlined with a dashed line
- identifying relationship is shown with a double diamond
- in this case the primary key for section is (<code>course_id, sec_id, semester, year</code>)

Note:
- the primary key of the strong entity set should not be stored explicitly with the weak entity set
- if <code>course_id</code> was stored in the weak entity, section then should be a strong entity
- a weak entity cannot exist without an owner [stackoverflow.com/questions/4741967]
  - example: a ROOM can only exist in a BUILDING
  - a TIRE, on the other hand, can be a strong entity because it can exist without a car 
  - QUESTION is strong - it always exists, but ANSWER is weak - there have to be a QUESTION for an ANSWER


Example:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-7.png" alt="Image">


## Reduction to [Relational](Relational_Databases) Schema
Entity sets and relationship sets can be expressed as relational schemas
- attributes of each schema typically correspond to attributes of entities and relationships 

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-6.png" alt="Image"> 

Translation
- strong entity becomes a schema with the same attributes
  - student(<u>ID</u>, name, tot_credit)
- weak entity becomes a table that includes a column for the PK pf the identifying entity set 
  - section(<u>course_id, sec_id, sem, year</u>)
- a many-2-many relationship set is represented as a schema with 
  - attributes for all the primary keys of all participating entities + 
  - descriptive attributes of the relationship set 
- many-2-one and one-2-many relationship sets can be represented by adding extra attribute to the "many" side
- instead of creating a schema for relationship set <code>inst_dept</code> we add an attribute <code>dept_name</code> to the schema for instructor
- for one-to-one relationship any side can be chosen to act as the "many" side
  - that is, an extra attribute is added to either side of the schema
- if participation is partial on the "many" side
  - extra attributes may point to <code>NULL</code> values



## Exercises
### Exercise 1
Car insurance company
- each customer has one or more cars 
- each car is associated with zero or more accidents 
- each insurance policy covers one or more cars and has one or more premium payments associated with a car 
- each payment is for particular period of time and has a due date and the date when payment is received


<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/er-example-8.png" alt="Image">



## Sources
- Database Systems Concept, slides for chapter 7 [http://codex.cs.yale.edu/avi/db-book/db6/slide-dir/index.html]: Most of the figures are taken from there
- [Data Warehousing (ULB)](Data_Warehousing_(ULB))
