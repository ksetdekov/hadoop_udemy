# Structure of hadoop ecosystem:
* HDFS - file system
* YARN - resourse negotiator
* MapReduce - built on top to map and reduce data processing steps
* Pig - high level programming API, scripts similar to SQL, use this without Python or Java)
* Hive - sits on top of map reduce - lets use DB as a SQL DB with querries
* Apache Ambari - on top of this - look at all and execute Pig, Hive, view state
* Mesos - alternative to YARN - similar, different pros and cons
* Spark - like mapreduce - extremely fast, very powerful
* Tez - at same level as Mapreduce, use to accelerate Hive
* Apache HBASE - noSQL db - very fast db, good for fast transaction rates
* Apache Storm - use to process streaming data
* OOZIE - way of sceduling jobs on a cluster
* Zookeeper - use to track states of the cluster
* Data ingestion:
  * Sqoop - connector from legacy to hadoop
  * flume - listen to web logs from servers to hadoop
  * kafka - collect data from different sources
* External data storage
  * sql dbs - can 
  * cassandra
  * mongo db
* can have many query engines
  * apache drill
  * HUE - interactive way to create querries
  * apache phoenix - similar to drill. adds additional guarantees
  * Presto
  * zeppelin - notebook style

# Install
#### links:
* https://www.virtualbox.org/wiki/Linux_Downloads
* https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html

# Using files 
## file view - explorer
## cmd line
```hadoop fs```

# Mapreduce
1. mapper
2. extract and organize data we care about
2. sorts and groups the mapped data ("shuffle and sort")
3. reducer - like counter of the rated movies

Mapreduce in JAVA

STREAMING allows interfacing to other languages (ie Python)

Today we have Spark, Hive.

## Running mapreduce with python on hadoop
intall prerequisites:

* pip
`yum install python-pip`
* MRjob
`
pip install mrjob==0.5.11
`
* Nano
`yum install nano`
* data
```commandline
wget http://media.sundog-soft.com/hadoop/RatingsBreakdown.py
wget http://media.sundog-soft.com/hadoop/ml-100k/u.data
```

## runnin locally
should work, but get syntax error
```commandline
python3 code/mapreduce_ex.py ml-100k/u.data
```
run with hadoop
```commandline
python RatingsBreakdown.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data
```
