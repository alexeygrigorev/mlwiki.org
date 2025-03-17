---
title: "Conjunctive Query"
layout: default
permalink: /index.php/Conjunctive_Query
---

# Conjunctive Query

## Conjunctive Query
A ''Conjunctive Query'' (CQ) is
- a [First Order Logic](First_Order_Logic) expression without negations and disjunctions


A CQ is an expression of the following form:

$\underbrace{Q(x_1, ..., x_n)}_{\text{head}} \leftarrow 
\underbrace{R(a_1, ..., a_m), ..., S(c_1, ..., c_k)}_{\text{body}}$
- it consists of two parts: head and body
- $V = (a_1, ..., a_m, ..., c_1, ..., c_k)$ - variables and constants from the body
- $X = (x_1, ..., x_n)$ is a set of variables from the head
  - $X \subseteq V$
  - the variables from $X$ are called ''distinguished variables'' (also ''free'' or ''placeholder'' variables)
- $Y = V - X$  - variables from the body which aren't in the head
  - $Y \subseteq V$
  - variables from $Y$ are called ''existential variables'' (also ''bound'' variables)
- note that the head doesn't necessarily have to contain only variables, it might as well contain constants
  - these constants will be returned in the results



$R(a_1, ..., a_m)$ is called an ''atom'' 
- if an atom does not contain any variables, only constants, it's a ''fact''
- so we can view a database as a set of facts 


Alternative vector form:
- $Q( \vec{x} ) \leftarrow A_1(\vec{u}_1), \ ..., \ A_k(\vec{u}_k)$


### Example
Suppose we have the following database

$
R \\
\begin{array}  \hline
  1 & 2 \\
  2 & 3 \\
  2 & 5 \\
  6 & 7 \\
  7 & 5 \\
  5 & 5 \\
  \hline
\end{array}
$
$
S \\
\begin{array}  \hline
  2 \\
  7 \\
  \hline
\end{array}
$

the query $Q(x, y) \leftarrow R(x, y), R(y, 5), S(y)$ wants to retrieve all pairs $(x, y)$ s.t.
- $(x, y)$ occurs in $R$
- $y$ then occurs in $R$ together with 5
- and that $y$ occurs as a value in $S$


### Substitution
'''def''': a ''substitution'' $f$ of $Q$ into database $D$ is 
: a function that maps all variables from $Q$ to constants from $D$

'''def''': a substitution $f$ of $Q$ into a database $D$ is a ''matching'' if
: $f(\text{body}) \subseteq D$, i.e. if we evaluate $f$ on the body of the query $Q$, we will get a subset of $D$
: so when we apply $f(\text{head})$ we get a tuple that is a part of the result of evaluating $Q$ on $D$

Then the result of a conjunctive query can be shown as:
- $Q(D) \leftarrow \{ f(\text{head}) |  f \text{ is a matching of $Q$ to $D$ } \}$ |

Let's consider the previous example: $Q(x, y) \leftarrow \underbrace{R(x, y)}_{(1)}, \underbrace{R(y, 5)}_{(2)}, \underbrace{S(y)}_{(3)}$ for the same database

Example with matching
1. $(1)$ gets a tuple form $R$
  - say it's (1, 2)
  - so it assigns $x \mapsto 1, y \mapsto 2$
1. : so our substitution so far is $f: x \mapsto 1, y \mapsto 2$
1. $(2)$ looks for a tuple in $R$ with $y = 2$ 
  - because we established the matching $f$ with $y \mapsto 2$
  - second value of this tuple must be a constant 5
  - we find such tuple: it's (2, 5)
  - nothing gets assigned at this step 
1. $(3)$ looks for a value in $S$ with $y = 2$
  - same reason: we have $y \mapsto 2$
  - it finds a fact $S(2)$ in the database
1. so it returns a matching pair (1, 2)
  - we say there is a matching (1, 2) in the database $D$


Example without matching
1. $(1)$ we try another tuple from $R$, say (7, 5)
  - we assign $x \mapsto 7, y \mapsto 5$
1. $(2)$ now we try to find a tuple ($y$, 5) = (5, 5) in $R$
  - no such tuple
1. therefor (7, 5) is not a matching and will not be returned by $Q$


So this way we try all values of our database table and return only matching ones 
- for this particular example the query returns two tuples: (1, 2) and (6, 7)
- i.e. $Q(D) = \{ (1, 2), (6, 7) \}$


### Translation
[First Order Logic](First_Order_Logic)
- CQs can be translated to [First Order Logic](First_Order_Logic) expressions
- for query $q(x_1, ..., x_n) = A_1(...), \ ..., \ A_n(...)$
- FOL expressions is $\{ x_1, ..., x_n \ |  \ \exists \ y_1, ..., y_m : A_1(...) \ \land \ ... \ \land \ A_n(...) \}$ |  - $x_1, ..., x_n$ - distinguished variables, and $y_1, ..., y_m$ are existential


[Relational Algebra](Relational_Algebra)
- CQs can be translated to a subset of RA expressions - [Select-Project-Join Expressions](Select-Project-Join_Expressions)
- see [Conjunctive Query/Translation](Conjunctive_Query_Translation)


### Properties
CQs have an interesting property
- The query containment problem is undecidable for SQL and [Relational Algebra](Relational_Algebra) (see [Logical Query Plan Optimization](Logical_Query_Plan_Optimization)), but it is decidable for Conjunctive Queries 
- The decidability of containment is NP-complete problem, but usually CQs are not big, so it is acceptable 

This makes CQs very suitable for [Logical Query Plan Optimization](Logical_Query_Plan_Optimization), namely, for [removing redundant joins](Logical_Query_Plan_Optimization#Removing_Redundant_Joins)



## Containment and Equivalence
### Containment
$Q_1$ ''is contained in'' $Q_2$ (denoted as $Q_1 \subseteq Q_2$) if
- for any database $D$ holds $Q_1(D) \subseteq Q_2(D)$
- i.e. the result of $Q_1$ is always a subset of the result of $Q_2$, no matter what database $D$ they are evaluated on

$Q_1$ ''is equivalent to'' $Q_2$ (denoted as $Q_1 \equiv Q_2$)
- iff $Q_1 \subseteq Q_2 \land Q_2 \subseteq Q_1$

Example 
- $A(x, y) \leftarrow R(x, w), G(w, z), R(z, y)$
- $B(x, w) \leftarrow R(x, w), G(w, w), R(w, y)$
- $B \subseteq A$

To show that we use the definition
- let $D$ be an arbitrary DB and 
- let $t \in B(D)$ (one arbitrary result of $B$ evaluated on $D$)
- there exists a matching $f$ of $B$ into $D$ s.t. $t = (f(x), f(y))$ (by definition of matching)
  - so we need to show that $t = (f(x), f(y)) \in A(D)$
- let $h$ be a substitution:
  - $h: x \mapsto f(x), y \mapsto f(y), w \mapsto f(w), z \mapsto f(w)$ 
- then $h$ is a matching of $A$ into $D$
  - $t = (f(x), f(y)) = (h(x), h(y)) \in A$ 


It is also possible to show that containment is decidable.


### Homomorphism
'''def''': a ''homomorphism'' of $Q_2$ to $Q_1$ is 
- a function $h$ that maps each variable in $Q_2$ to either
  - a variable from $Q_1$ or
  - a constant form $Q_1$
- s.t. 
  - $h(\text{head}_2) = \text{head}_1$
  - $h(\text{body}_2) \subseteq \text{body}_1$
  - i.e. the values returned by queries are always the same, and body of one query is a subset of the other's query body


Examples
- see [Conjunctive Query/Homomorphism](Conjunctive_Query_Homomorphism)


### Containment Theorem
'''Thm''': $Q_1 \subset Q_2 \iff $ there's a homomorphism from $Q_2$ to $Q_1$

Proof of $\Leftarrow$ (if)
- let $h: Q_2 \to Q_1$ be a homomorphism
- let $D$ be a database
- if we fix an arbitrary tuple $t \in Q_1(D)$, we need to prove that $t \in Q_2(D)$
- since $t \in Q_1(D)$ we know that 
  - $t = f(\text{head}_1)$ 
  - with a matching $f$ of $Q_1$ into $D$ 
  - (by semantics of CQs)
- let's consider a composition $f \circ h$ (composition of $f$ with the homomorphism $h$)
  - this is a substitution of $Q_2$ into $D$|   (we fist applied the homomorphism and then the matching - and got the substitution) |  - since $h$ is a homomorphism, $h(\text{body}_2) \subseteq \text{body}_2$ (by def of homomorphism) |  - $\to$ $f(h(\text{body}_2)) \subseteq f(\text{body}_1) \subseteq D$
  - in other words, $f \circ h$ is a matching of $Q_2$ into $D$
- hence 
  - $f(h(\text{body}_2)) \in Q_2(D)$
  - and finally $t = f(\text{head}_1) = f(h(\text{head}_2)) \in Q_2(D)$

Proof of $\Rightarrow$ (only if) 
- suppose that $Q_1 \subseteq Q_2$
- let's consider variables in $Q_1$ as constants
  - we can view $\text{body}_1$ as a mini-database $D_{Q_1}$ 
  - (this database is called a ''canonical database'' of $Q_1$) 
- the identity function is a matching of $Q_1$ to $D_{Q_1}$
  - hence $\text{head}_1 \in Q_1(D_{Q_1})$
- since $Q_1 \subseteq Q_2$ we know that $\text{head}_1 \in Q_2(D_{Q_1})$
  - by construction of our database $D_{Q_1}$
- so there exists a matching $f$ from $Q_2$ to $D_{Q_1}$ s.t.
  - $\text{head}_1 = f(\text{head}_2)$ and
  - $f(\text{body}_2) \subseteq D_{Q_1} = \text{body}_1$
- $f$ is a homomorphism of $Q_2$ to $Q_1$ by the definition (by considering variables again as variables)

$\blacksquare$


From the second part of the proof we may get a way of checking for containment: the Golden Method


### The Golden Method
To decide whether $Q_1 \subseteq Q_2$
- evaluate $Q_2$ on a canonical database $D_{Q_1}$ (which is a body of $Q_1$, see [#Containment Theorem](#Containment_Theorem))
- check if the head of $Q_1$ is in the results 


QueryContainment($Q_1$, $Q_2$)
- input
  - $Q_1(\vec{x}) \leftarrow g_1(\vec{x}_1), ..., g_n(\vec{x}_n)$
  - $Q_2(\vec{y}) \leftarrow h_1(\vec{y}_1), ..., h_m(\vec{y}_m)$
- freeze $Q_1$: construct a canonical database $D_{Q_1} \equiv \{ g_i \big( v( \vec{x}_i ) \big) \}$
  - with $v$ being a matching 
- if $v(\vec{x}) \in Q_2(D_{Q_1})$ return '''yes''', otherwise '''no'''



### Exercise
- [Conjunctive Query/Containment Exercise](Conjunctive_Query_Containment_Exercise)


## Sources
- [Database Systems Architecture (ULB)](Database_Systems_Architecture_(ULB))
- Database Systems Architecture lecture notes #2 by S. Vansummeren [https://dl.dropboxusercontent.com/sh/r0zvy3zaycbevx8/U0XnqCSwGZ/lect2-notes-conjunctive.pdf]
- Web Data Management book [http://webdam.inria.fr/Jorge]


[Category:Relational Databases](Category_Relational_Databases)