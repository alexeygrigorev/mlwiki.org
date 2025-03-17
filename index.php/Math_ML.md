---
title: "Math ML"
layout: default
permalink: /index.php/Math_ML
---

# Math ML

{{ draft}}

## MathML
MathML Mathematical Markup Language - is a standard for mathematical expressions defined by W3C that browsers should support to render math formulas 


There are two types of MathML: 
- presentation - how browsers show draw a mathematical expression
- meaning - what is the meaning of this expression? 


## Presentation Elements
The presentation elements are meant to express the syntactic structure of mathematical notation
- MathML expressions trees with nested layout.


A ''token'' in MathML is an individual symbol, name or number. Tokens are grouped together to form MathML expressions. 

Tokens can be:
- identifier, variable or function names
- numbers 
- operators (including brackets - so called "fences")
- text and whitespaces 

A "symbol" is not necessarily one character: it could be a string such as <code><mi>sin</mi></code> or <code><mn>24</mn></code>. In MathML they are treated as single tokens.


As in mathematics, MathML expressions are constructed recursively from smaller expressions or single tokens. Complex expressions are created with so-called "layout" constructor elements, while tokens are created with token elements.

Let us consider an example. A mathematical expression $(a + b)^2$ can be represented in MathML as follows:

```xml
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mrow>
      <mo>(</mo>
      <mrow>
        <mi>a</mi>
        <mo>+</mo>
        <mi>b</mi>
      <mrow>
      <mo>)</mo>
    </mrow>
    <mn>2</mn>
  </msup>
$
```


It has the tree structure and recursive. If we take another mathematical expression $\cfrac{3}{(a + b)^2}$. It is a fraction and we see that its denominator is the same as the previous expression. This is also true for the MathML representation:


```xml
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>3</mn>
    <msup>
      <mrow>
        <mo>(</mo>
        <mrow>
          <mi>a</mi>
          <mo>+</mo>
          <mi>b</mi>
        <mrow>
        <mo>)</mo>
      </mrow>
      <mn>2</mn>
    </msup>
  </mfrac>
$
```


### Token Elements
Token elements are needed for representing tokens: the smallest units of mathematical notation that convey some meaning. 

There are several token elements:
- <code>mi</code> identifier
- <code>mn</code> number
- <code>mo</code> operator, fence, or separator
- <code>mtext</code> text
- <code>mspace</code> space
- <code>ms</code> string literal


Often tokens are just single characters, like <code><mi>E</mi></code> or <code><mn>5</mn></code>, but there are cases when tokes are multi-character, e.g. <code><mi>sin</mi></code> or <code><mi>span</mi></code>. 

In MathML <code>mi</code> elements represent some symbolic name or text that should be rendered as identifiers. Identifiers could be variables, function names, and symbolic constants.


Transitional mathematical notation often involve some special typographical properties of fonts, e.g. using bold symbols e.g. $\mathbf x$ to denote vectors or capital script symbols e.g. $\mathcal G$ to denote groups and sets. To address this, there is a special attribute "mathvariant" that can take values such as "bold", "script" and others. 


Numerical literals are represented with <code>mn</code> elements. Typically they are sequences of digits, sometimes with a decimal point, representing an unsigned integer or real number, e.g. <code><mn>50</mn></code> or <code><mn>50.00</mn></code>. 


Finally, operators are represented with <code>mo</code> elements. Operators are ...



### Layout Elements
Layout elements are needed to form complex mathematical expressions from simple ones. They group elements in some particular way. For example:

- <code>mrow</code> groups any number of sub-expressions horizontally
- <code>mfrac</code> form sa fraction from two sub-expressions
- <code>msqrt</code> forms a square root (radical without an index)

Some layout elements are used to add subscripts and superscripts:
- <code>msub</code> attach a subscript to a base
- <code>msup</code> attach a superscript to a base
- <code>msubsup</code> attach a subscript-superscript pair to a base

And special kinds of scripts (TODO: describe in more details)
- <code>munder</code> attach an underscript to a base
- <code>mover</code> attach an overscript to a base
- <code>munderover</code> attach an underscript-overscript pair to a base


For example, $\vec v$ will be rendered as 

```xml
<math xmlns='http://www.w3.org/1998/Math/MathML'>
  <mover>
    <mi>v</mi>
    <mo>&rarr;</mo>
  </mover>
$
```


This is how we would represent $\hat{ \mathbf x}$ (a bold x with a hat) in MathML:

```xml
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mrow>
    <mover>
      <mrow>
        <mi mathvariant="bold">x</mi>
      </mrow>
      <mo>&#x005E;<|  -- ^ --></mo> |    </mover> |  </mrow>
$
```


There are more complex elements such as <code>mtable</code>.


MathML presentation elements only suggest specific ways of rendering



### Math Entities
Certain characters are used to name identifiers or operators that in traditional notation render the same as other symbols or usually rendered invisibly. 

entities <code>&InvisibleTimes;</code> <code>&rarr;</code>

The complete list of MathML entities is described in [Entities](http://www.w3.org/TR/MathML3/appendixg.html#Entities). 



## Sources
- http://www.w3.org/TR/MathML3/
- Miner, Robert, and Jeff Schaefer. "A gentle introduction to MathML." (1998). [http://www.dessci.com/en/reference/mathml/]


[Category:Mathematics](Category_Mathematics)
[Category:XML](Category_XML)
[Category:Thesis](Category_Thesis)