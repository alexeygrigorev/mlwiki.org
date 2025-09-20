---
layout: default
permalink: /index.php/GAV_Mediation
tags:
- data-integration
title: GAV Mediation
---
## GAV Mediation
There are two main approached for [Mediating](Mediator_(Data_Integration)) in [Data Integration](Data_Integration) 
- [GAV Mediation](GAV_Mediation) - defining global relations in terms of local
- [LAV Mediation](LAV_Mediation) - defining local relations in terms of global


GAV - Global-as-View Mediation
- global is constrained by views of the local relations
- See some notation in [Mediator (Data Integration)](Mediator_(Data_Integration))


## GAV Mapping
A GAV mapping is an expression of the form 
- $R(x_1, ..., x_n) \supseteq Q(x_1, ..., x_n)$
- where $Q(x_1, ..., x_n)$ is a [Conjunctive Query](Conjunctive_Query) of the same arity as $R$
- since $Q(x_1, ..., x_n) \leftarrow A_1(...), \ ..., \ A_k(...)$, can rewrite as $R(x_1, ..., x_n) \supseteq A_1(...), \ ..., \ A_k(...)$
- so a mapping is some query over some source relations, also called a ''view''


[FOL](First_Order_Logic) Semantics of this mapping
- $\forall \ x_1, ..., x_n \ \exists \ y_1, ..., y_m \ : \ A_1(...), \ ..., \ A_k(...) \Rightarrow R(x_1, ..., x_n)$
- $x_1, ..., x_n$ - distinguished variables,
- $y_1, ..., y_n$ - existential variables


### GAV Mapping Example
Data sources:
- S1.Catalogue(nomUniv, programme). - programs in French universities
- S2.Erasmus(student, course, univ). - European Erasmus students 
- S3.CampusFr(student, program, university). - foreign students in France
- S4.Mundus(program, course). - international master programs

Global Schema:
- MasterStudent(studentName), 
- University(uniName),
- MasterProgram(title), 
- MasterCourse(code),
- EnrolledIn(studentName,title), 
- RegisteredTo(studentName, uniName).


The GAV mapping for the global schema is the following
- MasterStudent(N) $\supseteq$ S2.Erasmus(N, C, U), S4.Mundus(P, C)
- MasterStudent(N) $\supseteq$ S3.CampusFr(N, P, U), S4.Mundus(P, C)
- University(U) $\supseteq$ S1.Catalogue(U, P)
- University(U) $\supseteq$ S2.Erasmus(N, C, U)
- University(U) $\supseteq$ S3.CampusFr(N, P, U)
- MasterProgram(T) $\supseteq$ S4.Mundus(T, C)
- MasterCourse(C) $\supseteq$ S4.Mundus(T, C)
- EnrolledIn(N, T) $\supseteq$ S2.Erasmus(N, C, U), S4.Mundus(T, C)
- EnrolledIn(N, T) $\supseteq$ S3.CampusFr(N, T, U), S4.Mundus(T, C)
- RegisteredTo(N, U) $\supseteq$ S3.CampusFr(N, T, U)
- left side: global; right side: local



## Query Answering
To evaluate a query
- for answering some query against the global schema, need to find the relevant data sources 
- then we issue queries for each data source and combine the result


'''GAV Unfolding''' (informal)
- for each atom $A_i(...)$ of the query
- if this atom can be matched to a head of some mapping $R_j(...)$
- replace the atom $A_i(...)$ by the body of the mapping $R_j(...)$


### Illustration
Illustration by example
- Consider this query:
- $Q(x) \leftarrow \underbrace{\text{RegistersTo}(s, x)}_\text{(1)}, \underbrace{\text{MasterStudent}(s)}_\text{(2)}$
- for $\text{(1)}$, one mapping can be found, for $\text{(2)}$ - two mappings
- so we can have two unfoldings:
  - $Q_1(x) \leftarrow S_3.\text{CampusFr}(s,v_1,x), S_2.\text{Erasmus}(s,v_2,v_3), S_4.\text{Mundus}(v_4,v_2)$
  - $Q_2(x) \leftarrow S_3.\text{CampusFr}(s,v_5,x), S_3.\text{CampusFr}(s,v_6,v_7), S_4.\text{Mundus}(v_6,v_8)$
- note that $Q_2$ can be simplified (by removing a redundant join)
  - so we have the following two rewritings:
  - $R_1(x) \leftarrow S_3.\text{CampusFr}(s,v_1,x), S_2.\text{Erasmus}(s,v_2,v_3), S_4.\text{Mundus}(v_4,v_2)$
  - $R_2(x) \leftarrow S_3.\text{CampusFr}(s,v_6,v_7), S_4.\text{Mundus}(v_6,v_8)$
- the final result: $R_1(x) \cup R_2(x)$


### GAV Unfolding
'''def''': ''GAV Query unfolding'' (or ''GAV rewriting'')
- let $Q(\vec{x}) \leftarrow G_1(\vec{z}_1), \ ..., \ G_n(\vec{z}_n)$ be a query over global schema 
- $\forall \ G_i \ \exists$ GAV mapping $G_i \supseteq q_i(\vec{x}_i, \vec{y}_i)$
  - where in $q_i(\vec{x}, \vec{y})$: $\vec{x}$ - distinguished variables, $\vec{y}$ - existential  
- ''an unfolding'' of $Q(\vec{x})$ is a query $U$ that is obtained by
- replacing each conjunct $G_i(\vec{z}_i)$ by $q_i \big( \Psi_i(\vec{x}, \vec{y}) \big)$
- $\Psi_i(\vec{x}, \vec{y})$ maps 
  - variables $\vec{x}$ of $q_i$ to $\vec{z}$ and 
  - existential variables $\vec{y}$ to some new variables (needed to avoid naming conflicts - and therefore unnecessary constraints)


Simplification
- each unfolding then simplified (redundant joins/conjuncts are removed)
- and obtain rewritings


## Main Limitations of GAV Mediation
- Adding and removing data sources is costly 
  - it may require revising all the mappings 
- for Web, servers may come and go 
- so another approach is needed
- thus, for [Semantic Web](Semantic_Web), [LAV Mediation](LAV_Mediation) is more preferred


## See Also
- [Data Integration](Data_Integration)
- [Mediator (Data Integration)](Mediator_(Data_Integration))
- [LAV Mediation](LAV_Mediation)

## Source
- Web Data Management book [http://webdam.inria.fr/Jorge]
