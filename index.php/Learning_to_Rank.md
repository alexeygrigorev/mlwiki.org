---
layout: default
permalink: /index.php/Learning_to_Rank
tags:
- information-retrieval
- machine-learning
title: Learning to Rank
---

## Learning to Rank

Learning to Rank for Information Retrieval
http://research.microsoft.com/en-us/people/tyliu/letor-tutorial-sigir08.pdf
(book in dropbox)

https://en.wikipedia.org/wiki/Learning_to_rank
see list of methods!

http://jmlr.org/proceedings/papers/v14/chapelle11a/chapelle11a.pdf 
Yahoo challenge overview

Learning to Rank

Talk:
https://www.youtube.com/watch?v=dKppAG0cdkM&index=21&list=PLq-odUc2x7i_-qsarQo7MNsrYz3rlXGMu

No need for labeling positive/negative - can use CTR, num of reposts, etc as a proxy for relevance

Do SVM on differences item_1 - item_2 -> +1/-1
no difference will result in 0 vector
positive difference indicates winner features
negative difference indicates loser features 

sample from pairs - don't have to use all of them

Then apply this model on the items themselves! not on the pairs 

Idea: positive weights for large winning features will lead to higher rank
negative weights for losing features will lead to lower rank

Evaluation: normalized discounted culative gain NDCG
