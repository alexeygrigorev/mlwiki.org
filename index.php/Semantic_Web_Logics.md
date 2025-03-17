---
title: Semantic Web Logics
layout: default
permalink: /index.php/Semantic_Web_Logics
---

# Semantic Web Logics

## Semantic Web Logics
In [Semantic Web](Semantic_Web), there are formal models behind [reasoning](Inference_in_Semantic_Web)
- [FOL](First_Order_Logic) give formal definitions of RDFS and OWL statements 
  - Classes - unary predicates
  - Properties - binary predicates
- [DL](Descriptive_Logic) is a subset of FOL where many interesting properties are decidable 



## Formal Definitions
Observe that these statements all have the same general form:
- $\forall \ ... \ (... \ \exists \ ...)$


### [RDFS](RDFS)
|   [RDFS](RDFS) statements  |  [FOL](First_Order_Logic) translation  |  [DL](Descriptive_Logic) notation  |  <code>i rdf:type C</code>  |  $C(i)$  |  $i \ : \ C$ or $C(i)$ ||  <code>i P j</code>  |  $P(i, j)$  |  $i \ P \ j$ or $P(i, j)$ ||  <code>C rdfs:subClassOf D</code>  |  $\forall X \ \big( C(X) \ \exists \ D(X) \big)$  |  $C \sqsubseteq D$ ||  <code>P rdfs:subPropertyOf R</code>  |  $\forall X, Y \ \big( P(X, Y) \ \exists \ R(X, Y) \big)$  |  $P \sqsubseteq R$ ||  <code>P rdfs:domain C</code>  |  $\forall X, Y \ \big( P(X, Y) \ \exists \ C(X) \big)$  |  $\exists P \sqsubseteq C$ ||  <code>P rdfs:range D</code>  |  $\forall X, Y \ \big( P(X, Y) \ \exists \ D(Y) \big)$  |  $\exists P^- \sqsubseteq D$ |

=== [RDFS-Plus](RDFS-Plus) === 
|   [RDFS-Plus](RDFS-Plus)  |  [FOL](First_Order_Logic)  |  [DL](Descriptive_Logic)  |  <code>P rdf:type owl:FunctionalProperty</code>  |  $\forall X, Y, Z \ \big( P(X, Y ) \land P(X, Z) \Rightarrow Y = Z \big)$  |  $(\text{funct} P)$ or $\exists P \sqsubseteq (\leqslant 1 P)$ ||  <code>P rdf:type owl:InverseFunctionalProperty</code>  |  $\forall X, Y, Z \ \big( P(X, Y) \land P(Z, Y) \Rightarrow X = Z)$  |  $(\text{funct} P^− )$ or $\exists P^− (\leqslant 1 P^− )$ ||  <code>P owl:inverseOf Q</code>  |  $\forall X, Y \ \big(P(X, Y) \Leftrightarrow Q(Y, X) \big)$  |  $P \equiv Q^−$ ||  <code>P rdf:type owl:SymmetricProperty</code>  |  $\forall X, Y \ \big(P(X, Y) \Rightarrow P(Y, X) \big)$  |  $P \sqsubseteq P^−$ |

=== [OWL](OWL) === 
Restrictions 

|   [OWL](OWL)  |  [FOL](First_Order_Logic)  |  [DL](Descriptive_Logic)  |  <code>owl:onProperty P; owl:allValuesFrom C</code>  |  $\forall Y \ \big(P(X, Y) \Rightarrow C(Y) \big)$  |  $\forall  P.C$ ||  <code>owl:onProperty P; owl:someValuesFrom C</code>  |  $\exists Y \ \big( P(X, Y) \land C(Y) \big)$  |  $\exists P.C$ ||  <code>owl:onProperty P; owl:minCardinality n</code>  |  $\exists Y_1 ... Y_n \  \big(P(X, Y_1) \land ... \land P(X, Y_n) \land [\forall i, j, i \ne j: Y_i \ne Y_j ]\big)$  |  $(\geqslant n P)$  ||  <code>owl:maxCardinality n</code>  |  (too complex)  |  $(\leqslant n P)$ |
Sets 
|   [OWL](OWL)  |  [FOL](First_Order_Logic)  |  [DL](Descriptive_Logic)  |  <code>C owl:disjointWith D</code>  |  $\forall X \ \big( C(X) \Rightarrow \lnot D(X) \big)$  |  $C \sqsubseteq \lnot D$ ||  <code>owl:intersectionOf (C, D...)</code>  |  $C(X) \land D(X) \land ...$  |  $C \sqcap D \ \sqcap \ ...$ ||  <code>owl:unionOf ( C, D...)</code>  |  $C(X) \lor D(X) \lor ...$  |  $C \sqcup D \ \sqcup \ ...$ ||  <code>owl:oneOf (e, f ...)</code>  |  $X = e \lor X = f \ \lor ...$  |  $\text{OneOf} \{e, f, ...\}$ |

## See Also
- [First Order Logic](First_Order_Logic)
- [Descriptive Logic](Descriptive_Logic)
- [RDFS](RDFS), [RDFS-Plus](RDFS-Plus), [OWL](OWL)

## Sources
- Web Data Management, Manolescu, Ioana, et al. [http://webdam.inria.fr/Jorge/]

[Category:Logic](Category_Logic)
[Category:Semantic Web](Category_Semantic_Web)