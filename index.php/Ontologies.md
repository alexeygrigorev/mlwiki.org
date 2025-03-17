---
title: "Ontologies"
layout: default
permalink: /index.php/Ontologies
---

# Ontologies

## Ontologies
Ontologies are semantic models in [Semantic Web](Semantic_Web)
- an ontology is some knowledge about concepts of some domain and the relations between them
- or, an ontology is a formal description that provides a user some (shared) understanding about a domain


Ontologies for Semantic Web:
- should be understandable by machines
- should allow [reasoning](Inference_in_Semantic_Web)
- [RDFS](RDFS) + [OWL](OWL) for describing ontologies on top of RDF graphs
- Tbox in [Descriptive Logic](Descriptive_Logic) as the formal foundation for inferencing
- in [OWL](OWL) there's a special property: <code>SOME_URI a owl:Ontology</code>


Useful for 
- organizing data in distributed and flexible way
- enhancing [Information Retrieval](Information_Retrieval) by exploiting some additional information from ontologies
- [Data Integration](Data_Integration) via [Ontology Based Data Access](Ontology_Based_Data_Access)


Types:
- upper ontologies - general things in abstract manner
- domain ontologies 
- lightweight ontologies for web



## Popular Ontologies
### FOAF
FOAF - friend of a friend (uses [RDFS-Plus](RDFS-Plus))
- a format for describing people and their relationships
- also, about organizations

### SKOS
SKOS  (uses [RDFS-Plus](RDFS-Plus))
- Simple Knowledge Organization System
- e.g. controlled vocabularies, taxonomies, thesauri - defines relationships between terms
- in a distributed and linkable way

### Others
- GR: Good Relations - for business to make descriptions of their offers (uses [OWL](OWL))
- QUDT - Quantity/Units/Dimensions/Types - for aligning data coming from multiple source  (uses [OWL](OWL))



## See Also
- [First Order Logic](First_Order_Logic)
- [Descriptive Logic](Descriptive_Logic)
- [RDFS](RDFS), [RDFS-Plus](RDFS-Plus), [OWL](OWL)

## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))
- Web Data Management, Manolescu, Ioana, et al. [http://webdam.inria.fr/Jorge/]


[Category:Semantic Web](Category_Semantic_Web)
[Category:Knowledge Representation](Category_Knowledge_Representation)