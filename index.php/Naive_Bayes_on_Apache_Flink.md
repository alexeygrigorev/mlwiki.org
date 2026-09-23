---
layout: default
permalink: /index.php/Naive_Bayes_on_Apache_Flink
tags:
- machine-learning
- hadoop
- java
title: Naive Bayes on Apache Flink
---

## Naive Bayes on Apache Flink

In this blog post we are going to implement a Naive Bayes classifier in Apache Flink - a system for distributed computation. We are going to use it for text classification and we will apply it to the 20 Newsgroup dataset. To understand what is going on, you should be familiar with Java and know what MapReduce is. If you have seen and understood a word count example in any system, be it Hadoop, Spark or anything else, you're good to go. 

Here we will use:

- Java 7 (or 8)
- Apache Maven for dependency management
- Apache Flink
- Stanford NLP for text preprocessing

## Theory
 

### Naive Bayes

First, let's review the theory. By the Bayes Rule, the probability that a document $\text{doc}$ belongs to the category $\text{cat}$ is given by 

$$P(\text{cat} \mid \text{doc}) = \cfrac{P(\text{doc} \mid \text{cat}) \cdot P(\text{cat})}{P(\text{doc})}$$

Then, in Naive Bayes, we assume that all the words in $\text{doc}$ are independent. That is, if we see a document is a set of words: 

Since $\text{doc} = \cup_i w_i$, then $P(\text{doc} \mid \text{cat}) = P(\cup_i w_i \mid \text{cat}) = \prod_i P(w_i \mid \text{cat})$.

To assign a document to some category, we select the category with highest $P(\text{cat} \mid \text{doc})$: 

$$\text{cat}^* = \operatorname{argmax}_\text{cat} \cfrac{P(\text{doc} \mid \text{cat}) \cdot P(\text{cat})}{P(\text{doc}} = \operatorname{argmax}_\text{cat} \cfrac{\prod P(w_i \mid \text{cat}) P(\text{cat})}{P(\text{doc})}$$

We can get rid of the denominator because it doesn't depend on $\text{cat}$:

$$\text{cat}^* = \operatorname{argmax}_\text{cat} \prod P(w_i \mid \text{cat}) P(\text{cat})$$

To avoid numerical underflow (easy to get when multiplying lots of probabilities) we take a log of this expression. We can do this because log is monotonically increasing. 

$$\text{cat}^* = \operatorname{argmax}_\text{cat} \log \left[ \prod P(w_i \mid \text{cat}) P(\text{cat}) \right] = \operatorname{argmax}_\text{cat}  \left[ \sum_i \log  P(w_i \mid \text{cat}) + \log P(\text{cat}) \right]$$

### Estimating

So we have our formula: 

$$\text{cat}^* = \operatorname{argmax}_\text{cat}  \left[ \sum_i \log  P(w_i \mid \text{cat}) + \log P(\text{cat}) \right]$$

We need two things here: $P(\text{cat})$ and $P(w_i \mid \text{cat})$. 
We estimate them using the data and get $\hat P(\text{cat})$ and $\hat P(w_i \mid \text{cat})$. 
Estimation is very easy: it's just counting.

$\hat P(\text{cat}) = \cfrac{\text{count(cat)}}{\text{total count}}$ we just count how many articles of this category are there

$\hat P(w_i \mid \text{cat}) = \cfrac{ \text{count($w_i$ in cat)} }{\sum_j \text{count($w_j$ in cat)}}$ in each category, we count how many times times a word $w_i$ occurs  divided by total number of words in the category

So, with minor modification, we can reduce the problem to the word count problem!

### Smoothing
 
What happens if we have never seen a certain word $w_0$ during the training training, but it occurs during classification? Because $P(w_0 \mid \text{cat}) = 0$, $P(\text{doc} \mid \text{cat})$ is also zero: $P(\text{doc} \mid \text{cat}) = \prod_i P(w_i \mid \text{cat}) = 0$

How we can avoid that? Laplace Smoothing is a simple and popular technique for that. We add some number $\lambda$ to each count: 

$$\hat P(w_i \mid \text{cat}) = \cfrac{ \text{count($w_i$ in cat) + \lambda} }{\sum_j \left( \text{count($w_j$ in cat) + \lambda \right) }}$$

Thus, unseen words will have estimated probability $$\hat P(w_0 \mid \text{cat})  = \cfrac{ \lambda} }{\sum_j \left( \text{count($w_j$ in cat) + \lambda \right) }} \ne 0$.

We can further rewrite this as 

$\hat P(w_i \mid \text{cat}) = \cfrac{ \text{count($w_i$ in cat) + \lambda} }{\sum_j \left( \text{count($w_j$ in cat) + \lambda \right) }} = \cfrac{ \text{count($w_i$ in cat) + \lambda} }{\sum_j \text{count($w_j$ in cat) + \sum_j \lambda }}$ 

We can move the $\lambda$ out of this sum and then recognize that in $\sum_j \lambda$ the index $j$ goes over all seen words, so $\sum_j \lambda = \text{# distinct words} \cdot \lambda$:

$\hat P(w_i \mid \text{cat}) = \cfrac{ \text{count($w_i$ in cat) + \lambda} }{\sum_j \text{count($w_j$ in cat) + \text{# distinct words} \cdot \lambda }}$

This is enough to start coding.

## Coding

### Data set

There are quite a lot text data sets for classification on the Internet. A good collection of them could be found here: http://disi.unitn.it/moschitti/corpora.htm

We are going to use one of them: the 20 Newsgroup dataset (http://qwone.com/~jason/20Newsgroups/). Here's the description: 

"it contains 19997 articles for 20 categories taken from the Usenet newsgroups collection. We used the subject and the body of each message only. Some of the newsgroups are very closely related to each other (e.g., IBM computer system hardware / Macintosh computer system hardware), while others are highly unrelated (e.g. misc forsale / social religion and christian). This corpus is different from the previous corpora because it includes a larger vocabulary and words typically have more meanings. Moreover, the stylistic writing (e-mail dialogues) is very distant from the other more technical collections."

So we can download it and unpack. We are going to use one with training/test split

wget http://qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz
tar -xzf 20news-bydate.tar.gz

### Initial Preprocessing

Here is how files in this data set look like 

	From: ho@cs.arizona.edu (Hilarie Orman)
	Subject: Re: Licensing of public key implementations
	Organization: U of Arizona, CS Dept, Tucson
	Lines: 6

	With regard to your speculations on NSA involvement in the creation of
	PKP, I find that it fails the test of Occam's butcher knife.  Never
	attribute to conspiracy what can be explained by forthright greed.

	Hilarie Orman

It's a file with id 14989 from "sci.crypt". So it's a big collections of email-like files, each of which is stored in a folder with category name. Such layout is very uncommon in Big Data, because there are lots of very small files, and it's not very effective to store them on a distributed system. So we first need to convert this set of small files into a few big ones.

To do this we can create a small python script that discards the header, removes all the linebreaks and then writes the entire content as a tuple (category, content) in a bigger file. The script is very simple, but if you want, you can have a look at it <a href="https://github.com/alexeygrigorev/itshared-howto/blob/master/naive-bayes/scripts/preprocessing.py">here</a>.

### Further Preprocessing

Now we need to work with the text more: 

- tokenize: split a text into separate tokens, e.g. "I love cookies!" to ["I", "love", "cookies", "!"]
- lemmatize: and reduce all forms of the same word to the common one, e.g. "walk", "walking", "walked" all reduce to "walk"
- discard stop words: words that carry no meaning but occur very commonly, e.g. "a", "the", etc.

To do this we will use <a href="http://nlp.stanford.edu/software/corenlp.shtml">Stanford NLP</a>:

First, let's add the library to our pom:

	<dependency>
		<groupId>edu.stanford.nlp</groupId>
		<artifactId>stanford-corenlp</artifactId>
		<version>3.5.1</version>
	</dependency>
	<dependency>
		<groupId>edu.stanford.nlp</groupId>
		<artifactId>stanford-corenlp</artifactId>
		<version>3.5.1</version>
		<classifier>models</classifier>
	</dependency>

We also will need <a href="http://commons.apache.org/proper/commons-lang/">Apache Commons Lang 3</a>:

	<dependency>
		<groupId>org.apache.commons</groupId>
		<artifactId>commons-lang3</artifactId>
		<version>3.3.2</version>
	</dependency>

And now we can use it to create a pipeline that will tokenize the text and return the lemmas:

	// create
	Properties props = new Properties();
	props.put("annotators", "tokenize, ssplit, pos, lemma");
	StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

	// use
	Annotation document = new Annotation(body);
	pipeline.annotate(document);

	List<CoreLabel> tokenized = document.get(TokensAnnotation.class);
	
	for (CoreLabel token : tokenized) {
		String lemma = token.get(LemmaAnnotation.class);
		// process lemma
	}

(You may notice that we have `ssplit` and `pos`: they are necessary for lemmatization, and therefore they are also included to the pipeline)

In our case, we also need to remove stop words, punctuation marks, emails and other things with no words in them. So we can use this simple filter before returning a word to the user:

	private boolean valid(String lemma) {
		if (lemma.length() < 2) {
			return false;
		}

		if (stopwords.contains(lemma)) {
			return false;
		}

		return StringUtils.isAlpha(lemma);
	}

The last line uses a method of the `StringUtils` class from Commons Lang that checks whether a string contains only letters or also something else (digits, special characters, etc). 

Lastly, we in the pipeline we use a Part-of-Speech tagger before the lemmatization, and "bad" symbols like "^", "~", "#" tend to confuse the tagger, so it also makes sense to remove them before parsing. 

The whole class for NLP preprocessing is <a href="https://github.com/alexeygrigorev/itshared-howto/blob/master/naive-bayes/src/main/java/org/itshared/flink/naivebayes/NlpPreprocessor.java">here</a>

Now it's time to use Flink. We can use it to apply the NLP preprocessing to each document.

So, let's start with adding dependencies to Flink:

	<dependency>
		<groupId>org.apache.flink</groupId>
		<artifactId>flink-clients</artifactId>
		<version>0.8.1</version>
		<scope>provided</scope>
	</dependency>
	<dependency>
		<groupId>org.apache.flink</groupId>
		<artifactId>flink-java</artifactId>
		<version>0.8.1</version>
		<scope>provided</scope>
	</dependency>

At the moment of writing, the last version is 0.8.1, but you may want to check if there's a newer version and use it. You can check this in flink's repository at maven central http://mvnrepository.com/artifact/org.apache.flink

If you have a problem like "missing artifact jdk.tools", then there's a hack to make it away: you may exclude the dependency on jdk.tools. See the whole <a href="https://github.com/alexeygrigorev/itshared-howto/blob/master/naive-bayes/pom.xml">pom.xml</a> for details. 

So, let's create a Flink job:

	ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
	DataSource<String> input = env.readTextFile(inputPath);
	DataSet<Tuple2<String, String>> output = input.flatMap(new NlpProcessingMapper());
	output.writeAsCsv(outputPath, "\n", "\t", WriteMode.OVERWRITE);

	public static class NlpProcessingMapper extends 
			RichFlatMapFunction<String, Tuple2<String, String>> {

		private NlpPreprocessor processor;

		@Override
		public void open(Configuration parameters) throws Exception {
			super.open(parameters);
			processor = NlpPreprocessor.create();
		}

		@Override
		public void flatMap(String value, Collector<Tuple2<String, String>> out) 
					throws Exception {
			String[] split = value.split("\t");
			if (split.length < 3) {
				return;
			}

			String category = split[0];

			List<String> words = processor.processBody(split[2]);
			if (!words.isEmpty()) {
				out.collect(new Tuple2<>(category, StringUtils.join(words, ",")));
			}
		}
	}

Here we read a tab-separated text file, and apply a flatMap function to it. FlatMap is similar to the map function, but for each input element it can produce 0 or many output elements. In this case, we do our NLP preprocession for each input document and output a tuple (category, comma-separated-words), or no tuple if the input is invalid for some reason. 

Also the `NlpProcessingMapper could implement the `FlatMapFunction` interface, but instead it extends `RichFlatMapFunction`. The reason is that we want to initialize the `NlpPreprocessor` before processing the data, and this could be done by overriding the `open` function. This function will be called before the mapper is used on data. 

We can run it locally (just press run in your IDE) or on a server. In this post we will run only locally, but it's quite easy to run it on a stand-alone Flink instance. 

And a final note: if you want speed and don't care much about the form of the words you end up using, you can use Snowball Stemmer from Apache Lucene. You can read on difference between lemmatization and stemming here. http://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html. It should increase the processing speed because there will be no need to do POS tagging and other expensive things. 

### Training: Probability Estimation

We are finally ready to move on to the training phase. 

So, let's start by reading the input file with training data

	ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
	DataSource<String> input = env.readTextFile(Config.TRAIN_DATA);

First thing: we need to estimate the prior probabilities $P(\text{cat})$

This is done by counting the documents in each category and then by dividing each count by the total number of documents. 

So, counting is easy:

	DataSet<Tuple2<String, Long>> labelFrequencies = 
			input.map(new LabelExtraction()).groupBy(0).sum(1);

	public static class LabelExtraction implements 
				MapFunction<String, Tuple2<String, Long>> {
		@Override
		public Tuple2<String, Long> map(String value) throws Exception {
			return new Tuple2<>(value.split("\t")[0], 1L);
		}
	}

So it's very similar to a word count: for each document we output only its label along with `1`, and then we group by the label and sum all these ones to get the total number of elements in the category. 

Next, we need to find the total sum. To do it we just sum over `labelFrequencies` again:

	DataSet<Tuple1<Long>> totalSum = labelFrequencies.sum(1).project(1);

And now we need to divide all elements of `labelFrequencies` by the total sum. It's a bit trickier: once we obtained the total count, we need to send this value to all the mappers across the cluster. This is done by "broadcasting" the variable:

	DataSet<Tuple2<String, Double>> priors = 
			labelFrequencies.map(new NormalizationMapper())
				.withBroadcastSet(totalSum, "totalSum");

	public static class NormalizationMapper extends
			RichMapFunction<Tuple2<String, Long>, 
							Tuple2<String, Double>> {
		private long totalSum;
		
		@Override
		public void open(Configuration parameters) throws Exception {
			super.open(parameters);
			List<Tuple1<Long>> totalSumList = 
					getRuntimeContext().getBroadcastVariable("totalSum");
			this.totalSum = totalSumList.get(0).f0;
		}

		@Override
		public Tuple2<String, Double> map(Tuple2<String, Long> value) 
					throws Exception {
			return new Tuple2<>(value.f0, ((double) value.f1) / totalSum);
		}
	}

Note `.withBroadcastSet(totalSum, "totalSum")`: this is how the value is broadcasted to all the mappers. We again use a rich function - `RichMapFunction`, and it allows us to access the runtime context and get the variable.

So we run this and get

<table>
<tr><td>`alt.atheism`</td>	<td>0.042</td></tr>
<tr><td>`comp.sys.ibm.pc.hardware`</td>	<td>0.051</td></tr>
<tr><td>`comp.windows.x`</td>	<td>0.052</td></tr>
<tr><td>`misc.forsale`</td>	<td>0.051</td></tr>
<tr><td>`rec.autos`</td>	<td>0.052</td></tr>
<tr><td>`rec.motorcycles`</td>	<td>0.052</td></tr>
<tr><td>`rec.sport.baseball`</td>	<td>0.052</td></tr>
<tr><td>`rec.sport.hockey`</td>	<td>0.053</td></tr>
<tr><td>`...`</td>	<td>...</td></tr>
</table>

We see that actually we the priors are almost the same for all the classes, so we might just as well skip this computation. But we will anyway use it in the classifier later. 

Next, we need to compute the word count per each category. To do this, first, for each word of a document we omit tuple `(category, word, 1)`, and then we group by `(category, word)` and finally sum over the last column:

	DataSet<Tuple3<String, String, Integer>> labelledWords = 
			input.flatMap(new TokenReaderMapper());
	DataSet<Tuple3<String, String, Integer>> wordCount = 
			labelledWords.groupBy(1, 0).sum(2);

	public static class TokenReaderMapper implements 
				FlatMapFunction<String, 
					Tuple3<String, String, Integer>> {

		@Override
		public void flatMap(String inputValue, 
				Collector<Tuple3<String, String, Integer>> out)
					throws Exception {
			String[] split = inputValue.split("\t");
			String category = split[0];

			for (String word : split[1].split(",")) {
				out.collect(new Tuple3<>(category, word, 1));
			}
		}
	}

As the result it will produce tuples like these:

comp.windows.x	dump	25

Finally, for we need to know how many words are there per category, so we count it this way:

	DataSet<Tuple2<String, Integer>> countPerCategory = 
			labelledWords.groupBy(0).sum(2).project(0, 2);

We have tuples (category, word, 1), so we just group by category, sum over the columns of ones and finally keep only (category, count) tuples

The result is something like this:

alt.atheism	72270
comp.sys.ibm.pc.hardware	51321
comp.windows.x	82099

The code for the entire class is here.

You may wonder why we created two separate jobs: one for NLP preprocessing and one for counting. There's no particular reason and in the real life you probably may want to do it in one job. But on the other hand the intermediate results get stored so it's better for debugging. 

Now we're ready for classification 

### Classification

In here we will assume that all the counts will fit into memory: all the heavy lifting (i.e. counting) has been done, so we just use the results. For very large datasets it will not be the case, so other techniques like joins or the <a href="http://en.wikipedia.org/wiki/Count%E2%80%93min_sketch">Count-min Sketch algorithm</a> should be used instead.

So, for each element of the test set we try to predict the label using the Naive Bayes classifier using the probability estimates from the previous step

First we need to read things we computed on the previous step

	DataSet<Tuple2<String, Double>> priors = 
			env.readTextFile(Config.OUT_PRIOR).map(new PriorsReaderMapper());
	DataSet<Tuple3<String, String, Integer>> counts = 
			env.readTextFile(Config.OUT_COND_COUNT).map(new CountsReaderMapper());
	DataSet<String> countDistict = env.readTextFile(Config.OUT_COUNT_DISTINCT);

The mappers here just convert the text input to tuples.

Each test instance will be classified in a map function that will output a tuple (actualClass, predictedClass). But to do this first we need to broadcast the estimates:

	int smoothing = 1;
	testSet.map(new ClassifierMapper(smoothing))
			.withBroadcastSet(priors, "priors")
			.withBroadcastSet(counts, "counts")
			.withBroadcastSet(totalCount, "totalCount");

After running we have accuracy 0.74. Not perfect, but also not very bad.
