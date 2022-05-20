| Balsamic tags                                                  | Mandatory   | HK tags                             | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------|-----------------------|
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                     | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor               | deliver, scout        |
| umi-normal-cram, cram                                          | False       | umi-cram, normal                    | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal              | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-research       | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True        | tnscope-umi, vcf-umi-research-index | deliver               |
| snv, research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-clinical       | deliver, scout        |
| research-vcf-pass-tnscope-umi-index, snv, vcf-pass-tnscope-umi | True        | tnscope-umi, vcf-umi-clinical-index | deliver, scout        |
| balsamic-config                                                | True        | balsamic-config                     | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                     | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                        | audit                 |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics                          | audit, cg, vogue      |
| multiqc-html, html                                             | True        | multiqc-html                        | audit, deliver, scout |
| multiqc-json, json                                             | True        | multiqc-json                        | audit                 |
| tumor-cram, cram                                               | True        | tumor, cram                         | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                   | deliver, scout        |
| normal-cram, cram                                              | False       | normal, cram                        | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                  | deliver, scout        |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research               | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-research-index         | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical               | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-clinical-index         | deliver, scout        |
| dnascope, snv, vcf-all, annotated-germline-vcf-all             | True        | dnascope, germline, vcf             | deliver               |
| dnascope, snv, vcf-all, annotated-germline-vcf-all-index       | True        | dnascope, germline, vcf-index       | deliver               |
| manta-germline, vcf-all, annotated-germline-vcf-all, sv        | True        | manta, germline, vcf                | deliver               |
| manta-germline, vcf-all, annotated-germline-vcf-all-index, sv  | True        | manta, germline, vcf-index          | deliver               |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv-research           | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-research-index     | deliver               |
| vcf-pass-tnscope, snv, clinical-vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical           | deliver, scout        |
| vcf-pass-tnscope, snv, clinical-vcf-pass-tnscope-index         | False       | tnscope, vcf-snv-clinical-index     | deliver, scout        |
| clinical-ascat-pdf, ascat-pdf                                  | False       | ascatngs, visualization             | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                   | deliver               |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv-research           | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-research-index     | deliver               |
| snv, clinical-vcf-pass-vardict, vcf-pass-vardict               | False       | vardict, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-vardict-index, snv, vcf-pass-vardict         | False       | vardict, vcf-snv-clinical-index     | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments           | deliver               |
| cnv-scatter, scatter                                           | False       | cnvkit, visualization, scatter      | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram      | deliver               |
| gene-metrics, cnv-gene-metrics                                 | False       | cnvkit, metrics, genes              | deliver               |
| cnv-somatic-cgh-file, cgh-file                                 | False       | cnvkit, vcf2cytosure                | deliver, scout        |
| clinical-rd-delly, rd-delly                                    | False       | delly, metrics                      | deliver               |
