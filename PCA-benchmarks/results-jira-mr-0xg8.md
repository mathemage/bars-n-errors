# PCA JMH benchmark of @wendycwong 's JIRA dataset on mr-0xg8
@mmalohlava recommended a dataset that @wendycwong used to test PCA (see comments above). I also switched to `mr-0xg8` machine, since `mr-0xd7` should be used only for Hadoop jobs. Hence, I benchmarked on a dedicated machine `mr-0xg8`:

```
mathemage@mr-0xg8:~/h2o-3$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                40
On-line CPU(s) list:   0-39
Thread(s) per core:    2
Core(s) per socket:    10
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Stepping:              2
CPU MHz:               1211.640
BogoMIPS:              5201.61
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              25600K
NUMA node0 CPU(s):     0-9,20-29
NUMA node1 CPU(s):     10-19,30-39

mathemage@mr-0xg8:~/h2o-3$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.5 LTS
Release:        14.04
Codename:       trusty

mathemage@mr-0xg8:~/h2o-3$ free -gt
             total       used       free     shared    buffers     cached
Mem:           125        123          2          0          0         41
-/+ buffers/cache:         82         43
Swap:          127        103         24
Total:         253        227         26
```

and here are the results...

### 1 warmup + 1 measurement iteration
| Benchmark                                            | Score     | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|------------------------------------------------------|-----------|---------------------|-------|--------------------------| 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 7.603006  | 5.396575            | ms/op | JAMA                     | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 12.941340 | 22.550269           | ms/op | MTJ                      | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 6.675360  | 4.172057            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 7.066895  | 6.008761            | ms/op | EVD_MTJ_SYMM             | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 11.911098 | 2.418632            | ms/op | JAMA                     | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 11.967880 | 1.683498            | ms/op | MTJ                      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 11.691213 | 0.637260            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 12.271872 | 1.429068            | ms/op | EVD_MTJ_SYMM             | 

### 10 warmup + 150 measurement iterations
| Benchmark                                    | Score         | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|----------------------------------------------|---------------|---------------------|-------|--------------------------| 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 392504.771497 | 100051.102020       | ms/op | JAMA                     | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 15521.286719  | 1062.093363         | ms/op | MTJ                      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 25114.277478  | 782.708886          | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 11476.616143  | 1464.335828         | ms/op | EVD_MTJ_SYMM             | 

Note that `JAMA` runs into a lot of troubles during benchmarking:
```
# JMH 1.18 (released 127 days ago)
# VM version: JDK 1.7.0_80, VM 24.80-b11
# VM invoker: /usr/lib/jvm/java-7-oracle/jre/bin/java
# VM options: -Dfile.encoding=US-ASCII -Duser.country=US -Duser.language=en -Duser.variant -Xmx16g -Dai.h2o.name=karel_PCABench
# Warmup: 10 iterations, 1 s each
# Measurement: 400 iterations, 1 s each
# Timeout: 15 min per iteration
# Threads: 1 thread, will synchronize iterations
# Benchmark mode: Average time, time/op
# Benchmark: hex.pca.PCAJMHTraining.measureQuasarTraining
# Parameters: (svdImplementation = JAMA)

# Run progress: 50.00% complete, ETA 00:46:36
# Fork: 1 of 1
# Warmup Iteration   1: 289189.575 ms/op
# Warmup Iteration   2: java.lang.ArrayIndexOutOfBoundsException: 1505
        at water.util.TwoDimTable.<init>(TwoDimTable.java:150)
        at hex.pca.PCA$PCADriver.buildTables(PCA.java:155)
        at hex.pca.PCA$PCADriver.computeStatsFillModel(PCA.java:253)
        at hex.pca.PCA$PCADriver.computeImpl(PCA.java:360)
        at hex.ModelBuilder$Driver.compute2(ModelBuilder.java:173)
        at water.H2O$H2OCountedCompleter.compute(H2O.java:1256)
        at jsr166y.CountedCompleter.exec(CountedCompleter.java:468)
        at jsr166y.ForkJoinTask.doExec(ForkJoinTask.java:263)
        at jsr166y.ForkJoinPool$WorkQueue.runTask(ForkJoinPool.java:974)
        at jsr166y.ForkJoinPool.runWorker(ForkJoinPool.java:1477)
        at jsr166y.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:104)
143455.825 ms/op
# Warmup Iteration   3: java.lang.ArrayIndexOutOfBoundsException
80779.007 ms/op
# Warmup Iteration   4: java.lang.ArrayIndexOutOfBoundsException
75347.968 ms/op
# Warmup Iteration   5: java.lang.ArrayIndexOutOfBoundsException
87158.757 ms/op
# Warmup Iteration   6: java.lang.ArrayIndexOutOfBoundsException
155068.816 ms/op
# Warmup Iteration   7: java.lang.ArrayIndexOutOfBoundsException
80308.500 ms/op
...
```

### 10 warmup + 400 measurement iterations
| Benchmark                                    | Samples | Score         | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|----------------------------------------------|---------|---------------|---------------------|-------|--------------------------| 
| hex.pca.PCAJMHScoring.measureQuasarScoring   | 3       | 39.701923     | 36.227966           | ms/op | MTJ                      | 
| hex.pca.PCAJMHScoring.measureQuasarScoring   | 27      | 174.801447    | 220.367041          | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 400     | 172049.874083 | 17059.100315        | ms/op | JAMA                     | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 400     | 13904.973061  | 581.715394          | ms/op | MTJ                      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 400     | 20494.275272  | 287.017995          | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 400     | 10526.038597  | 755.710913          | ms/op | EVD_MTJ_SYMM             | 

### 5 warmup + 1000 measurement iterations
| Benchmark                                    | Score         | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|----------------------------------------------|---------------|---------------------|-------|--------------------------| 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 127006.895907 | 8329.317490         | ms/op | JAMA                     | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 17057.334141  | 371.901861          | ms/op | MTJ                      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 20915.395808  | 183.976679          | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAJMHTraining.measureQuasarTraining | 14794.415830  | 485.443178          | ms/op | EVD_MTJ_SYMM             | 


## Conclusion
It seems that PCA implementation using *netlib-java* does help on this dataset, and the beste method appears to be `EVD_MTJ_SYMM`, i.e. spectral decomposition of the Gram matrix that I suggested.

Nevertheless, the benchmark with 150 measurement iterations did fail to measure scoring time. I am not entirely sure whether scoring is relevant for benchmarking, however, I will investigate and re-run this.

EDIT 23/4/2017
I've re-run JMH benchmarks with 400 iterations (see results above). Scoring still fails, training just confirms the superiority of my `EVD_MTJ_SYMM` method...