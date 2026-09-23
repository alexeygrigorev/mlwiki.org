---
layout: default
permalink: /Ridge_Regression
tags:
- machine-learning
- statistics
- optimization
title: Ridge Regression
---

## Ridge Regression

http://www.quora.com/What-is-Ridge-Regression-in-laymans-terms
http://www.quora.com/How-does-ridge-regression-work

Ridge regression is a method of decreasing the variance of regression parameters by accepting some bias in them.

OLS models are BLUE - best linear unbiased estimateors.

But sometimes forcing unbiasedness causes other problems. In particular, if the independent variables are fairly collinear, then the variances of the parameter estimates will be huge and small differences in the input data can make huge differences in the parameter estimates.

Ridge regression allows some bias in order to lower the variance.

https://tamino.wordpress.com/2011/02/12/ridge-regression/ - see PCA/SVD here!

http://stats.stackexchange.com/questions/118712/why-does-ridge-estimate-become-better-than-ols-by-adding-a-constant-to-the-diago/120073#120073

@Glen_b's demonstration is wonderful. I would just add that aside from the exact cause of the problem and description about how quadratic penalized regression works, there is the bottom line that penalization has the net effect of shrinking the coefficients other than the intercept towards zero. This provides a direct solution to the problem of overfitting that is inherent in most regression analyses when the sample size is not enormous in relation to the number of parameters estimate. Almost any penalization towards zero for non-intercepts is going to improve predictive accuracy over an un-penalized model.

It also gives better numerical stability. We can get some insights if we look at this from the Principal Component Analysis point of view. For $d$-dim space, PCA calculates $d$ principal directions (eigenvectors) of the scatter matrix $X^T X$, and the corresponding eigenvalues are variances along these directions. For PCA it is very common to see this kind of pictures: the variance is concentrated at first principal components and there is not much variance for "less" principal components:

![enter image description here]

Let's diagonalize $X^T X = U \Lambda V$, so $(X^T X)^{-1} = V^{-1} \Lambda^{-1} U^{-1}$

$\Lambda = \begin{bmatrix} 
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}$, thus $\Lambda^{-1} = \begin{bmatrix} 
1/\lambda_1 & 0 & \cdots & 0 \\
0 & 1/\lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1/\lambda_n
\end{bmatrix}$

We know that first $\lambda_i$'s are big, so $1/\lambda_i$ are small. But lots of $\lambda_i$ are very small, so $1/\lambda_i$ are very large! Thus, in usual regression, small influences in $X^T X$ have big impact on $(X^T X)^{-1}$.

What about $X^T X + \lambda \, I$? $(X^T X + \lambda \, I)^{-1} = V^{-1} (\Lambda + \lambda \, I)^{-1} U^{-1}$ (here we replaced $I = U U^T = U V$)

$\Lambda + \lambda \, I = \begin{bmatrix} 
\lambda_1 + \lambda & 0 & \cdots & 0 \\
0 & \lambda_2 + \lambda & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n + \lambda
\end{bmatrix}$, thus $(\Lambda + \lambda \, I)^{-1} = \begin{bmatrix} 
\frac{1}{\lambda_1 + \lambda} & 0 & \cdots & 0 \\
0 & \frac{1}{\lambda_2 + \lambda} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{1}{\lambda_n + \lambda}
\end{bmatrix}$

This has little effect on big variances, but huge effect on small variances. For example, consider $\lambda_1 = 1000, \lambda_n = 0.0001$ and let $\lambda = 1$. $\frac{1}{\lambda_1 + \lambda} = \frac{1}{1001} \approx \frac{1}{1000} = \frac{1}{\lambda_1}$ - almost no effect on $\lambda_1$. But, $\frac{1}{\lambda_n + \lambda} = \frac{1}{1.0001} \approx 1$ - huge difference with unregularized $\lambda_n$

http://i.stack.imgur.com/5M8QP.png
