| Balsamic tags                                                  | Mandatory   | HK tags                             | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                     | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                     | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                        | audit                 |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics                          | audit, cg, vogue      |
| html, multiqc-html                                             | True        | multiqc-html                        | audit, deliver, scout |
| multiqc-json, json                                             | True        | multiqc-json                        | audit                 |
| tumor-cram, cram                                               | True        | tumor, cram                         | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                   | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                        | deliver, scout        |
| normal-cram-index, cram                                        | False       | normal, cram-index                  | deliver, scout        |
| umi-tumor-cram, cram                                           | False       | umi-cram, tumor                     | deliver, scout        |
| cram, umi-tumor-cram-index                                     | False       | umi-cram-index, tumor               | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                    | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal              | deliver, scout        |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv-research               | deliver               |
| vcf-svdb, research-vcf-svdb-index                              | True        | svdb, vcf-sv-research-index         | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical               | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index         | deliver, scout        |
| annotated-germline-vcf-all, dnascope, snv, vcf-all             | True        | dnascope, germline, vcf             | deliver               |
| dnascope, snv, annotated-germline-vcf-all-index, vcf-all       | True        | dnascope, germline, vcf-index       | deliver               |
| annotated-germline-vcf-all, sv, manta-germline, vcf-all        | True        | manta, germline, vcf                | deliver               |
| sv, manta-germline, annotated-germline-vcf-all-index, vcf-all  | True        | manta, germline, vcf-index          | deliver               |
| research-vcf-tnscope, vcf-tnscope                              | False       | tnscope, vcf-snv-research           | deliver               |
| research-vcf-tnscope-index, vcf-tnscope                        | False       | tnscope, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-tnscope, snv, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-tnscope-index, snv, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index     | deliver, scout        |
| ascat-pdf, clinical-ascat-pdf                                  | False       | ascatngs, visualization             | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                    | False       | ascatngs, metrics                   | deliver               |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv-research-index     | deliver               |
| clinical-vcf-pass-vardict, vcf-pass-vardict, snv               | False       | vardict, vcf-snv-clinical           | deliver, scout        |
| clinical-vcf-pass-vardict-index, vcf-pass-vardict, snv         | False       | vardict, vcf-snv-clinical-index     | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | False       | tnscope-umi, vcf                    | deliver               |
| vcf-tnscope-umi, research-vcf-tnscope-umi-index                | False       | tnscope-umi, vcf-index              | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | False       | tnscope-umi, vcf-snv-research       | deliver, scout        |
| research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi, snv | False       | tnscope-umi, vcf-snv-research-index | deliver, scout        |
| cnv-cns, cns                                                   | False       | cnvkit, segments                    | deliver               |
| scatter, cnv-scatter                                           | False       | cnvkit, visualization, scatter      | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram      | deliver               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, genes, metrics              | deliver               |
| cgh-file, cnv-somatic-cgh-file                                 | False       | cnvkit, vcf2cytosure                | deliver, scout        |
| clinical-rd-delly, rd-delly                                    | False       | delly, metrics                      | deliver               |
