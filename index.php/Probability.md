---
layout: default
permalink: /index.php/Probability
tags:
- probability
title: Probability
---
## Events and Trials

An *event* is called *random* if, under a certain set of conditions $S$, it may or may not occur.

An event is the result of a *trial*.

Example
- A shooter fires at a target. The shot is a trial. Hitting or missing is an event.



Events are *mutually exclusive* if the occurrence of one of them precludes the occurrence of the others in the same trial.

Example
- A ball is drawn from a box. "A red ball is drawn" and "A blue ball is drawn" are mutually exclusive events;
- Getting heads and tails are mutually exclusive events.


Several events form a *complete group* if at least one of these events will occur as a result of a trial. A complete group of events is denoted by $\Omega$.

If the events forming a complete group are pairwise mutually exclusive, then only one of them can occur.

Example
- Heads and tails form a complete group of events


Two events are called *complementary* if they are the only two possible events forming a complete group. The event complementary to event $A$ is denoted $\bar{A}$.


Two events are called *compatible* if the occurrence of one does not preclude the occurrence of the other in the same trial.

Example
- A die is thrown. Event $A$ is rolling 4, and event $B$ is rolling an even number. Events $A$ and $B$ are compatible.

## Classical Definition of Probability

*Probability* is a number characterizing the degree of likelihood of an event occurring.

Each possible outcome of a trial is an *elementary outcome*.

*The probability of event $A$* is the ratio of the number of elementary outcomes favorable to event $A$ to the total number of outcomes, denoted $P(A)$.

$P(A) = \frac{m}{n}$, where $m$ is the number of favorable outcomes, $n$ is the total number of outcomes.


*Example*

- All possible elementary outcomes
:* $\omega_1$ - white ball
:* $\omega_2$ - white ball
:* $\omega_3$ - black ball

- Events
  $A$ - a white ball is drawn
  $B$ - a black ball is drawn

- Probabilities
  $P(A) = \frac{2}{3}$
  $P(B) = \frac{1}{3}$

### Properties of Probability

1. . Probability of a certain event $A$: $P(A) = 1$
1. . Probability of an impossible event $A$: $P(A) = 0$
1. . Probability of a random event $A$: $0 < P(A) < 1$

Thus, $0 \leqslant p \leqslant 1$


## Statistical Definition of Probability

The classical definition of probability assumes a finite number of elementary outcomes. In practice, however, this number can be infinite. Also, it is often impossible to represent the result as a collection of elementary events.

*Statistical definition of probability* - the relative frequency $\frac{m}{n}$ is taken as the probability.

All properties of probability still hold: $0 \leqslant p = \frac{m}{n} \leqslant 1$


## Principle of Practical Impossibility of Unlikely Events

If a random event has a very small probability, then in practice it can be considered that this event will not occur in a single trial.

*Significance level* - a sufficiently small probability at which an event can be considered impossible.

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vyssh. shk., 2003.
