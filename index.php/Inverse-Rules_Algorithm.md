---
title: "Inverse-Rules Algorithm"
layout: default
permalink: /index.php/Inverse-Rules_Algorithm
---

# Inverse-Rules Algorithm

## Inverse-Rules Algorithm
This is an approach for query rewriting used in [LAV Mediation](LAV_Mediation)
- radically different from [Bucket](Bucket_Algorithm_(Data_Integration)) and [Minicon](Minicon_Algorithm)
- idea: transform [LAV mappings](LAV_Mediation) to [GAV mappings](GAV_Mediation) (called ''inverse rules'')
- to do that, use query unfolding instead of query rewriting


### Overview
Steps:
- constructing ''inverse rules'' from a set of LAV mappings
- unfolding a global query to obtain local queries 


Important thing:
- 1st step of the algorithm is independent from queries 
- it only needs to consider a set of LAV mappings 


One LAV Mapping is replaced by several GAV Mappings 
- one for each atom in the body of the rule 
- but need to keep bindings between different occurrences of the same existential variables in the body
- done by using [First Order Logic](First_Order_Logic) function - [Skolem Function](Skolem_Function)


### Illustraction by Example
Here we will use the following example to illustrate the algorithm

Global query:
- $Q(x) \leftarrow U(y,z), R(x,z), T(z,y), R(y',x)$

And two LAV mappings:
- $V_1(u,v) \subseteq T(w,u), U(v,w), R(v,u)$
- $V_2(u,v,v') \subseteq T(w,u), U(v,w), R(v',w)$


## [Skolem Function](Skolem_Function)
### Logical Intuition
For $V_1$, [FOL](First_Order_Logic) meaning is 
- $\forall \ u, v \Big[ V_1(u, v) \Rightarrow \exists \ w \ : \ T(w, u) \land U(v, w) \land R(v, u)  \Big]$
- suppose a tuple $(a, b)$ belongs to the data source that backs $V_1$
  - so we have a fact $V_1(a, b)$
- from this fact $V_1(a, b)$ can infer that $R(b, a)$ 
  - $V_1(a, b) \Rightarrow R(b, a)$
  - (all conjuncts have to be true for a statement to be true, so it means the last conjuncts holds true)
- so $b$ can be an answer to a global query Q(x) = $R(x, y)$


But we can infer other things as well
- e.g. $V_1(a, b) \Rightarrow \exists \ d_1 \ : \ T(d_1, a) \land U(b, d_1)$ 
- where $d_1$ is some constant
  - we don't know its value, but we know it exists (since it's existentially qualified) and 
  - it depends on constants $a$ and $b$
- so we can denote this dependency as $d_1 = f_1(a, b)$


[Skolem Function](Skolem_Function)
- the symbol $f_1(u, v)$ is a Skolem Function of arity 2
  - $f_1(u, v)$ denotes that there exists some constant that depends on values of $u$ and $v$
- given two distinct Skolem terms, e.g. $f_1(1, 2)$ and $f_1(2, v_3)$ we never can say if they belong to the same constant or not


## Creating Inverse Rules
So we can create these GAV mappings and their FOL translations 

### Example 1
Inverse Rules of the 1st LAV mapping:
- $V_1(u,v) \subseteq T(w,u), U(v,w), R(v,u)$


|   Rule  |  Mapping  |  FOL   |  $\text{IN}_{1,1}$  |  $V_1(u,v) \subseteq T \big(f_1(u,v), u \big)$  |  $\forall \ u, v \Big[ V_1(u,v) \Rightarrow T \big( f_1(u, v), u \big) \Big]$ ||  $\text{IN}_{1,2}$  |  $V_1(u,v) \subseteq U \big(v, f_1(u,v) \big)$  |  $\forall \ u, v \Big[ V_1(u,v) \Rightarrow U \big(v, f_1(u, v) \big) \Big]$ ||  $\text{IN}_{1,3}$  |  $V_1(u,v) \subseteq R \big(v, u \big)$  |  $\forall \ u, v \Big[ V_1(u,v) \Rightarrow R \big(v, u \big) \Big]$ |


### Algorithm
Algorithm for creating the inverse rules
- for each LAV mapping $M_i$ with $n_i$ atoms 
  - create $n_i$ GAV mappings (i.e. inverse rules)
  - for each existential variable introduce a Skolem function of all distinguished variables


### Example 2
For example, for the second mapping the result is 
- mapping: $V_2(u,v,v') \subseteq T(w,u), U(v,w), R(v',w)$
- $\text{IN}_{2,1} \ : \ V_2(u,v,v') \subseteq T \big(f_2(u,v,v'), u \big)$
- $\text{IN}_{2,2} \ : \ V_2(u,v,v') \subseteq U \big(v, f_2(u,v,v') \big)$
- $\text{IN}_{2,3} \ : \ V_2(u,v,v') \subseteq R \big(v', f_2(u,v,v') \big)$

So, for each existentially qualified variable we define some Skolem function
- this is a function of all distinguished variables
- for $V_2$ we define $w = f_2(u,v,v')$


## Step 2: Query Unfolding
Query Unfolding
- The process of unfolding query is different from [GAV Mediation](GAV_Mediation)
- Reason = Skolem terms


### GAV vs Inverse-Rules
Before (in [GAV Mediation](GAV_Mediation))
- for each query atom $G_i(x_1, ..., x_m)$
  - match with some GAV mapping atom of the form $G_i(z_1, ..., z_m)$ 
  - with mapping $\forall i: \ x_i \mapsto z_i$
- here each atom is unfolded <u>in isolation</u>
- but here it doesn't work: we have Skolen Functions

Now:
- need ''unification'' of atoms with functions
- more complex than simple unfolding
- may require substitution of some variables with function terms - Skolem terms


### Unification Algorithm
Unification
- let $\sigma$ be an empty set of substitutions
- let $PR$ be a partial rewriting of $Q$, $PR \leftarrow Q$
- For each atom $G_i(...) \in Q$ (in turn)
  - unify $G_i \in Q$ with some atom $V_j \subseteq G_i$ from the set of rules
    - backtrack when we have a Skolem term in $V_j$
  - $\sigma_i$ - the substitution that made this unification possible
  - in $PR$, replace $G_i$ with the head $V_j$ of $G_i$
  - apply obtained $\sigma_i$ to the partial rewriting $PR$: $PR \leftarrow \sigma_i(PR)$
  - keep all mappings from $\sigma_i$: $\sigma \leftarrow \sigma \cup \sigma_i$ 
- let $R$ be a rewriting of $Q$: $R \leftarrow PR$
- return $R$



### Example
Consider this query
- $Q(x) \leftarrow \underbrace{U(y,z)}_\text{(1)}, \underbrace{R(x,z)}_\text{(2)}, \underbrace{T(z,y)}_\text{(3)}, \underbrace{R(y',x)}_\text{(4)}$


Inverse Rules:
- $\text{IN}_{1,1} \ : \ V_1(u,v)    \subseteq T \big(f_1(u,v), u \big)$
- $\text{IN}_{1,2} \ : \ V_1(u,v)    \subseteq U \big(v, f_1(u,v) \big)$
- $\text{IN}_{1,3} \ : \ V_1(u,v)    \subseteq R \big(v, u \big)$
- $\text{IN}_{2,1} \ : \ V_2(u,v,v') \subseteq T \big(f_2(u,v,v'), u \big)$
- $\text{IN}_{2,2} \ : \ V_2(u,v,v') \subseteq U \big(v, f_2(u,v,v') \big)$
- $\text{IN}_{2,3} \ : \ V_2(u,v,v') \subseteq R \big(v', f_2(u,v,v') \big)$


Now try to unify each atom of $Q$ with some atom from the rules
- we use ''most general unifier'' (''mgu'')


Atom 1: $U(y, z)$
- $U(y, z)$ can be ''unified'' with $U \big(v, f_1(u,v) \big)$ (from $\text{IN}_{1,2}$)
- the mgu is a substitution $\sigma = \{ y \mapsto v_1, v \mapsto v_1, z \mapsto f_1(v_2,v_1), u \mapsto v_2 \}$
- $v_1$ and $v_2$ are new fresh variables to avoid conflicts
- $y$ and $v$ map to the same variable $v_1$ because they are at the same position
- substitution $\sigma$ is called a ''unifier'' of two expressions and $U \big(v, f_1(u,v) \big)$
- it's a unifier because applying $\sigma$ results in identical expressions:
  - $\sigma \Big( U(y, z) \Big) \equiv \sigma \Big( U \big(v, f_1(u,v) \big) \Big) \equiv U \big(v_1, f_1(v_2, v_1) \big)$
- apply $\sigma$ to the rest of atoms in $Q$ and unfold the first query atom of $Q$
  - the head of $U \big(v, f_1(u,v) \big)$ is $V_1(u,v)$
  - because of the substitution $v \mapsto v_1, u \mapsto v_2$ it becomes $V_1 \big( v_2, v_1 \big)$
  - the remaining atoms are $R(x,z), T(z,y), R(y',x)$, and by substitution we obtain 
    - $R \big(x, z \big) \to R \big(x, f_1(v_2,v_1) \big)$ 
    - $T \big(z, y \big) \to T \big(f_1(v_2,v_1), v_1 \big)$
    - $R \big(y',x \big) \to R \big(y', x \big)$
- so we have:
  - $PR_1(x) \leftarrow  V_1 \big( v_2, v_1 \big), R \big(x, f_1(v_2,v_1) \big), T \big(f_1(v_2,v_1),v_1 \big), R \big(y',x \big).$


Atom 2: $R(x, z) \to R \big(x, f_1(v_2,v_1) \big)$
- (taking into account the substitutions made in previous iterations)
- $R(x,z)$ can be unified with $\ V_1(u,v) \subseteq R \big(v, u \big)$ ($\text{IN}_{1,3}$)
- unfolding of atom $(2)$ gives us the following partial rewriting
  - $PR_2(x) \leftarrow  V_1 \big( v_2, v_1 \big), V_1 \big( f_1(v_2,v_1), x \big), T \big(f_1(v_2,v_1), v1 \big), R \big(y', x \big)$
- note that now we have a Skolem term in the matched head
  - so it's useless to continue unfolding 
  - there's no way to match $V_1 \big( f_1(v_2,v_1), x \big)$ with any fact in our data source 
  - because we don't know what is the constant resulting from $f_1(v_2,v_1)$, we know only that it exists
- so, we backtrack to atom 1 


Atom 1: $U(y, z)$
- now try to unfold it using $\text{IN}_{2,2}$
- with substitution 
  - $\sigma_1^{(2)} = \{ y \mapsto v_1, v \mapsto v_1, z \mapsto f_2(v_2,v_1,v_3), u \mapsto v_2, v' \mapsto v3  \}$
- using this $\sigma_1^{(2)}$ we obtain the following partial rewriting
- $PR'_1(x) \leftarrow V_2 \big(v_2,v_1,v_3 \big), R \big(x,f_2(v_2,v_1,v_3) \big), T \big(f_2(v_2,v_1,v_3),v_1 \big), R \big(y',x \big)$


Atom 2: $R \big(x, z \big) \to R \big(x, f_2(v_2,v_1,v_3) \big)$ 
- try to use $\text{IN}_{2,3}$
- with substitution
  - $\sigma_2^{(2)} = \{ v' \mapsto x, v_3 \mapsto x, u \mapsto v_2, v \mapsto v_1 \}$
- $PR'_2(x) \leftarrow V_2 \big(v_2,v_1,v_3 \big), \underbrace{V_2 \big(v_2,v_1,x \big)}_{\color{blue}{\text{redundant}}}, T \big(f_2(v_2,v_1,v_3),v_1 \big), R \big(y',x \big)$
  - $PR'_2(x) \leftarrow V_2 \big(v_2,v_1,v_3 \big), T \big(f_2(v_2,v_1,v_3),v_1 \big), R \big(y',x \big)$


Atom 3: $T(z,y) \to T \big(f_2(u,v,v'),u \big)$
- need to match with $T \big( f_2(v_2,v_1,x), v_1 \big)$ from $\text{IN}_{2,3}$
- substitution $\{ v_2 \mapsto v_3, u \mapsto v_3, v_1 \mapsto v_3, v \mapsto v_3, v' \mapsto x \}$
- so we have this partial rewriting 
  - $PR'_3(x) \leftarrow V_2(v_2,v_1,x), V_2(v_3,v_3,x), R(y',x)$
  - first atom is redundant, so have $PR'_3(x) \leftarrow  V_2(v_3,v_3,x), R(y',x)$


Atom 4: $R(y',x)$
- match with $R \big(v, u \big)$ from $\text{IN}_{1,3}$
- and have $RP'_4(x) \leftarrow  V_2(v_3,v_3,x), V_1(y', x)$


So, final rewriting 
- $R_1(x) \leftarrow  V_2(v_3,v_3,x), V_1(y', x)$


## Advantages
Main advantage
- producing inverse rules is independent from processing queries 



## See Also
- [Data Integration](Data_Integration)
- [Mediator (Data Integration)](Mediator_(Data_Integration))
- [GAV Mediation](GAV_Mediation)
- [Bucket Algorithm (Data Integration)](Bucket_Algorithm_(Data_Integration))
- [Minicon Algorithm](Minicon_Algorithm)

## Sources
- Web Data Management book [http://webdam.inria.fr/Jorge]

[Category:Data Integration](Category_Data_Integration)