---
title: Phonetic Normalization
layout: default
permalink: /index.php/Phonetic_Normalization
---

# Phonetic Normalization

## Phonetic Normalization
Phonetic normalization is a form of [Text Normalization](Text_Normalization) done for [Information Retrieval](Information_Retrieval) applications

Problem:
- in English (and many other languages) words that are pronounced the same way can be spelled differently
- some IR applications need to account for that 
- use phonetic normalization to reduce similar-sounding words to the same token


So, phonetic normalization algorithm should:
- facilitate the retrieval of words with similar sound.


## Soundex
Soundex is a phonetic normalization algorithm 
- encodes words according to their pronunciation 
- each word is compressed into a 4 characters code: Soundex code.

Algorithm:
- keep the first letter of the name 
- drop all a, e, i, o, u, y, h, w.
- replace similar-sounding ("phonetically clone") consonants with digits:
  - bfpv -> 1;
  - cgjkqsxz -> 2; 
  - dt -> 3;
  - l -> 4; 
  - mn -> 5; 
  - r -> 6;
- now remove all consequent occurrences of the same digit 
- keep only first four characters of the resulting string (append with zeros if needed)


Examples:
- Herman -> H655
- Veronika, Veronique -> V652

### Usage
Useful for
- First and last names
- Street names 
- etc


## Sources
- [Information Retrieval (UFRT)](Information_Retrieval_(UFRT))

[Category:Information Retrieval](Category_Information_Retrieval)