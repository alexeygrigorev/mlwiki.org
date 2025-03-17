---
title: "RDFS-Plus"
layout: default
permalink: /index.php/RDFS-Plus
---

# RDFS-Plus

## RDFS-Plus
In [Semantic Web](Semantic_Web) [RDFS-Plus](RDFS-Plus) is an extension of [RDFS](RDFS), and a subset of [OWL](OWL)
- even though the namespace is [OWL](OWL), it's considered as a subset 
- [Inference](Inference_in_Semantic_Web) rules are shown with [SPARQL](SPARQL) CONSTRUCT queries
- for logical semantics behind there expressions see [Semantic Web Logic](Semantic_Web_Logic)
- DL-Lite something


## Basic Constructs
### <code>owl:inverseOf</code>: Inverse
Example
- suppose we have <code>:hasParent</code> - then the inverse is <code>:hasChild</code>
- the construction <code>owl:inverseOf</code> makes this relation explicit

In math, 
- inverse of $f$ is $f^{-1}$: 
- if $f(x) = y$, then $f^{-1}(y) = x$
- the same idea is in RDFS-Plus

```text only
CONSTRUCT { ?y ?q ?x }
WHERE {
  ?p owl:inverseOf ?q .
  ?x ?p ?y .
}
```


Example:
- <code>lit:Shakespeare lit:wrote lit:Macbeth </code>
- we know that <code>lit:wrote owl:inverseOf lit:writtenBy</code>
- so, can infer that <code>lit:Macbeth lit:writtenBy lit:Shakespeare</code>


### <code>owl:SymmetricProperty</code>: Symmetric Properties
- in real life, a relation "married" is both-way: 
  - if $A$ is married on $B$, then $B$ is married on $A$
- suppose we have this assertion: <code>bio:Anne bio:married lit:Shakespeare</code>
- consider this query
  - <code>SELECT ?who WHERE { ?lit:Shakespeare bio:married ?who }</code>
  - it returns no answer|    |- now state that married is both-way: it's inverse of itself |  - <code>bio:married owl:inverseOf bio:married</code>
  - now that query returns something 
- this is an example of a <code>owl:SymmetricProperty</code>
  - so instead of <code>owl:inverseOf</code> can say
  - <code>bio:married rdf:type owl:SymmetricType</code>

```text only
CONSTRUCT { ?p owl:inverseOf ?p. } 
WHERE { ?p a owl:SymmetricProperty . }
```


Also, can be useful to say that <code>owl:inverseOf</code> is symmetric
- <code>owl:inverseOf rdf:type owl:SymmetricProperty</code>
- now the following hold:
  - $:P_1$ <code>owl:inverseOf</code> $:P_2 \Rightarrow$
  - $:P_2$ <code>owl:inverseOf</code> $:P_1$


### <code>owl:TransitiveProperty</code>: Transitivity
In math:
- $R$ is transitive if
- $a \ R \ b \land b \ R \ c \Rightarrow a \ R \ c$

In RDFS-plus, <code>owl:TransitiveProperty</code> is used for that:
- <code>:P rdf:type owl:TransitiveProperty</code>

Meaning:
```text only
CONSTRUCT { ?x ?p ?z .} 
WHERE {
  ?x ?p ?y . 
  ?y ?p ?x . 
  ?p a owl:TransitiveProperty . 
}
```

Note that for longer chains like $a \to b \to ... \to q$ the rule also holds


### <code>owl:equivalentClass</code>: Equivalence
Identity
- URIs give the global notion of identity
- but what if we merging two different sources that have the same concept, but under different URIs? 
- i.e. we want to say that $:A \equiv :B$
- use [RDFS](RDFS):
  - <code>:A rdfs:subClassOf :B</code> $\land$ <code>:B rdfs:subClassOf :A</code>
- semantically same effect is achieved with <code>owl:equivalentClass</code>

```carbon
CONSTRUCT { ?r rdf:type ?b .} 
WHERE { 
  ?a owl:equivalentClass ?b . 
  ?r rdf:type ?a . 
}

CONSTRUCT { ?r rdf:type ?a .} 
WHERE { 
  ?a owl:equivalentClass ?b . 
  ?r rdf:type ?b . 
}
```

Note that we need to have 2 CONSTRUCT statements 
- because <code>owl:equivalentClass</code> is symmetric
- but instead of repeating twice can say that 
  - <code>owl:equivalentClass rdf:type owl:SymmetricProperty</code>
- can add the following and have no need to state anything
  - <code>owl:equivalentClass rdfs:subPropertyOf rdfs:subClassOf</code>


### <code>owl:sameAs</code>: Same Individuals
Suppose in 3 namespaces we have 3 different ways of describing a person
- how we can say that in all these 3 cases something/somebody is the same resource? 
- e.g. <code>pr:WilliamShakspere owl:sameAs lit:Shakespeare</code>

it's defined by 3 rules:
```text only
-- when it's a subject
CONSTRUCT { ?s ?p ?x. } 
WHERE {
  ?s ?p ?y.
  ?x owl:sameAs ?y .
}

-- when it's an object
CONSTRUCT { ?x ?p ?o. } 
WHERE {
  ?y ?p ?o .
  ?x owl:sameAs ?y .
}

-- when it's a predicate
CONSTRUCT {?s ?x ?o. } 
WHERE {
  ?s ?y ?o .
  ?x owl:sameAs ?y .
}
```

To avoid adding 3 more rules
- say that it's symmetric:
- <code>owl:sameAs rdf:type owl:SymmetricProperty</code>


## Sameness: Functional Properties
### <code>owl:FucntionalProperty</code>
Functional - of functions (in math)
- a property is functional if
- for some input value there could be only one output value

Examples (from RL):
- <code>hasMother</code> - can have only one biological mother
- <code>hasBirthplace</code> 
- <code>birthdate</code>

In RDFS-plus use <code>owl:FucntionalProperty</code> to describe that
- a property can give only one value for one particular entry
```carbon
CONSTRUCT { ?a owl:sameAs ?b . } 
WHERE {
  ?p rdf:type owl:FunctionalProperty .
  ?x ?p ?a . 
  ?x ?p ?b . 
}
```

Note the semantics
- if $x^2 = a \land x^2 = b \Rightarrow a = b$
- so if some resources participate in a functional property
- we conclude that these resources refer to the same entity (i.e. they are the same)


### <code>owl:InverseFunctionalProperty</code>
Inverse of <code>owl:FucntionalProperty</code>
- a single value of an inverse functional property cannot be shared by two entities 
- instead it infers that these two entities are the same
- and it doesn't signalize any errors|   |- examples: SSN, driver license,  etc - anything that can be an ID number |
```carbon
CONSTRUCT { ?a owl:sameAs ?b . } 
WHERE {
  ?p rdf:type owl:InverseFunctionalProperty .
  ?a ?p ?x . 
  ?b ?p ?x . 
}
```


### Examples
Student ID
- a student has an identity 
- this ID # belongs only to one person 
- so have this in the schema
  - <code>:hasIdentityNo rdfs:domain :Student .</code>
  - <code>:hasIdentityNo rdfs:range xsd:Integer .</code>
- now ensure the uniqueness 
  - <code>:hasIdentityNo rdf:type owl:FunctionalProperty .</code>
  - <code>:hasIdentityNo rdf:type owl:InverseFunctionalProperty .</code>

### Summary
Functional Only
- <code>hasMotheris</code> a functional property only. 
- Someone has exactly one mother, but many people can share the same mother.

Inverse Functional Only
- <code>hasDiary</code> is an inverse functional property only
- A person may have many diaries, but a diary is authored by one person only

Both Functional and Inverse Functional
- SSN, Student #, etc


## Other Constructs
### <code>owl:DatatypeProperty</code> and <code>owl:ObjectPropery</code>
In [RDF](RDF), subjects and objects are resource
- they can be either another resources or some data items 

Examples:
- <code>uni:studentId a owl:DatatypeProperty</code>
- <code>bio:married a owl:ObjectProperty</code>

### <code>owl:Class</code>
<code>owl:Class rdfs:subClassOf rdfs:Class . </code>


## See Also
- [RDFS and OWL Summary](RDFS_and_OWL_Summary)
- [Semantic Web](Semantic_Web)
- [RDFS](RDFS) and [OWL](OWL)
- [Inference in Semantic Web](Inference_in_Semantic_Web)
- [Semantic Web Logics](Semantic_Web_Logics)


## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
- [XML and Web Technologies (UFRT)](XML_and_Web_Technologies_(UFRT))

[Category:Semantic Web](Category_Semantic_Web)