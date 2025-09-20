---
layout: default
permalink: /index.php/RDFS_and_OWL_Summary
tags:
- semantic-web
title: RDFS and OWL Summary
---
Summary from [RDFS](RDFS), [RDFS-Plus](RDFS-Plus) and [OWL](OWL)


## [RDFS](RDFS)
### Fundamental concepts
- <code>rdfs:subClassOf</code> - Members of subclass are also member of superclass.
- <code>rdfs:subPropertyOf</code> - Relations described by subproperty also hold for superproperty.
- <code>rdfs:domain</code> - The subject of a triple is classified into the domain of the predicate.
- <code>rdfs:range</code> - The object of a triple is classified into the range of the predicate.


### Annotation properties
- <code>rdfs:label</code> - No inferential semantics, printable name.
- <code>rdfs:comment</code> - No inferential semantics, information for readers of the model.


## [OWL](OWL)
### Equality
- <code>owl:equivalentClass</code> - Members of each class are also members of the other.
- <code>owl:equivalentProperty</code> - Relations that hold for each property also hold for the other.
- <code>owl:sameAs</code> - All statements about one instance hold for the other.


### Property characteristics
- <code>owl:inverseOf</code> - Exchange subject and object.
- <code>owl:TransitiveProperty</code> - Chains of relationships collapse into a single relationship.
- <code>owl:SymmetricProperty</code> - A property that is its own inverse.
- <code>owl:FunctionalProperty</code> - Only one value allowed (as object).
- <code>owl:InverseFunctionalProperty</code> - Only one value allowed (as subject).
- <code>owl:ObjectProperty</code> - Property can have resource as object.
- <code>owl:DatatypeProperty</code> - Property can have data value as object


### Restrictions
- <code>owl:Restriction</code> - describes classes by restricting the values allowed for certain properties.
- <code>owl:hasValue</code> - refers to a single value for a property.
- <code>owl:someValuesFrom</code> - refers to a set from which some value for a property must come.
- <code>owl:allValuesFrom</code> - refers to a set from which all values for a property must come.
- <code>owl:onProperty</code> - A link from a restriction to the property it restricts.


### Restrictions - set operations
- Each of these is used to create a new class, based on the specified set
- <code>owl:unionOf</code>, <code>owl:intersectionOf</code>,  <code>owl:complementOf</code>
- <code>owl:oneOf</code> - Specifies that a class consists just of the listed members.
- <code>owl:differentFrom</code> - Specifies that one individual is not <code>owl:sameAs</code> another. 
  - This is particularly useful when making counting arguments.
- <code>owl:disjointWith</code> Specifies that two classes cannot share a member. 
  - This is often used as a sort of wholesale version of <code>owl:differentFrom</code>.
- <code>owl:cardinality</code>, <code>owl:minCardinality</code>, <code>owl:maxCardinality</code> 
  - specifies information about the number of distinct values for some property. 


## See Also
- [RDFS](RDFS), [RDFS-Plus](RDFS-Plus), [OWL](OWL)
- [Semantic Web](Semantic_Web)
- [Inference in Semantic Web](Inference_in_Semantic_Web)



## Sources
- [Semantic Web for the Working Ontologist (book)](Semantic_Web_for_the_Working_Ontologist_(book))
