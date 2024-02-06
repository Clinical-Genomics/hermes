| Microsalt tags                        | Mandatory | HK tags                      | Used by        |
|---------------------------------------|-----------|------------------------------|----------------|
| sampleinfo, analysis                  | True      | config                       | storage, audit |
| microsalt-qc, result_aggregation      | True      | qc-report, visualization     | deliver        |
| result_aggregation, microsalt-type    | False     | typing-report, visualization | deliver        |
| microsalt-json, result_aggregation    | False     | typing-report, qc-metrics    | storage        |
| analysis, runtime-settings            | True      | microsalt-config             | storage, audit |
| assembly                              | False     | assembly                     | storage        |
| trimmed-forward-reads, concatination  | False     | fastq, forward-strand        | storage        |
| concatination, trimmed-reverse-reads  | False     | fastq, reverse-strand        | storage        |
| concatination, trimmed-unpaired-reads | False     | fastq, unpaired-reads        | storage        |
| analysis, logfile                     | False     | microsalt-log                | audit          |
| assembly, quast-results               | False     | qc-metrics, assembly         | audit          |
| alignment, reference-alignment-sorted | False     | bam                          | storage        |
| insertsize_calc, picard-insertsize    | False     | qc-metrics, picard           | audit          |
