| Balsamic tags                                                  | Mandatory   | HK tags                                 | Used by               |
|----------------------------------------------------------------|-------------|-----------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                         | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                         | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                            | audit                 |
| multiqc-html, html                                             | True        | multiqc-html                            | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                            | audit                 |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics                              | audit, cg, vogue      |
| cram, tumor-cram                                               | True        | tumor, cram                             | deliver, scout        |
| tumor-cram-index, cram                                         | True        | tumor, cram-index                       | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                            | deliver, scout        |
| normal-cram-index, cram                                        | False       | normal, cram-index                      | deliver, scout        |
| dnascope, vcf-all, annotated-germline-vcf-all, snv             | True        | dnascope, germline, vcf                 | deliver               |
| dnascope, annotated-germline-vcf-all-index, vcf-all, snv       | True        | dnascope, germline, vcf-index           | deliver               |
| genotype-vcf-dnascope, vcf-dnascope                            | False       | dnascope, normal, vcf                   | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                      | False       | dnascope, normal, vcf-index             | cg, genotype          |
| annotated-germline-vcf-all, vcf-all, manta-germline, sv        | True        | manta, germline, vcf                    | deliver               |
| annotated-germline-vcf-all-index, vcf-all, manta-germline, sv  | True        | manta, germline, vcf-index              | deliver               |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research                   | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-research-index             | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                   | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index             | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv-research               | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-research-index         | deliver               |
| clinical-vcf-pass-tnscope, vcf-pass-tnscope, snv               | False       | tnscope, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-tnscope, snv, clinical-vcf-pass-tnscope-index         | False       | tnscope, vcf-snv-clinical-index         | deliver, scout        |
| clinical-ascat-pdf, ascat-pdf                                  | False       | ascatngs, visualization                 | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                       | deliver               |
| rd-delly, clinical-rd-delly                                    | True        | delly, coverage                         | deliver               |
| cgh-tumor, cnv-somatic-cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure             | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                             | False       | tiddit, normal, vcf2cytosure            | deliver, scout        |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv-research               | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-research-index         | deliver               |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index         | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments               | deliver               |
| cnv-scatter, scatter                                           | False       | cnvkit, visualization, scatter          | deliver               |
| cnv-diagram, diagram                                           | False       | cnvkit, visualization, diagram          | deliver               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes                  | deliver               |
| clinical-cov-tumor-tiddit, cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                 | deliver               |
| clinical-cov-normal-tiddit, cov-normal-tiddit                  | False       | tiddit, normal, coverage                | deliver               |
| umi-tumor-cram, cram                                           | True        | umi-cram, tumor                         | deliver, scout        |
| umi-tumor-cram-index, cram                                     | True        | umi-cram-index, tumor                   | deliver, scout        |
| umi-normal-cram, cram                                          | False       | umi-cram, normal                        | deliver, scout        |
| umi-normal-cram-index, cram                                    | False       | umi-cram-index, normal                  | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv-research       | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True        | tnscope-umi, vcf-umi-snv-research-index | deliver               |
| clinical-vcf-pass-tnscope-umi, snv, vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical       | deliver, scout        |
| clinical-vcf-pass-tnscope-umi-index, snv, vcf-pass-tnscope-umi | True        | tnscope-umi, vcf-umi-snv-clinical-index | deliver, scout        |
