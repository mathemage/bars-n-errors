### Jama
```
Benchmark                                                   Mode  Cnt  Score   Error  Units
PCAImputeMissingScoringBench.measureImputeMissingScoring                     N/A  avgt   10    0.658 ±  0.429  ms/op
PCAImputeMissingTrainingBench.measureImputeMissingTraining                   N/A  avgt   10    2.310 ±  1.111  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                1  avgt   10    0.748 ±  1.056  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                2  avgt   10    1.009 ±  1.172  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                3  avgt   10    0.564 ±  0.705  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                4  avgt   10    0.552 ±  0.779  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                5  avgt   10    1.260 ±  0.787  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                6  avgt   10    1.003 ±  0.716  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              1  avgt   10    5.077 ±  2.474  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              2  avgt   10    7.640 ±  6.329  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              3  avgt   10    6.764 ±  7.270  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              4  avgt   10    7.304 ±  4.105  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              5  avgt   10  705.364 ± 50.947  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              6  avgt   10  691.045 ± 60.670  ms/op
```

### MTJ (netlib-java)
```
Benchmark                                                   Mode  Cnt  Score   Error  Units
PCAImputeMissingScoringBench.measureImputeMissingScoring                     N/A  avgt   10    0.781 ±   0.646  ms/op
PCAImputeMissingTrainingBench.measureImputeMissingTraining                   N/A  avgt   10    2.479 ±   1.466  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                1  avgt   10    2.066 ±   7.888  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                2  avgt   10    0.492 ±   0.667  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                3  avgt   10    0.568 ±   0.708  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                4  avgt   10    1.206 ±   2.768  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                5  avgt   10    2.338 ±   6.228  ms/op
PCAWideDataSetsScoringBench.measureWideDataSetsBenchScoringCase                6  avgt   10    0.670 ±   0.487  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              1  avgt   10    4.111 ±   1.610  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              2  avgt   10    6.223 ±   4.150  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              3  avgt   10    5.835 ±   3.349  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              4  avgt   10    7.771 ±   4.570  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              5  avgt   10  140.828 ±  96.366  ms/op
PCAWideDataSetsTrainingBench.measureWideDataSetsBenchTrainingCase              6  avgt   10  156.375 ± 112.684  ms/op
```

### System info
```bash
$ inxi 
CPU~Dual core Intel Core i5-4300M (-HT-MCP-) speed/max~2485/3300 MHz Kernel~4.4.0-72-generic x86_64 Up~3:37 Mem~2390.6/3831.1MB HDD~500.1GB(50.1% used) Procs~247 Client~Shell inxi~2.2.35  

$ inxi -S
System:    Host: ThinkPad-T440p Kernel: 4.4.0-72-generic x86_64 (64 bit) Desktop: Cinnamon 2.8.6
           Distro: Ubuntu 16.04 xenial
```
