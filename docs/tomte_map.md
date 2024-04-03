| Tomte tags                           | Mandatory | HK tags                                  | Used by         |
|--------------------------------------|-----------|------------------------------------------|-----------------|
| fraser, fraser-clinical              | FALSE     | fraser, clinical                         | deliver         |
| fraser, fraser-research              | FALSE     | fraser, research                         | deliver         |
| outrider, outrider-clinical          | FALSE     | outrider, clinical                       | deliver         |
| outrider, outrider-research          | FALSE     | outrider, research                       | deliver         |
| star, star-cram                      | TRUE      | cram                                     | deliver, scout  |
| star, star-cram-index                | TRUE      | cram-index                               | deliver         |
| coverage, bigwig                     | TRUE      | coverage, bigwig                         | deliver, scout  |
| junction, bed                        | TRUE      | junction, bed                            | deliver, scout  |
| junction, bed-index                  | TRUE      | junction, bed-index                      | deliver         |
| stringtie, assembly                  | TRUE      | stringtie, assembly                      | deliver         |
| gffcompare                           | TRUE      | gffcompare                               | deliver         |
| star, raw-gene-counts                | TRUE      | gene-counts                              | deliver         |
| software-versions                    | TRUE      | software-versions                        | cg              |
| samplesheet                          | TRUE      | samplesheet                              | cg              |
| nextflow-config                      | TRUE      | nextflow-config                          | cg              |
| qc-metrics                           | TRUE      | qc-metrics                               | cg              |
| multiqc, multiqc-html                | TRUE      | multiqc-html, rna                        | deliver, scout  |
| multiqc, multiqc-json                | TRUE      | multiqc-json                             | deliver         |
| multiqc, multiqc-fastp               | TRUE      | qc-metrics, multiqc, fastp               | janus           |
| multiqc, multiqc-fastqc              | TRUE      | qc-metrics, multiqc, fastqc              | janus           |
| multiqc, multiqc-bcftools-stats      | TRUE      | qc-metrics, multiqc, bcftools-stats      | janus           |
| multiqc, multiqc-gffcompare          | TRUE      | qc-metrics, multiqc, gffcompare          | janus           |
| multiqc, multiqc-picard-rnaseq       | TRUE      | qc-metrics, multiqc, picard-rnaseq       | janus           |
| multiqc, multiqc-star                | TRUE      | qc-metrics, multiqc, star                | janus           |
| multiqc, multiqc-general-stats       | TRUE      | qc-metrics, multiqc, general-stats       | janus           |
| multiqc, multiqc-picard-insert-size  | TRUE      | qc-metrics, multiqc, picard-insert-size  | janus           |