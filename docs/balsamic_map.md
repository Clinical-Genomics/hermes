| Balsamic tags                                                  | Mandatory   | HK tags                             | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------|-----------------------|
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                     | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor               | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                    | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal              | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-research       | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True        | tnscope-umi, vcf-umi-research-index | deliver               |
| vcf-pass-tnscope-umi, snv, research-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-clinical       | deliver, scout        |
| vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi-index, snv | True        | tnscope-umi, vcf-umi-clinical-index | deliver, scout        |
| balsamic-config                                                | True        | balsamic-config                     | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                     | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                        | audit                 |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics                          | audit, cg, vogue      |
| html, multiqc-html                                             | True        | multiqc-html                        | audit, deliver, scout |
| multiqc-json, json                                             | True        | multiqc-json                        | audit                 |
| cram, tumor-cram                                               | True        | tumor, cram                         | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                   | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                        | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                  | deliver, scout        |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research               | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-research-index         | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical               | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-clinical-index         | deliver, scout        |
| vcf-all, snv, dnascope, annotated-germline-vcf-all             | True        | dnascope, germline, vcf             | deliver               |
| vcf-all, snv, dnascope, annotated-germline-vcf-all-index       | True        | dnascope, germline, vcf-index       | deliver               |
| sv, manta-germline, vcf-all, annotated-germline-vcf-all        | True        | manta, germline, vcf                | deliver               |
| sv, manta-germline, vcf-all, annotated-germline-vcf-all-index  | True        | manta, germline, vcf-index          | deliver               |
| research-vcf-tnscope, vcf-tnscope                              | False       | tnscope, vcf-snv-research           | deliver               |
| research-vcf-tnscope-index, vcf-tnscope                        | False       | tnscope, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-tnscope, snv, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-tnscope-index, snv, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index     | deliver, scout        |
| ascat-pdf, clinical-ascat-pdf                                  | False       | ascatngs, visualization             | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                    | False       | ascatngs, metrics                   | deliver               |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv-research           | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-vardict, snv, vcf-pass-vardict               | False       | vardict, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-vardict-index, snv, vcf-pass-vardict         | False       | vardict, vcf-snv-clinical-index     | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments           | deliver               |
| scatter, cnv-scatter                                           | False       | cnvkit, visualization, scatter      | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram      | deliver               |
| gene-metrics, cnv-gene-metrics                                 | False       | cnvkit, metrics, genes              | deliver               |
| cgh-file, cnv-somatic-cgh-file                                 | False       | cnvkit, vcf2cytosure                | deliver, scout        |
| rd-delly, clinical-rd-delly                                    | False       | delly, metrics                      | deliver               |
