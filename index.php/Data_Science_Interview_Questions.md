---
title: Data Science Interview Questions
layout: default
permalink: /index.php/Data_Science_Interview_Questions
---

# Data Science Interview Questions

The result: http://www.itshared.org/2015/10/data-science-interview-questions.html


## Data Science Interview Questions
The term "Data Science" is not yet well establish, so interviews for Data Science jobs might include a very broad range of questions - depending on the interpretation of the term by a particular company. This post is an attempt to organize Data Science interview questions in some usable form, but it might also be biased by how I see Data Science myself. I hope you also can find it useful.

The sources of the questions are: 
- my own data science interviews (being on the interviewee side)
- links that I discovered on the Internet, mostly from Quora and Reddit (see the links at the bottom of the post). 


## Background Questions
### Careers
For background questions be ready to talk about a summary of your career. 
- Summarize your experience 
- What companies you worked at? What was your role?
- Do you have a project portfolio? What projects you implemented? Discuss some of them in details 


Preparation: 
- Review presentation of your projects or the code
- Try to explain the goal of these projects to yourself or your friend
- Prepare technical and non-technical summary of the projects. You'll need the non-technical summary if you're asked to explain the project in "layman's terms"
- Be ready to explain why a particular tool/algorithm was used and what other options you had


### General Questions
There also be some questions not directly related to the projects you did. For example:
- What is the latest paper you read? Why did you read it and what did you learn? 
- What data science blogs do you follow? 


Other general questions:
- What have you done to improve your data analytics knowledge in the past year?
- What are your career goals?
- For aspiring data scientists: Why do you want a career in data science?



## Process
All Machine Learning, Data Mining and Data Science projects should follow some process, so there can be questions about it. 

Data Mining process questions:
- Can you outline the steps in an analytics project?
- Have you heard of [CRISP-DM](CRISP-DM) (Cross Industry Standard Process for Data Mining)?


CRISP-DM defines the following steps:
- Problem Definition 
- Data Exploration
- Data Preparation
- Modeling 
- Evaluation
- Deployment (for the production)


So next you may discuss each of these steps in details
- What is the goal of each step? 
- What are possible activities at each step?




## Background Mathematics
### Linear Algebra
Basic Linear Algebra questions might include:
- What is $A \mathbf x = \mathbf b$? How to solve it?
- How do we multiply matrices? 
- What is an Eigenvalue? And what is an Eigenvector? What is Eigenvalue Decomposition or The Spectral Theorem?
- What is [Singular Value Decomposition](Singular_Value_Decomposition)? 
- You can expect tons of LA questions in the Machine Learning part of the interview


### Other Areas
- Analysis, Discrete Mathematics and Logics are not that important for Data Science 
- Probability and Statistics are core skills and discussed in the next section
- Optimization is usually discussed in the Machine Learning and usually when talking about a particular algorithm


## Probability and Statistics
Probability and Statistics is an important part of an interview, because it's the basics for Machine Learning. It is also useful if the company is doing some marketing or website optimization, so they could ask about A/B tests. 


### Basic Probability
You can have a couple of simple questions to check your understanding of probability. 

For example:
- Given two fair dices, what is the probability of getting scores that sum to 4? to 8?
- A simple questions on Bayes rule: Imagine a test with a true positive rate of 100% and false positive rate of 5%. Imagine a population with a 1/1000 rate of having the condition the test identifies. Given a positive test, what is the probability of having that condition?


### Distributions
You can expect questions about probability distributions:
- What is the normal distribution? Give an example of some variable that follows this distribution
- What about log-normal?
- Explain what a long tailed distribution is and provide three examples of relevant phenomena that have long tails. Why are they important in classification and prediction problems?
- How to check if a distribution is close to Normal? Why would you want to check it? What is QQ Plot? 
- Give examples of data that does not have a Gaussian distribution, or log-normal. 
- Do you know what the exponential family is?
- Do you know the Dirichlet distribution? the multinomial distribution?


### Basic Statistics
- What is the Laws of Large Numbers? Central Limit Theorem?
- Why are they important for Statistics?
- What summary statistics do you know?


=== Experiment Design === 
Sampling and Randomization
- Why do we need to sample and how? 
- Why is randomization important in experimental design?
- Some 3rd party organization randomly assigned people to control and experiment groups. How can you verify that the assignment truly was random?
- How do you calculate needed sample size? 
- Power analysis


Biases
- When you sample, what bias are you inflicting?
- How do you control for biases?
- What are some of the first things that come to mind when I do X in terms of biasing your data?


Other questions
- What are confounding variables? 


### Point Estimates
Confidence intervals
- What is a point estimate? What is a confidence interval for it?
- How they are constructed?
- Why you standardize?
- How to interpret confidence intervals?


### Testing
Hypothesis tests
- Why do we need hypothesis testing? What is P-Value?
- What is the null hypothesis? How do we state it? 
- Do you know what type-I (type-II) error is?
- What is t-Test/F-Test/ANOVA? When to use it? 
- How would you test if two populations have the same mean? What if you have 3 or 4 populations?
- You applied ANOVA and it says that the mean is different. How do you identify the populations where the means are different? 
- What are the distributions / is the distribution of p-value's, in general?


=== A/B Tests === 
- What is A/B testing? How is it different from usual Hypothesis testing? 
- How can you prove that one improvement you've brought to an algorithm is really an improvement over not doing anything? How familiar are you with A/B testing? 
- How can we tell whether our website is improving?
- What are the metrics to evaluate a website? A search engine? 
- What kind of metrics would you track for you music streaming website?
- Common metrics: Engagement / retention rate, conversion, similar products / duplicates matching, how to measure them.
- Real-life numbers and intuition: Expected user behavior, reasonable ranges for user signup / retention rate, session length / count, registered / unregistered users, deep / top-level engagement, spam rate, complaint rate, ads efficiency.


### Bayesian Statistics
In my interviews I didn't have any questions about Bayesian Stats, not did I found a lot of questions on the Internet. But here are some: 
- Have you ever seen Bayes Theorem?
- Do you know what a conjugate-prior is?

You might also get questions about Bayesian non-parametric models, but I'm not sure if it's common. 


=== Time Series === 
- What is a time series? 
- What is the difference between data for usual statistical analysis and time series data? 
- Have you used time series models? Cross-correlations with time lags? Correlograms? Spectral analysis? Signal processing and filtering techniques? In which context?
- Have you used any of the following: Time series models, Cross-correlations with time lags, Correlograms, Spectral analysis, Signal processing and filtering techniques? If yes, in which context?
- In time series modeling how can we deal with multiple types of seasonality like weekly and yearly seasonality?


### Advanced
Resampling 
- Explain what resampling methods are and why they are useful. Also explain their limitations.
- Bootstrapping - how and why it is used? 
- How to use resampling for hypothesis testing? Have you heard of Permutation Tests? 
- How would you apply resampling to time series data? 



## Machine Learning
In my experience the Machine Learning part is usually the largest part of the interview. It may be a few basic questions, but it's helpful to be prepared to more in-depth ML questions, especially if you claim to have worked with ML on your CV. 


### General ML Questions
The ML part may start with something quite simple, like: 
- What is the difference between supervised and unsupervised learning? Which algorithms are supervised learning and which are not? Why? 
- What is your favorite ML algorithm and why? 


### Regression
- Describe the regression problem. Is it supervised learning? Why? 
- What is linear regression? Why is it called linear? 
- Discuss the bias-variance tradeoff.


Linear Regression:
- What is Ordinary Least Squares Regression? How it can be learned? 
- Can you derive the OLS Regression formula? (For one-step solution)
- Is model $Y = X_1 + X_2 + X_1 \, X_2 + \varepsilon$ still linear? Why? 
- Do we always need the intercept term? When do we need it and when do we not? 
- What is collinearity and what to do with it? How to remove multicollinearity? 
- What if the design matrix is not full rank? 
- What is overfitting a regression model? What are ways to avoid it?
- What is Ridge Regression? How is it different from OLS Regression? Why do we need it? 
- What is Lasso regression? How is it different from OLS and Ridge? 


Linear Regression assumptions:
- What are the assumptions required for linear regression? (see [Multivariate Linear Regression](Multivariate_Linear_Regression))
- What if some of these assumptions are violated? 


Significant features in Regression
- You would like to find significant features. How would you do that? 
- You fit a multiple regression to examine the effect of a particular feature. The feature comes back insignificant, but you believe it is significant. Why can it happen? 
- Your model considers the feature $X$ significant, and $Z$ is not, but you expected the opposite result. Why can it happen?


Evaluation
- How to check is the regression model fits the data well? 


Other algorithms for regression
- Decision trees for regression
- KNN for regression
- Do you know others? E.g. Splines? LOESS/LOWESS? 


### Classification
Basic:
- Can you describe what is the classification problem? 
- What is the simplest classification algorithm?
- What classification algorithms do you know? Which one you like the most? 


Decision trees:
- What is a decision tree? 
- What are some business reasons you might want to use a decision tree model?
- How do you build it? 
- What impurity measures do you know? 
- Describe some of the different splitting rules used by different decision tree algorithms.
- Is a big brushy tree always good? Why would you want to prune it? 
- Is it a good idea to combine multiple trees? 
- What is Random Forest? Why is it good? [https://medium.com/@D33B/the-unreasonable-effectiveness-of-random-forests-f33c3ce28883]



Logistic regression:
- What is logistic regression? 
- How do we train a logistic regression model?
- How do we interpret its coefficients?



Support Vector Machines
- What is the maximal margin classifier? How this margin can be achieved and why is it beneficial?
- How do we train SVM? What about hard SVM and soft SVM?
- What is a kernel? Explain the Kernel trick
- Which kernels do you know? How to choose a kernel? 


Neural Networks
- What is an Artificial Neural Network?
- How to train an ANN? What is back propagation? 
- How does a neural network with one layer and one input and output compare to a logistic regression?
- What is deep learning? What is CNN or RNN? 


Other models: 
- What other models do you know? 
- How can we use Naive Bayes classifier for categorical features? What if some features are numerical? 
- Tradeoffs between different types of classification models. How to choose the best one? 
- Compare logistic regression with decision trees and neural networks.


### Regularization
- What is Regularization? 
- Which problem does Regularization try to solve? 
- What does it mean (practically) for a design matrix to be "ill-conditioned"?
- When might you want to use ridge regression instead of traditional linear regression?
- What is the difference between the $L_1$ and $L_2$ regularization?
- Why (geometrically) does LASSO produce solutions with zero-valued coefficients (as opposed to LASSO ridge)?
- Let us go through the derivation of OLS or Logistic Regression. What happens when we add $L_2$ regularization? How do the derivations change? What if we replace $L_2$ regularization with $L_1$ regularization?



### Dimensionality Reduction
Basics:
- What is the purpose of dimensionality reduction and why do we need it? 
- What ways of reducing dimensionality do you know? 
- Is feature selection a dimensionality reduction technique? 
- What is the difference between feature selection and feature extraction? 


PCA:
- Is it beneficial to perform dimensionality reduction before fitting an SVM? Why or why not?
- Are dimensionality reduction techniques supervised or not? Are all of them are (un)supervised? 
- What is Principal Component Analysis (PCA)? What is the problem it solves? How is it related to eigenvalue decomposition (EVD)? 
- What's the relationship between PCA and SVD? When SVD is better than EVD for PCA?
- Under what conditions is PCA effective?
- Why do we need to center data for PCA and what can happed if we don't do it? Do we need to scale data for PCA? 
- Is PCA a linear model or not? Why? 


Other DR techniques:
- Do you know other DR techniques? 
- What is Independent Component Analysis (ICA)? What's the difference between ICA and PCA? 
- Suppose you have a very sparse matrix where rows are highly dimensional. You project these rows on a random vector of relatively small dimensionality. Is it a valid dimensionality reduction technique or not? 
- Have you heard of Kernel PCA or other non-linear dimensionality reduction techniques? What about LLE (Locally Linear Embedding) or t-SNE (t-distributed Stochastic Neighbor Embedding)
- What is Fisher Discriminant Analysis? How it is different from PCA? Is it supervised or not? 



### Cluster Analysis
- What is the cluster analysis problem?
- Which cluster analysis methods you know? 
- Describe K-Means. What is the objective of K-Means? Can you describe the Lloyd algorithm? 
- How do you select K for K-Means? 
- How can you modify k-means to produce soft class assignments?
- How to assess the quality of clustering? 
- Describe any other cluster analysis method. E.g. DBSCAN.


### Optimization
You may have some basic questions about optimization:
- What is the difference between a convex function and non-convex? 
- What is Gradient Descent Method?
- Will Gradient Descent methods always converge to the same point?
- What is a local optimum? 
- Is it always bad to have local optima?
- What the Newton's method is?
- What kind of problems are well suited for Newton's method? Simplex? BFGS? SGD?
- What are "slack variables"?
- Describe a constrained optimization problem and how you would tackle it.



### Recommendation
- What is a recommendation engine? How does it work?
- How would you approach the Netflix Prize?
- How to do customer recommendation?
- What is Collaborative filtering?
- How would you generate related searches for a search engine?
- How would you suggest followers on Twitter?


### Feature Engineering
- How to apply machine learning to audio data, images, texts, graphs, etc? 
- What is feature engineering? Can you give an example? Why do we need it? 
- How to go from categorical variables to numerical? 



### Natural Language Processing
If the company deals with text data, you can expect some questions on NLP and Information Retrieval:
- What is NLP? How is it related to Machine Learning? 
- How would you turn unstructured text data into structured data usable for ML models?
- What is the Vector Space Model?
- What is TF-IDF?
- Which distances and similarity measures can we use to compare documents? What is cosine similarity? 
- Why do we remove stop words? When do we not remove them?
- Language Models. What is N-Grams? 


### Meta Learning
Feature selection
- Are all features equally good? 
- What are the downfalls of using too many or too few variables?
- What is Feature Selection and why do we need it? 
- How many features should you use? How do you select the best features? Describe several feature selection methods. Are these methods depend on the model or not?


Model selection
- You have built several different models. How would you select the best one? 
- You have one model and want to find the best set of parameters for this model. How would you do that? 
- How would you look for the best parameters? Do you know something else apart from grid search? 
- What is Cross-Validation? 
- What is 10-Fold CV?
- What is the difference between holding out a validation set and doing 10-Fold CV.


Model evaluation
- How do you know if your model overfits? 
- How do you assess the results of a logistic regression?
- Which evaluation metrics you know? Something apart from accuracy?
- Which is better: Too many false positives or too many false negatives?
- What precision and recall are?
- What is a ROC curve? What is AU ROC (AUC)? How to interpret ROC and AU ROC? 
- Do you know about Concordance or Lift? 



Discussion Questions:
- You have a marketing campaign and you want to send emails to users. You developed a model for predicting if a user will reply or not. How can you evaluate this model? Is there a chart you can use?



### Miscellanea
Curse of Dimensionality
- What is Curse of Dimensionality? How does it affect distance and similarity measures? 
- What are the problems of large feature space? How does it affect different models, e.g. OLS? What about computational complexity? 
- What dimensionality reductions can be used for preprocessing the data?
- What is the difference between density-sparse data and dimensionally-sparse data? 



You are training an image classifier with limited data. What are some ways you can augment your dataset?

### LA for ML

How does the "power method" work?
How are sparse matrices special/useful?
Why is the QR factorization often used to solve OLS regression problems instead of the better known matrix form of the normal equations?


## Computer Science
Knowledge in Computer Science is as important for Data Science as knowledge in Machine Learning. So you may get the same type of questions as for any software developer position, but possible with lower expectations on your answers.

I was a Java developer for quite some time, so here is a list of questions I asked (and often was asked) for job interviews. This list can also be helpful for preparing to a Data Science interview [Java interview questions](Java_interview_questions).


### Libraries and Tools
You can be asked about libraries:
- Which libraries for Analytics/DS you are familiar in Python/R/Java?
- Have you used numpy, scipy, pandas, sklearn?
- What are some features of the sklearn api that differentiate it from fitting models in R?
- What are some features of pandas/scipy that you like? Hate? Same questions for R.
- Why is "vectorization" such a powerful method for optimizing numerical code? What is going on that makes the code faster relative to alternatives like nested for loops?
- When is it better to write your own code than using a data science software package?
- State any 3 positive and negative aspects about your favorite statistical software.
- Describe a difficult bug you've encountered and how you resolved it.
- How does floating point affect precision of calculations? Equality tests?
- What is BLAS? LAPACK?



### Algorithms
And also some algorithm related questions, like
- What is big O? 
- What sorting algorithm do you know? 
- How to HashMap is implemented? 
- What are hash table collisions? How is it avoided? How frequently does it happen?


Implementation
- implement some simple model, e.g. OLS regression or logistic regression 


Data generation:
- Given an unfair coin with the probability of heads not equal to 0.5. What algorithm could you use to create a list of random 1s and 0s?
- Given a set of $n$ objects, write an algorithm to select a random subset of size $k$ (where $k \leqslant n$) without replacement.


Other questions:
- What is probabilistic merging (AKA fuzzy merging)? Is it easier to handle with SQL or other languages?
- Which languages would you choose for semi-structured text data reconciliation?


### Databases
- Have you been involved in database design and data modeling?
- SQL-Related questions: e.g. what's group by? 
- Or given some DB schema you may be asked to write a simple SQL query.

Describe different NoSQL technologies you're familiar with, what they are good at, and what they are bad at.

What is a "star schema"?


### Distributed Systems and Big Data
Basic "Big Data" questions:
- What is the biggest data set that you have processed and how did you process it? What was the result?
- Do you know about Apache Hadoop, Apache Spark, Apache Flink? Have you used Apache Mahout?



MapReduce
- What are the advantages/disadvantages of "shared-nothing" architecture?
- What is MapReduce? Why is it "shared-nothing" architecture?
- Can you implement word count in MapReduce? What about something a bit more complex like TF-IDF? Naive Bayes? 
- What is load balance? How to make sure a mapreduce application has good load balance? 
- Can you give examples where MapReduce does not work? 
- What are examples of "embarassingly parallelizable" algorithms?


Implementation questions
- How do you optimize a web crawler to run much faster, extract better information and summarize data to produce cleaner databases?
- How would you estimate the median of a dataset that is too big to hold in your computer memory?




## Hands-On

### Problem to Solve
Quite often you are given some problem description and asked how would you approach it. 

For example:

Assume that you are asked to lead a project on churn detection, and have dataset of known users who stopped using the service and ones who are still using. This data includes demographics and other features.

Do the following:
# Describe the methodology and model that you will chose to identify churn, and describe your thought process.
# Think how would you communicate the results to the CEO? 
# Suppose in the dataset only 0.025 of users churned. How would you make it more balanced? 

Also:
- How would you implement it if you had one day? One month? One year? 
- How would your approach scale? 


Other problems: 
- How would you approach identifying plagiarism? 
- How to detect individual paid accounts shared by multiple users?
- How to detect bogus reviews, or bogus Facebook accounts used for bad purposes?
- Usually the domain of the problem is related to what the company is doing. If they're doing marketing, it will most likely be marketing related. 


Additionally, you may be asked: 
- How would you approach collecting the data if you didn't have the dataset? 


### Problem Solving Coding
- Sometimes you even may be presented a small dataset and ask to do a particular task with any tool. For example, write a script to extract features, then do some exploratory data analysis and finally apply some ML algorithm to this dataset. Or just the last two, with a ready to use dataset in tabular form. 


Anyway, the right way to conduct a data science interview is to create a dataset (i.e. from a Kaggle, etc) that resembles the problem you want to solve, and have the 'scientist' work through the different steps from start to finish of what they would do:

- What data would they choose?
- How would they clean the data?
- What types of features? How could features be enhanced with domain knowledge?
- What model would they use? why / why not?
- What evaluation metrics? (f1 / recall / precision, etc)
- What are other papers saying about this? What is the academic benchmark for a problem like this?
- Who in academia has presented papers on this type of problem?
- etc.


### Papers
It's also possible that you'll be asked to read some ML paper and share your thoughts on it, and then discuss the proposed algorithm, it's time complexity, how it can be implemented and improved. I wasn't asked to do it myself, but based on my experience working as a ML developer, I believe that reading papers and being able to understand them is an important skill, so don't be surprised if somebody tries to check this ability.




## Sources
- My own interviews
- http://www.quora.com/What-is-a-typical-data-scientist-interview-like
- http://www.quora.com/What-are-the-interview-questions-on-regression-modeling
- http://www.quora.com/How-should-I-prepare-for-statistics-questions-for-a-data-science-interview
- http://www.quora.com/A-B-Testing/What-kind-of-A-B-testing-questions-should-I-expect-in-a-data-scientist-interview-and-how-should-I-prepare-for-such-questions
- http://www.quora.com/What-are-20-questions-to-detect-fake-data-scientists
- http://www.quora.com/What-are-some-common-Machine-Learning-interview-questions
- http://www.quora.com/What-are-the-best-interview-questions-to-evaluate-a-machine-learning-researcher
- https://www.quora.com/Are-CS-questions-part-of-a-data-scientist-interview-at-Facebook
- http://www.quora.com/Data-Science/How-should-I-prepare-for-statistics-questions-for-a-data-science-interview
- http://stats.stackexchange.com/questions/5465/statistics-interview-questions
- http://www.reddit.com/r/datascience/comments/2nhb4k/what_interview_questions_have_you_been_asked/
- http://www.reddit.com/r/statistics/comments/310h76/i_have_an_interview_for_a_parttime_data_analyst/
- https://www.reddit.com/r/datascience/comments/3fsz54/my_top10_technical_questions_for_job_candidates/
- https://www.reddit.com/r/datascience/comments/3kzf69/data_scientist_interview_questions_on_pca_svm/
- http://www.reddit.com/r/MachineLearning/comments/392nwy/interview_questions_for_data_scientist_positions/
- http://blog.udacity.com/2015/04/data-science-interview-questions.html
- http://alyaabbott.wordpress.com/2014/10/01/how-to-ace-a-data-science-interview/
- http://www.marketingdistillery.com/2014/09/03/how-to-successfully-recruit-a-data-scientist/ 
- http://www.edureka.co/blog/frequently-asked-data-science-interview-questions
- http://www.galvanize.it/blog/how-to-nail-a-data-science-interview
- http://analyticsindiamag.com/common-analytics-interview-questions/
- http://www.datasciencecentral.com/profiles/blogs/66-job-interview-questions-for-data-scientists



## Useful Links
- http://www2.udacity.com/rs/udacity/images/Ultimate%20Skills%20Checklist%20For%20Your%20First%20Data%20Analyst%20Job.pdf
- http://www.quora.com/What-are-some-important-questions-to-ask-a-recruiter-when-interviewing-for-a-data-science-job
- http://www.quora.com/In-a-data-scientist-interview-should-I-use-Python-or-C++-for-algorithm-data-structure-questions
- http://www.quora.com/How-do-I-prepare-for-a-data-scientist-interview
- http://datascienceinterview.quora.com/Data-Science-Interview-Preparation
- http://datascienceinterview.quora.com/Answers-1
- https://github.com/gkamradt/Lessons-Learned-Data-Science-Interviews
- http://mathewanalytics.com/2015/08/18/homework-during-the-hiring-process-no-thanks/
- https://medium.com/@D33B/interview-questions-for-data-scientist-positions-5ad3c5d5b8bd
- https://medium.com/@D33B/interview-questions-for-data-scientist-positions-part-ii-ac294c2c7241
- http://www.jasq.org/just-another-scala-quant/new-agey-interviews-at-the-grocery-startup


[Category:Interview Questions](Category_Interview_Questions)
[Category:Interviews](Category_Interviews)
[Category:Machine Learning](Category_Machine_Learning)
[Category:Statistics](Category_Statistics)