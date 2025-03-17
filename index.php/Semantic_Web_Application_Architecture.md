---
title: Semantic Web Application Architecture
layout: default
permalink: /index.php/Semantic_Web_Application_Architecture
---

# Semantic Web Application Architecture

## [Semantic Web](Semantic_Web) Application Architecture
How to use [Semantic Web](Semantic_Web) in your application?

Main tools:
- [RDF](RDF) parsers, serializers and converters 
- RDF Store (sometimes called ''Triple Store'')
- RDF Query Engine

### Parsers & Serializers
Parser
- RDF can be in [XML/RDF](XML_RDF) or [Turtle](Turtle) format
- Parser converts in into an [RDF](RDF) graph

Serializer
- does the opposite: from a graph it creates a serialized version of it


### RDF Converters
Sometimes the data source is not in RDF form
- e.g. relational databases, spreadsheets 
- but also can be microformats - special attributes in HTML tags  (business cards or events)
- or RDFa - same idea, embed RDF into HTML attributes
  - to have machine-processable HTML data


### RDF Store
This is a database
- tuned for storing and retrieving triples 
- also should have an ability to merge information from multiple data sources (unlike [Relational Databases](Relational_Databases))


### RDF Query Engine
Closely related to [#RDF Store](#RDF_Store)
- [SPARQL](SPARQL): runs structured queries on the store to retrieve data
- SPARQL is not only a query language, but also a protocol
- so a query engine can be a web service 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-app.png" alt="Image">



## Libraries
- Sesame [http://openrdf.org] - RDF Store and QE
- SimpleNLG [https://code.google.com/p/simplenlg/] - translates RDF statements into English
  - NLG - Natural Language Generation

## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- Web Data Management, Manolescu, Ioana, et al. [http://webdam.inria.fr/Jorge/]

[Category:Semantic Web](Category_Semantic_Web)