| Balsamic tags                                                  | Mandatory   | HK tags                             | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                     | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                     | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                        | audit                 |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                          | audit, cg, vogue      |
| html, multiqc-html                                             | True        | multiqc-html                        | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                        | audit                 |
| cram, tumor-cram                                               | True        | tumor, cram                         | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                   | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                        | deliver, scout        |
| normal-cram-index, cram                                        | False       | normal, cram-index                  | deliver, scout        |
| cram, umi-tumor-cram                                           | False       | umi-cram, tumor                     | deliver, scout        |
| cram, umi-tumor-cram-index                                     | False       | umi-cram-index, tumor               | deliver, scout        |
| umi-normal-cram, cram                                          | False       | umi-cram, normal                    | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal              | deliver, scout        |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research               | deliver               |
| vcf-svdb, research-vcf-svdb-index                              | True        | svdb, vcf-sv-research-index         | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical               | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index         | deliver, scout        |
| snv, vcf-all, dnascope, annotated-germline-vcf-all             | True        | dnascope, germline, vcf             | deliver               |
| snv, vcf-all, dnascope, annotated-germline-vcf-all-index       | True        | dnascope, germline, vcf-index       | deliver               |
| sv, vcf-all, manta-germline, annotated-germline-vcf-all        | True        | manta, germline, vcf                | deliver               |
| sv, vcf-all, manta-germline, annotated-germline-vcf-all-index  | True        | manta, germline, vcf-index          | deliver               |
| research-vcf-tnscope, vcf-tnscope                              | False       | tnscope, vcf-snv-research           | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-tnscope, snv, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-tnscope-index, snv, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index     | deliver, scout        |
| ascat-pdf, clinical-ascat-pdf                                  | False       | ascatngs, visualization             | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                   | deliver               |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv-research-index     | deliver               |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical           | deliver, scout        |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index     | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | False       | tnscope-umi, vcf-umi-research       | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | False       | tnscope-umi, vcf-umi-research-index | deliver               |
| snv, vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi       | False       | tnscope-umi, vcf-umi-clinical       | deliver, scout        |
| snv, vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi-index | False       | tnscope-umi, vcf-umi-clinical-index | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments           | deliver               |
| scatter, cnv-scatter                                           | False       | cnvkit, visualization, scatter      | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram      | deliver               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes              | deliver               |
| cgh-file, cnv-somatic-cgh-file                                 | False       | cnvkit, vcf2cytosure                | deliver, scout        |
| clinical-rd-delly, rd-delly                                    | False       | delly, metrics                      | deliver               |
