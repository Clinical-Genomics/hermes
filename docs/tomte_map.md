| Tomte tags                          | Mandatory   | HK tags                                 | Used by                                     |
|-------------------------------------|-------------|-----------------------------------------|---------------------------------------------|
| fraser, fraser-clinical             | False       | fraser, clinical                        | clinical-delivery, long-term-storage        |
| fraser, fraser-research             | False       | fraser, research                        | clinical-delivery, long-term-storage        |
| outrider-clinical, outrider         | False       | outrider, clinical                      | clinical-delivery, long-term-storage        |
| outrider-research, outrider         | False       | outrider, research                      | clinical-delivery, long-term-storage        |
| star, star-cram                     | True        | cram                                    | clinical-delivery, scout                    |
| star-cram-index, star               | True        | cram-index                              | clinical-delivery                           |
| coverage, bigwig                    | True        | coverage, bigwig                        | clinical-delivery, scout, long-term-storage |
| bed, junction                       | True        | junction, bed                           | clinical-delivery, scout, long-term-storage |
| bed-index, junction                 | True        | junction, bed-index                     | clinical-delivery                           |
| assembly, stringtie                 | True        | stringtie, assembly                     | clinical-delivery, long-term-storage        |
| gffcompare                          | True        | gffcompare                              | clinical-delivery, long-term-storage        |
| raw-gene-counts, star               | True        | gene-counts                             | clinical-delivery, long-term-storage        |
| samplesheet                         | True        | nextflow-samplesheet                    | cg, long-term-storage                       |
| nextflow-config                     | True        | nextflow-config                         | cg, long-term-storage                       |
| qc-metrics                          | True        | qc-metrics                              | cg, long-term-storage                       |
| multiqc-html, multiqc               | True        | multiqc-html, rna                       | clinical-delivery, scout, long-term-storage |
| multiqc, multiqc-json               | True        | multiqc-json                            | clinical-delivery, long-term-storage        |
| multiqc-fastp, multiqc              | True        | qc-metrics, multiqc, fastp              | janus                                       |
| multiqc-fastqc, multiqc             | True        | qc-metrics, multiqc, fastqc             | janus                                       |
| multiqc-bcftools-stats, multiqc     | True        | qc-metrics, multiqc, bcftools-stats     | janus                                       |
| multiqc-gffcompare, multiqc         | True        | qc-metrics, multiqc, gffcompare         | janus                                       |
| multiqc-picard-rnaseq, multiqc      | True        | qc-metrics, multiqc, picard-rnaseq      | janus                                       |
| multiqc-star, multiqc               | True        | qc-metrics, multiqc, star               | janus                                       |
| multiqc-general-stats, multiqc      | True        | qc-metrics, multiqc, general-stats      | janus                                       |
| multiqc-picard-insert-size, multiqc | True        | qc-metrics, multiqc, picard-insert-size | janus                                       |
| software-versions                   | True        | software-versions                       | cg, long-term-storage                       |
