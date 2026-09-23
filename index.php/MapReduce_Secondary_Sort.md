---
layout: default
permalink: /MapReduce_Secondary_Sort
tags:
- hadoop
title: MapReduce Secondary Sort
---

## MapReduce Secondary Sort
A secondary sort in [Hadoop MapReduce](Hadoop_MapReduce) is a sort where not only keys are sorted, but also values

You need: 
- a compound key that includes both key and value 
- two comparators: sorting comparator and grouping comparator
- a special partitioning function

Suppose you want to count on how many domains a particular word appeared 

 SELECT COUNT(DISTINCT domain) FROM word_domain GROUP BY word; 

Instead of keeping the entire domain, we may keep only it's hash (e.g. 64 bites of Murmur Hash)

Input is a set of tuples (url, words)

for each word in words, you extract the domain of the url and output its hash 
then in the reducer you calculate how many distinct hashes are there 

but there could be a lot of domains, so it's better to sort by domains within each group and then just iterate over it, incrementing count each time a new hash is seen 

First, we create a WritableComparable with two fields: word and hash 
The compareTo of this comparable will be used for sorting values 

So, say it'll be <code>PairWritable(String word, long hash)</code>

in mapper, for each word you output 
the composite writable and the hash

 key.set(word, hash);
 value.set(hash);
 context.write(key, value);

Next, you need to provide a grouping comparator that will only use the <code>word</code> field and which will ignore the <code>hash</code> field

When you have two comparators: sorting and grouping, 
- sorting comparator will be used at the shuffle stage for sorting the tuples 
- grouping comparator will be used to determine which <code>Iterable</code> values will reducer read 

Finally, you also need to provide a partitioning function, because the default one will use the hash of the entire PairWritable object, but need to hash only based on word - to make sure all records with the same key end up at the same reducer 

 class PariPartitioner extends Partitioner<PairWritable, LongWritable> {
     @Override
     public int getPartition(Partitioner key, LongWritable value, int numPartitions) {
         int hash = key.getWord().hashCode();
         return Math.abs(hash) % numPartitions;
     }
 }

This way the output will be sorted using the comparator of the key

Then you can use this to count distinct in the Reducer: 

 // input: PairWritable pair, Iterable<LongWritable> domainHashes
 Iterator<LongWritable> it = domainHashes.iterator();
 
 if (!it.hasNext()) {
     return;
 }
 
 LongWritable inputWriteable = it.next();
 long prevHash = inputWriteable.get();
 long countDistinct = 1;
 
 while (it.hasNext()) {
     LongWritable next = it.next();
     long currentHash = next.get();
 
     if (prevHash != currentHash) {
         prevHash = currentHash;
         countDistinct++;
     }
 }
 
 token.set(pair.getWord());
 domainFrequency.set(countDistinct);
 context.write(token, domainFrequency);

Finally, you can also use combiner to reduce the size of set data (so only unique hashes are sent)

 LongWritable inputWriteable = it.next();
 long prevHash = inputWriteable.get();
 
 valueWritable.set(prevHash);
 context.write(text, valueWritable);
 
 while (it.hasNext()) {
     LongWritable next = it.next();
     long currentHash = next.get();
 
     if (prevHash == currentHash) {
         duplicates++;
         continue;
     } 
 
     prevHash = currentHash;
     valueWritable.set(currentHash);
     context.write(text, valueWritable);
 }

Job settings may look like this:

 job.setMapOutputKeyClass(PairWritable.class);
 job.setMapOutputValueClass(LongWritable.class);
 
 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(LongWritable.class);
 
 job.setMapperClass(DomainFrequencyMapper.class);
 job.setCombinerClass(DomainFrequencyCombiner.class);
 job.setReducerClass(DomainFrequencyReducer.class);
 
 job.setPartitionerClass(DomainFrequencyPartitioner.class);
 
 job.setGroupingComparatorClass(PairWritable.GroupingComparator.class);
 job.setCombinerKeyGroupingComparatorClass(PairWritable.GroupingComparator.class);
