---
title: "Error Analysis"
layout: default
permalink: /index.php/Error_Analysis
---

# Error Analysis

## Prioritizing
- Suppose we want to build a spam classifier 
- How we should spend time to do that? 

Options: 
- Collect more data to have more samples 
- Develop sophisticated features based on email routing etc 
- Develop sophisticated algorithm to detect misspelled words such as m0rtgage etc 

How to choose what is better? 


## Error Analysis
Recommended Approach 
- Start with the simplest possible algorithm (avoid premature optimization|  ) that you can implement quickly |  - Implement it and test it on your [cross-validation set](Cross-Validation) |- Plot [Learning Curves](Learning_Curves) to decide if more data features is likely to help
- Do the Error Analysis 
  - Manually examine the examples (in your CV set) that your algorithm misclassified.
  - See if you spot any systematic trend in what types of examples it makes errors on


### Example
$m_{\text{cv}} = 500$, and our algorithm misclassifies 100 of them 

so we manually examine the 100 errors and categorize them based on
- what type of email it is 
  - pharmacy 12
  - replica 4
  - '''steal password 53''' - seems it's worth investing time in this category|   |  - other 31 |- what features might help the algorithm to classify it correctly 
  - deliberate misspelling 15
  - unusual email routing 16
  - '''unusual punctuation 32''' - so concentrate on this|    | |
## Numerical Evaluation
- Error Analysis may not be helpful for deciding if this is likely to improve performance 
- The only solution in this case is to try it and see if it works 
- But we need a numerical evaluation (e.g. [Cross-Validation](Cross-Validation) error) of algorithm's performance with and without the new code/idea/etc
- So we need to use [Error Metrics](Error_Metrics)


## See also
- [Cross-Validation](Cross-Validation)
- [Learning Curves](Learning_Curves)

## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))

[Category:Machine Learning](Category_Machine_Learning)