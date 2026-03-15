---
layout: default
permalink: /index.php/Poisson_Process
tags:
- probability
title: Poisson Process
---
## Poisson Process
Consider events occurring at random moments in time.

An event stream (or flow of events) is a sequence of events that occur at random moments in time.

Examples:
- calls to a telephone exchange,
- arrivals of aircraft at an airport,
- arrivals of customers at a business,
- a sequence of component failures.


## Properties of a Simple (Poisson) Stream
A simple stream is a stream that possesses the following properties:

### Stationarity
The probability of $k$ events occurring in any interval depends only on $k$ and the length $t$ of the interval, and does not depend on the starting point. The time intervals are assumed to be non-overlapping.

### Lack of Aftereffect (Memorylessness)
The probability of $k$ events occurring in any time interval does not depend on whether events occurred before that interval or not. That is, the history of the stream does not affect the probability of an event occurring in the near future.

### Orderliness
In an infinitesimally small time interval, at most one event can occur.


If a stream represents the sum of a very large number of independent events, each of which has a negligible influence on the total sum, then the aggregate stream (provided it is orderly) is close to a simple (Poisson) stream.


## Stream Intensity
The intensity $\lambda$ of a stream is the average number of events occurring per unit of time.

If $\lambda$ is known, then the probability of $k$ events in a simple stream is given by the [Poisson formula](Poisson_Limit_Theorem):

$P_t(k) = (\lambda t)^k \frac{e^{-\lambda t}}{k!}$
This formula satisfies all three properties.

## Example
During one minute, on average 2 calls arrive at a telephone exchange. Find the probability that over 5 minutes:
1. exactly 2 calls arrive
1. fewer than 2 calls arrive
1. at least 2 calls arrive



- Since the event stream is simple, $\lambda = 2, t = 5, k = 2$
- $P_t(k) = (\lambda t)^k \frac{e^{-\lambda t}}{k!}$
- 1. exactly 2 calls arrive in 5 minutes
  $P_5(2) = 10^2 \frac{e^{-10}}{2!} \approx 0.00225$
- 2. fewer than 2 calls arrive
  - by the addition theorem,
  $P_5(k < 2) = P_5(0) + P_5(1) = e^{-10} + \frac{10 e^{-10}}{1!} \approx 0.000495$
- 3. at least 2 events occur
  - the complementary event is "fewer than 2 events occurred"
  $P_5(k \geqslant 2) = 1 - P_5(k < 2) \approx 0.999505$


## See also
- [Poisson Limit Theorem](Poisson_Limit_Theorem)
- [Poisson Distribution](Poisson_Distribution)

## Sources
- Gmurman V.E., Probability Theory and Mathematical Statistics -- 9th edition. Moscow: Vysshaya Shkola, 2003.
