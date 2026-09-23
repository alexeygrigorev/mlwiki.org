---
layout: default
permalink: /Data_Snooping
tags:
- statistics
- machine-learning
title: Data Snooping
---

## Data Snooping

- The test results are not reliable if the statements of the hypotheses are suggested by data.
- This is called *data snooping* - So hypotheses should be specified before any data is collected

Summary statistics (source: table 5.27 OpenIntro):

|  | OF | IF | DH | C |
|---|---|---|---|---|
| Sample size ($n_i$) | 120 | 154 | 14 | 39 |
| Sample mean ($\bar{x}_i$) | 0.334 | 0.332 | 0.348 | 0.323 |
| Sample SD ($s_i$) | 0.029 | 0.037 | 0.036 | 0.045 |

http://habrastorage.org/files/05a/241/ce5/05a241ce52204838a53ad13554c3372d.png
(source: fig 5,28)

We see that DH and C look really different. Why don't we just check if $\mu_\text{DH} = \mu_\text{C}$?
the primary issue: we're inspecting the data before doing the check 
this is called [Data Snooping](Data_Snooping) (or Data Fishing)
naturally we'd pick up the groups with largest differences and run the formal test
but it would lead to Type I Errors

it's also called Prosecutor's Fallacy
