---
title: "Bucket Algorithm (Data Integration)"
layout: default
permalink: /index.php/Bucket_Algorithm_(Data_Integration)
---

# Bucket Algorithm (Data Integration)

## Bucket Algorithm
This is an approach for query rewriting used in [LAV Mediation](LAV_Mediation)

### Overview
3 steps
- determine local relations relevant to the query:
  - for each atom $G$ from the body of the global query $Q$ 
  - construct it's bucket - which groups the view atoms from which $G$ can be inferred
- create candidate rewritings - by combining atoms within the same bucket
- verification step
  - for each candidate, check if it's valid


## Bucket Creation
- let $G$ be a query atom 
- all atoms in $\text{bucket}(G)$ are
  - heads of mappings that have some atom $G^*$ in their bodies
  - s.t. $G$ can be inferred from $G^*$ (i.e. matched)

A atom $G$ of global query $Q$ is ''satisfied by local data'' if
- $G$ can be matched to an atom $R_j$ in the body of some mapping $M_i$ and
- the head of this mapping $M_i$ can be matched to the fact from the data sources

A matching between $G$ and atom $R_j$ of some mapping $M_i$ says
- that the corresponding data source $S_i$ provides relevant information for query $Q$


Need some extra constraints to guarantee that $G$ can be logically inferred:
- the $\text{Bucket}(G)$ contains a view atom $V$ only if 
- and atom in the body of $V$ can be matched with $G$ by a variable mapping s.t.
- the variables mapped to the distinguished variables of $G$ are also distinguished variables in that view $V$ that defined the mapping


### Bucket Creation Example
Consider this LAV mapping:
- $M_1$: S1.Catalogue(U, P) $\subseteq$ FrenchUniversity(U), Program(P), OfferedBy(P, U), OfferedBy(P', U), MasterProgram(P')
- $M_2$: S2.Erasmus(S, C, U) $\subseteq$ Student(S), EnrolledInCourse(S, C), PartOf(C, P), OfferedBy(P, U), EuropeanUniversity(U), EuropeanUniversity(U') RegisteredTo(S, U'), U $\neq$ U'
- $M_3$: S3.CampusFr(S, P, U) $\subseteq$ NonEuropeanStudent(S), Program(P), EnrolledInProgram(S, P), OfferedBy(P, U), FrenchUniversity(U), RegisteredTo(S, U) 
- $M_4$: S4.Mundus(P, C) $\subseteq$ MasterProgram(P), OfferedBy(P, U), OfferedBy(P, U'), EuropeanUniversity(U), NonEuropeanUniversity(U'), PartOf(C, P)


Global Query:

$Q(x) \leftarrow \underbrace{\text{RegisteredTo}(s, x)}_\text{(1)}, \underbrace{\text{EnrolledInProgram}(s, p)}_\text{(2)}, \underbrace{\text{MasterProgram}(p)}_\text{(3)}.$

Consider an atom $G \equiv (1)$
- variable $x$ is distinguished here
- we can find two mappings $M_2$ and $M_3$: some body atom in them can be matched with $G$


For example, $M_3$ 
- $G$ matches to $\text{RegisteredTo}(S, U)$
  - mapping is $S \mapsto s, U \mapsto x$
  - $U$ is distinguished in $M_3$
  - therefore, applying this mapping to the head of $M_3$ enforces the matching of $G$ and $\text{RegisteredTo}(S, U)$
  - $P$ is not present there, so mapping it to some fresh variable $v_1$: $P \mapsto v_1$
- so, $S_3.\text{CampusFr}(s, v_1, x) \ \land \ \text{FOL}(M_3) \vDash \ \exists s: \text{RegisteredTo}(s, x) $
  - where
  - $\text{FOL}(M_3)$ logical meaning of $M_3$ (in the [First Order Logic](First_Order_Logic) form)
  - $\vDash$ means "enforces"
- and $S_3.\text{CampusFr}(s, v_1, x)$ is added to $\text{Bucket}(G)$
  - note mapping $P \mapsto v_1$ in $S_3.\text{CampusFr}(S, P, U)$


Consider mapping $M_2$
- match between $G \equiv (1)$ and $\text{RegisteredTo}(S, U')$
- mapping $S \mapsto s, U' \mapsto x$
- but $U'$ is qualified existentially in this view
- i.e. this mapping doesn't enforce matching of $G$ and $\text{RegisteredTo}(S, U')$
- so, $S_2.\text{Erasmus}(s, v_2, v_3) \ \land \ \text{FOL}(M_2) \not \vDash \exists \ s : \text{RegisteredTo}(s, x)$


why?
- $\text{FOL}(M_2) \equiv \forall S, C, U \ \Big[ S_2.\text{Erasmus}(S, C, U) \ \Rightarrow \ \exists \ P, U' \ : \ \text{EuropeanStudent}(S)$ $\ \land \ \text{EnrolledInCourse}(S,C) \ \land \
\text{PartOf}(C,P)$ $\ \land \ \text{OfferedBy}(P,U)
\ \land \ \text{EuropeanUniversity}(U)$ $\ \land \ \text{RegisteredTo}(S, U') \ \land \ U \neq U' \Big]$
- so, from fact $S_2.\text{Erasmus}(s, v_2, v_3)$ it follows that $\exists \ s, U' \ : \ \text{RegisteredTo}(s,U')$
- $\exists \ s \ : \ \text{RegisteredTo}(s, x)$, where $x$ is fixed is strictly weaker
- but it can't be satisfied, so  $\exists \ s, U' \ : \ \text{RegisteredTo}(s,U')$ also isn't


### Bucket Algorithm
Bucket($G$, $Q$, $M$):
- Input: 
  - An atom $G(u_1, ... , u_m)$ of the query $G$ 
  - a set of LAV mappings $M$
- Output: 
  - The set of view atoms from which $G$ can be inferred
- $\text{Bucket}(G) \leftarrow \varnothing$
- for each LAV mapping $S(\vec{x}) \subseteq Q(\vec{x}, \vec{y})$ from $M$
  - if $\exists$ atom $G(z_1, ..., z_m) \in Q(\vec{x}, \vec{y})$ s.t. 
    - $\forall z_i: z_i \mapsto u_i$ and $z_i$ is distinguished in $G$ and $u_i$ is distinguished in $Q$
  - let $\Psi$ be the mapping $\forall z_i: z_i \mapsto u_i$
    - extend $\Psi$ by mapping the head variables $x_i \in \vec{x}$ s.t. $x_i \not \in \{ z_1, ..., z_m \}$ to new fresh variables:
    - $\forall x_i \in \vec{x} \ \land \ x_i \not \in \{ z_1, ..., z_m \} \ : \ x_i \mapsto v_k $ where $k$ is some counter
  - add $S \big( \Psi(\vec{x}) \big)$ to $\text{Bucket}(G)$:
    - $\text{Bucket}(G) \leftarrow \text{Bucket}(G) \cup S \big( \Psi(\vec{x}) \big)$
- return $\text{Bucket}(G)$


Theorem: 
- let $G(u_1, ..., u_m) \in Q$ be an atom of the query $Q$ 
- let $\vec{u}$ be a (possible empty) set of existential variables from $\{ u_1, ..., u_m \}$
- let $m$ be a LAV mapping $S(\vec{x}) \subseteq Q(\vec{x}, \vec{y})$
- then
- $S(\vec{v}), \text{FOL}(m) \ \vDash \ \exists \ \vec{u} \ : \ G(u_1, ..., u_m)$ iff
- $\exists H \in \text{Bucket}(G)$ s.t. $H \equiv S(\vec{x})$ up to renaming fresh variables


Example
- query $Q(x) \leftarrow \underbrace{\text{RegisteredTo}(s, x)}_\text{(1)}, \underbrace{\text{EnrolledInProgram}(s, p)}_\text{(2)}, \underbrace{\text{MasterProgram}(p)}_\text{(3)}.$
- the following buckets are obtained
  - for $\text{RegisteredTo}(s, x) \ (1)$
    - $S_3.\text{CampusFr}(s, v_1, x)$
  - for $\text{EnrolledInProgram}(s, p) \ (2)$
    - $S_3.\text{CampusFr}(s, p, v_2)$
  - for $\text{MasterProgram}(p) \ (3)$
    - $S_1.\text{Catalogue}(v_3, v_4)$
    - $S_4.\text{Mundus}(p, v_5)$


## Constructing Candidate Rewritings
Obtain candidates 
- by combining the view atoms to each bucket

### Validation
- it's possible that a candidate is not a valid rewriting of a query
- by the Thm we know only that 
  - each candidate rewriting entails each atom of the query <u>in isolation</u>
  - i.e. without taking into account the possible bindings of existential variables within the query


''Expanding'' a rewriting $R$: 
- for each atom $A$ from the body of rewriting $R$ 
  - replace $A$ by the corresponding LAV mapping for $A$ 
  - new existential variables are introduced - to avoid naming conflicts
- the result - the expansion of $R$: $\text{Exp} \big[ R(...) \big]$


Validation Algo:
- for a rewriting $R$ find $\text{Exp} \big[ R(...) \big]$
- check for containment: $\text{Exp} \big[ R(...) \big] \subseteq Q(...)$ where $Q$ is the global query (see [CQ Containment](Conjunctive_Query#Containement))
- if $\text{Exp} \big[ R(...) \big] \subseteq Q(...)$, then $R$ is a valid rewriting


### Validation Example
We obtained these rewritings:
- $r_1(x) \leftarrow S_3.\text{CampusFr}(s,v_1,x), S_3.\text{CampusFr}(s,p,v_2), S_1.\text{Catalogue}(v_3,v_4)$
- $r_2(x) \leftarrow S_3.\text{CampusFr}(s,v_1,x), S_3.\text{CampusFr}(s,p,v_2), S_4.\text{Mundus}(p,v_5)$


Validation
- $r_1$ is not a valid rewriting of $Q$
- expand $r_1$:
  - $
\begin{array}{l l}
\text{Exp} \big[ r_1(x) \big] \leftarrow & \text{NonEuropeanStudent}(s), \text{Program}(v_1), \\
& \text{EnrolledInProgram}(s,v_1), \text{OfferedBy}(v_1,x), \\
& \text{FrenchUniversity}(x), \text{RegisteredTo}(s,x), \\
& \text{Program}(p), \text{EnrolledInProgram}(s,p), \\
& \text{OfferedBy}(p,v_2), \text{FrenchUniversity}(v_2), \\
& \text{RegisteredTo}(s,v_2), \text{FrenchUniversity}(v_3), \\
& \text{Program}(v_4), \text{OfferedBy}(v_4,v_3), \\
& \text{OfferedBy}(v_5,v_3), \text{MasterProgram}(v_5) \\
\end{array}
$
- Now check the containment:
- the following is the canonical database $D_{r_1(x)}$ for $\text{Exp} \big[ r_1(x) \big]$
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/xml/sw/lav-bucket-validation-candb.png" alt="Image">
- evaluation of $Q$ on this canonical database is empty: $Q\big( D_{r_1(x)} \big) \equiv \varnothing$ 
  - no way to assign variables $s$ and $p$ 
- so it's not a valid rewriting
- but $r_2$ is a valid rewriting


## Final Result
The final result is
- the union of all valid rewritings



## See Also
- [Data Integration](Data_Integration)
- [Mediator (Data Integration)](Mediator_(Data_Integration))
- [GAV Mediation](GAV_Mediation)
- [Minicon Algorithm](Minicon_Algorithm)
- [Inverse-Rules Algorithm](Inverse-Rules_Algorithm)

## Sources
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Data Integration](Category_Data_Integration)