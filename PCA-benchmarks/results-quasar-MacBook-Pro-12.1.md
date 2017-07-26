# PCAQuasar on MacBook Pro 12.1
Here are the PCA benchmarks of the Quasar dataset on my MacBook Pro...

### 5 warmup + 10 measurement iterations
| Benchmark                               | Score     | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|-----------------------------------------|-----------|---------------------|-------|--------------------------| 
| hex.pca.PCAQuasar.measureQuasarTraining | 30.995952 | 18.537174           | ms/op | JAMA                     | 
| hex.pca.PCAQuasar.measureQuasarTraining | 32.865912 | 22.690285           | ms/op | MTJ                      | 
| hex.pca.PCAQuasar.measureQuasarTraining | 30.612890 | 25.187364           | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasar.measureQuasarTraining | 31.386312 | 23.365714           | ms/op | EVD_MTJ_SYMM             | 

### 5 warmup + 100 measurement iterations
| Benchmark                               | Score     | Score Error (99.9%) | Unit  | Param: svdImplementation | 
|-----------------------------------------|-----------|---------------------|-------|--------------------------| 
| hex.pca.PCAQuasar.measureQuasarTraining | 28.331931 | 1.714558            | ms/op | JAMA                     | 
| hex.pca.PCAQuasar.measureQuasarTraining | 27.914069 | 5.555480            | ms/op | MTJ                      | 
| hex.pca.PCAQuasar.measureQuasarTraining | 27.514898 | 2.425912            | ms/op | EVD_MTJ_DENSEMATRIX      | 
| hex.pca.PCAQuasar.measureQuasarTraining | 27.174700 | 2.726259            | ms/op | EVD_MTJ_SYMM             | 

## Conclusion
It does not seem to be such a speedup for alternative implementation of PCA. I am yet to run JMH with larger number of measurement iterations (500), we'll see what will be the result. Also, the scoring of PCAQuasar needs to be measured...