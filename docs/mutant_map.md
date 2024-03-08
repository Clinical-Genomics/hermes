| Mutant tags                           | Mandatory   | HK tags                                                        | Used by          |
|---------------------------------------|-------------|----------------------------------------------------------------|------------------|
| sampleinfo, runinfo                   | True        | config                                                         | storage, audit   |
| instrument-properties, report         | False       | fohm-delivery, instrument-properties                           | storage, audit   |
| runtime-settings, runinfo             | True        | mutant-config                                                  | storage, audit   |
| software-versions, runinfo            | True        | software-versions                                              | storage, audit   |
| runinfo, logfile                      | True        | mutant-log                                                     | audit            |
| concatination, forward-reads          | True        | fastq, forward-strand                                          | storage          |
| concatination, reverse-reads          | False       | fastq, reverse-strand                                          | storage          |
| report, SARS-CoV-2-info               | False       | fohm-delivery, komplettering, visualization                    | deliver          |
| result_aggregation, SARS-CoV-2-qc     | False       | fohm-delivery, pangolin-typing, csv, visualization             | audit            |
| report, pangolin-typing               | False       | fohm-delivery, pangolin-typing, visualization, csv             | audit            |
| report, pangolin-typing-fohm          | False       | fohm-delivery, pangolin-typing-fohm, csv                       | deliver          |
| alignment, reference-alignment-sorted | False       | bam                                                            | storage          |
| vcf-covid, genotyping                 | False       | vcf, vcf-report, fohm-delivery                                 | deliver          |
| vcf-covid, variant-calling            | False       | tsv, vcf-report                                                | deliver          |
| result_aggregation, metrics           | False       | metrics                                                        | storage          |
| report, multiqc-json                  | True        | multiqc-json                                                   | storage          |
| report, nextclade-summary             | True        | ks-delivery, typing-summary, nextclade                         | deliver          |
| report, ks-results                    | True        | ks-delivery, ks-results, typing-report, visualization, csv     | deliver          |
| report, ks-aux-results                | True        | ks-delivery, ks-aux-results, typing-report, visualization, csv | deliver          |
| consensus, analysis                   | True        | ks-delivery, fastq, consensus                                  | deliver, storage |
| consensus, consensus-sample           | False       | fohm-delivery, fasta, consensus-sample                         | deliver, storage |
| multiqc-html, report                  | True        | ks-delivery, multiqc-html                                      | deliver          |
| report, SARS-CoV-2-sum                | False       | artic-sum, csv                                                 | audit            |
| report, SARS-CoV-2-var                | False       | artic-var, csv                                                 | audit            |
| typing, SARS-CoV-2-type               | False       | artic-type, csv                                                | audit            |
