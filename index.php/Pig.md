---
layout: default
permalink: /index.php/Pig
tags:
- hadoop
title: Pig
---
## Pig
Pig Latin is a SQL-like declarative query language that runs on top of [Hadoop](Hadoop)

Pig Latin
- needs data model in form of UDF (user defined function)
- first it generated a query plan
- then compiles it into a set of MR jobs
- some optimizations are applied


## Example
SQL:

```sql
SELECT SUM(s.Sale), c.City 
FROM Sales s, Cities c
WHERE s.AddrId = c.AddrId
GROUP BY City;
```


Pig Latin
```text only
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

in Pig FOREACH $\approx$ [Map](MapReduce#Map_Function)


## See also
- [Hadoop](Hadoop)
- [Hive](Hive)

## Links
- http://www.slideshare.net/jayshao/introduction-to-apache-pig
- Official website: http://pig.apache.org/ 
- Process your data with Apache Pig [and [http://www.ibm.com/developerworks/ru/library/l-apachepigdataquery/](http://www.ibm.com/developerworks/linux/library/l-apachepigdataquery/]) (на русском)

## Sources
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))
