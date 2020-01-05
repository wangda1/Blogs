---
title: InputFormat
date: 2019-12-10 10:34:55
categories:
- BigDataSystem
- Batch
tags:
- BigDataSystem
- Batch
---

# Hadoop InputFormat

## What is Hadoop InputFormat?

>Hadoop InputFormat describes the input-specification for execution of the Map-Reduce job.

>InputFormat describes how to split up and read input files. In MapReduce job execution, InputFormat is the first step. It is also responsible for creating the input splits and dividing them into records.

> Input files store the data for MapReduce job. Input files reside in HDFS. Although these files format is arbitrary, we can also use line-based log files and binary format. Hence, In MapReduce, InputFormat class is one of the fundamental classes which provides below functionality:

- InputFormat selects the files or other objects for input.
- It also defines the Data splits. It defines both the size of individual Map tasks and its potential execution server.
- Hadoop InputFormat defines the RecordReader. It is also responsible for reading actual records from the input files.

## Types of InputFormat in MapReduce

- `FileInputFormat`
- `TextInputFormat`
- `KeyValueTextInputFormat`
- `SequenceFileAsTextInputFormat`
- `SequenceFileAsBinaryInputFormat`
- `NlineInputFormat`
- `DBInputFormat`

## Conclusion

> Hence, InputFormat defines how to read data from a file into the Mapper instances. In this tutorial, we have learned many types of InputFormat like FileInputFormat, TextInputFormat etc. The default input format is TextInputFormat. If you have any query related to MapReduce InputFormat, so feel free to share with us. Hope we will solve them.