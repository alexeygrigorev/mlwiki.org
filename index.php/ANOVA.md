---
title: "ANOVA"
layout: default
permalink: /index.php/ANOVA
---

# ANOVA

{{draft}}{{stub}}

## ANOVA
ANOVA is ANalysis Of VAriance
- it's a set of statistical models 
- they are used to analyze differences between group means and their associated procedures
  - e.g. variation among and between groups 


## Types
### [One-Way ANOVA F-Test](One-Way_ANOVA_F-Test)
Goal: compare many means in a single hypothesis 
- instead of doing pairwise [$t$-test](t-tests), do ANOVA
- but you can still perform [$t$-test](t-tests) or [Tukey HSD Test](Tukey_HSD_Test) as post-ANOVA analysis
- also, a good way of checking independence between two variables: numerical and categorical 

Some authors argue that the ANOVA step is in fact unnecessary and we could perform the Tukey HSD test alone. Nevertheless, the ANOVA + Tukey approach is considered standard is most books.


### Not Normal?
If not Normal, use these non-parametric tests
- [Wilcoxon-Mann-Whiney Test](Wilcoxon-Mann-Whiney_Test) if the class variable is binary 
- [Kruskal-Wallis Test](Kruskal-Wallis_Test) for any nominal variable 


## Links
- http://www.marketingdistillery.com/2014/08/10/multiple-abn-tests-in-marketing-with-anova-and-r/
- Book with chapters about ANOVA [http://vassarstats.net/textbook/toc.html]
  - Conceptual Introduction to the Analysis of Variance [http://vassarstats.net/textbook/ch13pt1.html]
  - ONE-way analysis for independent samples [[http://vassarstats.net/textbook/ch14pt2.html](http://vassarstats.net/textbook/ch14pt1.html])
  - The Kruskal-Wallis Test for 3 or More Independent Samples [http://vassarstats.net/textbook/ch14a.html]
- http://www.personality-project.org/r/r.anova.html


## Sources
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- http://en.wikipedia.org/wiki/Analysis_of_variance

[Category:Statistical Tests](Category_Statistical_Tests)
[Category:Statistics](Category_Statistics)