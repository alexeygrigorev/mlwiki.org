---
layout: default
permalink: /index.php/Arrow's_Impossibility_Theorem
tags:
- voting-theory
title: Arrow's Impossibility Theorem
---
## Arrow's Impossibility Theorem
Arrow's Impossibility Theorem is a [Voting Theory](Voting_Theory) theorem (sometimes called ''Arrow's Paradox'')

In contrast to [May's Theorem](May's_Theorem), in this theorem we assume 3 (and more) candidates, not 2:
- $A = \{x, y, z\}$


## [Voting Theory Relations](Voting_Theory_Relations)
We define the following [relations](Voting_Theory_Relations):

$P$ the preference relation 
- $P_i$ is a individual preference of voter $i$
  - $x \ P_1 \ y$  means that voter 1 prefers $x$ to $y$
- $P$ is the global aggregated preference

$I$ is the indifference relation
- $I_i$ is an individual indifference of voter $i$
- $I_i$ is symmetric: $a \ I_1 \ b \iff b \ I_1 \ a$ 

$S$ is the "at least as good as" relation
- $S \equiv (P \lor I)$
- $x \ S \ y \iff x \ (P \lor I) \ y \Rightarrow {\color{grey}{(1)}} \ x \ P \ y  \lor {\color{grey}{(2)}} \ x \ I \ y \lor {\color{grey}{(3)}} \ y \ P \ x$


; We can express $P$ and $I$ only via $S$
1. $x \ P \ y \equiv [x \ S \ y] \land [y \ \overline{S} \ x]$
1. $x \ I \ y \equiv [x \ S \ y] \land [y \ S \ x]$


## Axioms
; Axiom 1: ''Completeness''
: $\forall x, y \in A:$ either  $x \ S \ y$ or $y \ S \ x$

; Axiom 2: ''Consistency'' (or ''Transitivity'')
: $\forall x, y, z \in A: x \ S \ y \land y \ S \ z \Rightarrow x \ S \ z$


## Lemmas
$\forall x, y, z \in A:$
- (1) $x \ S \ x$ (''reflectivity'')
- (2) $x \ P \ y \Rightarrow x \ S \ y$
- (3) $x \ P y \land y \ P \ z \Rightarrow x \ P \ z$ (''transitivity'' for $P$)
- (4) $x \ I \ y, y \ I \ z \Rightarrow x \ I \ z$ (?)
- (5) either $x \ S \ y$ or $y \ P \ x$
- (6) $x \ P \ y \land y \ S \ z \Rightarrow x \ P \ z$


### Lemma 3: Transitivity for $P$
We want to show that $\forall x, y \in A: x \ P \ y \land y \ P \ z \Rightarrow x \ P \ z$

By Axiom 2 we have transitivity for $S$:
- $x \ S \ y \land y \ S \ z \Rightarrow x \ S \ z$

$x \ S \ z \equiv x \ (P \lor I) \ y \equiv \underbrace{[x \ P \ y]}_\text{(1)} \lor \underbrace{[x \ I \ z]}_\text{(2)}$
- (1) this is what we want to show
- (2) want to show that assuming it leads to contradiction and therefore the only possible outcome is (1)


Assuming (2): $x \ I \ z$
- by Symmetry $x \ I \ z \iff z \ I \ x$
- $z \ I \ x \Rightarrow [z \ S \ x] \land [x \ S \ z] \Rightarrow z \ S \ x$

$z \ S \ x \land x \ S \ y \Rightarrow z \ S \ y$ (by transitivity of $S$)
- since $S$ is less strict than $P$ we have:
: $x \ P \ y \Rightarrow x \ S \ y$ and $y \ P \ z \Rightarrow y \ S \ z$
- $z \ S \ y$ contradicts with $y \ P \ z$
: $z \ S \ y$ means one of the following: $z \ P \ y$ or $z \ I \ y$, and neither of them are true

Contradiction. $\square$


### Lemma 5
$\forall x, y \in A: x \ S \ y \lor y \ P \ x$

Let's prove that by contradiction:
- assume the opposite: $\exists x, y \in A: \overline{ x \ S \ y \lor y \ P \ x }$
- $\overline{ x \ S \ y \lor y \ P \ x } \equiv  \overline{ x \ S \ y} \land  \overline{ y \ P \ x } \equiv y \ P \ x  \land y \ \overline{S} \ x$
- this is clearly a contradiction: they both can never be true at the same time


Another way to show that is by completeness of $P$ and $S$


### Lemma 6
$\forall x, y \in A: x \ P \ y \land y \ S \ z \Rightarrow x \ P \ z$

- $x \ P \ y \equiv [x \ S \ y] \land [y \ \overline{S} \ x]$ just rewriting $P$ with $S$ 
- $[x \ S \ y] \land [y \ S \ z] \Rightarrow x \ S \ z$ by transitivity
- $x \ S \ z \iff \underbrace{ x \ P \ z}_\text{(1)} \lor \underbrace{x \ I \ z}_\text{(2)}$
- if (2) is false then (1) must be true for the Lemma to hold

Assume $x \ I \ z$
- $x \ I \ z \equiv \underbrace{x \ S \ z}_\text{true} \land z \ S \ x$
- consider the initial hypothesis $y \ S \ z$ and $z \ S \ x$:
  - by transitivity  $y \ S \ z \land z \ S \ x \Rightarrow y \ S \ x$
- but $y \ S \ x$ contractions with $a \ P \ y$
- therefore $x \ P \ y$  (1) must be true

$\square$



## Conditions
The ''social welfare function'' $H$ it takes two individual rankings and produces the global (social) choice:
: $H(R_1, R_2) \to R$

$H$ must satisfy the following conditions:
- Universality
- [Monotonicity](Monotonicity)
- [Independence to Third Alternatives](Independence_to_Third_Alternatives)
- Non-Imposition
- No Dictatorship


### Condition 1: Universality
$H$ is defined for every pair $R_1$ and $R_2$
- i.e. for each pair there should exist a solution
- we want to avoid the [Condorcet Problem](Condorcet's_Rule#Condorcet's_Paradox) - a cycle

This condition is also called ''Unrestricted Domain''


### Condition 2: [Monotonicity](Monotonicity)
Monotonicity is satisfied if
- if an alternative $x$ rises or does not fall in the individual ordering
- and if $x$ was preferred to another alternative $y$ before the change in the individual orderings
- then $x$ should still be preferred to $y$ in the global ordering


### Condition 3: [Independence to Third Alternatives](Independence_to_Third_Alternatives)
Independence to Third Alternatives is satisfied when
- given the set of alternatives $A = \{x, y\}$
- individual preferences over $A$ are not affected by other alternatives $z$ that are not in $A$
- when these alternatives $z$ are also considered in $A' = A \cup {z}$ it should not affect the ordering between alternatives from $A$  


### Condition 4: Non-Imposition
$H$ should not be imposed

$H$ is ''imposed'' if
- for some distinct $x$ and $y$, for rankings $R_1$ and $R_2$: $x \ S \ y$
- $S$ relates to the global ordering obtained from $H$

In other words, 
- $x$ is always as good as $y$ or better in the aggregated ordering
- no matter what $y$ is 

Example of some imposed conditions:
- men preferred to women, 
- one religion is preferred to other,
- etc


### Condition 5: No Dictatorship
$H$ should not be dictatorial

$H$ is dictatorial if 
- $\exists$ individual $i$ s.t. $\forall x, y \in A: x \ P_i \ y \Rightarrow x \ P \ y$
- no matter what is the individual ranking $R_i$
- such individual $i$ is called ''the dictator''

In other words:
- for any alternatives, the choice of the dictator determines the outcome


## Theorem
; Arrow's Impossibility Theorem
: All five conditions cannot be satisfied simultaneously. 


## Consequences
### Consequence 1: [Unanimity](Unanimity)
Unanimity is satisfied ($N = 2$) if
- $x \ P_1 \ y$ and $x \ P_2 \ y$ then $x \ P \ y$
- or $x$ is globally preferred to $y$ if both voters vote for $x$

It follows from Non-Imposition and Monotonicity

Non-Imposition
- $H$ is imposed if $\exists x, y: \forall R_1, R_2: x \ S \ y$
- thus $H$ is not imposed if $\exists R_1, R_2: x \ P \ y$

From $R_1$ and $R_2$ we can build two rankings
- $R_1 \to R'_1$ and $R_2 \to R'_2$
- we assume only that $x$ improves his positions in these rankings: 
- $x$ has the same or better position in $R' = H(R'_1, R'_2)$ 
- by [Monotonicity](Monotonicity) if he was preferred to $y$ in $R$, he's still preferred to $y$ in $R'$

?

For example: 
- $R: y < x < z \ \to \ R': x < y < z$
- $x$ improved his positions 


### Consequence 2: Dictatorship
We have a dictator if:
- $\exists x, y \in A: x \ P \ y \land x \ P_1 \ y \land y \ P_2 \ x \Rightarrow [ x \ P_1 \ y \to x \ P \ y ]$
- if we have two opposite points of view of voters $a_1$ ($x$ is better) and $a_2$ ($y$ is better) and the opinion of voter $a_1$ becomes the global opinion
- then no matter how $a_2$ votes, the opinion of $a_1$ determines the global preference 

Let's consider two rankings:
- $R_1: x < \ ...$ one where $x$ is on the first position
- $R_2$ any ranking with $x$ at some position - $R_2: \ ... < x < \ ...$ 

We can build two new rankings $R'_1$ and $R'_2$ from them:
- $R'_1 \equiv R_1$: also with $x$ on the first position
- $R'_2: \ ... < x$: by taking $R_2$ and moving $x$ to the last position
- this way we constructed two rankings with completely opposite points of view 
  - (this corresponds to $x \ P_1 \ y \land y \ P_2 \ x$)
- $H(R'_1, R'_2) = R'$, and by our hypothesis $x \ P \ y$ in $R'$

Now let's return from $R'_2$ to $R_2$:
- $x$ improves his positions by going from $R'_2$ to $R_2$:
- by [Monotonicity](Monotonicity) he should remain the winner 

I.e. no matter what is the ranking $R_2$, $R_1$ always determines the outcome
- or $x \ P_1 \ y \to x \ P \ y$

$\square$


### Consequence 3: Indifference
In a strong conflict the only possible outcome is indifference:
- if $x \ P_1 \ y \land y \ P_2 \ x \Rightarrow x \ I \ y$
- otherwise we have dictatorship

Assume $x \ I \ y$ is false. It means:
- ether $x \ P \ y$
- or $y \ P \ x$ 

Assume $x \ P \ y$:
- $x \ P_1 \ y \land y \ P_2 \ x \Rightarrow x \ P \ y$
- it means that the voter 1 is dictator 

Same for $y \ P \ x$:
- it would mean the the voter 2 is dictator


### Consequence of Consequences
Suppose we have two ratings:
- $R_1: {\color{blue}{x < y}} < z$
- $R_2: z < {\color{blue}{x < y}}$
- i.e. both candidates agree that $x \ P \ y$

But there's a strong opposition when it comes to $z$:
- '''(1)''' $x$ vs $z$
  - $x \ P_1 z \land z \ P_2 \ x$
  - the only possible outcome in this case is indifference (by Consequence 3)
  - $x \ I \ z$
- '''(2)''' $y$ vs $z$
  - $y \ P_1 z \land z \ P_2 \ y \Rightarrow y \ I \ z$


by '''(1)''' + '''(2)''':
- $y \ I \ z  \equiv z \ I \ y $
- $x \ I \ z \land z \ I \ y \Rightarrow x \ I \ y$ by transitivity of $I$ (Lemma 4)
- but it contradicts with $x \ P \ y$

Therefore, these 5 conditions cannot be satisfied simultaneously.


## Solution
How to overcome this limitation? 
- Relax 1-st condition: don't need to always return the entire rankings, it's enough to return just one candidate 


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- EC228 Voting Theory Lecture Notes [http://www2.warwick.ac.uk/fac/soc/economics/current/modules/ec228/details/lecturenotes/lecturenotesbook.pdf]
