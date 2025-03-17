---
title: "Data Integration"
layout: default
permalink: /index.php/Data_Integration
---

# Data Integration

## Data Integration
Goal of Data Integration - provide uniform access to heterogeneous data sources in some domain. 


## Main approaches
### [Data Warehousing](Data_Warehousing)
- data from all data sources are federated into one main warehouse (using [ETL](ETL)s)
- the queries are issued to this federated storage
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/architecture-dwh.png" alt="Image">


### [Mediator](Mediator_(Data_Integration))
- data remains in the data sources 
- sometimes called "virtual data integration"
- better for the Web - there are many DBs, and we would like to find something, no matter what DB provides it
  - so it can be a preferred approach for [Ontology Based Data Access](OBDA)
- also better if you want to access "fresh" data
- but way harder to implement - need to transform data during the query time 
  - need to use [Ontologies](Ontologies) for that, no [ETL](ETL)s
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/architecture-mediator.png" alt="Image">


## See Also
- [Data Transformation](Data_Transformation)
- [ETL](ETL)
- [Data Warehousing](Data_Warehousing)

## Links
- http://en.wikipedia.org/wiki/Data_integration

## Source
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Data Integration](Category_Data_Integration)