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
