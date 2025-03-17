---
title: Plurality Voting
layout: default
permalink: /index.php/Plurality_Voting
---

# Plurality Voting

## Plurality Voting
This a voting mechanism from [Voting Theory](Voting_Theory)

- $A$ - the sets of candidates
- Every voter tells his preferred candidate in the form of personal ranking
- let $S(a)$ define the number of voters that prefer $a$ to all other candidates
- the candidate $a$ that gets the majority of votes (the best $S(a)$ score) gets elected 


### Example
- $a > b > c$ - 11 votes
- $b > a > c$ - 8 votes
- $c > b > a$ - 2 votes

$a$ wins:
- $S(a) = 11, S(b) = 8, S(c) = 2$


## Criteria
Satisfies: 
- [Monotonicity](Monotonicity)
- [Separability](Separability)

Does not satisfy:
- [Independence to Third Alternatives](Independence_to_Third_Alternatives)
- [Condorcet Fairness Criterion](Condorcet's_Rule#Fairness)


### [Monotonicity](Monotonicity)
$R$ some ranking and $S$ are the Plurality Voting scores

Suppose the candidate $a$ improves his positions by one vote
- let $S'$ be the new scores and $R'$ be the new ranking
- let $b$ be the candidate from who $a$ took the vote
- $S'(a) = S(a) + 1, S'(b) = S(b) - 1$
- we don't care about other candidates $c$: $S'(c) = S(c)$


Consider two cases: 
- (a) the candidate $x$ does not become the winner
- (b) the candidate $x$ becomes the winner 

Case (a): 
- $R'(a) \ne 1$: $a$ is not the winner
- then he was not the winner before: $R(a) \ne 1$
- his position didn't become worse nor better: he still looses 

Case (b):
- $R'(a) = 1$: the candidate $a$ is now the winner
- there are two cases:
  - either he was the winner already and took one vote from a loosing candidate - and $a$ still winner (his position didn't become worse)
  - or he took the vote from the winner and became the winner himself - $a$ improved his positions


Therefore, the [Monotonicity](Monotonicity) criterion is satisfied by the Plurality Voting.


### [Separability](Separability)
Suppose we have two regions: $A$ and $B$, $V = A \cup B$
- for $A$ the ranking is $a_1 > ... > a_n$
- for $B$ the ranking is $a_1 > ... > a_n$

Then the scores are:
- for $A$: $S_A(a_1) > ... > S_A(a_n)$
- for $B$: $S_B(a_1) > ... > S_B(a_n)$

And for $V$ they are:
- $S_V(a_1) = S_A(a_1) + S_B(a_1)$
- $S_V(a_2) = S_A(a_2) + S_B(a_2)$
- $...$
- $S_V(a_n) = S_A(a_n) + S_B(a_n)$

Or,
- $S_V(a_1) > ... > S_V(a_n) \Rightarrow$
- for $V$ the ranking is $a_1 > ... > a_n$
- therefore, [Separability](Separability) is satisfied

Note that it will hold for any partition of $V$


### [Independence to Third Alternatives](Independence_to_Third_Alternatives)
There is a counter-example that shows that this property is not satisfied. 

Preferences:
- $4: a {\color{grey}{> b > c}}, S(a) = 4$
- $2: c {\color{grey}{> b > a}}, S(c) = 2$
- $3: b {\color{grey}{> c > a}}, S(b) = 3$
- note that here only the first candidate in ranking is important
- $a$ wins the election

Now assume $c$ withdraws:
- $4: a > b$
- $2 + 3: b > a$
- two extra voters now prefer $b$ because they can no longer vote for $c$ 
- so now $b$ wins
- therefore this method suffers from Manipulation


### [Condorcet Fairness Criterion](Condorcet's_Rule#Fairness)
This property is not satisfied
- see example in [Voting Theory Examples#Example 1: Plurality Voting](Voting_Theory_Examples#Example_1__Plurality_Voting)


## Links
- http://www.ctl.ua.edu/math103/voting/pluralit.htm


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
- Social Choice Theory and Multicriteria Decision Aiding [http://www-desir.lip6.fr/publications/pub_1389_1_BouyssouMarchantPerny_soc_choice.pdf]

[Category:Voting Theory](Category_Voting_Theory)