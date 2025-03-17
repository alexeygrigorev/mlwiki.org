---
title: RDFS
layout: default
permalink: /index.php/RDFS
---

# RDFS

## RDFS
Is a schema language for [RDF](RDF)
- roughly, [RDF](RDF) is for defining graphs, RDFS - for defining sets 
- RDFS tells how to use the graph structure - gives some semantics to the used vocabulary
  - how items and their properties are related
- also provides some basic [inferencing capabilities](Inference_in_Semantic_Web) (for Knowledge Discovery)
  - [Inference](Inference_in_Semantic_Web) rules are nice to show with [SPARQL](SPARQL) CONSTRUCT queries
  - RDFS statements can be interpreted as [FOL](First_Order_Logic) statements 
  - for logical semantics behind there expressions see [Semantic Web Logic](Semantic_Web_Logic)
- RDFS is expressed using [RDF](RDF) triples 


RDFS "extends" RDF
- in the sense that it gives some meaning to the triples 



## Basic Constructs
### <code>rdfs:Class</code>
A set is identified in RDFS with <code>rdfs:Class</code>
- note the use of <code>rdfs:</code> namespace

```carbon
:AllStarPlayer rdf:type rdfs:Class. 
:MajorLeaguePlayer rdf:type rdfs:Class. 
:Surgeon rdf:type rdfs:Class. 
:Staff rdf:type rdfs:Class. 
:Physician rdf:type rdfs-subproperty:Class.
```


### <code>rdfs:subClassOf</code>
Suppose we have the following assertions
- <code>:Apple rdfs:subClassOf :Fruit</code>
- <code>:RedDelicions a :Apple</code>
- can infer that <code>:RedDelicions a :Fruit</code>

The inference rule is 
```carbon
CONSTRUCT { ?r rdf:type ?B } 
WHERE {
  ?A rdfs:subClassOf ?B .
  ?r rdf:type ?A
}
```


### <code>rdfs:subPropertyOf</code>
Example:
- relation "brother" is more specific than "sibling"
- if smb is my brother, he also is my sibling
- so <code>:brother rdfs:subPropertyOf :sibling</code>

The inference rule is 
```text only
CONSTRUCT { ?x ?r ?y } 
WHERE {
  ?x ?q ?y . 
  ?q rdfs:subPropertyOf ?r
}
```

Another example
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdfs-subproperty.png" alt="Image">


### <code>rdfs:domain</code> and <code>rdfs:range</code>
Typing data by usage (also - ''implicit'' typing)
- as opposed to the ''explicit'' typing <code>rdf:type</code>
- <code>rdfs:domain</code> - set of values for which a property is defined (subject)
- <code>rdfs:range</code> - set of values it can take (object)

Can define them as 
```carbon
CONSTRUCT {?y rdf:type ?D .} 
WHERE {
  ?P rdfs:range ?D . 
  ?x ?P ?y .
} 

CONSTRUCT {?x rdf:type ?D .} 
WHERE {
  ?P rdfs:domain ?D . 
  ?x ?P ?y .
}
```

'''NB''': 
- there's no notion of incorrect/inconsistent inference in RDFS
- it doesn't signalize an error if a property isn't used consistently with the declaration
- RDFS will [infer](Inference_in_Semantic_Web) the type to make this property consistent 
- this declaration is quite aggressive - even with one triple it can result in surprising inferences


### Example
Suppose we have the following schema
- <code>:MarriedWoman rdfs:subClassOf :Woman.</code>
- <code>:hasMaidenName rdfs:domain :MarriedWoman.</code>
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/rdfs-ex-dom.png" alt="Image">

And the following assertions: 
- <code>:Karen :hasMaidenName "Stephens".</code>

Inference:
- Even if we don't know that <code>:Karen</code> is a <code>:Woman</code>, we can infer that she's married
- infer that <code>:Karen rdf:type :MarriedWoman</code> based on <code>rdfs:domain</code>
- infer that <code>:Karen rdf:type :Woman</code> based on <code>rdfs:subClassOf</code>


## Modeling with RDFS
There are some basic modeling patterns that can be used in RDFS

### Intersection
$C \equiv A \cap B$
- <code>:C rdfs:subClassOf :A</code>
- <code>:C rdfs:subClassOf :B</code>
- need to be a subclass of both $A$ and $B$ to be in $C$


### Union
$C \equiv A \cup B$
- <code>:A rdfs:subClassOf :C</code>
- <code>:B rdfs:subClassOf :C</code>
- $x \in C$ when $x$ is a subclass of $A$, or subclass of $B$ (or both)


### Properties
Intersection and Union can also be used for properties, e.g.
- Intersection
  - <code>:R rdfs:subPropertyOf :P . </code>
  - <code>:R rdfs:subPropertyOf :Q .</code>
- Union
  - <code>:P rdfs:subPropertyOf :R . </code>
  - <code>:Q rdfs:subPropertyOf :R .</code>


### Example: ''Terminology reconciliation''
- A military plane needs to determine if it can attach something or not
- it has 2 sources of data
  - "never-target" list: schools, churches, hospitals
  - "off-limit airspace": no-fly zones
- a target is off-limit if it belongs to one of these classes 
  - solution: use union
  - <code>fc:Civilian rdfs:subClassOf cc:OffLimitTarget</code>
  - <code>space:NoFlyZone rdfs:subClassOf cc:OffLimitTarget</code>


### Example 2: Property union
- if <code>:A rdfs:label "something"</code>, then "something" is a printable name of <code>:A</code>
- it's more readable than URIs
- but suppose that in our data source we don't have it, but have something else with some textual information
  - <code>:person1 :personName "James Dean"</code>
  - <code>:movie1 :movieTitle "Giant"</code>
- we want to use these properties as labels
- solution: use property union:
  - <code>:personName rdfs:subPropertyOf rdfs:label</code>
  - <code>:movieTitle rdfs:subPropertyOf rdfs:label</code>


## Non-modeling Properties in RDFS
There are properties that aren't used for inference, but just for description
- <code>rdfs:label</code> - text representation
- <code>rdfs:seeAlso</code>  - cross referencing
- <code>rdfs:isDefinedBy</code> - primary source/description of a resource
- <code>rdfs:comment</code> - a comment


## See Also
- [RDFS and OWL summary](RDFS_and_OWL_summary)
- [Semantic Web](Semantic_Web)
- [Inference in Semantic Web](Inference_in_Semantic_Web)
- [RDFS-Plus](RDFS-Plus) - a subset of [OWL](OWL) and an extension of [RDFS](RDFS) with more inferencing capabilities
- [OWL](OWL) 
- [Semantic Web Logics](Semantic_Web_Logics)


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:Semantic Web](Category_Semantic_Web)