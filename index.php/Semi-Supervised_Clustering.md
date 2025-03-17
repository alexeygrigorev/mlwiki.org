---
title: Semi-Supervised Clustering
layout: default
permalink: /index.php/Semi-Supervised_Clustering
---

# Semi-Supervised Clustering

{{stub}}

## Semi-Supervised Clustering
Semi-supervised clustering is a bridge between [Supervised Learning](Supervised_Learning) and [Cluster Analysis](Cluster_Analysis)
- it's about learning with both labeled and unlabeled data:
- sometimes we have some prior knowledge about clusters, e.g. we could have some label information 
- such knowledge can be useful in creating clusters - especially when the number of examples is very big


Where these labels come from?
- you can sample your data and manually label it 
- or try to extract the label e.g. from the unstructured data if you have at least some prior knowledge


## Approaches
### Seeded Approach
Use labeled data to help initialize clusters 
- it will bias clustering towards a good region in the search space


Papers 
- Basu, Sugato, Arindam Banerjee, and Raymond Mooney. "Semi-supervised clustering by seeding." 2002.


### Constrained Approach
Force to keep the grouping of labels unchanged 


### Feedback-Based Approach
- First run regular clustering 
- then adjust clusters based on labeled data 
- account for user feedback


### Probabilistic frameworks
Papers
- Basu, Sugato, Mikhail Bilenko, and Raymond J. Mooney. "A probabilistic framework for semi-supervised clustering." 2004. 


## [Document Classification](Document_Classification)
It's also useful for document classification

Papers:
- Nigam, Kamal, et al. "Learning to classify text from labeled and unlabeled documents." (1998). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.49.6837&rep=rep1&type=pdf]
- Nigam, Kamal, et al. "Text classification from labeled and unlabeled documents using EM." (2000). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.154.3651&rep=rep1&type=pdf]



## Sources
- Aggarwal, Charu C., and ChengXiang Zhai. "A survey of text clustering algorithms." Mining Text Data. Springer US, 2012. [http://ir.nmu.org.ua/bitstream/handle/123456789/144935/d1784ebed3eab2708026b202b2b65309.pdf?sequence=1#page=90]
- Jing, Liping. "Survey of text clustering." (2008). [http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.112.3476&rep=rep1&type=pdf]


[Category:Cluster Analysis](Category_Cluster_Analysis)
[Category:Machine Learning](Category_Machine_Learning)