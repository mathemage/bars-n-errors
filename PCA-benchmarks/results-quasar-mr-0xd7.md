# PCAQuasar on mr-0xd7
@mmalohlava conjectured there might be a problem with the machine where the JMH benchmarks are run (my MacBook Pro 12. 1). Hence, I benchmarked on `mr-0xd7` machine:

```
mathemage@mr-0xd7:~$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                32
On-line CPU(s) list:   0-31
Thread(s) per core:    2
Core(s) per socket:    8
Socket(s):             2
NUMA node(s):          2
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 62
Stepping:              4
CPU MHz:               1200.000
BogoMIPS:              5201.42
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              20480K
NUMA node0 CPU(s):     0-7,16-23
NUMA node1 CPU(s):     8-15,24-31

mathemage@mr-0xd7:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 12.04.5 LTS
Release:        12.04
Codename:       precise

mathemage@mr-0xd7:~$ free -gt
             total       used       free     shared    buffers     cached
Mem:           251        204         47          0          2        174
-/+ buffers/cache:         27        224
Swap:          292          0        292
Total:         544        204        340
```

and here are the PCA benchmarks of the Quasar dataset on my ...

### 5 warmup + 20 measurement iterations
| Benchmark                                            | Score     | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|------------------------------------------------------|-----------|---------------------|-------|--------------------------| 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 5.040279  | 4.246233            | ms/op | JAMA                     | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 4.055162  | 1.280782            | ms/op | MTJ                      | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 5.445747  | 5.099791            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 4.424066  | 2.252146            | ms/op | EVD_MTJ_SYMM             | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 16.054728 | 16.982757           | ms/op | JAMA                     | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 15.517405 | 12.940478           | ms/op | MTJ                      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 14.569685 | 8.985811            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 12.221897 | 2.179354            | ms/op | EVD_MTJ_SYMM             | 

### 5 warmup + 100 measurement iterations
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

### 10 warmup + 1000 measurement iterations
| Benchmark                                            | Samples | Score      | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|------------------------------------------------------|---------|------------|---------------------|-------|--------------------------| 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 671     | 275.311175 | 283.175552          | ms/op | JAMA                     | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 667     | 165.287250 | 193.313163          | ms/op | MTJ                      | 
| hex.pca.PCAQuasarScoringBench.measureQuasarScoring   | 725     | 213.407434 | 226.836498          | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 1000    | 18.326709  | 1.026075            | ms/op | JAMA                     | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 1000    | 19.991994  | 1.823643            | ms/op | MTJ                      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 1000    | 19.262403  | 0.909833            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasarTrainingBench.measureQuasarTraining | 1000    | 20.365253  | 6.598955            | ms/op | EVD_MTJ_SYMM             | 

## Conclusion
Still it does not seem to be such a speedup for alternative implementation of PCA. I will do following improvements:
* run on the dataset `bigdata/laptop/jira/re0.wc.arff.txt.zip` suggested by @mmalohlava and @wendycwong 
* benchmarking via dedicated JUnit Test, which will be implemented in form of **for** loops and with warmup and measurement iterations