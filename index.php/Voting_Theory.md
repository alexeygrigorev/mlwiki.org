---
title: "Voting Theory"
layout: default
permalink: /index.php/Voting_Theory
---

# Voting Theory

## Voting Theory
Voting Theory studies how to take individual rankings of voters and aggregate them to form the global ranking.

Examples:
- Votes for a president of a company/country, etc. All voters communicate their results and based on that the president is chosen
- Search engines: there are many results, how to show them? 


## Notation and Relations
- let $A = \{a, b, c, ...\}$ be the set of candidates
- there are $N$ voters 
- each voter can express his preference on the basis of a ''total order''
  - i.e. he has to rank all the candidates 

For this notation we define the following relations ([Voting Theory Relations](Voting_Theory_Relations))
- Weak and Strong Preference
- Indifference


## Voting Mechanisms and Principles
A ''voting mechanism'' (or ''voting procedure'' or ''voting method'') takes a collection of votes (individual preferences of the candidates from set $A$) and forms the global ranking. Usually it choses a single candidate from the set $A$.

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/de/vt/voting-mechanism.png" alt="Image">

There are several voting procedures:
- [Plurality Voting](Plurality_Voting)
- [Two-Round Voting](Two-Round_Voting)
- [Borda's Rule](Borda's_Rule)
- [Condorcet's Rule](Condorcet's_Rule)


### Criteria
How to characterize "good" voting methods?

There are several criteria 
- [Monotonicity](Monotonicity)
- [Independence to Third Alternatives](Independence_to_Third_Alternatives)
- [Condorcet Fairness Criterion](Condorcet's_Rule#Fairness)
- Solution Existence 
- [Separability](Separability)


|    |  [PV](Plurality_Voting)  |  [2PV](Two-Round_Voting)  |  [Borda](Borda's_Rule)  |  [Cond.](Condorcet's_Rule)  |   [Monotonicity](Monotonicity)  |  [{{yes}}](Plurality_Voting#Monotonicity) ||  [{{no}}](Two-Round_Voting#Monotonicity)  ||  [{{yes}}](Borda's_Rule#Monotonicity) ||  [{{no}}](Condorcet's_Rule#Monotonicity) ||   Solution Existence  |  {{yes}}  |  {{yes}}  |  {{yes}}  |  [{{no}}](Condorcet's_Rule#Condorcet_Paradox) ||   [Manipulation](Independence_to_Third_Alternatives)  |  [{{no}}](Plurality_Voting#Independence_to_Third_Alternatives) ||  [{{no}}](Two-Round_Voting#Independence_to_Third_Alternatives)  ||  [{{no}}](Borda's_Rule#Independence_to_Third_Alternatives)  ||  [{{no}}](Condorcet's_Rule#Independence_to_Third_Alternatives) ||   [Separability](Separability)  |  [{{yes}}](Plurality_Voting#Separability) ||  [{{no}}](Two-Round_Voting#Separability)  ||  [{{yes}}](Borda's_Rule#Separability) ||  [{{yes}}](Condorcet's_Rule#Separability) ||   [Condorcet Fairness](Condorcet's_Rule#Fairness)  |  {{no}}  ||  {{no}}  ||  [{{no}}](Borda's_Rule#Condorcet_Fairness)  ||  {{yes}} |

Other principles:
- [Unanimity](Unanimity)


## Theorems
- [May's Theorem](May's_Theorem)
- [Arrow's Impossibility Theorem](Arrow's_Impossibility_Theorem)


## Examples and Exercises
- [Voting Theory Exercises](Voting_Theory_Exercises)
- [Voting Theory Examples](Voting_Theory_Examples)


## Misc.
- [Banzhaf Power Index](Banzhaf_Power_Index) - shows how strong a party is
- [Parliamentary Allocation](Parliamentary_Allocation) - how to allocate seats between parties in a parliament


## Links
- Mathematics of Voting - slides [http://www.ms.uky.edu/~lee/ma111fa09/slides01.pdf] 
- Criteria [http://www.ctl.ua.edu/math103/voting/whatdowe.htm]
- EC228 Voting Theory Lecture Notes [http://www2.warwick.ac.uk/fac/soc/economics/current/modules/ec228/details/lecturenotes/lecturenotesbook.pdf]
- Social Choice Theory and Multicriteria Decision Aiding [http://www-desir.lip6.fr/publications/pub_1389_1_BouyssouMarchantPerny_soc_choice.pdf]
- Book: Voting, Arbitration, and Fair Division [http://xaravve.trentu.ca/pivato/Teaching/voting.pdf]
- Methods vs Voting Criteria [http://en.wikipedia.org/wiki/Voting_system_criterion]

## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- The mathematics of voting and elections: Paradox, deception, and chaos [http://xaravve.trentu.ca/pivato/Teaching/votingslides.pdf]

[Category:Voting Theory](Category_Voting_Theory)