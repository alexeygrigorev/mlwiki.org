---
layout: default
permalink: /index.php/Apache_Mahout_Samsara
tags:
- machine-learning
- hadoop
title: "Apache Mahout Samsara: The Quick Start"
---


<a href="https://mahout.apache.org/"><img src="http://habrastorage.org/files/acf/77c/9c5/acf77c9c55b94e42b0ed2ecd2435c70a.png" alt="Mahout"></a>

Last week the newest [Apache Mahout](https://mahout.apache.org/) 0.10 [was released](http://mail-archives.us.apache.org/mod_mbox/www-announce/201504.mbox/%3CCAOtpBjhD7kG_JSdTkZDQwrQSh7xwMnnQqUYMzp-Ct5qFSBe=GQ@mail.gmail.com%3E). One of the new features it has is a new math environment called "Samsara", or Mahout Scala/Spark Bindings. 

Samsara is a Linear Algebra library for Mahout. It's written in Scala, which makes it possible to use operator overloading and it features nice R-like or Matlab-like syntax for basic Linear Algebra operations. For example, matrix multiplication is just `X %*% Y`.  What is more, these operations can be distributed and run by an executing environment - currently by Apache Spark.  

In this article we will see how to quickly set up a basic skeleton project and then we'll try to do some very simple analysis on a 200 MB dataset. 


We will use: 

- Java 1.7, Scala 2.10.4 
- Scala IDE or any other IDE with a Scala plugin
- Apache Maven
- Apache Mahout and Apache Spark

The code is available on [github](https://github.com/alexeygrigorev/itshared-howto/tree/master/mahout-spark-binding).

## Preliminaries

This article is based on and inspired by the article [Playing with Mahout's Spark Shell](https://mahout.apache.org/users/sparkbindings/play-with-shell.html), so you may want to read it before continuing. Also, the [Scala and Spark Bindings manual](https://mahout.apache.org/users/sparkbindings/ScalaSparkBindings.pdf) gives a good overview of the syntax. 

Before we start, let me introduce you to a couple of concepts that we will use throughout this post.

- RDD, which stands for "Resilient Distributed Dataset", is the basic abstraction for Apache Spark data flows. You can read about them in Spark official documentation, for example, in the official [Quick Start guide](https://spark.apache.org/docs/latest/quick-start.html).
- DRM, which stands for "Distributed Row Matrix", is the main abstraction for matrices in Apache Mahout: these are matrices that are distributed and stored by rows. DRMs can be backed by Spark's RDDs or anything else, e.g. Apache Hadoop or Apache Flink. 
- in-core matrices/vectors - it's the "opposite" of DRM: they are usual matrices or vectors that are kept in the memory of JVM, they are not distributed. 

DRMs could be of two types: one row at a time or by blocks ("blockified"). Let's illustrate this.  Suppose we have the following matrix:

$$\mathbf X = \begin{bmatrix}
2 & 2 & 10.5 & 10 \\
1 & 2 & 12 & 12 \\
1 & 1 & 12 & 13 \\
2 & 1 & 11 & 13 \\
1 & 2 & 12 & 11 \\
2 & 1 & 16 & 8 \\
6 & 2 & 17 & 1 \\
3 & 2 & 13 & 7 \\
3 & 3 & 13 & 4 \\
\end{bmatrix}$$

If we index it by rows, and then store one row at a time, we will have the following representation: 

![](http://habrastorage.org/files/d75/076/3ad/d750763ad90840f7904680e92e42fe5c.png)

So, here it's a distributed collection of `(Int, Vector)` pairs. 

But we can also take blocks of the matrix - i.e. several rows at a time:

![](http://habrastorage.org/files/7bc/a99/e55/7bca99e55fa64a59911218f934e84c55.png)

In this representation, it's a distributed collection of `(Array[Int], Matrix)` pairs. 

Under the hood, Mahout usually operates on DRMs of the second type, i.e. "blockified" DRMs because typically it's more efficient. 

Math 
-------

Let's very briefly review some math we need for this article. 

First, we will go over the basics of [Ordinary Least Squares](http://en.wikipedia.org/wiki/Ordinary_least_squares) (OLS) Regression. In short, for OLS we are given a dataset $\mathcal D = \{ (\mathbf x_i, y_i) \}$, where $\mathbf x_i$ are vectors of observed "predictors" or features and $y_i$ are observed values ("responses"). We put all $\mathbf x_1, \ ... \ , \mathbf x_N$ as rows into a matrix $\mathbf X$ (sometimes called the "design" or "data" matrix) and all $y_i$  in a vector $\mathbf y = (y_1, \ ... \ , y_N)$ of observed values ("responses"). The goal is to find $\hat{\mathbf w}$ such that minimizes the squared error $\| \mathbf X \hat{\mathbf w} - \mathbf y \|^2$.

This problem can be solved with the Normal Equation: we need to find a solution to the system $\mathbf X^\mathbf T \mathbf X \hat {\mathbf w} = \mathbf X^\mathbf T \mathbf y$, and the solution is $\hat {\mathbf w} = (\mathbf X^\mathbf T \mathbf X)^{-1} \mathbf X^\mathbf T \mathbf y$.

For a new unseen data item $\mathbf x$ the predicted value $\hat y$ is $\hat y = \mathbf x^\mathbf T \, \hat{\mathbf w} = x_1 \, w_1 + \ ... \ + x_p \, w_p$. Note that it's a line, and we usually should have an interception term $w_0$, so instead we need to write $\hat y = w_0 + x_1 \, w_1 + \ ... \ + x_p \, w_p = w_0 + \mathbf x^\mathbf T \, \hat{\mathbf w}$. To incorporate this intercept, we add a *bias term* $x_0 = 1$ for all observations: i.e. we add an additional row to $\mathbf X$ and this row contains only ones. With this we can easily write $\mathbf x^\mathbf T \, \hat{\mathbf w}$. 

<!-- You can read more about OLS Regression and Least Squares in our blogpost [The Least Squares: Projection onto Subspaces](http://www.itshared.org/2015/04/the-least-squares-projection-onto.html) -->

Ridge Regression is a regularized version of the OLS regression, and instead of solving $(\mathbf X^\mathbf T \mathbf X) \, \mathbf {\hat w} = \mathbf X^\mathbf T \mathbf y$ we solve $(\mathbf X^\mathbf T \mathbf X + \mathbf I \lambda) \, \mathbf {\hat w} = \mathbf X^\mathbf T \mathbf y$. 

For Ridge Regression it is important to standardize the data (for reasons described [here](http://stats.stackexchange.com/questions/111017/question-about-standardizing-in-ridge-regression)).  Usually it's done by applying [$Z$-standardization](http://en.wikipedia.org/wiki/Standard_score): let $\boldsymbol \mu$ be the mean over all observations and let $\boldsymbol \sigma$ be the standard deviation, and then each item $\mathbf x$ is standardized as $\tilde {\mathbf x} = \cfrac{\mathbf x - \boldsymbol \mu}{\boldsymbol \sigma}$.

Lastly, [Dimensionality Reduction](http://en.wikipedia.org/wiki/Dimensionality_reduction) is a set of techniques for transforming a high-dimensional data into some lower-dimensional representation. [Principal Component Analysis](http://en.wikipedia.org/wiki/Principal_component_analysis) is the most popular method, and it is typically done via [Singular Value Decomposition](http://en.wikipedia.org/wiki/Singular_value_decomposition). It is [important to center the data](http://stats.stackexchange.com/questions/22329/how-does-centering-the-data-get-rid-of-the-intercept-in-regression-and-pca) (i.e. subtract the mean of each column) before applying PCA. 

For more detailed theory I would recommend to refer to two excellent books [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) and [The Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/), both freely available as pdf to download.

And now we're ready to start. 

## The Cereal Regression

To get started, let's first try to reproduce the OLS regression example on the cereals dataset from the [cereals manual](https://mahout.apache.org/users/sparkbindings/play-with-shell.html). 

But before that, you need to have an IDE that supports Scala. I personally prefer the Eclipse-based [Scala IDE](http://scala-ide.org/download/sdk.html), but any other IDE with Scala plugin should be equally good. Also, make sure you're running Scala 2.10.x: if it's Scala 2.11 or greater, it might not work, because some packages are built under 2.10 and might not work for the latest Scala compilers. 

Then we need to tell Maven that we're going to use Scala. To do this, add the following lines to your `<plugins>` section

    <plugin>
      <groupId>net.alchim31.maven</groupId>
      <artifactId>scala-maven-plugin</artifactId>
      <version>3.1.3</version>
      <executions>
        <execution>
          <goals>
            <goal>add-source</goal>
            <goal>compile</goal>
            <goal>testCompile</goal>
          </goals>
        </execution>
      </executions>
    </plugin>

Now we can add dependencies to Mahout Math, Mahout Scala Bindings and Mahout Spark Bindings. You'll also need Spark dependency as well

    <dependency>
      <groupId>org.apache.mahout</groupId>
      <artifactId>mahout-math</artifactId>
      <version>${mahout.math.version}</version>
    </dependency>
    <dependency>
      <groupId>org.apache.mahout</groupId>
      <artifactId>mahout-math-scala_2.10</artifactId>
      <version>${mahout.math.version}</version>
    </dependency>
    <dependency>
      <groupId>org.apache.mahout</groupId>
      <artifactId>mahout-spark_2.10</artifactId>
      <version>${mahout.math.version}</version>
    </dependency>
    <dependency> 
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-core_2.10</artifactId>
      <version>${spark.version}</version>
    </dependency>

Additionally, add this to your `<properties>` section:

    <mahout.math.version>0.10.0</mahout.math.version>
    <spark.version>1.1.1</spark.version>

The latest version of Spark is 1.3.0, but the Mahout Spark Binding is built with Spark 1.1.1, so it's better to use it, otherwise you may get crazy exceptions like "method not found" (though it should be fixed soon by [this pull request](https://github.com/apache/mahout/pull/117)).

Having done this, we're ready to start. Let's create a scala object with the `main` method and add the following imports:

	import org.apache.mahout.math._
	import org.apache.mahout.math.scalabindings._
	import org.apache.mahout.math.drm._
	import org.apache.mahout.math.scalabindings.RLikeOps._
	import org.apache.mahout.math.drm.RLikeDrmOps._
	import org.apache.mahout.sparkbindings._
 
The important imports here are:

- `scalabindings._` adds functions like `eye`, `diag`; `dense` and `sparse` for matrix creation and `svec`, `dvec` for vector creation
- `RLikeOps._` adds r-like operators, for example `%*%` for matrix multiplication
- `sparkbindings._` for distributing the Linear Algebra operations with Spark

With this, we're ready to code. The very first thing is to set up the `DisributedContext`, in our case - Spark-based. The "right" way to initialize the Spark context is 

	implicit val ctx = 
		mahoutSparkContext(masterUrl="local[*]", appName="mahout spark binding")

Here we assume you're running locally, otherwise you need to change `"local[*]"` to your Spark server instance. 

However using the `mahoutSparkContext` method requires additional configuration steps, like installing Mahout or building Mahout from sources and setting the `MAHOUT_HOME` environment variable. If you don't do it, you'll get an error. For a quick start we don't want to build Mahout from sources, so instead we'll use the following set up:

    val conf = new SparkConf()
      .setAppName("Simple Application")
      .setMaster("local[*]")
      .set("spark.serializer", 
           "org.apache.spark.serializer.KryoSerializer")
      .set("spark.kryo.registrator",
           "org.apache.mahout.sparkbindings.io.MahoutKryoRegistrator")
    implicit val sc = new SparkDistributedContext(new SparkContext(conf))

So we configure the context manually: first, create a `SparkConf` object the way we usually do it for Spark application. The last two parameters are needed for properly serializing and deserializing Mahout's `Vector` objects, and without it, you'll be seeing "Failed to serialize task" errors.

Let's enter the matrix with the data from the cereal manual:

    val matrix = dense(
      (2, 2, 10.5, 10, 29.509541), // Apple Cinnamon Cheerios
      (1, 2, 12, 12, 18.042851), // Cap'n'Crunch
      (1, 1, 12, 13, 22.736446), // Cocoa Puffs
      (2, 1, 11, 13, 32.207582), // Froot Loops
      (1, 2, 12, 11, 21.871292), // Honey Graham Ohs
      (2, 1, 16, 8, 36.187559), // Wheaties Honey Gold
      (6, 2, 17, 1, 50.764999), // Cheerios
      (3, 2, 13, 7, 40.400208), // Clusters
      (3, 3, 13, 4, 45.811716)) // Great Grains Pecan)

Now we need to transform it to a DRM: 

    val drmData = drmParallelize(matrix, numPartitions = 2)

The first 4 columns of the matrix are our matrix $\mathbf X$, and the last one is the vector $\mathbf y$. In order to extract them we use slicing operators.

    val drmX = drmData(::, 0 until 4)
    val y = drmData.collect(::, 4)

`0 until 4` gets the slice of columns from 0 to 4 (exclusive) and `::` returns all the rows. The `collect` function "materializes" the vector: it creates an in-core `Vector` back from a DRM.

So to solve the OLS problem we need to compute $\mathbf X^\mathbf T \mathbf X$ and $\mathbf X^\mathbf T \mathbf y$: 

    val drmXtX = drmX.t %*% drmX
    val drmXty = drmX.t %*% y

Now we need to solve the system $\mathbf X^\mathbf T \mathbf X \hat {\mathbf w} = \mathbf X^\mathbf T \mathbf y$:  

    val w = solve(drmXtX, drmXty)
    println(w)

The output is:

	{
	  0  =>	{0:5.247349465378446}
	  1  =>	{0:2.750794578467531}
	  2  =>	{0:1.1527813010791554}
	  3  =>	{0:0.10312017617608908}
	}

Note that `w` here is a one-column matrix, not a vector. To transform it to a vector, we use `w(::, 0)`.

Now, when we found the best $\hat{\mathbf w}$, we can use it to calculate $\hat {\mathbf y}$ - values the model predict for each $\mathbf x_i$:

    val yFitted = (drmX %*% w).collect(::, 0)
    println(yFitted)

And we see the output

	{0:29.131693510783975,
	 1:25.819756349376444,
	 2:23.172081947084997,
	 3:27.266650111384287,
	 4:25.716636173200357,
	 5:32.514955735899626,
	 6:56.68608824372747,
	 7:36.95163570033205,
	 8:39.393069750271316}

Let's wrap this into functions:

	def ols(drmX: DrmLike[Int], y: Vector) = {
	  val sol = solve(drmX.t %*% drmX, drmX.t %*% y)
	  sol(::, 0)
	}

And goodness of fit is the error $\| \mathbf X \hat {\mathbf w} - \mathbf y \|$:

	def goodnessOfFit(drmX: DrmLike[Int], w: Vector, y: Vector) = {
	  val fittedY = (drmX %*% w) collect (::, 0)
	  (y - fittedY).norm(2)
	}

Now we can call these functions:

    val sol = ols(drmX, y)
    println(goodnessOfFit(drmX, sol, y))

And you'll see the result:

	14.200396723606845

## Million Song Dataset

Now when we got a bit familiar with the syntax, let's try to analyze a bigger dataset. We will use "YearPredictionMSD" from  http://archive.ics.uci.edu/ml/datasets/YearPredictionMSD. It's the biggest dataset for regression at UCI ML repository and there are 515.000 instances. It's a subset of the [Million Song Dataset](http://labrosa.ee.columbia.edu/millionsong/).

Here's the description of the dataset: 

> Abstract: Prediction of the release year of a song from audio features. Songs are mostly western, commercial tracks ranging from 1922 to 2011, with a peak in the year 2000s.

> Attribute Information:

> 90 attributes, 12 = timbre average, 78 = timbre covariance
> The first value is the year (target), ranging from 1922 to 2011.
> Features extracted from the 'timbre' features from The Echo Nest API.
>  We take the average and covariance over all 'segments', each segment being described by a 12-dimensional timbre vector.

So in this dataset there are 90 different features extracted from songs, and the goal is to predict the year when the song was released. We can download it from http://archive.ics.uci.edu/ml/machine-learning-databases/00203/.

The first step is setting up the environment the way we did before:

    val conf = new SparkConf()
      .setAppName("Simple Application")
      .setMaster("local[*]")
      .set("spark.serializer", 
           "org.apache.spark.serializer.KryoSerializer")
      .set("spark.kryo.registrator",
           "org.apache.mahout.sparkbindings.io.MahoutKryoRegistrator")
    implicit val sc = new SparkDistributedContext(new SparkContext(conf))

Let's read the data. For that we'll use Spark's methods for reading from text files:

    val data = sc.textFile(textFilePath, numPartitions)
    val rdd = data.map(line => line.split(",").map(_.toDouble)).map(dvec(_))

Now we have an RDD of `DenseVector` objects. DRM's are indexed rows, so we want to add an index to each row with `withWithIndex` function in Spark. However, it would give us tuples `(Vector, Long)`, while we need `(Int, Vector)`, so we'll need to do an additional step:

	val rddMatrixLike: DrmRdd[Int] = 
			rdd.zipWithIndex.map { case (v, idx) => (idx.toInt, v) }

`DrmRdd[Int]` is an alias for `RDD[DrmTuple[Int]]`, and `DrmTuple[Int]` is an alias for `(Int, Vector)`, so `DrmRdd[Int]` is actually `DrmRdd[(Int, Vector)]`.

Now we convert the RDD to Mahout's DRM: 

    val matrix = drmWrap(rddMatrixLike)

In this data set there is a predefined training/test split, so let's cut it: 

    val nrow = matrix.nrow.toInt
    val train = matrix(0 until 463715, ::)
    val test = matrix(463715 until nrow, ::)

And extract the first column as target $\mathbf y$, and the rest as the data matrix $\mathbf X$:

    val ncol = matrix.ncol
    val X = train(::, 1 until ncol)
    val y = train.viewColumn(0)

Now using the `ols` procedure we already implemented, let's run the regression:

    val w = ols(X, y)
    println(w)

But we forgot to do an important preprocessing step: adding the bias term. So let's write a function `addBias` that prepends `1` to every vector of our dataset

    def addBias(drmX: DrmLike[Int]) = {
      drmX.mapBlock(drmX.ncol + 1) {
        case (keys, block) => {
          val block_new = block.like(block.nrow, block.ncol + 1)
          block_new.zip(block).foreach {
            case (row_new, row_orig) =>
              row_new(0) = 1.0
              row_new(1 to block.ncol) := row_orig
          }
          keys -> block_new
        }
      }
    }

Let's try to understand what's happening here. We need to apply a transformation to every row of the dataset, and to do this we use the `mapBlock` function. It takes 2 arguments: the number of columns in the new DRM and a function to be applied to each block of the DRM. Recall that DRMs can be stored in row blocks, so each row block is itself a matrix (a object of class `Matrix`).

So the first thing is creating a new matrix that looks exactly like the old block, but with one additional column, by using the `like` method. It is possible to iterate over all rows of a `Matrix` because it implements `java.lang.Iterable` and it can be used in Java's foreach loop. But to use them in Scala and to be able to use all Scala's handy functions like `map`, we need to add the following imports: 
 
	import collection._
	import collection.JavaConversions._

This way it can wrap Java collections into Scala ones and enable us to use Scala functions on them. What we do here is `zip`ping two matrices - row-by-row, and then, for each pair, we assign the first element of the new row to 1.0 and copy the rest from the old row. 

At the end we just return the pair of the input keys (untouched) and the block with rows with 1.0 prepended. 

So now we can call it: 

    val w = ols(addBias(X), y)

And calculate the goodness of fit on the testing set:

    val X_test = test(::, 1 until ncol)
    val y_test = test.viewColumn(0)
    val error = goodnessOfFit(addBias(X_test), w, y_test)
    println(error)

The result is around 2160. 
 
Ok, good. But can we do better? Maybe we are overfitting and need to regularize the model? Let's try using the Ridge Regression on this dataset.

## Regularization

Ridge Regression is a regularized version of OLS regression, and instead of solving $(\mathbf X^\mathbf T \mathbf X) \, \mathbf {\hat w} = \mathbf X^\mathbf T \mathbf y$ we solve $(\mathbf X^\mathbf T \mathbf X - \mathbf I \lambda) \, \mathbf {\hat w} = \mathbf X^\mathbf T \mathbf y$.

So it's pretty similar, but we need to add the regularization parameter $\lambda$ to each diagonal element of $\mathbf X^\mathbf T \mathbf X$:

    def ridge(drmX: DrmLike[Int], y: Vector, lambda: Double = 1.0) = {
      val XTX = drmX.t %*% drmX
      val XTy = drmX.t %*% y
      val reg = diag(lambda, XTX.ncol)
        
      val sol = solve(XTX.plus(reg), XTy)
      sol(::, 0)
    }

Note that if we try to add a matrix to an DRM using the `plus` function, the DRM gets implicitly converted to a "in-core" matrix, so don't do this for large matrices. 

However for Ridge Regression we typically need to standardize the data, so every feature is on the same scale. Standardization is done by calculating $\tilde {\mathbf x} = \cfrac{\mathbf x - \boldsymbol \mu}{\boldsymbol \sigma}$. 

Let's write a function to do that:

    def standardize(drmX: DrmLike[Int])(implicit ctx: DistributedContext) = {
      val meanVec = drmX.colMeans
      val variance = (drmX * drmX).colMeans - (meanVec * meanVec)
  
      val mean = drmBroadcast(meanVec)
      val std = drmBroadcast(variance.sqrt)
    
      val res = drmX.mapBlock(drmX.ncol) {
        case (keys, block) => {
          val copy = block.cloned
          copy.foreach(row => row := (row - mean) / std)
          (keys, copy)
        }
      }

      res
    }

To calculate means for all the features we use the `colMeans` function which returns a vector of means for each column. 

To calculate variance, we use the formula $\text{var}(X) = \mathbb E \, [ X^2 ] - \big( \mathbb E \, [X] \big)^2$ and the code for it is straightforward.  

There's one caveat though: by default, `drmX * drmX` (element-wise Matrix multiplication) has side effects. That is, executing `drmX * drmX` will change `drmX`, and it will write the results back to `drmX` as if we did `drmX := drmX * drmX`. I assume this is done for optimization reasons. Luckily there's a way to change this behavior, and this is done by setting the `"mahout.math.AewB.inplace"` property to `false`: 

    System.setProperty("mahout.math.AewB.inplace", "false")

You will need to add line in your header with the setup (or maybe in the configuration files in your `mahout/conf` folder).

As a side note: there's an alternative method for computing the standard deviation without side effects: we first compute the covariance matrix  $\mathbf C = \cfrac{1}{N - 1} \, (\mathbf X - \boldsymbol \mu) ^\mathbf T (\mathbf X - \boldsymbol \mu)$ and then take elements on the diagonal of $\mathbf C$, but it is probably more expensive computationally. 

This allows you to compute vectors $\boldsymbol \mu$ and $\boldsymbol \sigma$ with mean and standard deviation over the entire input space. 

But the DRM we want to standardize lays across several machines, and  what we want to do is to send the computed $\boldsymbol \mu$ and $\boldsymbol \sigma$  vectors to all these machines. This is done via the `drmBroadcast` method: it broadcasts the vectors and it's possible to use them in the `mapBlock` function.

Now for each row $\mathbf x$ we need to compute $\tilde {\mathbf x} = \cfrac{\mathbf x - \boldsymbol \mu}{\boldsymbol \sigma}$. We can do this transformation by using `mapBlock` function. Remember that DRMs could be stored in rows or in blocks of rows, and usually they are stored in blocks. This function applies a specified `map` function to every such block of your matrix (it will convert the matrix into the block representation if needed). 

Next we need to apply this transformation to every row, and to do this we'll use the familiar `mapBlock` function:  
	
    val res = drmX.mapBlock(drmX.ncol) {
      case (keys, block) => {
        val copy = block.cloned
        copy.foreach(row => row := (row - mean) / std)
        (keys, copy)
      }
    }

Here we want to avoid side effects and therefore clone the matrix, and then we transform each row of the block matrix. 

I think it looks more complex than it needs and I hope [one day](https://issues.apache.org/jira/browse/MAHOUT-1691) there will be a simpler way of doing it, for example, something like this: 

    val res = drmX.mapBlock(drmX.ncol) {
      case (keys, block) => {
        keys -> block.map(row => (row - mean) / std)
      }
    }

Another note: in many cases it is fine to have some side effects, if we're not going to use our `drmX` again. So instead we can write 

    val res = drmX.mapBlock(drmX.ncol) {
      case (keys, block) => {
        block.foreach(row => row := (row - mean) / std)
        (keys, block)
      }
    }

Don't forget that we need to do the standardization before adding the bias term, otherwise we will lose the intercept. Now let's run it!

    val w_reg = ridge(addBias(standardize(X)), y, lambda = 10.0)
    val error_reg = goodnessOfFit(addBias(standardize(X_test)), w_reg, y_test)
    println("error ridge", error_reg)

$\lambda = 10$ is taken arbitrarily, and in real life we should use cross validation techniques for selecting it. Actually we see that the error doesn't decrease at all, but at least we played around with some Mahout functionality. 

You can try to implement [Cross Validation](http://en.wikipedia.org/wiki/Cross-validation_%28statistics%29) yourself: e.g. take another subset from `X_Train` and perform validation on it, or even split it in 10 subsets and do a 10-fold CV.

### Dimensionality Reduction

90 attributes is quite a lot, so let's try to reduce the dimensionality of our data set with using [Principal Component Analysis](http://en.wikipedia.org/wiki/Principal_component_analysis) techniques and then run an OLS regression on it (this sometimes called "[Principal component regression](http://en.wikipedia.org/wiki/Principal_component_regression)").  

Luckily there are algorithms in Mahout such as SVD and PCA that could be helpful in this. There are distributed implementations of these algorithms in the 
`org.apache.mahout.math.decompositions` package, for example, DSSVD (Distributed Stochastic SVD). Unfortunately, for this particular data set it took very long to compute SVD on my machine, so I stopped it after running 30 minutes. 

But what we can do instead is to take a subsample of our training data and do in-memory SVD on this smaller matrix (which is also implemented in Mahout Math), and then learn the principal components and use this information to transform the entire training set as well as the testing set. 

Let's do it. First, we need to take a sample from the training set, and to do that we need to sample rows from the data matrix $\mathbf X$. Suppose we have an $N \times p$ data matrix $\mathbf X$ and we want to sample rows from this matrix. We can use linear algebra and matrix multiplication for it: we create a sampling matrix $\mathbf S$ of size $M \times N$ where $M$ is the amount of rows you want to sample and $N$ is the number of rows in the original matrix. We let element $S_{ij}$ be 1 if we want to take row $j$ from the original matrix $\mathbf X$ and put it as a row $j$ in the sampled matrix. Then, to get the rows, we multiply $\mathbf X$ to $\mathbf S$ on the right: $\mathbf S \mathbf X$ will return the rows we need. 

This matrix will mostly contain zero entries, i.e. it will be a very sparse matrix. Therefore, to save the memory, we will need to use sparse vectors to build the sampling matrix. Mahout `RandomAccessSparseVector` is a sparse implementation of the `Vector` interface. Let's write the `sample` function:

    def sample(drm: DrmLike[Int], size: Int, seed: Int) = {
      val nrow = drm.nrow.toInt
      val rnd = new Random(seed)
  
      val randomIdx = Seq.fill(size)(rnd.nextInt(nrow))
      val Srows = randomIdx.map { j =>
        val vec = new RandomAccessSparseVector(nrow)
        vec.setQuick(j, 1)
        vec
      }
  
      val S = new SparseRowMatrix(size, nrow)
      S := Srows
      S %*% drm
    }

What we do here is setting up a random number generator and create a matrix $\mathbf S$ where for each row $i$ in $\mathbf S$ we generate some random index $j$ and set $S_{ij}$ to 1. `S := Srows` is just a way of converting a sequence of vectors to a matrix: internally it assigns each row of the sequence to a row of the matrix. And finally we do a left multiplication to take rows from $\mathbf X$.

Now, after sampling some data points, we can do in-memory SVD:

    def dimRed(X_train: Matrix, dim: Int): DrmLike[Int] => DrmLike[Int] = {
      val V = svd(X_train)._2
      val V_red = V(::, 0 until dim)
  
      def fit(X: DrmLike[Int]): DrmLike[Int] = {
        X %*% V_red
      }
  
      fit
    }

We apply SVD (it's a way of doing PCA) to our matrix and take only first `dim` elements from the principal component matrix. This function returns another function that can be used to apply the learned transformation to other datasets, and it's done simply by matrix multiplication. 

Since we're doing dimensional reduction via PCA, as we discussed earlier, it's important to center all the features: transform them such that their expected value is 0. It's really easy and very similar to what we did for `standardize`, but we only need to subtract the mean and don't need to divide by standard deviation. 

So we sample our matrix, then center it and train the PCA on the sample

    val X_subset = center(sample(X, 5000, seed = 0x31337))
    val pca = dimRed(X_subset, dim = 20)

Value of 20 dimensions is taken arbitrarily here, in practice we usually keep enough dimensions to explain at least 95% of variance in the data set (for details you may refer, e.g. [here](http://stats.stackexchange.com/questions/22569/pca-and-proportion-of-variance-explained)).

Now we apply the transformation we learned to the entire (recall that `dimRed` returns a function which we cann `pca` that is used for transformation) 

    val w_pca = ols(addBias(pca(center(X))), y)
  
Let's check how well it does:

    val error_pca = goodnessOfFit(addBias(pca(center(X_test))), w_pca, y_test)
    println("error pca", error_pca)

We see that it prints 2390, so it's worse than simple OLS regression. Maybe for this particular case we don't keep enough dimensions, so you may try to experiment with selecting the right dimensionality for this data. 

## Conclusions

Even though the simplest OLS regression for this data set in our experiments turned out to be the best method, we learned how to do many useful things with Mahout Samsara: how to distribute linear algebra operations and prepare the environment for this, how to incorporate it into Spark dataflows. We also learned a little bit about internals of Samsara: how matrices are represented and how we can apply efficient block-wise transformations to our matrices.

Mahout Samsara is a relatively new project and there are still many things that are not yet implemented, but needed. For example, in this post we had to implement calculating standard deviation and standardization ourselves. However it’s still a pretty promising tool. What’s more, it’s not just one implementation, but rather an API for performing distributed Linear Algebra calculations. Currently it's running only on top of Apache Spark, but backends for other distributed engines are being implemented. For example for H2O and for Apache Flink. So you can take this library to your current data pipeline and have out-of-the-box distributed Linear Algebra library. 

All the source code is available at [github](https://github.com/alexeygrigorev/itshared-howto/tree/master/mahout-spark-binding).

Acknowledgments
-------------

This post is inspired by an article ["Playing with Mahout's Spark Shell"](https://mahout.apache.org/users/sparkbindings/play-with-shell.html) and I used the code and the data from there in the introduction. Also, the [Scala and Spark Bindings manual](https://mahout.apache.org/users/sparkbindings/ScalaSparkBindings.pdf) gives a good overview of the syntax. The implementation of sampling rows from a matrix is taken from a paper "Efficient Sample Generation for Scalable Meta Learning" by Sebastian Schelter and others ([pdf](http://ssc.io/wp-content/uploads/2014/11/ICDE15_research_150.pdf)). 

Thanks for reading and stay tuned!
