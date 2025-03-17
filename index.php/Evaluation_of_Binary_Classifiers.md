---
title: "Evaluation of Binary Classifiers"
layout: default
permalink: /index.php/Evaluation_of_Binary_Classifiers
---

# Evaluation of Binary Classifiers

## Evaluation of Binary Classifiers
Evaluation is important:
- models have to predict classes of new unlabeled data
- sometimes it's an integral part of the training process (e.g. in [Decision Tree (Data Mining)](Decision_Tree_(Data_Mining)) for pruning) (see [Cross Validation](Cross_Validation))
- also it's needed when we want to compare two or more different models (see [Meta Learning](Meta_Learning))



### Baseline
So for evaluating a classifier we need to set some baseline 
- base rate
  - accuracy of a trivial classifier
  - the one that always predicts the majority class 
- random rate
  - accuracy of random guess
  - need to have some domain knowledge to assign Random [Distribution](Distribution)


### Skewed Classes
- Suppose we have a binary classifier, e.g. cancer prediction. 
  - We built some classification model $h_{\theta}(x)$
  - if we have $h_{\theta}(x) = 1$, we predict cancer, and if $h_{\theta}(x) = 0$, we predict no cancer. 
- Then we find out that we have 1% errors for our classifier on test set, and 99% were correctly diagnosed 
  - So the ''error rate'' is 1%
- But now suppose only 0.5% of patients have cancer 
  - This is a ''skewed class'' - it's a tiny portion of another class 
- We would predict better by always returning 0 (by using the trivial classifier)
  - (we'll have 0.5% error which is better than 1%)
- $\Rightarrow$ We need different evaluation metrics, not just error rate



## Confusion Matrix
Confusion matrix is a $2 \times 2$ [Contingency Table](Contingency_Table)
- We divide our predictions and mis-predictions into this matrix


| + Diagnostic Testing Measures  [http://en.wikipedia.org/wiki/Template:DiagnosticTesting_Diagram] ||  colspan="2" rowspan="2" style="border:none;"| ||   colspan="2" | Actual Class $y$  |  Positive ||  Negative ||   rowspan="2" | $h_{\theta}(x)$ <br/> Test<br />outcome  |  Test<br />outcome<br />positive || style="background:#ccffcc;"| '''True positive'''<br/> ($\text{TP}$) || style="background:#eedddd;"| '''False positive'''<br />($\text{FP}$, Type I error) ||  Precision =<br /> $\cfrac{\# \text{TP}}{\# \text{TP} + \# \text{FP}}$ ||  Test<br />outcome<br />negative || style="background:#eedddd;"| '''False negative'''<br />($\text{FN}$, Type II error) || style="background:#ccffcc;"| '''True negative'''<br /> ($\text{TN}$) ||  Negative predictive value =<br /> $\cfrac{\# \text{TN}}{\# \text{FN} + \# \text{TN}}$ || colspan="2" style="border:none;" | ||  Sensitivity =<br /> $\cfrac{\# \text{TP}}{\# \text{TP} + \# \text{FN}}$ ||  Specificity =<br /> $\cfrac{\# \text{TN}}{\# \text{FP} + \# \text{TN}}$ ||  Accuracy =<br /> $\cfrac{\# \text{TP} + \# \text{TN}}{\# \text{TOTAL}}$ |

Main values of this matrix:
- '''True Positive''' - we predicted "+" and the true class is "+"
- '''True Negative''' - we predicted "-" and the true class is "-"
- '''False Positive''' - we predicted "+" and the true class is "-" (Type I error)
- '''False Negative''' - we predicted "-" and the true class is "+" (Type II error)
- (see also [Statistical Tests of Significance#Type I and Type II Errors](Statistical_Tests_of_Significance#Type_I_and_Type_II_Errors))


The following measures can be calculated:
- Accuracy
- Misclassification Error (or Error Rate)
- Positive predictive value (or precision)
  - $P = \cfrac{\text{TP}}{\text{TP} + \text{FP}}$
- Negative predictive value
- True Positive Rate (also Sensitivity or Recall)
  - Fraction of positive examples correctly classified 
  - $\text{tpr} = \cfrac{\text{TP}}{\text{TP} + \text{FN}}$  
- False Positive Rate (also Fall-Out)
  - Fraction of negative examples incorrectly classified
  - $\text{fpr} = \cfrac{\text{FP}}{\text{FP} + \text{TN}}$  
- Specificity
- Support - fraction of positively classified examples
  - $\text{sup} = \cfrac{\text{TP} + \text{FP}}{N} = \cfrac{\text{predicted pos}}{\text{total}}$



### Accuracy and Error Rate
In practice, these are the most widely used metrics
- Accuracy: $\text{acc} = \cfrac{TP + TN}{N}$
  - fraction of correctly classified examples
- Error Rate: $\text{error} = \cfrac{FN + FP}{N} = 1 - \text{acc}$
  - Fraction of misclassified examples 


### Precision
For all input data that we predicted $h_{\theta}(x) = 1$ what fraction actually have $y = 1$?

$P = \text{Precision} = \cfrac{\text{# TP}}{\text{# predicted positives}} = \cfrac{\text{# TP}}{\text{# TP} + \text{# FP}}$

- Out of all the people we thought have cancer, how many actually had it? 
- High precision is good
- we don't tell many people that they have cancer when they actually don't 


### Recall
For all input data that actually have $y = 1$, what fraction did we correctly detect as $h_{\theta}(x) = 1$?

$R = \text{Recall} = \cfrac{\text{# TP}}{\text{# actual positives}} = \cfrac{\text{# TP}}{\text{# TP + # FN}}$

- Out of all the people that do actually have cancer, how much we identified? 
- The higher the better:
- We don't fail to spot many people that actually have cancer


- For a classifier that always returns zero (i.e. $h_{\theta}(x) = 0$) the Recall would be zero
- That gives us more useful evaluation metric
- And we're much more sure 


The [F Measure](F_Measure) is a combination of [Precision and Recall](Precision_and_Recall)


### Example

| + Diagnostic Testing Wikipedia Example [http://en.wikipedia.org/wiki/Template:DiagnosticTesting_Example] || colspan="2" rowspan="2" style="border:none;"| || colspan="2" style="background:#eeeebb;"|'''Patients with bowel cancer<br />(as confirmed on endoscopy)''' || style="background:#ffffcc;"| Positive || style="background:#ddddaa;"| Negative || rowspan="2" style="background:#bbeeee;"|'''Fecal<br />Occult<br />Blood<br />Screen<br />Test<br />Outcome''' || style="background:#ccffff;"|Test<br />Outcome<br />Positive || style="background:#ccffcc;"|<span style="color:#006600;">'''True Positive'''</span><br />(TP) = 20 || style="background:#eedddd;"|<span style="color:#cc0000;">'''False Positive'''</span><br />(FP) = 180 || style="background:#ccffff;"|Positive predictive value<div style="text-align:left; margin-left:1em;">= TP / (TP + FP)<br />= 20 / (20 + 180)<br />= '''10%'''</div> || style="background:#aadddd;"|Test<br />Outcome<br />Negative || style="background:#eedddd;"|<span style="color:#cc0000;">'''False Negative'''</span><br />(FN) = 10 || style="background:#bbeebb;"|<span style="color:#006600;">'''True Negative'''</span><br />(TN) = 1820 || style="background:#aadddd;"|Negative predictive value<div style="text-align:left; margin-left:1em;">= TN / (FN + TN)<br />= 1820 / (10 + 1820)<br />&asymp; '''99.5%'''</div> || colspan="2" style="border:none;" | || style="background:#ffffcc;"|Sensitivity<div style="text-align:left;">= TP / (TP + FN)<br />= 20 / (20 + 10)<br />&asymp; '''67%'''</div> || style="background:#ddddaa;"|Specificity<div style="text-align:left;">= TN / (FP + TN)<br />= 1820 / (180 + 1820)<br />= '''91%'''</div> |



## Visual Analysis
Visual ways of evaluating the performance of a classifier
- [ROC Analysis](ROC_Analysis) - True Positive Rate vs False Positive Rate
- [Cumulative Gain Chart](Cumulative_Gain_Chart)s - True Positive Rate vs Predicted Positive Rate



## Not Binary Classifiers
When we have multi-class classifiers we can use:
- [Contingency Table](Contingency_Table)
  - just show misclassified examples side-by-side
- [Cost Matrix](Cost_Matrix)
  - we define the cost for each misclassification 
  - and calculate the total cost
- some measures can be extended to multiclass classifiers: 
  - see [Evaluation of Multiclass Classifiers](Evaluation_of_Multiclass_Classifiers)


## See Also
- [Statistical Tests of Significance](Statistical_Tests_of_Significance)


## Sources
- [Machine Learning (coursera)](Machine_Learning_(coursera))
- [Data Mining (UFRT)](Data_Mining_(UFRT))
- http://en.wikipedia.org/wiki/Binary_classification#Evaluation_of_binary_classifiers
- http://en.wikipedia.org/wiki/Template:DiagnosticTesting_Diagram
- http://en.wikipedia.org/wiki/Template:DiagnosticTesting_Example
- [Introduction to Data Science (coursera)](Introduction_to_Data_Science_(coursera))

[Category:Machine Learning](Category_Machine_Learning)
[Category:Classifiers](Category_Classifiers)
[Category:Model Performance Evaluation](Category_Model_Performance_Evaluation)