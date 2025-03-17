---
title: "Feature Filtering"
layout: default
permalink: /index.php/Feature_Filtering
---

# Feature Filtering

{{ stub }}

## Feature Filtering
Given $D$ features $f_1, \ ... \ , f_D$ and outcome $Y$
- rank these features according to some criterion of "importance"
- keep only important ones

Important? 
- top $d$
- ones with scores above some threshold


Criteria of usefulness :
- [Information Theory](Information_Theory) measures ([Shannon's Information Measures](Shannon's_Information_Measures)))
- [Entropy-Based Ranking](Entropy-Based_Ranking)
- [Information Gain](Information_Gain)
- [Mutual Information](Mutual_Information)
- [Odds Ratio](Odds_Ratio)
- [Chi-Squared Ranking](Chi-Squared_Ranking)


- All these functions capture the intuition that the best features for predicting the outcome $Y$ is ones that distribute very differently given values of $Y$
- Usually these functions measure (in)dependence between $f_i$ and $Y$ 
- the more dependent the feature is, the better it is for classification


E.g. $\chi^2$ measures how the results of an observation differs from the result expected according to the null hypothesis 
- lower values indicate less dependency 
- so for $\chi^2$ we want to take biggest values 


## Sources
- Sebastiani, Fabrizio. "Machine learning in automated text categorization." (2002). [http://arxiv.org/pdf/cs/0110053.pdf]


[Category:Dimensionality Reduction](Category_Dimensionality_Reduction)
[Category:Feature Filtering](Category_Feature_Filtering)