---
layout: default
permalink: /Pig
tags:
- hadoop
title: Pig
---
## Pig
Pig Latin is a SQL-like declarative query language that runs on top of [Hadoop](Hadoop)

Pig Latin
- needs [data model](Data_Model) in form of UDF (user defined function)
- first it generated a [query plan](Query_Plan)
- then compiles it into a set of MR jobs
- some [optimizations](Optimization) are applied


## Example
SQL:

```sql
SELECT SUM(s.Sale), c.City 
FROM Sales s, Cities c
WHERE s.AddrId = c.AddrId
GROUP BY City;
```


Pig Latin
```
-- 1
tmp = COGROUP Sales BY AddrId,
              Cities BY AddrId
-- 2 
join = FOREACH tmp GENERATE 
       FLATTEN(Sales), FLATTEN(Cities)
-- 3
grp = GROUP join BY City

-- 4
res = FOREACH grp GENERATE SUM(Sale)
```

in Pig FOREACH $\approx$ [Map](MapReduce#map-function)


## See also
- Hadoop
- [Hive](Hive)

## Links
- http://www.slideshare.net/jayshao/introduction-to-apache-pig
- Official website: http://pig.apache.org/ 
- [Process your data with Apache Pig](http://www.ibm.com/developerworks/linux/library/l-apachepigdataquery/) (in Russian)

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_%28coursera%29)
