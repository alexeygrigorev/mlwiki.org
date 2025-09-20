---
layout: default
permalink: /index.php/Confidence_Intervals_and_Statistical_Tests
tags:
- statistics
title: Confidence Intervals and Statistical Tests
---
## Relationship between Confidence Intervals and Tests
How to connect [Hypothesis Testing](Statistical_Tests_of_Significance) and [Confidence Intervals](Confidence_Intervals)? 

## Example
- Remember [the beer cap flipping experiment](Confidence_Intervals#Beer_Cap_Flipping)? 
- We test: $H_0: p = 0.5, H_A: p \neq 0.5$ (2-sided)
Observations:
- $n = 1000$
- $\hat{p} = 0.576$
- under $H_0$, is difference $|  \hat{p} - p | = | \hat{p} - 0.5 | = 0.076$ too large to reject H_0? |

We calculate $p$-value
: $P(| \hat{p} - 0.5| \geqslant 0.076) \approx P(|N(0, 1)| \geqslant 4.81 ) \approx 1 / 663000 \leqslant 0.05$ |
And reject the $H_0$ because the $p$-value is small


Now let's calculate 95% CI:
- $\hat{p} \pm 1.96 \sqrt{p(1-p)/n} = [0.532, 0.620]$
- The CI misses 0.5 
- and this is '''not''' a coincidence|    | |
## General Test
Suppose we have a test of the following form
- $H_0: \mu = \mu_0, H_A: \mu \neq \mu_0$
- Our observations are: $n$, $\bar{X}$, $s$, 
- We're interested in the difference between observed mean and the true mean:
: $\Delta = | \bar{X} - \mu_0|$ |
So we reject $H_0$ if
- $P(| \bar{X} - \mu_0| \geqslant \Delta) \leqslant \alpha$ |- $P\left(\left|  \cfrac{\bar{X} - \mu_0}{\sqrt{s^2 / n}} \right| \geqslant \cfrac{\Delta}{\sqrt{s^2 / n}} \right) = P\left(\left| t_{n - 1} \right| \geqslant \cfrac{\Delta}{\sqrt{s^2 / n}} \right) \leqslant \alpha$ |

This will only happen if
- $\cfrac{\Delta}{\sqrt{s^2 / n}} \geqslant T_{\alpha/2, n-1}$
- where $T_{\alpha/2, n-1}$ is ''critical value'' s.t.
: $P(| t_{n-1}| \geqslant T_{\alpha/2, n-1} ) = \alpha$ |

And $(1 - \alpha)$ [Confidence Intervals](Confidence_Intervals) for $\mu$ is
- $\bar{X} \pm T_{\alpha/2, n-1} \cdot \sqrt{s^2 / n}$
- This misses $\mu_0$ when 
: $| \bar{X} - \mu_0 | \geqslant T_{\alpha/2, n-1} \cdot \sqrt{s^2 / n}$ |

So these are equivalent:
: Reject $H_0$ when C.I. misses $\mu_0$

## See also
- [Confidence Intervals](Confidence_Intervals)
- [Statistical Tests of Significance](Statistical_Tests_of_Significance)

## Sources
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
