---
layout: default
permalink: /index.php/OLAP
tags:
- data-warehousing
- databases
title: OLAP
---
## OLAP

OLAP (Online Analytical Processing) is an approach to data analysis where data is explored with multidimensional analytical queries. It is the typical workload of a [Data Warehouse](Data_Warehouse), in contrast to OLTP systems, which handle many short transactional operations.

## Data Cubes

The central OLAP concept is the [data cube](Multi-Dimensional_Indexes) — a multidimensional array of values:

- **dimensions** are the perspectives of analysis, e.g. time, geography, product
- **measures** are the numeric facts being aggregated, e.g. sales amount, number of transactions
- each cell of the cube holds an aggregation of measures over a combination of dimension values

## OLAP Operations

- **roll-up** — aggregate data by climbing up a dimension hierarchy, e.g. from cities to countries
- **drill-down** — the opposite of roll-up: get more detailed data, e.g. from quarters to months
- **slice** — fix one dimension and take a sub-cube, e.g. data for one year only
- **dice** — select a sub-cube by constraining several dimensions
- **pivot** — rotate the cube to look at it from another perspective

Data transformation steps like these are part of typical analytical workflows — see [Data Transformation](Data_Transformation).

## OLAP vs OLTP

| | OLAP | OLTP |
|--|--|--|
| purpose | analytics, decision support | transaction processing |
| queries | complex, read-mostly, aggregations | short, read/write |
| data | historical, aggregated, denormalized | current, detailed, normalized |
| typical systems | data warehouses, column stores | relational databases |

## Implementation Approaches

- **MOLAP** — multidimensional storage: data is stored directly in cubes
- **ROLAP** — relational storage: cubes are emulated on top of a relational schema
- **HOLAP** — hybrid: summary data in MOLAP, detailed data in relational tables

Column-oriented databases (see [Column-Oriented Databases](Column-Oriented_Databases)) and some [NoSQL](NoSQL) systems are especially good for analytical queries like these.

Note that [OLAP is not a good fit for MapReduce](Hadoop_MapReduce): map-reduce frameworks work well for batch processing, while OLAP expects interactive response times.

## See Also

- [Data Warehouse](Data_Warehouse)
- [Data Warehousing](Data_Warehousing)
- [Multi-Dimensional Indexes](Multi-Dimensional_Indexes)
