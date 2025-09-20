---
layout: default
permalink: /index.php/RDF
tags:
- data-models
- semantic-web
title: RDF
---
## Motivation
Data integration
- suppose we have a distributed database across many servers
- each row is some entity, a column represents some property of this entity, and the cell contains a value described by this property
- inside a cell we can refer to another entity, and the meaning of the relationship is described by the name of the column
- so each cell of this database can be seen as a triple <code>row column value</code>
  - row = resource/subject
  - column = predicate
  - value = object
- since the database is distributed, how to know if a resource on one server is the same resource from another?
  - describe resources with a global ID - URI (uniform resource identifier_
- this is the main idea of RDF


## RDF
RDF - resource description framework, a way to represent knowledge for the [Semantic Web](Semantic_Web)
- knowledge representation based on triples $\langle \text{subject}, \ \text{predicate}, \ \text{object} \rangle$
- the triples can form a graph
  - nodes - resources
  - edges - predicates
  - both represented with URIs

[Descriptive Logic](Descriptive_Logic)
- there's a strong link between RDF and logic
- a set of RED triples can be interpreted as a conjunction of positive literals


### Namespaces
one word can have several meaning
- e.g. Washington - state, city, person
- how to tell them apart?
- use namespaces

namespaces are typically URIs (like in [XML](XML))
- e.g. 
  - <code>http://www.example.com/states#Washington</code>
  - <code>http://www.example.com/cities#Washington</code>
  - <code>http://www.example.com/people#Washington</code>
- and as in XML, it's possible to use '''qnames''' - URI abbreviations for local use
  - qnames have 2 parts: namespace and id
  - <code>states</code> - <code>http://www.example.com/states#</code>
  - so use <code>states:Washington</code> to refer to Washington state
- default namespace in this case is empty
  - use <code>:Washington</code> for thins in the default namespace

Default namespaces in RDF
- <code>xsd:</code> for primitive XML types
- <code>rdf:</code> for default things in rdf
- <code>rdfs:</code> for [RDFS](RDFS)
- <code>owl:</code> for [OWL](OWL)



### Examples
#### Example 1
- suppose we have these statements
  - <code>doc.html</code> is written by Fabien
  - <code>doc.html</code> is about music 
- so we have these tripes
  - <code>doc.html isWrittenBy fabien</code>
  - <code>doc.html about music</code> 
- it can be represented by the following graph
  - <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-ex1.png" alt="Image">
  - every edge in this graph is an RDF triple


#### Example 2: Modeling with RDF
- suppose you need to make an RDF statement from the following sentence:
  - "a flower which is red and has a round shape"
- In RDF triples it can be
  - <code>flower color red</code>
  - <code>flower shape round</code>
- first, you need to find some definition of a flower
  - ideally it should be some resource you trust
  - e.g. http://botanie.example.org/type/fleur
- then you look for relations and their definitions
  - has color - http://concept.example.org/couleur
  - has shape - http://concept.example.org/forme
- finally, you find appropriate instances for colors and shape
  - http://colors.example.org/rouge - red
  - http://shapes.example.org/ronde - round
- so you have (shortened)
  - <code>:fleur :couleur :rouge</code>
  - <code>:fleur :forme :ronde</code>
- graphically, it's 
  - <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-ex2.png" alt="Image">


### Types and Properties
<code>rdf:type</code> predicate provides basic typing system
- e.g. <code>geo:Washington rdf:type geo:USState</code>


### Blank Nodes
RDF allows resources to have no id at all
- Sometimes we know that something exists
- And even know something about it 
- but don't know its identity

For example, 
- we know that Shakespeare had a mistress, but we don't know her
- and that she was the source of the inspiration for one of his works
- try to model as follows

```carbon
"unknown" rdf:type bio:Woman
"unknown" bio:livedIn geo:England
lit:Sonnet79 lit:hasInspiration "unknown"
```

We should interpret it as 
- there exists a woman who lived in England and is the source of inspiration for "Sonnet 79"
- so blank nodes interpreted as existential variables 

In Turtle it's 
- <code>lit:Sonnet78 lit:hasInspiration [a bio:Woman; bio:livedIn geo:England]</code>



## [Semantic Web](Semantic_Web)
RDF is a basis for the Semantic Web 
- [RDFS](RDFS) is schema for RDF that allows some basic inference
- [RDFS-Plus](RDFS-Plus) extension of RDFS, and subset of [OWL](OWL)
- [OWL](OWL) - Web Ontologies Language 

All of them use RDF to express the language constructs

### Querying
- [SPARQL](SPARQL) is used for querying RDF graphs


## RDF Serialization
Default is triplets - not very compact and user friendly
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdf-tripples.png" alt="Image">
- need different representation

There are several:
- [RDF/XML](RDF_XML)
- [Turtle](Turtle)


## See Also
- [Semantic Web](Semantic_Web)
- [RDFS](RDFS), [OWL](OWL)
- [Ontologies](Ontologies)

## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))
