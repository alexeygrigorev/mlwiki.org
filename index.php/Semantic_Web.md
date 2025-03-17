---
title: "Semantic Web"
layout: default
permalink: /index.php/Semantic_Web
---

# Semantic Web

## Semantic Web
Semantic Web is a web that is used to represent knowledge
- Semantic Webs - part of Knowledge Representation, AI
- principles: be able to describe things in document in machine-processable way
- [RDF](RDF) is the main tool for representing knowledge in Semantic Web

What we currently have in WWW:
- mostly have links of the form $a \ \text{href} \ b$
- what we want: $A \ \text{dependsOn} \ a$, $a \ \text{isDescribedBy} \ b$, etc -
  - i.e. we want links to have some meaning behind
  - so we can use semantic web and [Ontologies](Ontologies) for that


### DIKW
DIKW [http://en.wikipedia.org/wiki/DIKW_Pyramid]: data $\to$ information $\to$ knowledge $\to$ wisdom $\Rightarrow$ decision 
- D - just collecting data, smb enters data into a web app - just values
- I - databases (RDBs, XML, etc) - now you have some structure
  - but also know when it was collected, by whom, etc - i.e. with some metadata
- K - reports, analysis - to facilitate decision making
- W - to increase effectiveness 
- see also [http://semanticabyss.blogspot.fr/2009/03/dikw-hierarchy-data-information.html]

<img src="http://upload.wikimedia.org/wikipedia/en/9/93/DIKW.png" alt="Image">


## Smart Web of Linked Data
So the goal is to have machine-readable linked data. We want to have "Smart Web" - linked and consistent.
- fundamental issue of the web: how to manage distributed data 


=== Motivation: Integration === 
Data integration and distribution
- suppose that two servers share the same tables
- but tables have different schemas 
- how do we know that one columns in first db corresponds to another one in second?
- so we need some coordination between the servers, like global reference
- so represent each cell of these tables with 3 values
  - global reference for row
  - global reference for column
  - global reference for the value in the cell 
- such cells can be stored on any of these servers 
- this is the basic idea of [RDF](RDF)
- and global references are URIs


Smart Managing of Data
- rows are "things" (or entities or individuals)
- columns specify properties of these things
- if a cell references some other "thing", the meaning of this relation can be understood from the name of the column
- can express this in a more meaningful form - with reference where this meaning is described
- so the "things" are resources that can relate to other resources
- to describe these things and relations, use URIs 


### Linked Data
Linked Open Data: a giant graph 
- all these sources provide RDF data
- every circle - a source of data, the bigger - the more articles it has 
- the bigger the arrow - the more links from one source to another
- <img src="http://lod-cloud.net/versions/2011-09-19/lod-cloud_colored_300px.png" alt="Image">
- http://dbpedia.org - the main hub in LOD
  - gets data from wikipedia:
  - http://en.wikipedia.org/wiki/Birmingham $\to$  http://dbpedia.org/resource/Birmingham


Other Sources:
- Freebase, UMBEL, YAGO2, OpenCyc
- Geography: Geonames, LinkedGeoData; EuroStat, World Factbook, US Census, Ordnance
Survey
- Media: BBC (/programmes, /music), WildlifeFinder, New York Times, Thomson Reuters: Open Calais (Named Entities extracted from text)
- Social Media: Open Graph Protocol (Facebook), Internet Movie Database
- Libraries American Lib. of Congress, GermanNational Lib. of Economics, LIBRIS, SwedishNat. Union Catalogue, OpenLibrary
- Scholarly articles (journal, conferences): DBLP, ACM, RKBexplorer, SemanticWeb, DogfoodServer
- Many others - see http://linkeddata.org and http://lod-cloud.net/


#### Linked data principles
These principles are recommendation - best practices 
- use URIs to talk about things 
- HTTP URIs are better so people can access them 
- when somebody uses this URI, make use of standards ([RDF](RDF), [SPARQL](SPARQL)) to describe things
- include links to other resources 

Links
- relationship links - point to related links (inside/outside)
- identity links - point to other resources that describe the same concept (in OWL: owl:sameAs)
- vocabulary links - definition of used terms 


### Main Assumptions
#### AAA Slogan
Main slogan for the web and the semantic web:
- AAA - Anyone can say Anything about Any topic 
- consequence: there always can be something else that somebody can say 

#### Open World Assumption
Open World assumption
- a consequence of the AAA slogan
- at any time some new information can appear


## Semantic Modeling
How to model data in such a way so it's good for the web scale 
- need to explain things in understandable way
- and then be able to reuse it 
- need to be formal so machines can understand it, and '''logical inference''' is possible
- Result of modeling: [Ontologies](Ontologies)


Semantic Web provides a number of modeling languages with different degree of expressivity:
- [RDF](RDF) - resource definition framework
  - the basic mechanism to make basic statements about anything
- [RDFS](RDFS) - schema for RDF, expresses classes, subclasses and properties
- [RDFS-Plus](RDFS-Plus) - a subset of OWL, more expressive than RDFS, less complex than OWL
- [OWL](OWL) - logics of Semantic Web, models detailed constraints between classes, properties and entities

Formal foundation for RDFS and OWL:
- [First Order Logic](First_Order_Logic)
- [Description Logic](Description_Logic)


### Logical Inference
{{ main |  Inference in Semantic Web }} |
[RDFS](RDFS) and [OWL](OWL) allow new tuples to be created from facts asserted in the database


## [Semantic Web/Application Architecture](Semantic_Web_Application_Architecture)
How to use the SW in your applications?
- tools, storage, parsers/serializers, etc


## Links
- [Data Semantics: Data Integration and the Semantic Web](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.6980&rep=rep1&type=pdf)
- http://www.cambridgesemantics.com/semantic-university/what-makes-a-good-semantic-web-application
- [Scalable Distributed Reasoning using MapReduce](http://www.few.vu.nl/~jui200/papers/ISWC09-Urbani.pdf)
- [Distributed Reasoning](http://www.cs.cf.ac.uk/Dave/AI2/node102.html)


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:Semantic Web](Category_Semantic_Web)