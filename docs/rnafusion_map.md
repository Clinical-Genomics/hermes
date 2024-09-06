| Rnafusion tags                       | Mandatory   | HK tags                                               | Used by                                  |
|--------------------------------------|-------------|-------------------------------------------------------|------------------------------------------|
| arriba                               | True        | arriba, fusion                                        | clinical-delivery, long-term-storage     |
| arriba, arriba-visualisation         | False       | arriba-visualisation, visualization, arriba, research | clinical-delivery, long-term-storage     |
| fusioncatcher                        | True        | fusioncatcher, fusion                                 | clinical-delivery, long-term-storage     |
| fusioncatcher, fusioncatcher-summary | True        | fusioncatcher-summary                                 | clinical-delivery                        |
| star-fusion                          | True        | star-fusion, fusion                                   | clinical-delivery, long-term-storage     |
| fusionreport, report                 | True        | fusionreport, research                                | clinical-delivery, long-term-storage     |
| report, fusioninspector              | False       | fusioninspector                                       | clinical-delivery, long-term-storage     |
| report, fusioninspector-html         | False       | fusioninspector-html, research                        | clinical-delivery, long-term-storage     |
| multiqc-html, report                 | True        | multiqc-html, rna                                     | clinical-delivery, long-term-storage     |
| star-fusion, star-fusion-cram        | True        | cram                                                  | clinical-delivery                        |
| star-fusion-cram-index, star-fusion  | True        | cram-index                                            | clinical-delivery                        |
| star-align-gene-counts, star-align   | True        | gene-counts                                           | clinical-delivery, long-term-storage     |
| multiqc-json                         | True        | multiqc-json                                          | cg                                       |
| vcf-fusion, vcf-collect              | False       | vcf-fusion                                            | clinical-delivery, long-term-storage     |
| multiqc, multiqc-fastp               | True        | qc-metrics, multiqc, fastp                            | janus                                    |
| multiqc, multiqc-picard-duplicates   | True        | qc-metrics, multiqc, picard-duplicates                | janus                                    |
| multiqc, multiqc-picard-insert-size  | True        | qc-metrics, multiqc, picard-insert-size               | janus                                    |
| multiqc, multiqc-picard-rnaseq       | True        | qc-metrics, multiqc, picard-rnaseq                    | janus                                    |
| multiqc, multiqc-general-stats       | True        | qc-metrics, multiqc, general-stats                    | janus                                    |
| multiqc, multiqc-star                | True        | qc-metrics, multiqc, star                             | janus                                    |
| samplesheet-valid                    | True        | samplesheet-valid                                     | cg                                       |
| software-versions                    | True        | software-versions                                     | cg, clinical-delivery, long-term-storage |
| qc-metrics                           | True        | qc-metrics, deliverable                               | cg, long-term-storage                    |
| manifest                             | False       | manifest                                              | scout, long-term-storage                 |
