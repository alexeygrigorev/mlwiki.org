---
title: "Hypothesis Testing Decision Errors"
layout: default
permalink: /index.php/Hypothesis_Testing_Decision_Errors
---

# Hypothesis Testing Decision Errors

## Hypothesis Testing Decision Errors
[Hypothesis Testing](Hypothesis_Testing) sometimes mistake - and we need to have tools quantify these mistakes 



## Type I and Type II Errors
| + Summary [http://en.wikipedia.org/wiki/Type_I_and_type_II_errors] ||    |  $H_0$ is true   |  $H_0$ is false  |   Reject $H_0$  |  align="center"| Type&nbsp;I error<br />False positive ||  align="center"| Correct outcome<br />True positive ||   Fail to reject $H_0$  |  align="center"| Correct outcome<br />True negative ||  align="center"| Type&nbsp;II error<br />False negative |

- A decrease in one type of error leads to increase the probability of other 
- So we need to have more evidence 


## Type I Error
- Reject $H_0$ when it's true
- This happens with probability \alpha
- (An innocent is falsely convicted)


Significance Level $\alpha$ controls Type I errors 


### Controlling Family-Wise Error Rate
- suppose we run [Multiple Comparisons Tests](Multiple_Comparisons_Tests)
- e.g. want to compare pair-wise 10 samples
- thus we need to make about $\sum_{i=1}^{10} i = 45$ comparisons
- the chances hight that among the 45 tests a couple of them will incorrectly reject $H_0$ - i.e. they will make Type 1 Error 
- the solution is to modify the significance level, e.g. using the [Bonferroni Correction](Bonferroni_Correction)
- see [Family-Wise Error Rate](Family-Wise_Error_Rate)



## Type II Error
- Fail to reject $H_0$ when $H_A$ is true 
- This happens with probability $\beta = 1 - \text{power}$
- We don't have enough power - probably the test size is too small
- (A criminal is freed)

The probability of making Type II Errors is called the ''Type II error rate''

### Controlling Type II Errors
Type II Errors can be controlled by:
- the Sample Size 
- [Power of a Test](Statistical_Power)


### Sample Size
- we may find a specific sample size such that we have some certain margin of error 
- see [Sample Size Estimation](Sample_Size_Estimation)


### [Power of a Test](Statistical_Power)
Power of a test also allows to control the 
- suppose the power of a test is 0.979. what's the type II error rate?
- it's 1 - 0.979 = 0.021 - this is the probability of failing to reject $H_0$ when it's true



## Sources
- [OpenIntro Statistics (book)](OpenIntro_Statistics_(book))
- [Statistics: Making Sense of Data (coursera)](Statistics__Making_Sense_of_Data_(coursera))
- http://en.wikipedia.org/wiki/Type_I_and_type_II_errors

[Category:Statistics](Category_Statistics)
[Category:Statistical Tests](Category_Statistical_Tests)