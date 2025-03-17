---
title: "Trigonometric Functions"
layout: default
permalink: /index.php/Trigonometric_Functions
---

# Trigonometric Functions

## Trigonometric Functions
The Trigonometric [Functions](Functions) are functions of angles
- they relate angles of a triangle to the length of its sides 

<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/trig-pythag.png" alt="Image">

- $\sin \theta$ = length of edge, opposite to $\theta$
- $\cos \theta$ = length of edge, adjacent to $\theta$
- when the hypotenuse is 1, by [Pythagoras Theorem](Pythagoras_Theorem), we get $\cos^2 \alpha + \sin^2 \alpha = 1$

Unit circle:
- <img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/trig-circle.png" alt="Image">


Other trigonometric functions are derives from sine and cosine:
- tangent: $\tan \alpha = \cfrac{\sin \alpha}{\cos \alpha}$
- cotangent: $\cot \alpha = \cfrac{\cos \alpha}{\sin \alpha}$
- secant: $\sec \alpha = \cfrac{1}{\cos \alpha}$
- co-secant: $\csc \alpha = \cfrac{1}{\sin \alpha}$


<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/trig-finctions.jpg" alt="Image">


Inverse Trigonometric functions:
- arcsin: $\arcsin \alpha = \sin^{-1} \alpha$
- arccos: $\arccos \alpha = \cos^{-1} \alpha$
- both have restricted domain $[-1, 1]$ because $\cos$ and $\sin$ can output only $[-1, 1]$


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Mplwp_arcsin_arccos_arctan_piaxis.svg" alt="Image">/320px-Mplwp_arcsin_arccos_arctan_piaxis.svg.png
(Source: [<img src="https://commons.wikimedia.org/wiki/File:Mplwp_arcsin_arccos_arctan_piaxis.svg" alt="Image">])



## [Taylor Expansion](Taylor_Series)
- $\cos x = \sum\limits_{k=0}^\infty (-1)^k \cfrac{x^{2k}}{(2k)|  }$ |- $\sin x = \sum\limits_{k=0}^\infty (-1)^k \cfrac{x^{2k + 1}}{(2k + 1)| }$ | |
[Euler's Formula](Euler's_Formula):
- relates Exponential Function and [Trigonometric Functions](Trigonometric_Functions)
- $e^{ix} = \cos x + i \sin x$ where $i = \sqrt {-1}$

With Taylor Expansions, we can pretend that $\sin x$, $\cos x$ and [Exponential](Exponential) are long [Polynomial Functions](Polynomial_Functions)



## Trigonometric Identities
- $\alpha$ radians = $180\, \alpha\, /\, \pi$ degrees
- $\beta$ degrees = $\pi\, \beta\, /\, 180$ radians

### Fundamental
- $\sin (-\alpha) = -\sin \alpha$
- $\cos (-\alpha) =  \cos \alpha$
- $\sin \left(\pi/2 - \alpha\right) = \cos \alpha$
- $\cos \left(\cfrac{\pi}{2} - \alpha \right) = \sin \alpha$
- $\sin^2 \alpha + \cos^2 \alpha = 1$
- $\tan \alpha = \cfrac{\sin \alpha}{\cos \alpha}$
- $\cot \alpha = \cfrac{\cos \alpha}{\sin \alpha} = \cfrac{1}{\tan \alpha}$

### Double angles
- $\sin 2\alpha = 2\, \sin \alpha \, \cos \alpha $
- $\cos 2\alpha = 2\, \cos^2 \alpha  - 1 = 1 - 2\, \sin^2 \alpha  = \cos^2 \alpha  - sin^2 \alpha $
- $\tan 2\alpha = \cfrac{2\, \tan \alpha}{1 - \tan^2 \alpha}$

### Sums
- $\sin \alpha + \sin \beta = 2\, \sin\cfrac{\alpha +\beta}{2}\, \cos\cfrac{\alpha - \beta}{2}$
- $\sin \alpha - \sin \beta = 2\, \cos\cfrac{\alpha +\beta}{2}\, \sin\cfrac{\alpha - \beta}{2}$
- $\cos \alpha + \cos \beta = 2\, \cos\cfrac{\alpha +\beta}{2}\, \cos\cfrac{\alpha - \beta}{2}$
- $\cos \alpha - \cos \beta = 2\, \sin\cfrac{\alpha +\beta}{2}\, \sin\cfrac{\beta - \alpha}{2}$

### Products
- $2\, \sin \alpha\, \sin \beta = \cos (\alpha - \beta) - \cos (\alpha + \beta)$
- $2\, \cos \alpha\, \cos \beta = \cos (\alpha - \beta) + \cos (\alpha + \beta)$
- $2\, \sin \alpha\, \cos \beta = \sin (\alpha + \beta) + \sin (\alpha - \beta)$

### Sums Inside Trigs
- $\sin (\alpha \pm \beta) = \sin \alpha\, \cos \beta \pm \sin \beta\, \cos \alpha$
- $\cos (\alpha \pm \beta) = \cos \alpha\, \cos \beta \mp \sin \alpha\, \sin \beta$
- $\tan (\alpha \pm \beta) = \cfrac{\tan \alpha \pm \tan\beta}{1 \mp \tan \alpha\, \tan \beta}$

### Secs and Cosecs
- $\sec \alpha = \cfrac{1}{\cos \alpha}$
- $\csc \alpha = \cfrac{1}{\sin \alpha}$
- $1 + \tan^2 \alpha = \sec^2 \alpha$
- $\tan \left(\cfrac{\pi}{2} - \alpha \right) = \cot \alpha$

### Inverse Trigs
- $\sin (\arcsin \alpha) = \alpha$
- $\cos (\arccos \alpha) = \alpha$
- $\tan (\arctan \alpha) = \alpha$
- $\arcsin (\sin \alpha) = \alpha$
- $\arccos (\cos \alpha) = \alpha$
- $\arctan (\tan \alpha) = \alpha$

### Tangents
- $\tan^2 \alpha  = \cfrac{1 - \cos \alpha}{1 + \cos \alpha}$
- $\tan \cfrac{2}{\alpha} = \cfrac{2\, \tan \alpha}{1 - \tan^2 \alpha}$
- $\tan \cfrac{\alpha}{2} = \cfrac{\sin \alpha}{1 + \cos \alpha} = \cfrac{1 - \cos \alpha}{\sin \alpha}$
- $\tan \cfrac{\alpha + \beta}{2} = \cfrac{\sin \alpha + \sin \beta}{\cos \alpha + \cos \beta}$
- $\tan \left(\cfrac{\alpha}{2} + \cfrac{\pi}{4}\right) = \tan \alpha + \sec \alpha = \cfrac{1 + \sin \alpha}{\cos \alpha}$
- $\tan 3\alpha = \cfrac{3\, \tan \alpha - \tan^3 \alpha}{1 - 3\, \tan^3 \alpha}$



## Derivatives and Integrals
### [Derivatives](Derivatives)
<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/crs/calc/trigs-derivs.png" alt="Image">

- $\sin' x =  \cos x$
- $\cos' x = -\sin x$
- $\tan' x =  \sec^2 x$
- $\big(\sin^2 x \big)' =  2\, \sin x\, \cos x =  \sin 2x$
- $\big(\cos^2 x \big)' = -2\, \cos x\, \sin x = -\sin 2x$
- $\big(\tan^2 x \big)' = 2\, \tan x + 2\, \tan^3 x$
- $\csc' x = -\cot x\, \csc x$
- $\sec' x =  \tan x\, \sec x$
- $\cot' x = -\csc^2 x$


### [Integrals](Integrals)
Basic Integrals:
- $\int \sin x\, dx = -\cos x + C$
- $\int \cos x\, dx = \sin x + C$
- $\int \tan x\, dx = -\ln |  \cos x | + C$ |- $\int \sec x\, dx = \ln |  \tan x + \sec x | + C$ |- $\int \csc x\, dx = -\ln |  \cot x + \csc x | + C$ |- $\int \cot x\, dx = \ln |  \sin x | + C$ |- $\int \sin^2 x\, dx = \cfrac{x}{2} - \cfrac{\sin 2x}{4} + C$
- $\int \cos^2 x\, dx = \cfrac{x}{2} + \cfrac{\sin 2x}{4} + C$
- $\int \sin x\, \cos x\, dx = -\cfrac{1}{2}\, \cos^2 x + C$


Harder Integrals:
- $\int x\, \sin x\, dx = \sin x - x\, \cos x + C$
- $\int x\, \cos x\, dx = \cos x + x\, \sin x + C$
- $\int \cfrac{1}{1 + \sin x}\, dx = \tan \left( \cfrac{x}{2} - \cfrac{\pi}{4} \right) + C$
- $\int \cfrac{1}{1 + \cos x} dx = \tan \left( \cfrac{x}{2} \right) + C$


## Sources
- [Calculus: Single Variable (coursera)](Calculus__Single_Variable_(coursera))
- http://calculus-geometry.hubpages.com/hub/Trig-Identities-Derivatives-Antiderivatives-sin-cos-tan-Formulas
- https://en.wikipedia.org/wiki/Trigonometric_functions

[Category:Calculus](Category_Calculus)
[Category:Derivatives](Category_Derivatives)
[Category:Integrals](Category_Integrals)
[Category:Cheat Sheets](Category_Cheat_Sheets)