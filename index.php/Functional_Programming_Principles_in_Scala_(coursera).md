---
title: Functional Programming Principles in Scala (coursera)
layout: default
permalink: /index.php/Functional_Programming_Principles_in_Scala_(coursera)
---

# Functional Programming Principles in Scala (coursera)

Конспект курса "Functional Programming Principles in Scala"

Ссылки:
- [Описание курса](http://www.coursera.org/course/progfun)
- [Все лекции для скачивания](http://rutracker.org/forum/viewtopic.php?t=4434746)
- [Конспект лекций](http://www.dropbox.com/s/kc0rc2s91f6erd8/Functional%20Programming%20Principles%20in%20Scala%20coursera.pdf)


## Функции и их вычисление
### Определения
Как только значения были определены, их больше нельзя изменить. Выражение присваивания некоторому идентификатору значения называется ''определением''.
```text only
def radius = 10
def pi = 3.14159
```


Определения могут иметь как параметры, так и тип возвращаемого значения - в этом случае их следует называть ''функциями''.

```scdoc
def square(x: Double) = x * x
square(2) => 4

def sumOfSquares(x: Double, y: Double) = square(x) * square(y)
def power(x: Double, y: Int): Double = ...
```

### Стратегии вычисления функций
Для вычисления значений функции используется [the Substitution Model](Functional_Programming#Вычисление_выражений))

#### call-by-value (<code>CBV</code>)
Сначала вычисляются значения аргументов, а затем вычисленные значения передаются функции

```scdoc
- square(2 + 2)
- square(4)
- 4 * 4
- 16
```

Плюсы:
- выражение вычисляется только раз - с самого начала

#### call-by-name (<code>CBN</code>)
Выражения передаются в качестве аргументов, которые вычисляются только при вызове внутри тела функции

```scdoc
- square(2 + 2)
- (2 + 2) * (2 + 2)
- 4 * 4
- 16
```

Плюсы:
- не вычисляется, если параметры потом не используются 


Если <code>CBV</code> заканчивает выполнение (т.е. не зацикливается и завершается), то <code>CBE</code> так же заканчивает, но обратное не всегда верно. 

```tera term macro
def loop = loop
def first(x: Int, y: Int) = x

first(1, loop)
```

При <code>CBN</code> выполнится только один раз и завершиться, а при <code>CBV</code> зациклиться и будет выполняться бесконечно. 
По умолчанию в Scala используется <code>CBV</code>, но, когда нужно, можно использовать <code>CBN</code>.

```text only
def countOne(x: Int, y: => Int) = 1
```

<code>x</code> вычисляется как <code>CBV</code>, <code>y</code> как <code>CBN</code>


#### Определения
Определения так же могут быть <code>CBN</code> и <code>CBV</code>

Ключевое слово <code>def</code> задаёт <code>CBN</code> определение, <code>val</code> - <code>CBV</code>

```text only
val x = 2
val y = square(2)
val z = square(x)
```

Для <code>val</code> правая часть вычисляется сразу же и используется впоследствии (т.е. <code>y</code> ссылается на <code>4</code>, а не на <code>square(2)</code>)

```tera term macro
def x = loop // OK
val x = loop // виснет
```


### Условия
''Условное выражение'' <code>if else</code> используется для выбора между двумя альтернативами

```tera term macro
def abs(x: Int) = if (x >= 0) x else -x
```


### Блоки и лексикографический контекст
Считается хорошим стилем программирования разбивать сложные функции на много маленьких, однако многие функции имеют значение только для какой-то конкретной реализации какого-либо алгоритма, и не предназначены для использования извне.

Например, дан алгоритм вычисления квадратного корня с помощью метода Ньютона [(см. также [http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html#%_sec_1.1.7](http://ru.wikipedia.org/wiki/Метод_Ньютона]))
```scdoc
def sqrt(x: Double): Double = 
  sqrtIter(1.0, x)

def sqrtIter(guess: Double, x: Double): Double = 
  if (isGoodEnough(guess, x)) guess
  else sqrtIter(improve(guess, x), x)

def isGoodEnough(guess: Double, x: Double) = 
  abs(guess * guess - x) / x < 0.001

def improve(guess: Double, x: Double) = 
  (guess + x / guess) / 2
```

Для того, чтобы избежать "namespace pollution", можно поместить все второстепенные функции внутрь sqrt:
```scdoc
def sqrt(x: Double): Double = {
  def sqrtIter(guess: Double, x: Double): Double = 
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

  def isGoodEnough(guess: Double, x: Double) = 
    abs(guess * guess - x) / x < 0.001

  def improve(guess: Double, x: Double) = 
    (guess + x / guess) / 2

  sqrtIter(1.0, x)
}
```

В данном случае фигурные скобки определяют ''блок кода'', который так же является выражением (и, следовательно, возвращает какое-либо значение). Это называется ''лексикографическим контекстом блока''.

Область видимости:
- Все определения внутри блока кода не видимы за его пределами (локальный контекст)
- Определения снаружи блока видимы внутри блока (родительский контекст)
- Определения внутри блока (в локальном контексте) перекрывают определения за пределами этого блока (т.е. родительского контекста)

```scdoc
val x = 0
val res = {
  val x = f(3)
  x * x
} + x
```

В этом примере в блоке переменная <code>x</code> перекрывается значением, которое возвращает функция <code>f</code>, затем блок возвращает значение, которое затем прибавляется к изначальному <code>x</code>. 


## Функции высшего порядка
Функции в Scala являются полноправными объектами. То есть функцию можно передать как параметр или вернуть, как значение. Функции, которые это делают, называются ''функциями высшего порядка''. 

```scdoc
def sum(f: Int => Int, a: Int, b: Int): Int = 
  if (a > b) 0
  else f(a) + sum(f, a + 1, b)

def sumInts(a: Int, b: Int) = sum(id, a, b)
def sumCubes(a: Int, b: Int) = sum(cube, a, b)
def sumFactorials(a: Int, b: Int) = sum(fact, a, b)

def id(x: Int): Int = x
def cube(x: Int): Int = x * x * x
def fact(x: Int): Int = if (x == 0) 1 else fact(x - 1)
```

Тип <code>A => B</code> описывает функцию, принимающую в аргумент типа <code>A</code> и возвращающую результат типа <code>B</code>. <code>Int => Int</code> -  принимает <code>Int</code>, возвращает <code>Int</code>. 

Функцию без имени называют ''анонимной функцией''

```scdoc
(x: Int) => x * x * x
(x: Int, y: Int) => x + y
```

В левой части функции перечисляются параметры, а правая часть называется ''телом'' анонимной функции. 

Параметры функции можно опустить, если компилятор может их вычислить сам.

```scdoc
def sumInts(a: Int, b: Int) = sum(x => x, a, b)
def sumCubes(a: Int, b: Int) = sum(x => x * x * x, a, b)
```

### Каррирование
Рассмотрим пример 

```text only
def sumInts(a: Int, b: Int) = sum(x => x, a, b)
```

Аргументы <code>a</code> и <code>b</code> просто передаются без изменений, поэтому возможно эту функцию возможно сделать еще короче

```tera term macro
def sum(f: Int => Int): (Int, Int) = {
  def sumF(a: Int, b: Int): Int =
    if (a > b) 0
    else f(a) + sum(a + 1, b)

  sumF
}
```

<code>sum</code> - это функция, которая возвращает другую функцию, которая "помнит" <code>f</code> и знает, как нужно вычислять значение. Далее можно написать

```scdoc
def sumInts = sum(x => x)
def sumCubes = sum(x => x * x * x)
def sumFactorials = sum(fact)
```

Т.е. 
```text only
sumCubes(1, 10) == (sum(cube))(1, 10)
```

<code>sum(cube)</code> возвращает функцию, которая тут же применяется к аргументам 1 и 10.

В Scala для таких функций существует специальный синтаксис:
```tera term macro
def sum(f: Int => Int)(a: Int, b: Int): Int = 
  if (a > b) 0 else f(a) + sum(f)(a + 1, b)
```

Это называется [''каррингом''](Functional_Programming#Карринг).


### Пример: Нахождение неподвижной точки
Нахождение неподвижной точки (Fixed Point) [[http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-12.html#%_sec_Temp_106](http://ru.wikipedia.org/wiki/Неподвижная_точка])

$x$ называется ''неподвижной точкой'' функции $f$ если $f(x) = x$

Для некоторых функций мы можем найти неподвижную точку, применив функцию к некоторому начальному значению, затем применив эту же функцию к полученному результату, затем опять и т.п.

$x, f(x), f(f(x)), f(f(f(x))), ...$

до тех пор, пока два соседних члена такой последовательности отличаются незначительно. 


```tera term macro
val tolerance = 0.0001

def isCloseEnough(x: Double, y: Double) =
  abs((x - y) / x) / x < tolerace

def fixedPoint(f: Double => Double)(firstGuess: Double) = {
  def iterate(guess: Double): Double = {
    val next = f(guess)
    if (isCloseEnough(guess, next)) next
    else iterate(next)
  }
  iterate(firstGuess)
}
```

Функция $f = \sqrt{x}$ возвращает число y такое, что $y \cdot y = x$, или, если разделить на $y$, $y = \frac{x}{y}$

Следовательно,  $f = \sqrt{x}$ - это неподвижная точка функции $y = \frac{x}{y}$

```text only
def sqrt(x: Double) = fixedPoint(y => x / y)(1.0)
```

Однако, такая функция не сойдётся, а будет колебаться: 1.0, 2.0, 1.0, 2.0, ...

Этого можно избежать с помощью нахождения среднего между двумя последними значениями:

```text only
def sqrt(x: Double) = fixedPoint(y => (x + x / y) / 2)(1.0)
```

Эта техника стабилизации колеблющейся функции называется ''average damp'', и она достаточно общая для того, чтобы вынести эту логику в отдельную функцию:

```text only
def averageDamp(f: Double => Double)(x: Double) = (x + f(x)) / 2
```

В итоге получаем
```text only
def sqrt(x: Double) = fixedPoint(averageDamp(x => x / y))(1.0)
```


### Пример: Sets
''Синонимом'' (type alias) называют новый идентификатор для уже существующего типа.

Для множеств мы можем определить следующий синоним:
```carbon
type Set = Int => Boolean
```

Т.е. множество можно представить как функцию, которая принимает число и возвращает <code>true</code>, если это число входит в множество, и <code>false</code> в противном случае.

Например, чтобы представить множество всех отрицательных чисел, можно написать следующие
```text only
(x: Int) => x < 0
```

Соответственно, функция <code>contains</code> принимает следующий вид:
```text only
def contains(s: Set, elem: Int): Boolean = s(elem)
```


## Функции и структуры данных
Как с помощью функций создавать и инкапсулировать структуры данных.

### Пример: Вещественные числа
Мы хотим спроектировать пакет, позволяющий выполнять арифметические операции над вещественными числами.

Вещественное число можно представить в виде двух чисел $x$ и $y$: числитель $x$ и знаменатель $y$

```perl6
class Rational(x: Int, y: Int) {
  def numer = x
  def denom = y
}
```

В этом определении <code>Rational</code> в код добавляется
- новый тип - <code>Rational</code>
- конструктор, с помощью которого можно создавать элементы типа <code>Rational</code>

```text only
new Rantional(1, 2) // конструктор
```

Определения <code>numer</code> и <code>denum</code> называются членами класса. Доступ к членам класса производится с помощью инфиксного оператора <code>.</code> (точка):

```gdscript
x.numer 
x.denum
```

Над вещественными числами можно совершать следующие операции:
- $\cfrac{n_1}{d_1} + \cfrac{n_2}{d_2} = \cfrac{n_1 d_2 + n_2 d_1}{d_1 d_2}$
- $\cfrac{n_1}{d_1} - \cfrac{n_2}{d_2} = \cfrac{n_1 d_2 - n_2 d_1}{d_1 d_2}$
- $\cfrac{n_1}{d_1} \cdot \cfrac{n_2}{d_2} = \cfrac{n_1 n_2}{d_1 d_2}$
- $\cfrac{n_1}{d_1} / \cfrac{n_2}{d_2} = \cfrac{n_1 d_2}{d_1 n_2}$
- $\cfrac{n_1}{d_1} = \cfrac{n_2}{d_2} \iff n_1 d_2 = d_1 n_2$

Для каждой из этих операций мы можем создать функцию

```scdoc
def addRational(r: Rational, s: Rational): Rational = 
  new Rational(r.numer * s.denom + s.numer * r.denom, r.denom * s.denom)

//...

def makeString(r: Rational) = 
  r.numer + "/" + r.denom
```

Но эти функции можно поместить внутрь абстракции <code>Rational</code> - тогда такие фукнции будут называться ''методами''. 


```perl6
class Rational(x: Int, y: Int) {
  def numer = x
  def denom = y

  def add(r: Rational) = 
    new Rational(numer * r.denom + r.numer * denom, denom * r.denom)

  //...

  def override toString = numer + "/" + denom
}
```

(Ключевое слово <code>override</code> говорит о том, что метод <code>toString</code> уже существует)

```text only
val x = new Rational(1, 3)
val y = new Rational(5, 7)
val z = new Rational(9, 11)

x.add(y).mul(z)
```

Можно заметить, что в некоторых случаях дробь можно упростить (сократить)

```perl6
class Rational(x: Int, y: Int) {
  private def gcd(a: Int, b: Int): Int = 
    if (b == 0) a else gcd(b, a % b)

  private val g = gcd(x, y)

  def numer = x / g
  def denom = y / g

  //...
}
```

Ключевое слово <code>private</code> используется в случаях, когда члены класса должны быть видимы только внутри определения класса и не должны быть видимы снаружи (т.е. к ним можно получить доступ только внутри класса <code>Rational</code>).


### Конструкторы
Определения класса неявно объявляет и его конструктор. Такой конструктор называется главным конструктором. 

Главный конструктор 
- принимает параметры класса 
- выполняет все выражения в теле класса

Мы так же можем объявить вспомогательные конструкторы - они объявляются с помощью метода с называнием <code>this</code>:

```perl6
class Rational(x: Int, y: Int) {
  //...

  def this(x: Int) = this(x, 1)
}

new Rational(2) // -> 2/1
```


### Идентификаторы и Операторы
В Scala возможно написать 

```text only
r add s
r mul s
```

вместо

```text only
r.add(s)
r.mul(s)
```

И оператор может быть использован, как идентификатор.

Правила наименования идентификаторов
- идентификатор может начинаться с буквы и состоять из букв и цифр
- идентификатор может начинаться с операторного символа и состоять из других операторных символов 
- <code>_</code> (нижнее подчеркивание) считается буквой
- буквенно-цифровые идентификаторы могут оканчиваться подчёркиванием, за которым следуют операторные символы

Например, <code>x1</code>, <code>*</code>, <code>+?%&</code>, <code>vector_++</code>, <code>counter_=</code>.

Таким образом, мы можем определить следующие методы:

```perl6
class Rational(x: Int, y: Int) {
  def numer = x
  def denom = y

  def +(r: Rational) = //...
  def -(r: Rational) = //...
  def *(r: Rational) = //...

  //...
}

val x = new Rational ...
val y = new Rational ...

x * x + y * y
// тоже самое, что 
(x * x) + (y * y)
```


Приоритеты у операторов определяются первым символом их имени. Приоритет:
- буквы
- <code>| </code> |- <code>^</code>
- <code>&</code>
- <code>< ></code>
- <code>= |  </code> |- <code>:</code> |- <code>+ -</code>
- <code>* / %</code>
- все остальные специальные символы

Пример:

```text only
a + b ^? c ^? d less a ==> b |  c |((a + b) ^? (c ^? d)) less ((a ==> b) |  c) |
```


### Создание иерархий классов
''Абстрактным классом'' называется класс, который может содержать методы, которые ещё не реализованы. 

Рассмотрим пример - множество целых чисел.
```text only
abstract class IntSet {
  def incl(x: Int): IntSet
  def contains(x: Int): Boolean
}
```

Оператор <code>new</code> неприменим к абстрактным классам - т.е. нельзя создать объект такого класса. 

''Расширением'' называется отношение между классами, в котором один из классов является ''базовым'' или ''суперклассом'' (superclass) для второго класса - ''подкласса'' (subclass). Базовый класс предоставляет свои методы для использования подклассу, который, в свою очередь, может добавлять новые методы (т.е. ''расширять'' базовый класс).

Если класс расширяет абстрактный класс, то он должен реализовать его абстрактные методы.

```gdscript
class Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
  def contains(x: Int): Boolean = 
    if (x < elem) left contains x
    else if (x > else) right contains x
    else true

  def incl(x: Int): IntSet = 
    if (x < elem)
      new NonEmpty(elem, left incl x, right)
    else if (x > elem)
      new NonEmpty(elem, left, right incl x)
    else this
}
```

Оба класса <code>Empty</code> и <code>NonEmpty</code> расширяют <code>IntSet</code> и оба соответствуют одному и тому же типу <code>IntSet</code> - объект типа <code>Empty</code> или <code>NonEmpty</code> может быть использован везде, где требуется объект типа <code>IntSet</code>.

<code>IntSet</code> является базовым классом для <code>Empty</code> и <code>NonEmpty</code>, а <code>Empty</code> и <code>NonEmpty</code> являются подклассами класса <code>IntSet</code>.

Классы <code>Empty</code> и <code>NonEmpty</code> реализуют абстрактные определения incl и contains из <code>IntSet</code>. Так же возможно переопределить существующие неабстрактные определения родительского класса в подклассе с помощью ключевого слова override.

```gdscript
abstract class Base {
  def foo = 1
  def bar: Int
}

class Sub extends Base {
  override def foo = 2
  def bar = 3
}
```

#### Value parameters
Для определения полей класса можно в конструкторе использовать ключевое слово val

```scalate server page
class Cons(val head: Int, val tail: IntList) extends IntList {
  // ...
}
```

Эта запись эквивалентна следующему:

```gdscript
class Cons(_head: Int, _tail: IntList) extends IntList {
  val head = _head
  val tail = _tail
  // ...
}
```

#### Синглтоны
В этом примере нужен только один EmptySet, и нет необходимости каждый раз создавать новый объект, и мы можем определить один ''объект-синглтон''. Существует только один объект-синглтон и нельзя создать больше.

```gdscript
object Empty extends IntSet {
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
}
```


#### Traits
Как в Java, так и в Scala, класс может иметь только один суперкласс. Для того, чтобы иметь возможность переиспользования кода из нескольких суперклассов, используются ''trait-ы'' (или ''типажи'' [http://ru.wikipedia.org/wiki/Типаж_(абстрактный_тип)])

Объявление trait-а похоже на объявление абстрактного класса, однако подкласс может использовать несколько trait-ов с помощью ключевого слова with

```gdscript
trait Planar {
  def height
  def width
  def surface = heigh * width
}

class Square extends Shape with Planar with Movable {
  // ...
}
```


Trait-ы похожи на интерфейсы в Java, но 
- они могут содержать поля и
- конкретные методы


### Организация кода
#### Точка входа в приложение
Точкой входа в приложение называется место, с которого начинает выполняться программа. В Scala этим местом является метод main:

```transact-sql
object Hello {
  def main(args: Array[String]) = println("hw|  ") |} |
```


Для того, чтобы запустить приложение, нужно написать

```text only
scala Hello
```

#### Пакеты
Пакеты используются для организации классов и объектов

```transact-sql
package progfun.exmaple

object Hello {
  def main(args: Array[String]) = println("hw|  ") |} |
```

''Полное имя класса'' ('fully-qualified name') состоит из названия пакета и имени класса, например, <code>progfun.example.Hello</code>

Для старта приложения нужно указывать полное имя класса:
```text only
scala progfun.example.Hello
```

#### Импорты
Мы можем ссылаться на класс/объект с помощью его полного имени

```text only
val r = new week3.Rational(1, 2)
```

Но это неудобно, и поэтому можно сделать импорт из другого пакета и затем использовать только короткое имя класса

```python
import week3.Rational
val r = new Rational(1, 2)
```

Так же можно перечислить, какие именно классы нужно импортировать из пакета, или импортировать все
```python
import week3.{Rational, Hello}
import week3._ // wildcard import
```

Импортировать можно не только из пакетов, но и из объектов

Некоторые классы и объекты импортируются автоматически. К их числу относится содержимое следующих пакетов
- java.lang
- scala
- scala.predef


## Типы
### Иерархии типов в Scala
- Базовым типом для всех типов в Scala является тип <code>Any</code>, который содержит базовые методы типа <code>==</code>, <code>|  =</code> и т.п. |- Для всех классов базовым классом является <code>AnyRef</code> (который является синонимом для <code>java.lang.Object</code>) |- Для примитивов базовым типом является тип <code>AnyVal</code>

<img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/class-hierarchy.png" alt="Image">" />


- Тип <code>Nothing</code> находится в самом низу иерархии и является подтипом для всех типов. 
- Так же в Scala существует тип <code>Null</code>, который является типом для значения <code>null</code>. <code>Null</code> является подклассом для всех подклассов <code>AnyRef</code>

```scalate server page
val x = null // x: Null
val y: String = null // y: String
val z: Int = null // error: type mismatch (не подкласс AnyRef)
```


### Параметризованные типы
Рассмотрим ''Cons-список'' - неизменяемый связный список, который строится из следующих элементов
- <code>Cons</code> - ячейка, содержащая элемент и ссылку на следующую часть списка
- <code>Nil</code> - пустой список 

```scalate server page
trait IntList ...
class Cons(val head: Int, val tail: IntList) extends IntList ...
class Nil extends IntList ...
```

Однако это определение слишком узко: такой список можно использовать лишь с типом Int. Но мы можем обобщить определение нашего списка с помощью ''параметров типа''

```scalate server page
trait List[T] ...
class Cons(val head: T, val tail: List[T]) extends List[T] ...
class Nil extends List[T] ...
```

Функции, как и классы, так же могут иметь такие параметры
```transact-sql
def signleton[T](elem: T) = new Cons[T](elem, new Nil[T])
signleton[Int](1)
signleton[Boolean](true)
```

Однако Scala может выводить нужный тип, и поэтому параметр можно опустить
```scdoc
signleton(1)
signleton(true)
```

### Функции как объекты
Функции в Scala являются объектами
Функциональный тип A => B на самом деле является сокращением от scala.Function[A, B], который определён как

```carbon
package scala 
trait Function1[A, B] {
  def apply(x: A): B
}
```

То есть, функции - это объекты, у которых есть метод <code>apply</code>

Объявление анонимной функции можно записать с помощью класса следующим образом:

```gdscript
// anonimous
(x: Int) => x * x

{ 
  class AnonFunc extends Function1[Int, Int] {
    def apply(x: Int) = x * x
  }

  new AnonFunc
}
```

Или, используя синтаксис для объявления анонимных классов

```scdoc
new Function1[Int, Int] {
  def apply(x: Int) = x * x
}
```

Например,

```scdoc
val f = (x: Int) => x * x
f(7)
```

Превращается в

```scdoc
val f = new Function1[Int, Int] {
  def apply(x: Int) = x * x
}
f.apply(7)
```

Методы не являются функциями, но их так же можно использовать, как функции - и они конвертируются в функции автоматически следующим образом

```text only
(x: Int) => f(x)
```


### Подтипы и генерики
#### Граничные типы (Type Bounds)
Рассмотрим метод <code>assertAllPos</code>, который
- Принимает <code>IntSet</code>
- Возвращает полученный <code>IntSet</code>, если все его элементы положительные
- Выбрасывает исключение в противном случае

Какой тип лучше всего подходит для параметра этого метода?

```text only
def assertAllPos(s: IntSet): IntSet
```

Но
- <code>assertAllPos(Empty)</code> должен вернуть <code>Empty</code>
- <code>assertAllPos(NonEmpty)</code> должен вернуть <code>NonEmpty</code>

Это можно сделать с помощью ''верхней границы'' (''upper bound'') параметризованного типа

```text only
def assertAllPos[S <: IntSet](r: S): S = ...
```

Это определение означает, что параметр <code>S</code> может принимать значения только типов, соответствующих <code>IntSet</code> (т.е. являющихся либо объектами этого класса, либо любого из его подклассов).

В общем случае используются следующие обозначения:
- <code>S <: T</code> - верхняя граница (ограничение сверху), <code>S</code> является подтипом <code>T</code>
- <code>S >: T</code> - нижняя граница (ограничение снизу), <code>S</code> является базовым типом (супертипом) для <code>T</code>, или <code>T</code> является подтипом для <code>S</code>

Так же возможно одновременно ограничивать тип как сверху, так и снизу. 
Например, <code>[S >: NonEmpty <: IntSet]</code> ограничивает <code>S</code> между <code>IntSet</code> и <code>NonEmpty</code>.

### Ковариация (Covariance)
Если <code>NonEmpty <: IntSet</code>, выполняется ли <code>List[NonEmpty] <: List[IntSet]</code>?

Такое отношение называется ''ковариацией'', а типы, которые поддерживают это, называются ''ковариантными''. 

Однако ковариация не во всех случаях имеет смысл. Например, массивы в Java ковариантны, но это вызывает ряд проблем. Рассмотрим следующий код:

```text only
NonEmpty[] a = new NonEmpty[] { new NonEmpty(...) }
IntSet[] b = a

b[0] = Empty
NonEmpty s = a[0] // ArrayStoreException
```

#### Принцип подстановки Лисков
Если <code>A <: B</code>, то тогда всё, что можно сделать со значением типа <code>B</code>, должно выполняться и для значений типа <code>A</code>. 


Как видно из примера, ковариация не всегда приносит пользу. Некоторые типы должны быть ковариантными, а некоторые не должны. 
Однако, если соблюсти некоторые условия, то неизменяемые типы могут быть ковариантными. Например, <code>List</code> может быть ковариантным.

Допустим, <code>C[T]</code> - параметризованный тип, а <code>A</code> и <code>B</code> типы, такие, что <code>A <: B</code>. Существуют три возможных отношения между C[A] и C[B]:

- C[A] <: C[B], т.е. тип C[A] является подтипом C[B]. Данное отношение называют ''ковариантным'' (covariant)
- C[A] >: C[B], т.е. тип C[B] является подтипом C[A]. Данное отношение называют ''контравариантным'' (contravariant)
- ни C[A], ни C[B] не являются подтипом друг друга. Такое отношение называют ''невариантным'' (non-variant)

В Scala используют следующие обозначения:
```transact-sql
class C[+A] {...} // covariant
class C[-A] {...} // contravariant
class C[A] {...}  // non-variant
```

#### Типы для функций
- Если <code>A2 <: A1</code> и <code>B1 <: B2</code>,
- <code>то A1 => B1 <: A2 => B2</code>

Т.е. функции контраварианты в типах их аргументах и ковариантны в типах их результатах. 

Таким образом, имеем следующее определение для функций:
```carbon
package scala 

trait Function1[-T, +U] {
  def apply(x: T): U
}
```

В примере с массивом проблемной операцией была операция обновления массива. Если представить массив в виде класса, то получим 
```perl6
class Array[+T] {
  def update(x: T)
}
```

В этом классе проблема вызвана
- Ковариантным параметром типа <code>T</code>
- Который используется для параметра в методе <code>update</code>

Компилятор Scala проверяет, что в коде нет таких проблемных комбинаций. 

Итого,
- Ковариантные типы могут быть использованы только в результатах методов
- Контравариантные типы только в параметрах методов
- Инвариантные методы могут использоваться везде

Мы можем сделать <code>List</code> ковариантным
```transact-sql
trait List[+T] {...}
object EmptyList extends List[Nothing] {...}
```

Мы хотели бы иметь объект-синглтон для пустого списка, ведь для пустого списка разницы нет, что внутри, он всегда пуст. 


Рассмотрим метод <code>prepend</code> который добавляет новый элемент и возвращает новый список 
```transact-sql
trait List[+T] {
  def prepend(elem: T): List[T] = new Cons(elem, this)
}
```

Такое определение не пройдет проверку на вариантность, так как ковариантный тип, использующийся в параметре метода. 

Более того, это нарушает принцип подстановки Лисков. Пусть у нас есть список <code>xs</code> типа <code>List[IntSet]</code>

```text only
xs.prepend(Empty)
```

К такому списку пустое множество. Но если рассмотреть список <code>ys</code> типа <code>List[NonEmpty]</code>, то мы получим ошибку при попытке присоединить пустой список:

```carbon
ys.prepend(Empty) // type mismatch, required: NonEmpty, found: Empty
```

Т.е. <code>List[NonEmpty]</code> не может быть подтипом <code>List[IntSet]</code>

Каким образом можно исправить это?

Мы можем ограничить снизу параметр типа для метода <code>prepend</code>

```transact-sql
def prepend[U >: T](elem: U): List[U] = new Cons(elem, this)
```

Это проходит проверку на вариантность потому что
- ковариантные параметры типов могут использоваться в качестве нижней границы для типов в методах
- аналогично, контравариантные параметры типов могут использоваться в качестве верхней границы

И, наконец, рассмотрим следующую функцию

```transact-sql
def f(xs: List[NonEmpty], x: Empty) = xs prepend x
```

Типом возвращаемого значения этой функции будет <code>List[IntSet]</code>



## Сопоставление с образцом (Pattern Matching)
В качестве примера рассмотрим небольшой интерпретатор для арифметических операций. Все выражения могут быть представлены в виде иерархии классов, с базовым trait-ом <code>Expr</code> и подклассами <code>Number</code> и <code>Sum</code> (ограничимся только числами и операцией сложения).

Мы можем использовать ООП-подход 
```gdscript
trait Expr {
  def eval: Int
}

class Number(n: Int) extends Expr {
  def eval: Int = n
}

class Sum(e1: Expr, e2: Expr) extends Expr {
  def eval: Int = e1.eval + e2.eval
}
```

Ограничение такого подхода:
- Что если мы захотим упростить выражения, используя некоторый набор правил? 
- Например $a \cdot b + a \cdot c = a \cdot (b + c)$. 
- Проблема состоит в том, что это упрощение не локальное, т.е. его нельзя инкапсулировать в метод только одного объекта 
- Необходимо вносить изменения во все классы при добавлении нового метода

### Case Classes
Рассмотрим следующее определение:
```gdscript
trait Expr
case class Number(n: Int) extends Expr
case classs Sum(e1: Expr, e2: Expr) extends Expr

object Number {
  def apply(n: Int) = new Number(n)
}

object Sum {
  def apply(e1: Expr, e2: Expr) = new Sum(e1, e2)
}
```

Объекты <code>Number</code> и <code>Sum</code> нужны для того, чтобы можно было писать <code>Number(1)</code> вместо <code>new Number(1)</code> (такие объекты называются ''companion objects'').

''Сопоставление с образцом (pattern matching)'' - генерализация конструкции <code>switch</code> из java для иерархий классов. Классы, помеченные ключевым словом <code>case</code> могут использоваться в конструкциях сопоставления с образцом. 

```text only
def eval(e: Expr): Int = e match {
  case Number => n
  case Sum(e1, e2) => eval(e1) + eval(e2)
}
```

Правила объявления:
- используется ключевое слово <code>match</code> и
- последовательность вида <code>pattern => expression</code> для каждого из ''случаев (case)''
- для каждого случая производится сопоставление выражения expression с образцом <code>pattern</code>
- если ни один из образцом нельзя сопоставить с данным значением, выкидывается ошибка <code>MatchError</code>

### Формы образцов
Образцы можно составить из
- конструкторов (например, <code>Number</code>, <code>Sum</code>)
- переменных (<code>n</code>, <code>e1</code>, <code>e2</code>)
- wildcard образцов (<code>_</code>), которые сопоставляются с любым значением
- константы, например, <code>1</code>, <code>true</code> и т.п.

Например, конструктор <code>Sum(x, y)</code> сопоставляется с объектом типа <code>Sum</code>, а в переменные <code>x</code> и <code>y</code> записываются значения для левого и правого операнда.

Также, в качестве образцов можно использовать кортежи (пары и т.п.) и списки (подробнее см. ниже)
- <code>case (c, count)</code> сопоставляется с парой, в <code>c</code> записывается первое значение, в <code>count</code> второе
- <code>x :: xs</code> сопоставляется со списком, в <code>x</code> записывается голова списка, в <code>xs</code> - хвост


Примеры:
```transact-sql
def singleton(trees: List[CodeTree]): Boolean = trees match {
  case x :: Nil => true
  case _ => false
}
```

```scdoc
def nextBranch(tree: Fork, bit: Bit): CodeTree = bit match {
  case 0 => tree.left
  case 1 => tree.right
  case _ => throw new IllegalArgumentException("unexpected value for bit: " + bit)
}
```

```transact-sql
def decode1(currentBranch: CodeTree, bits: List[Bit]): List[Char] = (currentBranch, bits) match {
  case (Leaf(char, _), Nil) => List(char)
  case (fork: Fork, head :: tail) => decode1(nextBranch(fork, head), tail)
  case (Leaf(char, _), head :: tail) => char :: decode1(tree, bits)
  case (_: Fork, Nil) => throw new IllegalStateException("the sequence of bits ended abruptly")
  case _ => throw new IllegalStateException()
}
```


Также можно использовать для каждого из образцов ''граничное условие'', только при соблюдении которого будет выполняться выражение. Например, 
```transact-sql
def positiveSingleton(xs: List[Int]): Boolean = xs match {
  case x :: Nil if x > 0 => true
  case _ => false
}
```


## Списки
Список, состоящий из элементов $x_1, ..., x_n$ в Scala записывается следующим образом:

```text only
List(x1, ..., xn)
```

Основные характеристики списков:
- Списки неизменяемые
- Списки заданы рекурсивно (список состоит из элемента, называемого ''головой списка'', и списка, называемого ''хвостом списка'').
- Списки ''гомогенны'' - т.е. могут состоять только из элементов одного и того же типа

В Scala списки составляются при помощи 
- Пустого списка <code>Nil</code>
- Оператора <code>::</code> (он же <code>Cons</code>) для присоединения нового элемента списка 

### Операции со списками
```text only
x :: xs
```
Присоединяет элемент $x$ к списку $xs$

```text only
fruit = "apples" :: ("pears" :: Nil)
nums = 1 :: (2 :: (3 :: Nil))
empty = Nil
```

Операция <code>::</code> право-ассоциативная, поэтому скобки можно опустить
```text only
fruit = "apples" :: "pears" :: Nil
nums = 1 :: 2 :: 3 :: Nil
```

Операция <code>::</code> является методом, поэтому следующие две записи эквивалентны
```text only
nums = 1 :: 2 :: 3 :: Nil
nums = Nil.::(3).::(2).::(1)
```

Cписки можно использовать в сопоставлениях с образцом
- <code>Nil</code> или <code>List()</code> сопоставляются с пустым списком 
- <code>x :: xs</code> сопоставляется с головой списка <code>x</code> и хвостом <code>xs</code>
- <code>List(x1, x2, x3)</code> сопоставляется со списком, состоящим из трех элементов 


Пример: сортировка вставками
```transact-sql
def sort(xs: List[Int]): List[Int] = xs match {
  case List() => List(x)
  case y :: ys => if (x <= y) x :: xs else y :: insert(x, ys)
}
```

Помимо этого, у списков определены следующие методы
- <code>xs.head</code> - возвращает первый элемент списка
- <code>xs.tail</code> - возвращает все элементы, кроме первого
- <code>xs.isEmpty</code> возвращает <code>true</code>, если список пуст, <code>false</code> в противном случае

Также:
- <code>xs.length</code> - длина списка
- <code>xs.last</code> - последний элемент
- <code>xs.init</code> - все элементы, кроме последнего
- <code>xs take n</code> - возвращает первые <code>n</code> элементов списка (или сам <code>xs</code>, если он содержит меньше, чем <code>n</code> элементов)
- <code>xs drop n</code> - возвращает список, полученный из данного путём отбрасывания первых <code>n</code> элементов 
- <code>xs(i)</code> или <code>xs.apply(i)</code> - возвращает <code>i</code>-тый элемент списка
- <code>xs ++ ys</code> - соединяет два списка
- <code>xs.reverse</code> - разворачивает список
- <code>xs.updated(n, x)</code> - возвращает список, полученный из данного, в котором на позиции <code>n</code> расположен элемент <code>x</code>
- <code>xs.indexOf(x)</code> - индекс элемента <code>x</code> в списке
- <code>xs.contains(x)</code> - <code>true</code> если элемент содержится в списке

=== Функции высшего порядка для списков === 
При обработке списков следующие задачи встречаются наиболее часто
- Трансформация каждого элемента списка
- Фильтрация элементов 
- Компоновка всех значений списка в одно

#### Map
Применяет функцию к каждому элементу 

```transact-sql
class List[T] {

  def map[U](f: T => U): List[U] = this match {
    case Nil => this
    case x :: xs => f(x) :: xs.map(f)
  }

}

val scaled = xs.map(x => x * factor)
val squares = xs.map(x => x * x)
```

#### Filter
Фильтрует элементы, удовлетворяющие некоторому условию

```transact-sql
class List[T] {
  def filter(p: T => Boolean): List[T] = this match {
    case Nil => this
    case x :: xs => if (p(x))
                      x :: xs.filter(p)
                    else
                      xs.filter(p)
  }
}
```

Вариации функции <code>filter</code>
- <code>xs filterNot</code> - то же самое, что <code>xs filter (x => |  p(x))</code> |- <code>xs partition p</code> - то же самое, что <code>(xs filter p, xs filterNot p)</code>, но выполненное за один проход |- <code>xs takeWhile p</code> - возвращает префикс списка, удовлетворяющие предикату
- <code>xs dropWhile p</code> - остаток списка после удаления элементов, удовлетворяющие предикату
- <code>xs span p</code> - то же самое, что <code>(xs takeWhile p, xs dropWhile p)</code>, но выполненное за один проход

Пример:
Функция <code>pack</code>, выполняющая следующее преобразование:

```text only
"a","a","a","b","c","c","c","a" => List("a","a","a"), List("b"), List("c","c","c"), List("a")
```

```transact-sql
def pack[T](xs: List[T]): List[List[T]] = xs match {
  case Nil => Nil
  case x :: xs1 => {
    (l, r) = xs.span(el => x == el)
    List(l) :: pack(r)
  }
}
```

#### Reduce
Редуцирует список.

Часто используемая операция, например
- сумма: $0 + x_1 + x_2 + ... + x_n$
- произведение: $1 \cdot x_1 \cdot x_2 \cdot ... \cdot x_n$

<code>reduceLeft</code>
```transact-sql
def sum(xs: List[Int]) = 
  (0 :: xs) reduceLeft((x, y) => x + y)

def product(xs: List[Int]) = 
  (1 :: xs) reduceLeft((x, y) => x * y)
```

Вместо того, чтобы писать <code>(x, y) => x + y</code>, можно написать <code>(_ * _)</code>
Каждый из <code>_</code> представляет собой параметр, поэтому функции выше можно переписать следующим образом:

```transact-sql
def sum(xs: List[Int]) = 
  (0 :: xs) reduceLeft(_ + _)

def product(xs: List[Int]) = 
  (1 :: xs) reduceLeft(_ * _)
```


<code>reduceLeft</code> определена с помощью более общей функции <code>foldLeft</code>. <code>foldLeft</code> работает примерно так же, как и <code>reduceLeft</code>, но в качестве аргумента так же принимает аккумулятор - значение, которое будет возвращено, при применении функции к пустому списку.

Таким образом, сумма и произведение могут быть записаны как

```transact-sql
def sum(xs: List[Int]) = 
  (xs foldLeft 0) reduceLeft(_ + _)

def product(xs: List[Int]) = 
  (xs foldRight 1) reduceLeft(_ * _)
```


Реализовать эти две функции можно следующим образом:

```transact-sql
class List[T] {
  def reduceLeft(op: (T, T) => T): T = this match {
    case Nil => throw ...
    case x :: xs => (xs foldLeft x)(op)
  }

  def foldLeft[U](z: U)(op: (U, T) => U): U = this match {
    case Nil => z
    case x :: xs => (xs foldLeft op(z, x))(op)
  }
}
```


Помимо <code>foldLeft</code> и <code>reduceLeft</code> так же определены функции <code>foldRight</code> и <code>reduceRight</code>

```transact-sql
class List[T] {
  def reduceRight(op: (T, T) => T): T = this match {
    case Nil => throw ...
    case x :: Nil => x
    case x :: xs => op(x, xs.reduceRight(op))
  }

  def foldRight[U](z: U)(op: (T, U) => U): U = this match {
    case Nil => z
    case x :: xs => op(x, (xs foldRight z)(op))
  }
}
```

Для операций, которые ассоциативные и коммутативные, функции <code>foldLeft</code> и <code>foldRight</code> эквивалентны, однако одна из них может быть более эффективной. 


## Коллекции
### Vector
Списки линейны, т.е. доступ к первому элементу списка очень быстрый, однако для того, чтобы получить элемент в середине или в конце, нужно пройти все предыдущие элементы. 

Однако в Scala существуют альтернативные реализации последовательностей (интерфейс <code>Seq</code>), например, <code>Vector</code>, который предоставляет более эффективные операции доступа к элементам.

```text only
val nums = Vector(1, 2, 3)
val people = Vector("Bob", "James", "Peter")
```

Векторы поддерживают те же самые операции, что и списки, за исключением операции <code>::</code>. Вместо неё определены следующие операции:

- <code>x +: xs</code> - создаёт новый вектор с элементом x в начале 
- <code>xs :+ s</code> - создаёт новый вектор с элементом x в конце

### Range
Объекты типа <code>Range</code> служат представлением равномерно распределённых целых чисел

Создаются с помощью трех операций:
- <code>to</code> (включительно)
- <code>until</code> (исключительно)
- <code>by</code> (шаг)

```scalate server page
val r: Range = 1 until 5 // 1, 2, 3, 4
val s: Range = 1 to 5 // 1, 2, 3, 4, 5

1 to 10 by 3 // 1, 4, 7, 10
6 to 1 by -2 // 6, 4, 2
```

### Seq
<code>Seq</code> - общий базовый класс для классов <code>Vector</code>, <code>List</code> и <code>Range</code>:

<img src="<img src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/legacy/collections-hier.png" alt="Image">" />

Строки (тип <code>String</code>) и массивы (тип <code>Array</code>) поддерживают те же самые операции, что и Seq, и неявно конвертируюся в тип <code>Seq</code> когда нужно (но они не могут быть подклассами последовательности, т.к. они из Java)

Для объектов класса Seq так же определяются следующие операции:
- <code>xs exists p</code> - <code>true</code> если хотя бы один элемент удовлетворяет <code>p</code>
- <code>xs forall p</code> - <code>true</code> если все элементы удовлетворяют <code>p</code>
- <code>xs zip ys</code> - возвращает последовательность пар, составленных из соотвествующих элементов из xs и ys
- <code>xs unzip ys</code> - операция, обратная <code>zip</code>
- <code>xs flatMap f</code> - для тех случаев, когда f возвращает коллекцию, flatMap "склеивает" общий результат в одну коллекцию

И так же
- <code>xs.sum</code>
- <code>xs.product</code>
- <code>xs.max</code>
- <code>xs.min</code>

<code>Примеры</code>

Все комбинации для $x \in [1..M]$ и $y \in [1..N]$

```text only
(1 to M) flatMap (x => (1 to N) map (y => (x, y)))
```


Скалярное произведение двух векторов:
```transact-sql
def scalarProduct(xs: Vector[Double], ys: Vector[Double]): Double = 
  (xs zip ys).map(xy => xy._1 * xy._2).sum
```

Что, используя сопоставление с образцом (pattern matching function value), можно записать следующим образом:

```scdoc
(xs zip ys).map { case (x, y) = x * y }.sum
```


Проверка числа на простоту
```carbon
def isPrime(n: Int): Boolean =
  (2 until n) forall (d => u % d |  = 0) |
``` |
### For-Expressions
Из списка людей мы хотим вывести имена тех, кто старше 20:

```text only
persons filter (p => p.age > 20) map (p => p.name)
```

Анологичное мы можем сделать с помощью конструкции <code>for</code>:

```s
for (p <- persons if p.age < 20) yield p.name
```

Синтакс:
```tera term macro
for (s) yield e
```

Где 
- <code>s</code> - последовательность генераторов и фильтров
- <code>e</code> - выражение, которое будет возвращено для каждого объекта

- генератор имеет вид <code>p <- e</code>
  - <code>p</code> - образец
  - <code>e</code> - выражение
- фильтр имеет вид <code>if f</code>
  - <code>f</code> - выражение, возвращающее <code>Boolean</code>

Последовательность должна начинаться с генератора. Если генераторов несколько, последний генератор изменяется быстрее, чем первый.

Вместо круглых скобок можно использовать <code>{}</code>, и тогда генераторы можно записывать в несколько строк

```s
for {
  i <- 1 until n
  j <- i until i
  if isPrime(i + j)
} yield (i, j)
```

Таким образом, скалярное произведение можно записать так:
```s
(for ((x, y) <- xs zip ys) yield y * x).sum
```

### Set
Тип данных, представляющий множество - коллекцию, в которой элементы не повторяются.

```text only
val fruit = Set("apple", "banana", "pear")
val s = (1 to 6).toSet
```

Большинство операций для последовательностей так же доступны и для множеств:

```scdoc
s map (_ + 2)
fruit filter (_.startsWith("app"))
```

### Пример: 8 Queens
Проблема [http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-15.html#%_thm_2.42]: как расставить $N$ ферзей так, чтобы ни один не мог сбить другого. Т.е. требуется расставить ферзей так, чтобы ни один из них не был на одной горизонтали, вертикали или диагонали. 

Алгоритм:
- допустим, мы уже имеем решение для первых $k-1$ ферзей на доске размера $n$
- каждое решение - это список длины $k-1$, содержащий номера вертикалей, на которых стоят ферзи (от 0 до $n-1$)
- для того, чтобы поставить ферзя на $k$-ю вертикаль, мы генерируем все возможные позиции и отфильтровываем те, в которых условия нарушаются

```transact-sql
def queens(n: Int) = {
  def placeQueens(k: Int): Set[List[Int]] = {
    if (k == 0)
      Set(List())
    else
      for {
        queens <- placeQueens(k - 1)
        col <- 0 until n
        if isSafe(col, queens)
      } yield col :: queens
  }
  placeQueens(n)
}

def isSafe(col: Int, queens: List[Int]): Boolean = ...
```

### Map (Структура данных)
Map[Key, Value] - ассоциативный контейнер для пар ключ-значение. 

```ecl
val roman = Map("I" -> 1, "V" -> 5, "X" -> 10)
val capitals = Map("US" -> "Washington", "Switzerland" -> "Bern")
```

Класс Map[Key, Value] расширяет класс Iterable[(Key, Value)], так что с объектами этого типа можно делать всё, что угодно:

```text only
val countries = capitals map { case (x, y) => (y, x) }
```

Для извлечения нужно просто применить мапу к ключу:

```text only
capital("Andorra")
```

Однако если ключа не существует, будет выброшено <code>java.utils.NoSuchElement</code>

Однако можно использовать метод get, который всегда возвращает значения типа Option

#### Option
Объекты типа <code>Option</code> бывают двух типов: в одном содержится какое-то значение, а другое всегда пустое. 

```transact-sql
trait Option[+A]
case class Some[+A](value: A) extends Option[A]
object None extends Option[Nothing]
```

Метод <code>get</code> возвращает
- <code>None</code>, если мапа не содержит ключ
- <code>Some(x)</code>, если содержит

```text only
def showCapital(country: String) = capital.get(country) match {
  case Some(capital) => capital
  case None => "missing data"
}
```

#### Group By
Коллекцию превратить в <code>Map</code> коллекций можно с помощью операции <code>groupBy</code>:
```scdoc
fruit groupBy(_.head)
```

Вернет
```ecl
Map(
  p -> List(pear, pineapple),
  a -> List(apple),
  o -> List(orange)
)
```

Так же можно создать мапу со значением по умолчанию, которое будет использоваться в случаях, когда ключ не найден
```text only
val cap1 = capitals withDefaultValue "unknown"
cap1("Andorra") // "unknown"
```

#### Параметры переменной длины
Допустим, у нас есть класс <code>Polynom</code>:

```ecl
Polynom(Map(1 -> 2.0, 3 -> 4.0, 5 -> 6.2))
```

Можно ли избежать передачи <code>Map</code>? Мы можем использовать параметр с повторением ("repeated parameter")

```scdoc
def Polynom(bindings: (Int, Double)*) = 
  new Polynom(bindings.toMap withDefaultValue 0)
```

Теперь можно это использовать без <code>Map</code>:

```ecl
Polynom(1 -> 2.0, 3 -> 4.0, 5 -> 6.2)
```


## Ленивые вычисления
### Stream
[http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-24.html#%_sec_3.5]. Дана задача: вычислить второе простое число в последовательности между 1000 и 10000.

```scdoc
((1000 to 10000) filter isPrime)(1)
```

Но этот код находит _все_ простые числа в заданном промежутке, но использует только 2.

Мы могли бы снизить верхнюю границу промежутка, но при этом рискуя тем, что второго простого числа в интервале просто может не оказаться. 

Однако мы можем избежать вычисления хвоста последовательности до тех пор, пока он явно не понадобится. 

Структура данных Stream построена на этом принципе, и внутри очень похожа на список. Единственное отличие: хвост стрима вычисляется только тогда, когда нужно. 

```text only
Stream.cons(1, Stream.cons(2, Stream.empty))
Stream(1, 2, 3)
```

Коллекции имеют специальный метод для получения Stream:

```transact-sql
(1 to 1000).toStream // > Stream[Int] = Stream(1, ?)
```

Все операции для списков можно применять и для этой структуры данных. 

Например,

```scdoc
((1000 to 10000).toStream filter isPrime)(1)
```

Однако <code>::</code> всегда создает список, а не Stream, поэтому для них используется <code>#::</code>:

```text only
x #:: xs == Stream.cons(x, xs)
```

Реализация стрима очень похожа на реализацию списка. Однако есть одно существенное отличие:

```transact-sql
def cons[T](hd: T, tl: => Stream) = new Stream {
  def isEmpty = false
  def head = hd
  def tail = tl
}
```

Для параметра <code>tl</code> используется передача по имени, а не по значению. Именно поэтому хвост вычисляется только тогда, когда необходимо. 

### Lazy Evaluation
Однако предложенная выше реализация имеет недостаток, из-за которого существенно страдает производительность: eсли элемент списка затребован несколько раз, каждый раз будет вычисляться весь список. 

Этого можно избежать, если при первом вызове сохранять вычисленное значение и при втором запросе возвращать уже заранее посчитанные данные.

Этот приём называется ''ленивая инициализация'', и в Scala осуществляется с помощью ключевого слова <code>lazy</code>:

```text only
lazy val x = expression
```

Таким образом, Stream можно переписать так:

```transact-sql
def cons[T](hd: T, tl: => Stream) = new Stream {
  def isEmpty = false
  def head = hd
  lazy val tail = tl
}
```

### Бесконечные последовательности
С помощью стримов можно создавать последовательности неограниченного размера [http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-24.html#%_sec_3.5.2]:

```transact-sql
def from(n: Int): Stream[Int] = n #:: from(n + 1)
val natural = from(0)
natural map (_ * 4)
```

При этом, если <code>for-expression</code> применить к бесконечному списку, результат так же будет ленивым

```s
val legals = b.legalNeighbors.toStream
for ((nextBlock, move) <- legals) yield (nextBlock, move :: history)
```

### Пример: Решето Эратосфена
Для вычисления простых чисел:
- Начинаем с $i = 2$
- Убираем из результата все делители $i$
- Переходим к следующему элементу результата и повторяем

```transact-sql
def sieve(s: Stream[Int]): Stream[Int] =
  s.head #:: sieve(s.tail filter (_ % s.head |  = 0)) | |val primes = sieve(from(2))

(primes take N).toList
```


## Остальное
### Кортежи и пары
Рассмотрим сортировку слиянием

Алгоритм:
- Разделить список пополам
- Отсортировать полученные подсписки
- Слить их в один отсортированный список

```transact-sql
def msort(xs: List[Int]): List[Int] = {
  val n = xs.length / 2
  if (n == 0) {
    xs
  } else {
    val (fst, snd) = xs splitAt n
    merge(msort(fst), msort(snd))
  }
}

def merge(xs: List[Int], ys: List[Int]) = xs match {
  case Nil => ys 
  case x :: xs1 =>
    ys match {
      case Nil => xs
      case y :: ys1 =>
        if (x < y) x :: merge(xs1, ys)
        else y :: merge(xs, ys1)
    }
}
```

В этом примере функция <code>splitAt</code> возвращает два подсписка, в виде ''пары''.

В Scala пара записывается в виде <code>(x1, x2)</code>

```text only
val pair = ("answer", 12) // тип: (String, Int)
```

Пары могут быть использованы в сопоставлениях с образцом:

```text only
val (label, value) = pair 
laber == "answer"
value == 12
```

Пара является кортежем из двух элементов, и для кортежей болей размерности все вышеперечисленное работает. 

Так как пары можно использовать в сопоставлениях с образцом, то функцию <code>merge</code> можно переписать следующим образом:

```transact-sql
def merge(xs: List[Int], ys: List[Int]): List[Int] = (xs, ys) match {
  case (Nil, _) => ys
  case (_, Nil) => xs
  case (x :: xs1, y :: ys1) =>
    if (x < y) 
      x :: merge(xs1, ys)
    else 
      y :: merge(xs, ys1)
}
```

### Неявные параметры
Функция <code>msort</code> сортирует только числа. Как сделать её более общей? 

Например, можно передавать функцию для сравнения двух объектов 

```transact-sql
def msort[T](xs: List[T], ys: List[T])(lt: (T, T) => Boolean): List[T] = {
  ...

  def merge[T](xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
    ...
    case (x :: xs1, y :: ys1) =>
      if (ls(x, y)) 
        ...
  }

  merge(msort(fst)(lt), msort(snd)(lt))
}

msort(xs)((x, y) => x < y)
msort(xs)((x, y) => x.compareTo(y) < 0)
```

В Scala уже есть функции для сравнения, которые можно использовать:

```python
import math.Ordering
msort(nums)(Ordering.Int)
msort(fruits)(Ordering.String)
```

Однако в этой реализации есть проблема: необходимо постоянно передавать параметр ls. Однако можно этого избежать при помощи неявных параметров (implicit parameters)

```transact-sql
def msort[T](xs: List)(implicit ord: Ordering) = {
  ...

  def merge(xs: List[T], ys: List[T]) = {
    ...
    if (ls(x, y)) 
    ...
  }

  merge(msort(fst), msort(snd))
}
```

Теперь можно целиком избежать передачи последнего параметра, компилятор найдёт правильное значение нужного типа для неявно заданного параметра 

```python
import math.Ordering
msort(nums)
msort(fruits)
```

Для того, чтобы значения могли использоваться компилятором неявно, они должны удовлетворять следующим правилам
- должны быть помечены с помощью ключевого слова <code>implicit</code>
- иметь соответствующий тип
- и быть видимыми

Во всех остальных случаях будет выброшено исключение

[Category:Russian](Category_Russian)
[Category:Functional Programming](Category_Functional_Programming)
[Category:Coursera](Category_Coursera)
[Category:Scala](Category_Scala)