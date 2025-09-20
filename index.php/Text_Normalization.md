---
layout: default
permalink: /index.php/Text_Normalization
tags:
- dimensionality-reduction
- information-retrieval
- nlp
title: Text Normalization
---
## Text Normalization
It's a part of [NLP Pipeline](NLP_Pipeline) for preprocessing text data 
- normalization = applying some linguistic models to [tokens](Tokenization) of text
- text tokens often have some minor difference in spelling, but refer to same thing
- need to recognize such tokens and reduce them to the same common form


[Information Retrieval](Information_Retrieval)
- it's important to do text normalization for IR:
- it reduces the dimensionality of [Vector Space Models](Vector_Space_Models) and the size of the [Index](Inverted_Index)


## Types
### Word Form Normalization
Forms can have many inclinations, but more often they are not important and we need to know only the base form of the word

Can be done by
- [Stemming](Stemming): keeping only the root of the word (usually just deleting suffixes)
  - economy, economic, economical, economically, economics, economize => econom
- [Lemmatization](Lemmatization): keeping only the lemma
- produce, produces, product, production => produce



### [Phonetic Normalization](Phonetic_Normalization)
In English words that are pronounced the same way can be spelled differently
- in some IR applications need to account for that 
- use phonetic normalization to reduce similar-sounding words to the same token


### Acronyms
Countries
- the US -> USA
- U.S.A. -> USA

Organizations
- UN -> United Nations


### Accents / Umlauts
- naïve -> naive
- météo -> meteo
- or can be the other way around - depending on application



### Capital Letters
In many cases capital letter aren't needed
- Product -> product
- usually the way to handle it is to lovercase all the letters


Careful: sometimes capitalization is needed
- e.g. for [Named Entity Recognition](Named_Entity_Recognition), some features that models use are capital letters
- 


### Values
Sometimes we want to enforce some specific format on some values of some types
- e.g:
- phones (+7 (800) 123 1231, 8-800-123-1231 => 0078001231231)
- dates, times (e.g. 25 June 2015, 25.06.15 => 2015.06.25)
- currency (\$400 => 400 dollars)
- addresses


Often we don't care about specific value, only what this value mean, so we can do the following normalization:
- \$400 => MONEY
- email@gmail.com => EMAIL
- 25 June 2015 => DATE
- +7 (800) 123 1231 => PHONE
- etc



### [Spelling Correction](Spelling_Correction)
Also in Natural Languages there are spelling mistakes
- In many applications it's useful to correct them
- e.g. infromation -> information



## Applications
Often text normalization can be seen as a set [Dimensionality Reduction](Dimensionality_Reduction) techniques applied to term-document matrices


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))
