---
title: "Meta Learning"
layout: default
permalink: /index.php/Meta_Learning
---

# Meta Learning

## Meta Learning
In Machine Learning there are so-called ''meta''-tasks: 
- [Model Selection](Model_Selection)
- [Parameter Tuning](Parameter_Tuning)
- Estimating model's ability to generalize to new data


Meta Learning is a set of Machine Learning techniques for addressing these tasks. The most popular are
- [Cross-Validation](Cross-Validation) for estimating the prediction quality of models 
- [Ensemble Learning](Ensemble_Learning) for creating stronger models by combining several weaker ones

These techniques generate samples from the data and then train and evaluate models based on these samples

They all have two common steps:
- samples are generated from the input data
- Machine Learning models are trained on these samples 


## Scalable Meta Learning
See the paper by S. Schelter: 
- Schelter, Sebastian, et al. "Efficient Sample Generation for Scalable Meta Learning." ([pdf](http://ssc.io/wp-content/uploads/2014/11/ICDE15_research_150.pdf)


## Links
- http://en.wikipedia.org/wiki/Meta_learning_(computer_science)
- http://www.scholarpedia.org/article/Metalearning for thorough treatment 


## Sources
- Schelter, Sebastian, et al. "Efficient Sample Generation for Scalable Meta Learning." ([pdf](http://ssc.io/wp-content/uploads/2014/11/ICDE15_research_150.pdf) [poster](http://www.icde2015.kr/media/posters/150.pdf))

[Category:Machine Learning](Category_Machine_Learning)