| Mutant tags                           | Mandatory | HK tags                                                        | Used by          |
|---------------------------------------|-----------|----------------------------------------------------------------|------------------|
| sampleinfo, runinfo                   | True      | config                                                         | storage, audit   |
| report, instrument-properties         | False     | fohm-delivery, instrument-properties                           | storage, audit   |
| runtime-settings, runinfo             | True      | mutant-config                                                  | storage, audit   |
| software-versions, runinfo            | True      | software-versions                                              | storage, audit   |
| logfile, runinfo                      | True      | mutant-log                                                     | audit            |
| forward-reads, concatination          | True      | fastq, forward-strand                                          | storage          |
| concatination, reverse-reads          | False     | fastq, reverse-strand                                          | storage          |
| SARS-CoV-2-info, report               | False     | fohm-delivery, komplettering, visualization                    | deliver          |
| result_aggregation, SARS-CoV-2-qc     | False     | fohm-delivery, pangolin-typing, csv, visualization             | audit            |
| pangolin-typing, report               | False     | fohm-delivery, pangolin-typing, visualization, csv             | audit            |
| report, pangolin-typing-fohm          | False     | fohm-delivery, pangolin-typing-fohm, csv                       | deliver          |
| reference-alignment-sorted, alignment | False     | bam                                                            | storage          |
| genotyping, vcf-covid                 | False     | vcf, vcf-report, fohm-delivery                                 | deliver          |
| variant-calling, vcf-covid            | False     | tsv, vcf-report                                                | deliver          |
| result_aggregation, metrics           | False     | metrics                                                        | storage          |
| multiqc-json, report                  | True      | multiqc-json                                                   | storage          |
| nextclade-summary, report             | True      | ks-delivery, typing-summary, nextclade                         | deliver          |
| report, ks-results                    | True      | ks-delivery, ks-results, typing-report, visualization, csv     | deliver          |
| ks-aux-results, report                | True      | ks-delivery, ks-aux-results, typing-report, visualization, csv | deliver          |
| consensus, analysis                   | True      | ks-delivery, fastq, consensus                                  | deliver, storage |
| consensus-sample, consensus           | False     | fohm-delivery, fasta, consensus-sample                         | deliver, storage |
| report, multiqc-html                  | True      | ks-delivery, multiqc-html                                      | deliver          |
| SARS-CoV-2-sum, report                | False     | artic-sum, csv                                                 | audit            |
| SARS-CoV-2-var, report                | False     | artic-var, csv                                                 | audit            |
| typing, SARS-CoV-2-type               | False     | artic-type, csv                                                | audit            |
