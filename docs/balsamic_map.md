| Balsamic tags                                                  | Mandatory   | HK tags                                 | Used by               |
|----------------------------------------------------------------|-------------|-----------------------------------------|-----------------------|
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                         | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                   | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                        | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal                  | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv-research       | deliver               |
| vcf-tnscope-umi, research-vcf-tnscope-umi-index                | True        | tnscope-umi, vcf-umi-snv-research-index | deliver               |
| snv, research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical       | deliver, scout        |
| snv, research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi | True        | tnscope-umi, vcf-umi-snv-clinical-index | deliver, scout        |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                              | audit, cg, vogue      |
| research-vcf-svdb, vcf-svdb                                    | True        | svdb, vcf-sv-research                   | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-research-index             | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                   | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-clinical-index             | deliver, scout        |
| snv, dnascope, vcf-all, annotated-germline-vcf-all             | True        | dnascope, germline, vcf                 | deliver               |
| snv, dnascope, vcf-all, annotated-germline-vcf-all-index       | True        | dnascope, germline, vcf-index           | deliver               |
| vcf-all, manta-germline, sv, annotated-germline-vcf-all        | True        | manta, germline, vcf                    | deliver               |
| vcf-all, manta-germline, sv, annotated-germline-vcf-all-index  | True        | manta, germline, vcf-index              | deliver               |
| research-vcf-tnscope, vcf-tnscope                              | False       | tnscope, vcf-snv-research               | deliver               |
| research-vcf-tnscope-index, vcf-tnscope                        | False       | tnscope, vcf-snv-research-index         | deliver               |
| snv, vcf-pass-tnscope, clinical-vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical               | deliver, scout        |
| snv, clinical-vcf-pass-tnscope-index, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index         | deliver, scout        |
| clinical-ascat-pdf, ascat-pdf                                  | False       | ascatngs, visualization                 | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                       | deliver               |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv-research               | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-research-index         | deliver               |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical               | deliver, scout        |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index         | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments               | deliver               |
| cnv-scatter, scatter                                           | False       | cnvkit, visualization, scatter          | deliver               |
| cnv-diagram, diagram                                           | False       | cnvkit, visualization, diagram          | deliver               |
| gene-metrics, cnv-gene-metrics                                 | False       | cnvkit, metrics, genes                  | deliver               |
| cnv-somatic-cgh-file, cgh-file                                 | False       | cnvkit, vcf2cytosure                    | deliver, scout        |
| clinical-rd-delly, rd-delly                                    | False       | delly, metrics                          | deliver               |
| balsamic-config                                                | True        | balsamic-config                         | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                         | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                            | audit                 |
| html, multiqc-html                                             | True        | multiqc-html                            | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                            | audit                 |
| cram, tumor-cram                                               | True        | tumor, cram                             | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                       | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                            | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                      | deliver, scout        |
