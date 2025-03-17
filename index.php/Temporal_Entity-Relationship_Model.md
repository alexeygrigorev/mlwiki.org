---
title: "Temporal Entity-Relationship Model"
layout: default
permalink: /index.php/Temporal_Entity-Relationship_Model
---

# Temporal Entity-Relationship Model

## Temporal Entity-Relationship Model
This is an extension of [ER-Diagrams](Entity-Relationship_Model) to [Temporal Databases](Temporal_Databases). 

Example:
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-ex1.png" alt="Image">
- temporality can be added to attributes, entities and relationships


## Translation to [Relational](Relational_Databases) Schema
### Entities and Lifecycles
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-entity.png" alt="Image">

If an entity is temporal, we create an additional table EntityLifecycle
- where we keep all changes 
- a lifecycle shows the state at some period of time of this entity

<code>Employee</code>
|   Name  |  BirthDate  |  Address  |  Salary  |  Projects  |  Peter  |  8/9/64  |  Rue de la Paix  |  5000  |  {MADS, HELIOS} |
<code>EmployeeLifecycle</code>
|   Name  |  FromDate  |  ToDate  |  Status  |  Peter  |  7/94  |  6/96  |  Active ||  Peter  |  7/96  |  6/97  |  Suspended ||  Peter  |  7/97  |  6/98  |  Active |

Note that there could be several type of lifecycle tables
- Continuous (not intermittent)
- Discontinuous (can be intermittent and after a while continued)
- <img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-continious.png" alt="Image">


### Temporal Attributes
Translating attributes
- If there's a clock then we keep the history of all changes to this attribute
- If not - the attribute is not temporal and we keep only the current version


<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-atr.png" alt="Image">
- Each temporal attribute is modeled with a separate table


<code>Employee</code>
|   Name  |  BirthDate  |  Peter  |  8/9/64 |
<code>EmployeeLifecycle</code>
|   Name  |  FromDate  |  ToDate  |  Peter  |  7/94  |  7/98 |
<code>EmployeeAddress</code>
|   Name  |  Address  |  FromTime  |  ToTime   |  Peter  |  Bd St Germain  |  1/85  |  12/87 ||  Peter  |  Bd St Michel  |  1/88  |  12/94 ||  Peter  |  Rue de la Paix  |  1/95  |  now |
<code>EmployeeSalary</code>
|   Name  |  Salary  |  FromTime  |  ToTime  |  Peter  |  4000  |  7/94  |  7/95 ||  Peter  |  5000  |  8/95  |  now |
<code>EmployeeProjects</code>
|   Name  |  Projects  |  FromTime  |  ToTime  |  Peter  |  {MADS}  |  7/94  |  8/95 ||  Peter  |  {MADS, HELIOS}  |  9/95  |  now |

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-atr2.png" alt="Image">
- there's a clock for the <code>manager</code> - so it's temporal
- when updating <code>manager</code> - adding an element to the manager history
- when updating <code>project.name</code> - just update the name 
- when updating the <code>project</code> - just update the name, but start a new history for manager


### Generalization
Temporality is inherited

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-inheritance1.png" alt="Image">
- Temporary and <code>Permanent</code> are implicitly temporal
- they inherit temporality from <code>Employee</code> but use the lifecycle of <code>Employee</code> (don't have their own)

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-inheritance2.png" alt="Image">
- but in this case <code>Student</code> and <code>Faculty</code> have their own lifecycles 


### Relationships
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/adb/td-er-temp-rel.png" alt="Image">
- note that the one-to-many relationship is temporal
- and it has a temporal attribute

<code>Employee</code>
|   Name  |  BirthDate  |  Address  |  John  |  3/7/55  |  Bd Haussman ||  Peter  |  8/10/64  |  Rue de la Paix |
<code>WorksOn</code>
|   Employee  |  Project  |  Hours   |  John  |  HELIOS  ||   |     |  30  |  x/x/x  |  x/x/x   |   |  John  |  MADS  ||   |     |  25  |  x/x/x  |  x/x/x   |      |  35  |  x/x/x  |  x/x/x   |   |  Peter  |  MADS  ||   |     |  25  |  x/x/x  |  x/x/x   |      |  35  |  x/x/x  |  x/x/x   |   
<code>Project</code>
|   Name  |  Manager  |  Budget  |  MADS  |  Christine  |  5000 ||  HELIOS  |  Yves  |  6000 |
- lifecycles for <code>Employee</code>, <code>WorksOn</code> and <code>Project</code> are not shown here
- if <code>WorksOn</code> wasn't temporal, it wouldn't have a lifecycle
- same for <code>Employee</code> and <code>Project</code>


## Sources
- [Advanced Databases (ULB)](Advanced_Databases_(ULB))

[Category:Relational Databases](Category_Relational_Databases)
[Category:Databases](Category_Databases)