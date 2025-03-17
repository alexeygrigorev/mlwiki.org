---
title: Minicon Algorithm
layout: default
permalink: /index.php/Minicon_Algorithm
---

# Minicon Algorithm

## Minicon Algorithm
This is an approach for query rewriting used in [LAV Mediation](LAV_Mediation)

### Overview
An optimized version of the [Bucket Algorithm](Bucket_Algorithm_(Data_Integration))
- avoids the last step: verification
- idea: not to put atoms that will generate invalid rewritings 
- an atom can be useless if its binding of variables doesn't match the bindings of other occurrences of this variable
  - recall ([Bucket Algorithm (Data Integration)#Validation Example](Bucket_Algorithm_(Data_Integration)#Validation_Example) - this is the reason why $r_1$ didn't validate)


So, steps are
- creating MCDs (corresponds to the Bucket creation step)
- combining MCDs (the second step)
- where MCDs are ''Minicon Descriptions'' - instead of buckets


### Example
The algorithm will be explained by this example

Consider this global query
- $Q(x) \leftarrow U(y,z), R(x,z), T(z,y), R(y',x)$


And two LAV mappings
- $V_1(u,v) \subseteq T(w,u), U(v,w), R(v,u)$
- $V_2(u,v,v') \subseteq T(w,u), U(v,w), R(v',w)$


## Step 1: Creating MCDs
In this step
- for each atom $A_i$ of the query $Q$
- for each LAV mapping $V_i$ 
- determine the relevance of $V_i$ w.r.t. rewriting $A_i$ 


### Illustration of Step 1
Consider first atom $U(y, z)$ of $Q$:


Vs [Bucket](Bucket_Algorithm_(Data_Integration)):
- Bucket would put $V_1(v_1, y)$ to $\text{Bucket} \Big( U(y, z) \Big)$
- because we have mapping $v \mapsto y, w \mapsto z \ \ (*)$
- $(*)$ allows the match between atom $U(y, z)$ and atom $U(v, w)$ from the body of $V_1(v_1, y)$ 

But here we don't consider $U(v, w) \in V_1(v_1, y)$ in isolation
- since $w$ there is existential and $w \mapsto z$
  - need to check that $(*)$ covers all <u>query</u> atoms ($\in Q$) that involve $z$
- i.e. also need to check query atoms $R(x, {\color{blue}{z}})$ and $T({\color{blue}{z}}, y)$
- it's the only way to enforce that all occurrences of $z$ are mapped to the same variable $w$

For this example ($U(y, z)$ vs $V_1(u, v)$)
- can we map $R(x, z) \in Q \mapsto R(_, w) \in V_1$? (i.e. try to expand $(*)$)
- no we can't: there doesn't exist such atom in $V_1$
- so no MCD is created from $V_1$


Now try to match $U(y, z)$ with $V_2(u, v, v')$
- we can match $U(y, z) \in Q$ to $U(v, w) \in V_2(u, v, v')$
- mapping is $v \mapsto y, w \mapsto z \ \ (**)$
- ${\color{blue}{z}}$ is existential, so check query atoms $R(x, {\color{blue}{z}})$ and $T({\color{blue}{z}}, y)$
  - $R(v', w) \mapsto R(x, {\color{blue}{z}})$ by adding $v' \mapsto x$
  - $T(w, u)  \mapsto T({\color{blue}{z}}, y)$ by adding $u \mapsto y$
- so an MCD is created for $V_2(u, v, v')$ 
- $\text{MCD}_1 = \Big( V_2(u, v, v'), \{1,2,3\} \Big)$
  - we also write the positions of the query atoms that this MCD covers ($\{1,2,3\}$) 
- since $\text{MCD}_1$ covers $\{1,2,3\}$, only atoms in $\{4\}$ remain uncovered, so need to cover them


Consider 4th query atom $R(y', x)$
- for $V_1$ we match with atom $R(v, u)$
  - mapping $v \mapsto y', u \mapsto x$
  - $x$ is a distinguished variable in $Q$, and $u$ is a distinguished variable in $V_1$ 
  - existential variable $y'$ has only single occurrence, so we can add it
- so we have the following MCD:
  - $\text{MCD}_2 = \Big(  V_1(x, y'), \{ 4 \} \Big)$
- for $R(v', w) \in V_2$ no MCD is created
  - mapping $v' \mapsto y', w \mapsto x$
  - but $w$ is existential in $V_2$, and $x$ is distinguished in $Q$
  - so no MCD



## Step 2: Combining MCDs
Combining step
- At this step we combine MCDs that cover mutually disjoint subsets of the atoms of query $Q$
  - (these subsets should together cover the entire $Q$)
- this way we obtain rewritings of the query $Q$ 
- the rewriting are guaranteed to be valid - so no checking 

So, a rewriting for $Q(x)$ is 
- $R(x) \leftarrow V_2(y, y, x), V_1(x, y')$


## See Also
- [Data Integration](Data_Integration)
- [Mediator (Data Integration)](Mediator_(Data_Integration))
- [GAV Mediation](GAV_Mediation)
- [Bucket Algorithm (Data Integration)](Bucket_Algorithm_(Data_Integration))
- [Inverse-Rules Algorithm](Inverse-Rules_Algorithm)


## Sources
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Data Integration](Category_Data_Integration)