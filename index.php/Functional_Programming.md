---
layout: default
permalink: /index.php/Functional_Programming
tags:
- functional-programming
- programming
title: Functional Programming
---
## Functional Programming

Key ideas:
- One or more data types
- Operations on that data
- Laws that describe the relationships between values and operations
- No mutations (state changes)
Goal:
- Focus on the key ideas
- Avoid state changes
- Be able to use abstraction to compose complex functions from simple ones


*Functional Programming*
- In the narrow sense - programming without state changes, loops, assignments, and other constructs inherent to imperative programming
- In the broad sense - focusing on functions
- Functions as the primary unit of abstraction
  - Functions can be defined anywhere, including inside other functions
  - Functions can be created, returned as results, and passed as parameters to other functions
  - Complex functions can be composed from simpler functions


Functions that take other functions as arguments or return them as results are called *higher-order functions*.

### Advantages
- Easy to understand and write
- Modularity
- Easy to parallelize


## Expression Evaluation
Since functional languages have no side effects (because there are no state changes), the Substitution Model [link](http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.5) can be used to evaluate expressions.
- The basic idea: gradually reduce the expression to some value
- This is called *$\lambda$-calculus* - the foundation of functional programming

A *side effect* is a change in previously established definitions. Functions with side effects cannot be expressed using this model.

### Algorithm
- Evaluate all function argument values from left to right
- Replace the function call in the code with the body of that function
- Replace formal arguments in the function body with the values

## Functional Languages
- [Scala](Scala) ([Functional Programming Principles in Scala (coursera)](Functional_Programming_Principles_in_Scala_(coursera)))
- [Haskell](Haskell)

## Literature
- Structure and Interpretation of Computer Programs [[link](http://newstar.rinet.ru/~goga/sicp/sicp.pdf)(http://mitpress.mit.edu/sicp/full-text/book/book.html])
- A. Field, P. Harrison, Functional Programming.

## Sources
- [Functional Programming Principles in Scala (coursera)](Functional_Programming_Principles_in_Scala_(coursera))
