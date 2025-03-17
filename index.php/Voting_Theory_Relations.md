---
title: "Voting Theory Relations"
layout: default
permalink: /index.php/Voting_Theory_Relations
---

# Voting Theory Relations

## Voting Theory Relations
The relations that are defined for [Voting Theory](Voting_Theory) principles and methods. Also used in theorems such as [May's Theorem](May's_Theorem) or [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)


### Notation
- let $A = \{ a_1, ..., a_k \}$ be the set of candidates
- let $V = \{ 1, 2, ..., N \}$ be the set of voters; there are $N$ voters 
- each voter can express his preference on the basis of a ''total order''
  - i.e. he has to rank all the candidates
  - $R_j(a_i)$ is the position of candidate $a_i$ in the ranking of voter $j$


Based on this notation let us define the following relations:
- Preference (or Strong Preference)
- Indifference 
- "At least as good as" Relation (or Weak Preference) - the combination of preference and indifference


## Preference Relation
$>$ (or $P$) is the (strong) preference relation, voters use it to express the preference

Example: 
- $A = \{a, b, c, d\}$
- a vote is $b > a > c > d$

It satisfies three axioms:
- ''completeness''
  - for any $x$ and $y$ either $x < y$ or $y < x$
- ''transitivity'' (or ''consistency'')
  - $\forall x, y, z \in A: x > y \land y > z \Rightarrow x > z$
- ''asymmetric''
  - $\forall x, y: (x > y) \Rightarrow \overline{ y > x }$


Notation
- $P_i$ shows the individual preference of voter $i$
  - $x \ P_1 \ y$  means that voter 1 prefers $x$ to $y$
- $P$ shows the global aggregated preference 



## Indifference Relation
$\sim$ or $I$ is the indifference relation, voters use it to express that both candidates are equally good

Properties: 
- indifference is ''symmetric''
  - $x \ I \ y \iff y \ I \ x$
- indifference is not always transitive
  - cups of coffee|   |  - but in some cases is: for instance, in the [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem) it's considered transitive |

Notation
- $I_i$ is an individual indifference of voter $i$
- $I$ is the global indifference  


### At Least As Good As Relation
$\geqslant$ or $S$ - means "at least as good as" - indifferent or better, sometimes referred as ''weak preference''
- $S \equiv (P \lor I)$ or $\geqslant \equiv [< \lor \sim]$
- the opposite of $a \ S \ b$ is $b \ P \ A$:
  - $\overline{a \ S \ b} \equiv (a \ \overline{S} \ b) \equiv (a \ \overline{P \lor I} \ b) \equiv (a \ (\overline{P} \land \overline{I}) \ b) \equiv a \ \overline{P} \ b \equiv b \ P \ a$
  - not preferred and not indifferent


Properties
- for any pair $(x, y), x,y \in A, x \ne y$ 
  - $x \ S \ y \iff [x \ P \ y] \lor [x \ I \ y]  \lor [y \ I \ x]$
  - $x \ S \ y \not \Rightarrow y \ P \ x$|  !! |- ''completeness'' |  - $\forall x, y \in A:$ either  $x \ S \ y$ or $y \ S \ x$
- ''transitivity''  (or ''consistency'')
  - $\forall x, y, z \in A: x \ S y \land y \ S \ z \Rightarrow x \ S \ z$

We can use express Preference and Indifference via this relation:
- $x \ P \ y \equiv [x \ S \ y] \land [y \ \overline{S} \ x]$
- $x \ I \ y \equiv [x \ S \ y] \land [y \ S \ x]$



## Links
- http://en.wikipedia.org/wiki/Pairwise_comparison

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))

[Category:Voting Theory](Category_Voting_Theory)