| Tomte tags                           | Mandatory | HK tags                                  | Used by                  |
|--------------------------------------|-----------|------------------------------------------|--------------------------|
| fraser, fraser-clinical              | FALSE     | fraser, clinical                         | clinical-delivery        |
| fraser, fraser-research              | FALSE     | fraser, research                         | clinical-delivery        |
| outrider, outrider-clinical          | FALSE     | outrider, clinical                       | clinical-delivery        |
| outrider, outrider-research          | FALSE     | outrider, research                       | clinical-delivery        |
| star, star-cram                      | TRUE      | cram                                     | clinical-delivery, scout |
| star, star-cram-index                | TRUE      | cram-index                               | clinical-delivery        |
| coverage, bigwig                     | TRUE      | coverage, bigwig                         | clinical-delivery, scout |
| junction, bed                        | TRUE      | junction, bed                            | clinical-delivery, scout |
| junction, bed-index                  | TRUE      | junction, bed-index                      | clinical-delivery        |
| stringtie, assembly                  | TRUE      | stringtie, assembly                      | clinical-delivery        |
| gffcompare                           | TRUE      | gffcompare                               | clinical-delivery        |
| star, raw-gene-counts                | TRUE      | gene-counts                              | clinical-delivery        |
| software-versions                    | TRUE      | software-versions                        | cg                       |
| samplesheet                          | TRUE      | samplesheet                              | cg                       |
| nextflow-config                      | TRUE      | nextflow-config                          | cg                       |
| qc-metrics                           | TRUE      | qc-metrics                               | cg                       |
| multiqc, multiqc-html                | TRUE      | multiqc-html, rna                        | clinical-delivery, scout |
| multiqc, multiqc-json                | TRUE      | multiqc-json                             | clinical-delivery        |
| multiqc, multiqc-fastp               | TRUE      | qc-metrics, multiqc, fastp               | janus                    |
| multiqc, multiqc-fastqc              | TRUE      | qc-metrics, multiqc, fastqc              | janus                    |
| multiqc, multiqc-bcftools-stats      | TRUE      | qc-metrics, multiqc, bcftools-stats      | janus                    |
| multiqc, multiqc-gffcompare          | TRUE      | qc-metrics, multiqc, gffcompare          | janus                    |
| multiqc, multiqc-picard-rnaseq       | TRUE      | qc-metrics, multiqc, picard-rnaseq       | janus                    |
| multiqc, multiqc-star                | TRUE      | qc-metrics, multiqc, star                | janus                    |
| multiqc, multiqc-general-stats       | TRUE      | qc-metrics, multiqc, general-stats       | janus                    |
| multiqc, multiqc-picard-insert-size  | TRUE      | qc-metrics, multiqc, picard-insert-size  | janus                    |