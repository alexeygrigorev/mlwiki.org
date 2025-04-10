---
title: "Functional Programming"
layout: default
permalink: /index.php/Functional_Programming
---

# Functional Programming

## Functional Programming

Основные идеи
- Одного или нескольких типов данных
- Операциях на этих данных
- Законы, которые описывают отношения между значениями и операциями
- Никаких мутаций|   (Изменений состояний) | |Цель: 
- Сконцентрироваться на основных идеях
- Избежать изменения состояния
- Иметь возможность использовать абстракцию для составление сложных функций из простых


''Functional Programming'' 
- В узком смысле - программирование без изменения состояния, циклов, присваивания и других структур, присущих императивному программированию
- В широком смысле - фокусирование на функциях
- Функции как основная единица абстракции
  - Функции могут быть определены где угодно, в том числе внутри других функций,
  - Функции могут создаваться, возвращаться как результат, и передаваться в качестве параметров другим функциям
  - Из простых функций можно составлять более сложные функции


Функции, которые принимают другие функции в качестве аргументов или возвращают в качестве результата, называют ''функциями высшего порядка''. 

### Преимущества
- Легко понимать и писать
- Модульность
- Легко параллелить


## Вычисление выражений
Так как в функциональных языках нет никаких побочных эффектов (т.к. нет изменений состояния), то для вычисления выражения можно использовать the Substitution Model [http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.5] 
- Основная идея: постепенно приводить выражение к некоторому значению
- Это называется ''$\lambda$-calculus (лямбда-вычисление)'' - основа функционального программирование

''Побочный эффект (side-effect)'' изменение в однажды заданных определениях. Функции с побочным эффектом не могут быть выражены с помощью этой модели.

### Алгоритм
- Вычислить все значения аргументов функции слева направо
- В коде заменить вызов функции на тело этой функции
- Заменить формальные аргументы в теле функции на значения

## Функциональные языки
- [Scala](Scala) ([Functional Programming Principles in Scala (coursera)](Functional_Programming_Principles_in_Scala_(coursera)))
- [Haskell](Haskell)

## Литература
- Structure and Interpretation of Computer Programs [[http://newstar.rinet.ru/~goga/sicp/sicp.pdf](http://mitpress.mit.edu/sicp/full-text/book/book.html])
- А. Филд, П. Харрисон, Functional Programming.

## Sources
- [Functional Programming Principles in Scala (coursera)](Functional_Programming_Principles_in_Scala_(coursera))

[Category:Russian](Category_Russian)
[Category:Programming](Category_Programming)
[Category:Functional Programming](Category_Functional_Programming)