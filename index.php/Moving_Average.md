---
layout: default
permalink: /index.php/Moving_Average
tags:
- statistics
title: Moving Average
---

## Moving Average

Moving Average

A moving average is used when you want to get a general picture of the trends contained in a data set. The data set of concern is typically a so-called "time series", i.e a set of observations ordered in time. Given such a data set X, with individual data points x_{i}, a 2n+1 point moving average is defined as \bar{x_{i}}=\frac{1}{2n+1}\sum_{k=i-n}^{i+n}x_{k}, and is thus given by taking the average of the 2n points around x_{i}. Doing this on all data points in the set (except the points too close to the edges) generates a new time series that is somewhat smoothed, revealing only the general tendencies of the first time series.

The moving average for many time-based observations is often lagged. That is, we take the 10 -day moving average by looking at the average of the last 10 days. We can make this more exciting (who knew statistics was exciting?) by considering different weights on the 10 days. Perhaps the most recent day should be the most important in our estimate and the value from 10 days ago would be the least important. As long as we have a set of weights that sums to 1, this is an acceptable moving-average. Sometimes the weights are chosen along an exponential curve to make the exponential moving-average.

http://en.wikibooks.org/wiki/Statistics/Summary/Averages/Moving_Average
