| Tomte tags                           | Mandatory | HK tags                                  | Used by                                      |
|--------------------------------------|-----------|------------------------------------------|----------------------------------------------|
| fraser, fraser-clinical              | FALSE     | fraser, clinical                         | clinical-delivery, long-term-storage         |
| fraser, fraser-research              | FALSE     | fraser, research                         | clinical-delivery, long-term-storage         |
| outrider, outrider-clinical          | FALSE     | outrider, clinical                       | clinical-delivery, long-term-storage         |
| outrider, outrider-research          | FALSE     | outrider, research                       | clinical-delivery, long-term-storage         |
| star, star-cram                      | TRUE      | cram                                     | clinical-delivery, scout                     |
| star, star-cram-index                | TRUE      | cram-index                               | clinical-delivery                            |
| coverage, bigwig                     | TRUE      | coverage, bigwig                         | clinical-delivery, scout, long-term-storage  |
| junction, bed                        | TRUE      | junction, bed                            | clinical-delivery, scout, long-term-storage  |
| junction, bed-index                  | TRUE      | junction, bed-index                      | clinical-delivery                            |
| stringtie, assembly                  | TRUE      | stringtie, assembly                      | clinical-delivery, long-term-storage         |
| gffcompare                           | TRUE      | gffcompare                               | clinical-delivery, long-term-storage         |
| star, raw-gene-counts                | TRUE      | gene-counts                              | clinical-delivery, long-term-storage         |
| software-versions                    | TRUE      | software-versions                        | cg, long-term-storage                        |
| samplesheet                          | TRUE      | samplesheet                              | cg, long-term-storage                        |
| nextflow-config                      | TRUE      | nextflow-config                          | cg, long-term-storage                        |
| qc-metrics                           | TRUE      | qc-metrics                               | cg, long-term-storage                        |
| multiqc, multiqc-html                | TRUE      | multiqc-html, rna                        | clinical-delivery, scout, long-term-storage  |
| multiqc, multiqc-json                | TRUE      | multiqc-json                             | clinical-delivery, long-term-storage         |
| multiqc, multiqc-fastp               | TRUE      | qc-metrics, multiqc, fastp               | janus                                        |
| multiqc, multiqc-fastqc              | TRUE      | qc-metrics, multiqc, fastqc              | janus                                        |
| multiqc, multiqc-bcftools-stats      | TRUE      | qc-metrics, multiqc, bcftools-stats      | janus                                        |
| multiqc, multiqc-gffcompare          | TRUE      | qc-metrics, multiqc, gffcompare          | janus                                        |
| multiqc, multiqc-picard-rnaseq       | TRUE      | qc-metrics, multiqc, picard-rnaseq       | janus                                        |
| multiqc, multiqc-star                | TRUE      | qc-metrics, multiqc, star                | janus                                        |
| multiqc, multiqc-general-stats       | TRUE      | qc-metrics, multiqc, general-stats       | janus                                        |
| multiqc, multiqc-picard-insert-size  | TRUE      | qc-metrics, multiqc, picard-insert-size  | janus                                        |