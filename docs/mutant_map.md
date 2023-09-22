| MUTANT tags                           | Mandatory | HK tags                                                        | Used by          |
|---------------------------------------|-----------|----------------------------------------------------------------|------------------|
| sampleinfo, runinfo                   | True      | config                                                         | storage, audit   |
| instrument-properties, report         | False     | fohm-delivery, instrument-properties                           | storage, audit   |
| runtime-settings, runinfo             | True      | mutant-config                                                  | storage, audit   |
| software-versions, runinfo            | True      | software-versions                                              | storage, audit   |
| runinfo, logfile                      | True      | mutant-log                                                     | audit            |
| concatination, forward-reads          | True      | fastq, forward-strand                                          | storage          |
| concatination, reverse-reads          | False     | fastq, reverse-strand                                          | storage          |
| SARS-CoV-2-info, report               | False     | fohm-delivery, komplettering, visualization                    | deliver          |
| SARS-CoV-2-qc, result_aggregation     | False     | fohm-delivery, pangolin-typing, csv, visualization             | audit            |
| pangolin-typing, report               | False     | fohm-delivery, pangolin-typing, csv, visualization             | audit            |
| pangolin-typing-fohm, report          | False     | fohm-delivery, pangolin-typing-fohm, csv                       | deliver          |
| alignment, reference-alignment-sorted | False     | bam                                                            | storage          |
| vcf-covid, genotyping                 | False     | vcf, vcf-report, fohm-delivery                                 | deliver          |
| vcf-covid, variant-calling            | False     | tsv, vcf-report                                                | deliver          |
| metrics, result_aggregation           | False     | metrics                                                        | vogue            |
| multiqc-json, report                  | True      | multiqc-json                                                   | vogue            |
| nextclade-summary, report             | True      | typing-summary, nextclade                                      | deliver          |
| ks-results, report                    | True      | ks-delivery, ks-results, typing-report, visualization, csv     | deliver          |
| ks-aux-results, report                | True      | ks-delivery, ks-aux-results, typing-report, visualization, csv | deliver          |
| consensus, analysis                   | True      | ks-delivery, fastq, consensus                                  | deliver, storage |
| consensus-sample, consensus           | False     | fohm-delivery, fasta, consensus-sample                         | deliver, storage |
| multiqc-html, report                  | True      | ks-delivery, multiqc-html                                      | deliver          |
| SARS-CoV-2-sum, report                | False     | artic-sum, csv                                                 | audit            |
| SARS-CoV-2-var, report                | False     | artic-var, csv                                                 | audit            |
| SARS-CoV-2-type, typing               | False     | artic-type, csv                                                | audit            |
