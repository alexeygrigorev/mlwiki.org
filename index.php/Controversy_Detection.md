---
layout: default
permalink: /index.php/Controversy_Detection
tags:
- nlp
- data-mining
title: Controversy Detection
---

## Controversy Detection

Cotroversy Detection

Controversy as defined in the previous chapter is a state of prolonged public dispute or debate, usually concerning a matter of conflicting opinion or point of view.

Examples
- "global warming is a hoax"
- political debates, economic issues
- same-sex marriage
- healthcare
- 

Results: not trustworthy information, e.g. "vaccines cause autism", etc

correlation: if a wikipedia page is controversial so is the topic of the page

Features: 
- len of page
- proportion of anonimous edits
- number of reverts 

hierarchy of controversial words and topics: [Awadallah2012, Popescu2010]

sentiment can also be a useful feature for controversy detection 

Approach: 

- map webpage to a wiki article 
- if the wiki article is controversial, so is the webpage

mapping:
- querying the wikipedia api
- take top 10 terms (e.g. most frequent expect stopwords) and then run a commercial search engine on them - and find the wiki page in the results 

Wikipedia scores:

- D - if dispute tags are absent - see Kittur2017, Rad2012. usually added to the "Talk" page, but only a small fraction of pages have them 
- C - predict controversy using wiki page metadata: see Kittur2017, model: Das2013
 * len of the page and its talk page
 * number of editors, number of anonimous editors 
- M - based on the concept of manual reverts and edit wars on wikipedia 
 * based on the reputation of the users involved in the "wars" 

These 3 scores are combined into one. D is omitted because the coverage is too small to have any effect on the model 

Data: http://ciir.cs.umass.edu/download

Papers: 

- Awadallah2012, Harmony and dissonance: organizing the people's voices on political controversies [http://dl.acm.org/citation.cfm?id=2124359&dl=ACM&coll=DL&CFID=685632707&CFTOKEN=42534054]
- Das2013 Manipulation Among the Arbiters of Collective Intelligence: How Wikipedia Administrators Mold Public Opinion [http://www.cse.wustl.edu/~allenlavoie/papers/wiki-cikm.pdf]
- Kittur2017, He says, she says: conflict and coordination in Wikipedia [http://www.kittur.org/files/Kittur_2007_Wikipedia_CHI.pdf]
- Popescu2010, Detecting controversial events from twitter [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.458.1082&rep=rep1&type=pdf]
- Rad2012, Identifying controversial articles in Wikipedia: A comparative study, [http://www.opensym.org/ws2012/p18wikisym2012.pdf]
