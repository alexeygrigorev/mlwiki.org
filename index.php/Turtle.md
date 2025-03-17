---
title: "Turtle"
layout: default
permalink: /index.php/Turtle
---

# Turtle

## Turtle
- a way of representing [RDF](RDF) 
- more compact than [RDF/XML](RDF_XML)
- used in [SPARQL](SPARQL)


### Syntax
uses qnames - binds them to global URIs
```turtle
@prefix mfg: <http://www.example.com/manufacturing#>
@prefix rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
```


triples are expressed in the following way, with dot separating triples
- <code>mfg:Product1 rdf:type mfg:Product .</code>


<code>a</code> is a shortcut for <code>rdf:type</code>
- so it can read in more natural English 
- Product1 is a Product
- <code>mfg:Product1 a mfg:Product .</code>


When we describe the same subject, can use ";":
- <code>mfg:Product1 rdf:type mfg:Product; mfg:productId "..." .</code>


When we have same subject and same predicate, just use spaces
- <code>lit:Shakespeare b:hasChild b:Susanne b:Judith b:Hamlet .</code>


Blank nodes:
- <code>[a bio:Woman; bio:livedIn geo:England]</code>
- can be used as a subject:
- <code>lit:Sonnet78 lit:hasInspiration [a bio:Woman; bio:livedIn geo:England]</code>


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:Semantic Web](Category_Semantic_Web)