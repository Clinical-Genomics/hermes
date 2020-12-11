| Microsalt tags                        | Mandatory   | HK tags                      | Used by        |
|---------------------------------------|-------------|------------------------------|----------------|
| analysis, sampleinfo                  | True        | config                       | storage, audit |
| microsalt-qc, result_aggregation      | True        | qc-report, visualization     | deliver        |
| microsalt-type, result_aggregation    | True        | typing-report, visualization | deliver        |
| microsalt-json, result_aggregation    | False       | typing-report, qc-metrics    | vogue          |
| runtime-settings, analysis            | True        | microsalt-config             | storage, audit |
| assembly                              | True        | assembly                     | storage        |
| concatination, trimmed-forward-reads  | False       | fastq, forward-strand        | storage        |
| concatination, trimmed-reverse-reads  | False       | fastq, reverse-strand        | storage        |
| concatination, trimmed-unpaired-reads | False       | fastq, unpaired-reads        | storage        |
| analysis, logfile                     | True        | microsalt-log                | audit          |
| assembly, quast-results               | False       | qc-metrics, assembly         | audit          |
| reference-alignment-sorted, alignment | True        | bam                          | storage        |
| insertsize_calc, picard-insertsize    | False       | qc-metrics, picard           | audit          |
