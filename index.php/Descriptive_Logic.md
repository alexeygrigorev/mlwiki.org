---
title: Descriptive Logic
layout: default
permalink: /index.php/Descriptive_Logic
---

# Descriptive Logic

## Descriptive Logic
Descriptive Logic (DL)
- Formal basis for [OWL](OWL)
- [FOL](First_Order_Logic) give formal definitions of RDFS and OWL statements 
  - Classes - unary predicates
  - Properties - binary predicates
- but inference in FOL is not decidable
- [DL](Descriptive_Logic) is a subset of FOL where many interesting properties are decidable 
- so it allows reasoning 
- exactly what needed for [Ontologies](Ontologies)


Mapping between [OWL](OWL), FOL and DL: 
- see [Semantic Web Logic](Semantic_Web_Logic)


## DL Knowledge Base
A DL knowledge base consists of:
- ''intentional'' part (''TBox'', $T$) - ontology: classes and concepts
- ''assertional'' part (''ABox'', $A$) - data
- So a ''DL KB'' is a tuple $\langle T, A\rangle$


In [Semantic Web](Semantic_Web) knowledge base is
- TBox: [Ontologies](Ontologies) in [RDFS](RDFS) and [OWL](OWL)
- ABox: Data in [RDF](RDF)-graphs


### TBox
TBox defines the ontology that serves as conceptual view over the data in the ABox


Terminology
- Classes = ''Concepts'' ($B, C, ...$)
- Properties = ''Roles'' ($R, E, ...$)


A TBox $T$ is a set of terminological axioms
- in form of inclusion and equivalences between
  - concepts: $B \sqsubseteq C$ or $B \equiv C$
  - roles: $R \sqsubseteq E$ or $R \equiv E$

### ABox
an ABox - set of assertions that 
- state ''membership'' of ''individuals'' to concepts 
  - $C(a)$
- and ''role membership'' for pairs
  - $R(a, b)$


### Constructing a DL Knowledge Base
"Ingridients": 
- a vocabulary $\langle C, R, O \rangle$:
  - set $C$ of atomic concepts ($A, B, ...$)
  - set $R$ of atomic roles ($P, Q, ...$)
  - and set $O$ of individuals ($a, b, c, ...$)
- a set of constructs for building complex concept and roles from atomic ones 
- a language of axioms for stating the constraints on the vocabulary
  - used to express domain constraints 


### Constructs and Axioms
''Conjunction'' construct $\sqcap$
- $\text{Student} \sqcap \text{Researcher}$
- this is a ''complex'' concept build from atomic concepts $\text{Student}$ and $\text{Researcher}$


''Inclusion'' $\sqsubseteq$ and ''equivalence'' $\equiv$ axioms
- We can relate any concepts (atomic and complex) to atomic concepts 
- e.g. 
  - $\text{PhDStudent} \sqsubseteq \text{Student} \sqcap \text{Researcher}$
  - $\text{PhDStudent} \equiv \text{Student} \sqcap \text{Researcher}$


Restriction constructs 
- ''value restriction'': $\forall \ R.C$ (<code>owl:allValuesFrom</code>)
- ''existential restriction'': $\exists \ R.C$ (<code>owl:someValuesFrom</code>)


Examples
- $\text{MathStudent} \equiv \text{Student} \ \sqcap \ \forall \text{RegisteredTo} . \text{MathCourse}$
  - a math student is a student is he's a student and registered to math courses only
- $\text{MathStudent} \equiv \text{Student} \ \sqcap \ \exists \text{RegisteredTo} . \text{MathCourse}$
  - a math student is a student is he's a student and registered to at least one math course


''Inclusion'' axiom  $\sqsubseteq$
- expresses relation between concepts / roles
- left side: more specific, right side: more general
- e.g.
  - $\text{MathCourse} \sqsubseteq \text{Course}$ (concepts)
  - $\text{LateRegisteredTo} \sqsubseteq \text{RegisteredTo}$ (roles)


### General Inclusion Axioms
General Inclusion Axioms (CGIs)
- inclusions between complex concepts

Example
- $\exists \text{TeachesTo} . \text{UndergraduateStudent} \sqsubseteq \text{Professor} \sqcup \text{Lecturer} $
- only professor or lecturer may teach undergraduate students 
- in [OWL](OWL) it will be the following

```actionscript 3
_:a rdfs:subClassOf owl:Restriction
_:a owl:onProperty :TeachesTo
_:a owl:someValuesFrom :Undergraduate 
_:b owl:unionOf (:Professor :Lecturer)
_:a rdfs:subClassOf _:b
```

<code>_:a</code> and <code>_:b</code> are just blank no-name nodes


## DL-Lite
In DL, reasoning is not always tractable
- but there's a trade-off between expressiveness and tracability
- DL-Lite $\subset$ DL
- [Conjunctive Queries](Conjunctive_Query) can be run over such DL-Lite KBs 
  - and thus, some [SPARQL](SPARQL)


Allowed:
- Constructs:
  - unqualified existential restriction on roles, inverse of roles ($\exists R$ and $\exists R^-$)
  - negation on roles
- Axioms in TBox
  - $B \sqsubseteq C$ and $B \sqsubseteq \lnot C$
  - where $B$ and $C$ are atomic concepts or existential restrictions
- negation allowed only in the right side of inclusion statements 

Also, there are two families of DL-Lite:

### DL-Lite${}_R$
- allow role inclusion statements 
  - $P \sqsubseteq Q$ or $P \sqsubseteq \lnot Q$ 
  - where $P$ and $Q$ are atomic or inversion of atomic roles


### DL-Lite${}_F$
- allow functional statements on roles
  - $(\text{funct} P)$ or $(\text{funct} P^-)$



## See Also
- [First Order Logic](First_Order_Logic)
- [RDFS](RDFS) and [OWL](OWL)

## Sources
- Web Data Management, Manolescu, Ioana, et al. [http://webdam.inria.fr/Jorge/]

[Category:Logic](Category_Logic)
[Category:Knowledge Representation](Category_Knowledge_Representation)