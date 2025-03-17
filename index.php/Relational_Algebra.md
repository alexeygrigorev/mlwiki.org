---
title: Relational Algebra
layout: default
permalink: /index.php/Relational_Algebra
---

# Relational Algebra

\(\newcommand{\AntiJoin}{ \ \bar{\Join} \ } \)

## Relational Algebra
- Relational Algebra repesents the operations on relations for [Relational Databases](Relational_Databases)
- Relational Algebra is algebra that consists of operations for constructing new relations from given relations 
  - (it's ''closed'', i.e. each operation always produces another relation)
- RA is not used as a query language, but usually [SQL is translated to it](Translating_SQL_to_Relational_Algebra) in RDBMS


## Relational Algebra Operators
Operations of traditional RA:
- usual set operations (union, intersection, difference)
- operations that remove some parts of the relation
: selections eliminate tuples (rows)
: projections eliminate attributes (columns)
- operations to combine tuples of two relations: Cartesian product, joins, etc
- renaming

Binary
- Union U
- Intersection
- Difference 

Unary
- Projection
- Join

Extended RA
- bags semantic
- duplicate elimination: $d$
- Grouping and aggregation: $\gamma$
- Sorting: $t$


## Traditional RA Operations
### Set-Based Union
$R_1 \cup R_2$

- Both $R_1$ and $R_2$ must have the same schema
- And the result is a relation with the same schema
- The result contains elements that are in $R_1$ or in $R_2$

SQL:
```sql
SELECT * FROM R1
UNION
SELECT * FROM R2
```

Example:

$\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
  a_2 & b_1 \\
\end{array}
\cup
\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
  a_3 & b_3 \\
\end{array}
=
\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
  a_2 & b_1 \\
  a_3 & b_3 \\
\end{array}
$


### Set-Based Difference
$R_1 - R_2$

- Both $R_1$ and $R_2$ must have the same schema
- And the result is a relation with the same schema
- The result contains elements that are in $R_1$ but not in $R_2$


```sql
SELECT * FROM R1
EXCEPT 
SELECT * FROM R2
```


Example: 
- $\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  a_1 & b_1 \\ 
  a_2 & b_1 \\
\end{array}
\cup
\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  a_1 & b_1 \\
  a_3 & b_3 \\
\end{array}
=
\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  a_2 & b_1 \\
\end{array}
$


### Set-Based Intersection
$R_1 \cap R_2$

- Both $R_1$ and $R_2$ must have the same schema
- And the result is a relation with the same schema
- The result contains elements that are in $R_1$ and in $R_2$


SQL 
```sql
SELECT * FROM R1
INTERSECT 
SELECT * FROM R2
```


Example

$\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
  a_2 & b_1 \\
\end{array}
\cup
\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
  a_3 & b_3 \\
\end{array}
=
\begin{array}{ c |  c } |  A & B \\
  \hline
  \hline
  a_1 & b_1 \\ 
\end{array}
$


Can be expressed via [Union](#Set-Based_Union) and [Difference](#Set-Based_Difference)
- $R_1 \cap R_2 = R_1 - (R_1 - R_2)$
- $R_1 \cap R_2 = R_1 \Join R_2$


### Selection
A binary operator 
- Takes a relation $R$
- Outputs all  tuples of $R$ that satisfy a certain condition $\theta$
- Attributes that take part in $\theta$ must be present in the relation $R$

in SQL:
```sql
SELECT ... FROM R WHERE {condition}
```

For example
- $\sigma_\theta(\text{Relation})$
- $\sigma_{A \geqslant 3} \left (
\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array} 
\right) 
= 
\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  3 & 4 \\
\end{array}
$


A condition can be anything
- salary > 40000 (inequality)
- name = "Smith" (equation)
- etc


### Set-Based Projection
$\pi_{A_1, ..., A_n}(R)$ 

A binary operator 
- Takes a relation $R$
- Outputs only specified attributes $A_1, ..., A_n$ of $R$
- All $A_1, ..., A_n$ must be present in $R$

SQL:
```sql
SELECT A1, ..., An FROM R
```

example
- $\pi_{\text{SSN}, \text{name}}(\text{Employee})$


Note that for set-based projection there are no duplicated in the output:
- $\pi_{A, C} \left( 
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 3 & 4 \\ 
  1 & 2 & 3 & 5 \\
  3 & 4 & 5 & 6 \\
  5 & 6 & 3 & 4 \\
\end{array}
\right) = 
\begin{array}{ c |  c} |  A & C \\
  \hline \hline
  1 & 3 \\ 
  3 & 5 \\
  5 & 3 \\
\end{array}$



### Cartesian Product
Sometimes also called "Cross-Product"

$R_1 \times R_2$
- Result of $R_1 \times R_2$ is a new relation 
- in which each tuple in $R_1$ concatenated with each tuple in $R_2$
- i.e. it outputs all possible combinations of tuples
- $R_1$ and $R_2$ must have disjoint schema

SQL 
```sql
SELECT * FROM R1, R2
```

Example:
- $\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array} 
\times 
\begin{array}{ c |  c} |  C & D \\
  \hline \hline
  2 & 6 \\ 
  3 & 7 \\
  4 & 9 \\
\end{array} 
=
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 2 & 6 \\
  1 & 2 & 3 & 7 \\
  1 & 2 & 4 & 9 \\
  3 & 4 & 2 & 6 \\
  3 & 4 & 3 & 7 \\
  3 & 4 & 4 & 9 \\
\end{array}
$


### Natural Join
Or "Equi-Join" 

$R \Join S$
- no requirements for schema for $R$ and $S$
- if they have one or more attributes in common, in the output tuples with same values will be matched
- if they don't have attributes in common - the result is the same as $R \times S$ ([Cartesian Product](#Cartesian_Product))

Example:
- $\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array} 
\Join
\begin{array}{ c |  c} |  B & D \\
  \hline \hline
  2 & 6 \\ 
  3 & 7 \\
  4 & 9 \\
\end{array} 
=
\begin{array}{ c |  c | c} |  A & B & D \\
  \hline \hline
  1 & 2 & 6 \\
  3 & 4 & 9 \\
\end{array}
$
- $\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array} 
\Join 
\begin{array}{ c |  c} |  C & D \\
  \hline \hline
  2 & 6 \\ 
  3 & 7 \\
  4 & 9 \\
\end{array} 
=
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 2 & 6 \\
  1 & 2 & 3 & 7 \\
  1 & 2 & 4 & 9 \\
  3 & 4 & 2 & 6 \\
  3 & 4 & 3 & 7 \\
  3 & 4 & 4 & 9 \\
\end{array}
$

### Theta Join
$R_1 \Join_{\theta} R_2$

- A join that involves some predicate $\theta$ 
- For all combinations of tuples from $R_1 \Join_{\theta} R_2$, a tuple is output if $\theta$ holds for the combination
- essentially is the same as [Cartesian Product](#Cartesian_Product) plus [Selection](#Selection)

Examples
- $R_1 \Join_{\theta} R_2 = \sigma_{\Theta}{R_1 \times R_2}$ 
- $\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array} 
\Join_{B = C}
\begin{array}{ c |  c} |  C & D \\
  \hline \hline
  2 & 6 \\ 
  3 & 7 \\
  4 & 9 \\
\end{array} 
=
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 2 & 6 \\
  3 & 4 & 4 & 9 \\
\end{array}
$


### Anti-Join
$R \AntiJoin S$
- if for a tuple in $R$ there is a match in $S$, we do not output this tuple from $R$
- $R \AntiJoin S \equiv R - (R \Join S)$
- The result is only tuples from $R$ (the resulting schema is also the same as in $R$)


Difference between $R \AntiJoin S$ and $R - S$ ([Difference](#Set-Based_Difference)):
- for Difference $R - S$ both $R$ and $S$ need to have the same schema
- for $R \AntiJoin S$ - any schema
- if $R$ and $S$ have the same schema, then $R \AntiJoin S \equiv R - S$

Example
- $\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
  5 & 6 \\
  6 & 7 \\
\end{array} 
\AntiJoin
\begin{array}{ c |  c | c } |  B & C & D \\
  \hline \hline
  2 & 5 & 6 \\ 
  6 & 4 & 2 \\
\end{array} 
=
\begin{array}{ c |  c } |  A & B \\
  \hline \hline
  3 & 4 \\
  6 & 7 \\
\end{array}
$



### Renaming
$\rho_{\text{prefix}}(R)$
- takes all attributes of $R$ and
- produces a new relation with $\text{prefix.}$ appended to all of them
- so the resulting relation is the same, but with changed schema 

SQL

```sql
SELECT * FROM Relation R
```

Example 
- $\rho_T \left( 
\begin{array}{ c |  c} |  A & B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array}
\right)
= 
\begin{array}{ c |  c} |  T.A & T.B \\
  \hline \hline
  1 & 2 \\ 
  3 & 4 \\
\end{array}$


### Examples
find all hospitals within 5 ms of a school


```sql
SELECT DISTINCT h.name 
FROM Hospital h, School s
WHERE distance(h.location, s.location) < 5
```

$\pi_\text{name} ( \rho_{\text{h}}(\text{Hospital}) \Join_{\text{h.location = s.location}} \rho_{\text{s}}(\text{School}) )$


### Outer Joins
...


### Semi Joins
$R \ltimes S = \pi_{R.*}(R \Join S)$

## Extended RA
- Adds additional operations to Transitional RA 
- Allows Bag semantics for operations

### Sets vs Bags
- ''Set'' of tuples: no duplicates allowed
- ''Bag'' of tuples: there can be duplicates
- In theory set semantics is usually assumed
- But in implementation - bag semantics

Duplicates 
- Practically we don't care about duplicates 
- We remove them only when required (duplicate elimination: $d$)

RA has two semantics: 
- set semantics = traditional RA
- bag semantics = extended RA 

All set-based operations are straightforwardly extended to bags


### Bag-Based Intersection, Difference, Union
Intersection
- If the same tuple occurs twice in one relation, 
- It must also occur twice in the second relation
- Then the result will also contain 2 tuples

Same idea with Difference and Union


### Grouping
$\gamma_{\text{grouping_attribute}, \ \text{func}(A) \ \to \ \text{name}}(R)$
- unary relation that takes $R$ as input 
- first parameter ($\text{grouping_attribute}$) is attribute on which $R$ will be grouped 
- function $\text{func}$ is applied to each group, and the result is written to attribute $\text{name}$
- '''NB''': all other (non-mentioned) attributes are not output to the result|    | |Example
- $\gamma_{A, \ \text{min}(B) \ \to \ D} \left(
\begin{array}{ c |  c | c } |  A & B & C \\
  \hline \hline
  1 & 2 & a \\
  1 & 3 & b \\
  2 & 3 & c \\
  2 & 4 & a \\
  2 & 5 & d \\
\end{array}
\right)
= 
\begin{array}{ c |  c | c } |  A & D \\
  \hline \hline
  1 & 2 \\
  2 & 3 \\
\end{array}
$



### Projection
- same as [Set-Based Projection](#Set-Based_Projection), but we don't need to eliminate duplicates
- hence it's more efficient 


In Extended RA we also can allow renaming in projection
- $\pi_{A, C \to D} \left( 
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 2 & 6 \\
  1 & 2 & 2 & 7 \\
  1 & 2 & 2 & 9 \\
  3 & 4 & 3 & 6 \\
  3 & 4 & 3 & 7 \\
  3 & 4 & 3 & 9 \\
\end{array}
\right) = 
\begin{array}{ c |  c} |  A & D \\
  \hline \hline
  1 & 2 \\
  1 & 2 \\
  1 & 2 \\
  3 & 3 \\
  3 & 3 \\
  3 & 3 \\
\end{array}
$ (bag semantics)
- $\pi_{A, C \to D} \left( 
\begin{array}{ c |  c | c | c} |  A & B & C & D \\
  \hline \hline
  1 & 2 & 2 & 6 \\
  1 & 2 & 2 & 7 \\
  1 & 2 & 2 & 9 \\
  3 & 4 & 3 & 6 \\
  3 & 4 & 3 & 7 \\
  3 & 4 & 3 & 9 \\
\end{array}
\right) = 
\begin{array}{ c |  c} |  A & D \\
  \hline \hline
  1 & 2 \\
  3 & 3 \\
\end{array}
$ (set semantics)
- $C$ is renamed to $D$

## Translating SQL to RA
{{ Main |  Translating SQL to Relational Algebra}} |


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
- Database Systems: The Complete Book (2nd edition) by H. Garcia-Molina, J. D. Ullman, and J. Widom


[Category:Relational Databases](Category_Relational_Databases)