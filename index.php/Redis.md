---
title: Redis
layout: default
permalink: /index.php/Redis
---

# Redis

## Redis
[Redis](http://redis.io/) is an in-memory database, good to be used as 
- a cache
- a message queue


## Installation
### Ubuntu
Installing Redis on ubuntu

- <code>sudo apt-get install redis-tools</code>
- default port is 6379
- Use <code>redis-cli</code> to enter redis commands 
- if you need redis instance be outside, do <code>nano /etc/redis/redis.conf</code>  and replace <code>bind 127.0.0.1</code> to <code>bind 0.0.0.0</code>
- restart the server <code>service redis-server restart</code>
- to check if you can connect to redis from another server, do <code>redis-cli -h 192.168.x.x ping</code>, should get <code>PONG</code> in return


### Python
Python library: 

- <code>sudo pip install redis</code> or
- <code>sudo easy_install install redis</code> or


## Building Blocks
### Databases
- Each redis server can have several databases
- they are indexed by integers: 0, 1, 2, ...
- 0 is the default db
- to choose the 1st db, use <code>select 1</code>
- redis keeps all the data in memory, but by default, redis also snapshots DB to disk after each $X$ changes 
- there's also append-only mode


### Key/Value Pairs
String key/values
- key can be anything, e.g. <code>users:ololo</code>, <code>:</code> doesn't have any specific meaning, but can be used to separate "table name" and "key name"
- command <code>set users:ololo '{"name":"ololo", ...}'</code> - the content can be any string, not necessarily JSON
- to get the value, use <code>get users:ololo</code>
- you can query only by key, never by value 


String functions:
- <code>strlen key</code> returns the lenth of the value associated with key <code>key</code>
- <code>getrange key 0 10</code> returns the substring from 0 to 10 of the value stored by <code>key</code>
- <code>append key value2</code> appends 'value2' to the current value stored by <code>key</code>


### Counters
- You can store counters in redis 
- <code>incr key</code> increment the integer value stored in <code>key</code>, or create a new key with value 1
- <code>decr key</code> decrement the value
- <code>incrby</code> and <code>decrby</code> are used to increase/decrease the values by some number


### Bitmaps
- you can store byte arrays in redis and set/get their specific bits
- commands: <code>setbit</code> and <code>getbit</code>
- this can be used for implementing [Sketching Algorithms](Sketching_Algorithms), e.g. [Bloom Filters](Bloom_Filters)


### Hashes
- hashes in redis are [associative arrays](Hash_Tables)
- to store a hash, not a string, use <code>hset</code> and <code>hget</code>
- <code>hset hashname field 30</code> is approximately equal to <code>hashname[field] = 30</code>
- if hash <code>hashname</code> doesn't exist, it will be created. If exists, but <code>field</code> doesn't, <code>field</code> will be created
- <code>hgetall hashname</code> returns all fields of the hash <code>hashname</code>
- <code>hdel hashname field</code> removes <code>field</code> from <code>hashname</code>


### Lists
- lists keep an array of values associated with a specific key
- <code>lpush listname new_value</code> adds the new value to the front of <code>listname</code>
- <code>ltrim listname 0 49</code> removes first 50 values from the list
- <code>lrange listname 0 9</code> returns first 10 values


### Sets
Unordered sets
- <code>sadd set1 val1 val2 val3</code> adds values "val1" "val2" "val3" to set <code>setkey</code>
- <code>smember set1 val1</code>
- <code>sinter set1 set2</code> intersection of two sets <code>set1</code> and <code>set2</code>
- <code>sinterstore set1 set2 new_set</code> store instersection of two sets in a new set <code>new_set</code>


Ordered sets
- the same commands, but they start with "z":
- <code>zadd</code>, <code>zmember</code>, ...


## Usage Patterns
- in redis it's fine to issue several requests ("round trips" to db) - because it's so fast 


### Avoiding Duplication
- suppose users can log in using their ids or emails - so you have two keys for the same user
- how can you avoid storing the same user twice? 
- first, keep the user data at <code>user:id</code>, e.g. <code>users:9001</code>
- use hash to lookup the id for email: <code>hget user:emails ololo@mlwiki.org</code>


### Expiration
- you can set time to live of a key 
- <code>expire key 30</code> where 30 is the time to live in seconds 
- <code>expireat key unix_timestamp</code>
- <code>ttl key</code> to see how much time the <code>key</code> has left to live


### Publish/Subscribe
- it's easy to implement the [Publish-Subscribe Model](Publish-Subscribe_Model) in redis - which makes it a lightweight message queue
- <code>blpop</code> and <code>brpop</code> - return and remove first (last) element of a list - or blocks until something is avialable 
- can use it to implement a [Queue](Queue)
- also can use <code>subscribe q_id</code> and <code>publish q_it message</code>


A P/S model implemented in Scala: https://gist.github.com/debasishg/7056696



### Lua Scripting
- finally, it's possible to write stored procedures in Lua 


## Sources
- Little Redis Book: https://github.com/karlseguin/the-little-redis-book

[Category:Databases](Category_Databases)