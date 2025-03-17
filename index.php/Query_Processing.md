---
title: Query Processing
layout: default
permalink: /index.php/Query_Processing
---

# Query Processing

## Query Processing Pipeline
<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/dbsa/query-processing-outline.png" alt="Image">

Steps:
# [Translating SQL to Relational Algebra](Translating_SQL_to_Relational_Algebra)
# [Logical Query Plan Optimization](Logical_Query_Plan_Optimization)
#* finding cheaper equivalent expression:
#* translating to [Conjunctive Query](Conjunctive_Query) and simplifying it
#* applying some heuristics (pushing selections and projections, etc)
# [Physical Query Plan Optimization](Physical_Query_Plan_Optimization)
#* doing the cost-based assignment of [physical operators](Physical_Operators_(databases))
#* assigning each node of Logical [Query Plan](Query_Plan) a physical operator
#* for that need to know statistics from [Database System Catalog](Database_System_Catalog) 
# execution engine - for that important things are:
#* [Physical Data Organization (databases)](Physical_Data_Organization_(databases))
#* [Indexing (databases)](Indexing_(databases))


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))

[Category:Database Systems Architecture](Category_Database_Systems_Architecture)
[Category:Relational Databases](Category_Relational_Databases)