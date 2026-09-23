---
layout: default
permalink: /Mean
tags:
- statistics
title: Mean
---

## Mean
- [Median](Summary_Statistics) is a measure of the center. 
- But there is another measure - [Mean](Mean) or average value
: $\text{mean} = \cfrac{1}{n} \sum x_i$
: Where $n$ - number of data values, and $x_i$ - each data value.

Robustness
- Mean is not *robust* (susceptibile to [outliers](Outliers)), but median is. 
- *10% trimmed mean* - mean calculated from 10% to 90% of our data, more robust to extreme values

10% trimmed mean in R
<pre class="brush: r">
mean(..., trim=0.1)
</pre>
