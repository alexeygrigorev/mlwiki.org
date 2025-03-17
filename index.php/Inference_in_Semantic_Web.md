---
title: Inference in Semantic Web
layout: default
permalink: /index.php/Inference_in_Semantic_Web
---

# Inference in Semantic Web

## Inferencing in [Semantic Web](Semantic_Web)
In [Semantic Web](Semantic_Web), using [RDFS](RDFS) and [OWL](OWL) many things can be inferred based on facts that are stored in the [RDF](RDF) triple store
- This is used for [Knowledge Discovery](Knowledge_Discovery) in Semantic Web
- All [RDF](RDF) statements or RDFS and OWL can be translated to [First Order Logic](First_Order_Logic) and [Descriptive Logic](Descriptive_Logic) to facilitate inferencing
  - see [Semantic Web Logics](Semantic_Web_Logics)


Inferencing - a systematic process of adding new tuples to an RDF graph based on some patterns (rules)
- ''asserted triples'' - RDF triples provided by some data source
- ''inferred triples'' - new triples added by inference rules
- ''inference rules'' - systematic patterns that define how and what to infer
- ''inference engine'' - engine that does the inference


### Motivating Example
Suppose you have a [SPARQL](SPARQL) query on your [RDF](RDF) graph 
- you look for <code>:RedDelicious</code> apples
- you are doing it in the <code>:Fruit</code> section 
- but the result is empty, because <code>:RedDelicious</code> is an <code>:Apple</code>, not a <code>:Fruit</code>
  - i.e. <code>:RedDelicious a :Apple</code>
  - and <code>:Apple :subClassOf :Fruit</code>

Possible solution:
- use [SPARQL#Transitive Queries](SPARQL#Transitive_Queries)

```scdoc
SELECT ?item 
WHERE {
  ?class :subClassOf* :Fruit . 
  ?item a ?class . 
}
```


But users will have to do it each time 
- alternatives? 
- can have rules if $X$ subclass of $Y$, then $\forall x \in X: x \in Y$
- ''inferencing'' - given some information we can determine related information - and consider that it's also stored in our database 
- so here we'd infer that if <code>:RedDelicious</code> is an <code>:Apple</code>, it's also a <code>:Fruit</code>
- <code>:Fruit</code> is broader than <code>:Apple</code>, so <code>:Fruit</code> is a subclass of <code>:Apple</code>


### Inferencing
The motivating example illustrates the ''type propagation rule''
- this is a part of the [RDFS](RDFS) language: <code>rdfs:subClassOf</code> relation
- rule: $X$ <code>rdfs:subClassOf</code> $Y \Rightarrow $ every member of $X$ is also a member of $Y$

Reference rules of [RDFS](RDFS)/[OWL](OWL) can be expressed using [SPARQL](SPARQL) Construct queries:
- this is a good way of describing rules

```carbon
CONSTRUCT { ?r rdf:type ?B } 
WHERE {
  ?A rdfs:subClassOf ?B 
  ?r rdf:type ?A
}
```


## Implementation Details
When the inference happens? 
- Cached Inference: 
  - inferred triples are stored along with asserted
  - risk an explosion of the triple store
  - also, change management is important - how to propagate changes and deletes
  - for deletes - same inferred tuple can be due to several facts, so need to be careful when deleting
- Just-In-Time Inference
  - To respond to queries only 
  - no inferred triples retained


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:Semantic Web](Category_Semantic_Web)