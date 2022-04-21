| Balsamic tags                                                         | Mandatory   | HK tags                               | Used by               |
|-----------------------------------------------------------------------|-------------|---------------------------------------|-----------------------|
| balsamic-config                                                       | True        | balsamic-config                       | audit, cg             |
| balsamic-report                                                       | True        | balsamic-report                       | audit                 |
| balsamic-dag                                                          | True        | balsamic-dag                          | audit                 |
| yaml, qc-metrics-yaml                                                 | True        | qc-metrics                            | audit, cg, vogue      |
| multiqc-html, html                                                    | True        | multiqc-html                          | audit, deliver, scout |
| multiqc-json, json                                                    | True        | multiqc-json                          | audit                 |
| cram, tumor-cram                                                      | True        | tumor, cram                           | deliver, scout        |
| cram, tumor-cram-index                                                | True        | tumor, cram-index                     | deliver, scout        |
| cram, normal-cram                                                     | False       | normal, cram                          | deliver, scout        |
| cram, normal-cram-index                                               | False       | normal, cram-index                    | deliver, scout        |
| cram, umi-tumor-cram                                                  | False       | umi-cram, tumor                       | deliver               |
| cram, umi-tumor-cram-index                                            | False       | umi-cram-index, tumor                 | deliver               |
| cram, umi-normal-cram                                                 | False       | umi-cram, normal                      | deliver               |
| cram, umi-normal-cram-index                                           | False       | umi-cram-index, normal                | deliver               |
| vcf-svdb, research-vcf-svdb                                           | True        | svdb, vcf-sv-research                 | deliver               |
| vcf-svdb, research-vcf-svdb-index                                     | True        | svdb, vcf-sv-research-index           | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                                 | True        | svdb, vcf-sv-clinical                 | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                           | True        | svdb, vcf-sv-clinical-index           | deliver, scout        |
| snv, vcf-all, dnascope, tumor, annotated-germline-vcf-all             | True        | dnascope, germline, tumor, vcf        | deliver               |
| annotated-germline-vcf-all-index, snv, vcf-all, dnascope, tumor       | True        | dnascope, germline, tumor, vcf-index  | deliver               |
| snv, vcf-all, normal, dnascope, annotated-germline-vcf-all            | False       | dnascope, germline, normal, vcf       | deliver               |
| annotated-germline-vcf-all-index, snv, vcf-all, normal, dnascope      | False       | dnascope, germline, normal, vcf-index | deliver               |
| manta-germline, vcf-all, sv, tumor, annotated-germline-vcf-all        | True        | manta, germline, tumor, vcf           | deliver               |
| annotated-germline-vcf-all-index, manta-germline, vcf-all, sv, tumor  | True        | manta, germline, tumor, vcf-index     | deliver               |
| manta-germline, vcf-all, normal, sv, annotated-germline-vcf-all       | False       | manta, germline, normal, vcf          | deliver               |
| annotated-germline-vcf-all-index, manta-germline, vcf-all, normal, sv | False       | manta, germline, normal, vcf-index    | deliver               |
| vcf-tnscope, research-vcf-tnscope                                     | False       | tnscope, vcf-snv-research             | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                               | False       | tnscope, vcf-snv-research-index       | deliver               |
| snv, vcf-pass-tnscope, clinical-vcf-pass-tnscope                      | False       | tnscope, vcf-snv-clinical             | deliver, scout        |
| snv, vcf-pass-tnscope, clinical-vcf-pass-tnscope-index                | False       | tnscope, vcf-snv-clinical-index       | deliver, scout        |
| tmb, snv, stat-somatic-tmb, tnscope                                   | False       | tnscope, tmb                          | deliver               |
| clinical-ascat-pdf, ascat-pdf                                         | False       | ascatngs, visualization               | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                           | False       | ascatngs, metrics                     | deliver               |
| research-vcf-vardict, vcf-vardict                                     | False       | vardict, vcf-snv-research-index       | deliver               |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict                      | False       | vardict, vcf-snv-clinical             | deliver, scout        |
| snv, vcf-pass-vardict, clinical-vcf-pass-vardict-index                | False       | vardict, vcf-snv-clinical-index       | deliver, scout        |
| tmb, snv, vardict, stat-somatic-tmb                                   | False       | vardict, tmb                          | deliver               |
| research-vcf-tnscope-umi, vcf-tnscope-umi                             | False       | tnscope-umi, vcf                      | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                       | False       | tnscope-umi, vcf-index                | deliver               |
| snv, vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi              | False       | tnscope-umi, vcf-snv-research         | deliver               |
| snv, vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi-index        | False       | tnscope-umi, vcf-snv-research-index   | deliver               |
| tmb, snv, stat-somatic-tmb, tnscope-umi                               | False       | tnscope-umi, tmb                      | deliver               |
| cns, cnv-cns                                                          | False       | cnvkit, segments                      | deliver               |
| cnv-scatter, scatter                                                  | False       | cnvkit, visualization, scatter        | deliver               |
| diagram, cnv-diagram                                                  | False       | cnvkit, visualization, diagram        | deliver               |
| cnv-gene-metrics, gene-metrics                                        | False       | cnvkit, genes, metrics                | deliver               |
| cgh-file, cnv-somatic-cgh-file                                        | False       | cnvkit, vcf2cytosure                  | deliver, scout        |