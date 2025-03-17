---
title: LAV Mediation
layout: default
permalink: /index.php/LAV_Mediation
---

# LAV Mediation

## LAV Mediation
There are two main approached for [Mediating](Mediator_(Data_Integration)) in [Data Integration](Data_Integration) 
- [GAV Mediation](GAV_Mediation) - defining global relations in terms of local
- [LAV Mediation](LAV_Mediation) - defining local relations in terms of global


LAV - Local-as-View Mediation
- local relations are defined as views (queries) over global relations
- goal: define the global schema in such a way that individual definitions don't change when new data sources are added or old are removed 
- See some notation in [Mediator (Data Integration)](Mediator_(Data_Integration))


## LAV Mapping
''LAV Mapping ''
- mapping $S \subseteq Q$ for some [Conjunctive Query](Conjunctive_Query) $Q(\vec{x}) \leftarrow A_1(\vec{u}_1), \ ..., \ A_k(\vec{u}_k)$ over the global relations 
- this gives loose-coupling between global and local schemas


[FOL](First_Order_Logic) Semantics:
- $\forall x_1, ..., x_n  \Big[ S(x_1, ..., x_n) \Rightarrow \exists \ y_1, ..., y_m \ : \ A_1(\vec{u}_1) \ \land \ ... \ \land \ A_k(\vec{u}_k) \Big]$
- $S(x_1, ..., x_n)$ - head of a view
- $y_1, ..., y_m$ - existential variables
- $A_1(\vec{u}_1) \ \land \ ... \ \land \ A_k(\vec{u}_k)$ - body


### Example
Suppose we have this global schema
- Student(studentName), 
- EuropeanStudent(studentName),
- University(uniName), 
- NonEuropeanStudent(studentName),
- FrenchUniversity(uniName), 
- EuropeanUniversity(uniName),
- NonEuropeanUniversity(uniName), 
- Program(title),
- MasterProgram(title), 
- EnrolledInProgram(studentName, title),
- Course(code), 
- EnrolledInCourse(studentName, code),
- PartOf(code, title), 
- RegisteredTo(studentName, uniName),
- OfferedBy(title, uniName).


Data sources from the previous examples
- S1.Catalogue(nomUniv, programme). - programs in French universities
- S2.Erasmus(student, course, univ). - European Erasmus students 
- S3.CampusFr(student, program, university). - foreign students in France
- S4.Mundus(program, course). - international master programs


LAV Mappings:
- $m_1$: S1.Catalogue(U, P) $\subseteq$ FrenchUniversity(U), Program(P), OfferedBy(P, U), OfferedBy(P', U), MasterProgram(P')
- $m_2$: S2.Erasmus(S, C, U) $\subseteq$ Student(S), EnrolledInCourse(S, C), PartOf(C, P), OfferedBy(P, U), EuropeanUniversity(U), EuropeanUniversity(U') RegisteredTo(S, U'), U $\neq$ U'
- $m_3$: S3.CampusFr(S, P, U) $\subseteq$ NonEuropeanStudent(S), Program(P), EnrolledInProgram(S, P), OfferedBy(P, U), FrenchUniversity(U), RegisteredTo(S, U) 
- $m_4$: S4.Mundus(P, C) $\subseteq$ MasterProgram(P), OfferedBy(P, U), OfferedBy(P, U'), EuropeanUniversity(U), NonEuropeanUniversity(U'), PartOf(C, P)


So,
- LAV mapping can be seen as a description of the data source in terms of the global schema
- for example, Erasmus students ($m_2$) are
  - European students
  - enrolled in an European university
  - that European university is different from their home university
  - they remain registered in their home university

Loose-Coupling
- This gives loose-coupling between local and global relations 
- which is important when participating data sources change frequently 


## Query Answering
suppose we're interested in Master students 
- define the following query
- $\text{MasterStudent}(E) \leftarrow \text{Student}(E), \text{EnrolledInProgram}(E, M), \text{MasterProgram}(M).$
- how to find which data sources to query?
- rewriting process is more complex, than for GAV

Algorithms to do that
- [Bucket Algorithm](Bucket_Algorithm_(Data_Integration))
- [Minicon Algorithm](Minicon_Algorithm)
- [Inverse-Rules Algorithm](Inverse-Rules_Algorithm)


## Sources
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Data Integration](Category_Data_Integration)