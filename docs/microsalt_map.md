| Microsalt tags                        | Mandatory   | HK tags                      | Used by        |
|---------------------------------------|-------------|------------------------------|----------------|
| sampleinfo, analysis                  | True        | config                       | storage, audit |
| microsalt-qc, result_aggregation      | True        | qc-report, visualization     | deliver        |
| microsalt-type, result_aggregation    | False       | typing-report, visualization | deliver        |
| result_aggregation, microsalt-json    | False       | typing-report, qc-metrics    | storage        |
| analysis, runtime-settings            | True        | microsalt-config             | storage, audit |
| assembly                              | False       | assembly                     | storage        |
| concatination, trimmed-forward-reads  | False       | fastq, forward-strand        | storage        |
| concatination, trimmed-reverse-reads  | False       | fastq, reverse-strand        | storage        |
| concatination, trimmed-unpaired-reads | False       | fastq, unpaired-reads        | storage        |
| logfile, analysis                     | False       | microsalt-log                | audit          |
| quast-results, assembly               | False       | qc-metrics, assembly         | audit          |
| alignment, reference-alignment-sorted | False       | bam                          | storage        |
| insertsize_calc, picard-insertsize    | False       | qc-metrics, picard           | audit          |
