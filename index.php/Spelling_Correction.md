---
layout: default
permalink: /Spelling_Correction
tags:
- nlp
- information-retrieval
title: Spelling Correction
---

## Spelling Correction
Spelling (Orthographic) mistakes in [NLP](NLP) may be caused:
- person 
- OCR misrecognition

## Correction of Isolated Words
- Usually done by checking each token against some dictionary 
- if the words is not there - try to find the closest one in terms of Edit Distance
- Edit distance may be weighed to account for frequent typos (e.g. q -> a) or frequent mis-recognitions (D -> O)

## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_%28UFRT%29)
