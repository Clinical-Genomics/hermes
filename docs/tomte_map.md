| Tomte tags                          | Mandatory   | HK tags                                 | Used by                                     |
|-------------------------------------|-------------|-----------------------------------------|---------------------------------------------|
| transcript-counts, salmon           | True        | salmon-quant                            | clinical-delivery, long-term-storage        |
| snv, research-vcf                   | True        | research, vcf, snv                      | clinical-delivery, long-term-storage        |
| snv, research-vcf-index             | True        | research, vcf-index, snv                | clinical-delivery, long-term-storage        |
| clinical-vcf, snv                   | True        | clinical, vcf, snv                      | clinical-delivery, scout, long-term-storage |
| snv, clinical-vcf-index             | True        | clinical, vcf-index, snv                | clinical-delivery, scout, long-term-storage |
| fraser, fraser-clinical             | False       | fraser, clinical                        | clinical-delivery, long-term-storage        |
| fraser-research, fraser             | False       | fraser, research                        | clinical-delivery, long-term-storage        |
| outrider-clinical, outrider         | False       | outrider, clinical                      | clinical-delivery, long-term-storage        |
| outrider-research, outrider         | False       | outrider, research                      | clinical-delivery, long-term-storage        |
| star, star-cram                     | True        | cram                                    | clinical-delivery, scout                    |
| star, star-cram-index               | True        | cram-index                              | clinical-delivery                           |
| bigwig, coverage                    | True        | coverage, bigwig                        | clinical-delivery, scout, long-term-storage |
| junction, bed                       | True        | junction, bed                           | clinical-delivery, scout, long-term-storage |
| junction, bed-index                 | True        | junction, bed-index                     | clinical-delivery                           |
| stringtie, assembly                 | True        | stringtie, assembly                     | clinical-delivery, long-term-storage        |
| gffcompare                          | True        | gffcompare                              | clinical-delivery, long-term-storage        |
| raw-gene-counts, star               | True        | gene-counts                             | clinical-delivery, long-term-storage        |
| nextflow-config                     | True        | nextflow-config                         | cg, long-term-storage                       |
| nextflow-params                     | True        | nextflow-params                         | cg, long-term-storage                       |
| multiqc, multiqc-html               | True        | multiqc-html, rna                       | clinical-delivery, scout, long-term-storage |
| multiqc-json, multiqc               | True        | multiqc-json                            | clinical-delivery, long-term-storage        |
| multiqc-fastp, multiqc              | True        | qc-metrics, multiqc, fastp              | janus                                       |
| multiqc-fastqc, multiqc             | True        | qc-metrics, multiqc, fastqc             | janus                                       |
| multiqc, multiqc-bcftools-stats     | True        | qc-metrics, multiqc, bcftools-stats     | janus                                       |
| multiqc, multiqc-gffcompare         | True        | qc-metrics, multiqc, gffcompare         | janus                                       |
| multiqc-picard-rnaseq, multiqc      | True        | qc-metrics, multiqc, picard-rnaseq      | janus                                       |
| multiqc-star, multiqc               | True        | qc-metrics, multiqc, star               | janus                                       |
| multiqc, multiqc-general-stats      | True        | qc-metrics, multiqc, general-stats      | janus                                       |
| multiqc, multiqc-picard-insert-size | True        | qc-metrics, multiqc, picard-insert-size | janus                                       |
| samplesheet                         | True        | nextflow-samplesheet                    | cg, long-term-storage                       |
| software-versions                   | True        | software-versions                       | cg, clinical-delivery, long-term-storage    |
| qc-metrics                          | True        | qc-metrics, deliverable                 | cg, long-term-storage                       |
| manifest                            | False       | manifest                                | scout, long-term-storage                    |
