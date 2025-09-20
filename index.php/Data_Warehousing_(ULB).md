---
layout: default
permalink: /index.php/Data_Warehousing_(ULB)
tags:
- data-warehousing
- it4bi
title: Data Warehousing (ULB)
---
## Info
- Course page: http://cs.ulb.ac.be/public/teaching/infoh419

## Syllabus
### Introduction
- OLTP vs OLAP
- Why a RDBMS is not suitable for Analytical Queries
  - Important conceptual notions
  - Data cube
  - Dimensions
  - Hierarchy
- Data Explosion Problem


Important database notions:
- ER Modelling
- Translation to the relational model
- Dependencies: Functional and foreign key dependencies

### Dimensional Modeling
- Dimensional Modeling
- Roll-up lattice

### Logical Modelling
- Special aggregation cases
- Additive and non-additive measures
- Star and snowflake schemas

- Logical design
- Dealing with changing dimensions
- Slowly Changing Dimensions
  - Type I, II, and II
  - Rapidly changing dimensions
  - Mini dimension
- Specific dimension types
  - Junk dimension
  - Outriggers
  - Degenerate dimension

### Physical level
- View materialization
- Indexing
  - Bitmap index, Projection index, Join index, Bitmap-join index
  - Indexing dimension and fact tables
- Partitioning


### ETL
- Data warehouse architectures
- ETL
