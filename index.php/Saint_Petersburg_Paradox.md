---
layout: default
permalink: /index.php/Saint_Petersburg_Paradox
tags:
- decision-under-risk
- probability
title: Saint Petersburg Paradox
---
## Saint Petersburg Paradox
Consider the following game:
- a "banker" $B$ plays with a "player" $P$
- $P$ must pay some fixed sum to enter the game
- $B$ flips a coin until TAILS appear - then the game stops 
- $B$ pays $2^n$ euro to $P$ if the game stops on $n$th toss

How much a rational should be willing to pay to play the game?
- [Expected Value](Expected_Value) could be a good model to estimate the costs for entering the game 

|   Seq  |  Gain  |  Prob  |  $T$  |  $2^1$  |  $0.5$ ||  $HT$  |  $2^1$  |  $0.5^2$ ||  $HHT$  |  $2^2$  |  $0.5^3$ ||  ...  |  ...  |  ... ||  $\underbrace{H..H}_{n}T$  |  $2^n$  |  $0.5^n$ |
Let's calculate the expected value
- $EV = 2 \cdot \cfrac{1}{2} + 2^2 \cdot \cfrac{1}{2^2} + 2^3 \cdot \cfrac{1}{2^3} + ... = \infty$
- so the expected value is $\infty$ with just 50% chance to win only 2 euro
- clearly this is not good enough to model such situation


## Sources
- [Decision Engineering (ULB)](Decision_Engineering_(ULB))
