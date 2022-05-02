| Balsamic tags                                                  | Mandatory   | HK tags                             | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                     | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                     | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                        | audit                 |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics                          | audit, cg, vogue      |
| multiqc-html, html                                             | True        | multiqc-html                        | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                        | audit                 |
| cram, tumor-cram                                               | True        | tumor, cram                         | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                   | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                        | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                  | deliver, scout        |
| cram, umi-tumor-cram                                           | False       | umi-cram, tumor                     | deliver, scout        |
| cram, umi-tumor-cram-index                                     | False       | umi-cram-index, tumor               | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                    | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal              | deliver, scout        |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research               | deliver               |
| vcf-svdb, research-vcf-svdb-index                              | True        | svdb, vcf-sv-research-index         | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical               | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-clinical-index         | deliver, scout        |
| dnascope, vcf-all, snv, annotated-germline-vcf-all             | True        | dnascope, germline, vcf             | deliver               |
| dnascope, annotated-germline-vcf-all-index, vcf-all, snv       | True        | dnascope, germline, vcf-index       | deliver               |
| annotated-germline-vcf-all, manta-germline, sv, vcf-all        | True        | manta, germline, vcf                | deliver               |
| annotated-germline-vcf-all-index, manta-germline, sv, vcf-all  | True        | manta, germline, vcf-index          | deliver               |
| research-vcf-tnscope, vcf-tnscope                              | False       | tnscope, vcf-snv-research           | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-tnscope, vcf-pass-tnscope, snv               | False       | tnscope, vcf-snv-clinical           | deliver, scout        |
| vcf-pass-tnscope, clinical-vcf-pass-tnscope-index, snv         | False       | tnscope, vcf-snv-clinical-index     | deliver, scout        |
| clinical-ascat-pdf, ascat-pdf                                  | False       | ascatngs, visualization             | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                   | deliver               |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-vardict, vcf-pass-vardict, snv               | False       | vardict, vcf-snv-clinical           | deliver, scout        |
| vcf-pass-vardict, clinical-vcf-pass-vardict-index, snv         | False       | vardict, vcf-snv-clinical-index     | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                      | False       | tnscope-umi, vcf-snv-research       | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | False       | tnscope-umi, vcf-snv-research-index | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | False       | tnscope-umi, vcf-snv-clinical       | deliver, scout        |
| vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi-index, snv | False       | tnscope-umi, vcf-snv-clinical-index | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments           | deliver               |
| scatter, cnv-scatter                                           | False       | cnvkit, visualization, scatter      | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram      | deliver               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes              | deliver               |
| cgh-file, cnv-somatic-cgh-file                                 | False       | cnvkit, vcf2cytosure                | deliver, scout        |
| clinical-rd-delly, rd-delly                                    | False       | delly, metrics                      | deliver               |
