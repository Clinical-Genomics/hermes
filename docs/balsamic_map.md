| Balsamic tags                                                  | Mandatory   | HK tags                                 | Used by               |
|----------------------------------------------------------------|-------------|-----------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                         | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                         | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                            | audit                 |
| multiqc-html, html                                             | True        | multiqc-html                            | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                            | audit                 |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                              | audit, cg, vogue      |
| cram, tumor-cram                                               | True        | tumor, cram                             | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                       | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                            | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                      | deliver, scout        |
| vcf-tumor, snv, germline-vcf-tumor, dnascope                   | True        | germline, vcf-snv-germline-tumor        | deliver               |
| vcf-tumor, germline-vcf-tumor-index, snv, dnascope             | True        | germline, vcf-snv-germline-tumor-index  | deliver               |
| germline-vcf-normal, snv, dnascope, vcf-normal                 | False       | germline, vcf-snv-germline-normal       | deliver               |
| germline-vcf-normal-index, snv, dnascope, vcf-normal           | False       | germline, vcf-snv-germline-normal-index | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                            | False       | dnascope, normal, vcf                   | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                      | False       | dnascope, normal, vcf-index             | cg, genotype          |
| vcf-tumor, germline-vcf-tumor, manta-germline, sv              | True        | germline, vcf-sv-germline-tumor         | deliver               |
| vcf-tumor, germline-vcf-tumor-index, manta-germline, sv        | True        | germline, vcf-sv-germline-tumor-index   | deliver               |
| sv, germline-vcf-normal, manta-germline, vcf-normal            | False       | germline, vcf-sv-germline-normal        | deliver               |
| vcf-normal, germline-vcf-normal-index, manta-germline, sv      | False       | germline, vcf-sv-germline-normal-index  | deliver               |
| research-vcf-svdb, vcf-svdb                                    | True        | svdb, vcf-sv                            | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-index                      | deliver               |
| research-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-research                   | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-research-index             | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                   | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-clinical-index             | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv                        | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-index                  | deliver               |
| vcf-pass-tnscope, snv, research-vcf-pass-tnscope               | False       | tnscope, vcf-snv-research               | deliver               |
| vcf-pass-tnscope, snv, research-vcf-pass-tnscope-index         | False       | tnscope, vcf-snv-research-index         | deliver               |
| vcf-pass-tnscope, snv, clinical-vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-tnscope, clinical-vcf-pass-tnscope-index, snv         | False       | tnscope, vcf-snv-clinical-index         | deliver, scout        |
| cnv-report-pdf, clinical-cnv-report-pdf                        | False       | cnv-report, visualization               | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                       | deliver               |
| clinical-rd-delly, rd-delly                                    | True        | delly, coverage                         | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure             | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                             | False       | tiddit, normal, vcf2cytosure            | deliver, scout        |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv                        | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-index                  | deliver               |
| research-vcf-pass-vardict, vcf-pass-vardict, snv               | False       | vardict, vcf-snv-research               | deliver               |
| vcf-pass-vardict, research-vcf-pass-vardict-index, snv         | False       | vardict, vcf-snv-research-index         | deliver               |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index         | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments               | deliver               |
| cnv-cnr, cnr                                                   | False       | cnvkit, metrics, regions                | storage               |
| cnv-scatter, scatter                                           | False       | cnvkit, visualization, scatter          | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram          | deliver               |
| gene-metrics, cnv-gene-metrics                                 | False       | cnvkit, metrics, genes                  | deliver               |
| clinical-cov-tumor-tiddit, cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                 | deliver               |
| clinical-cov-normal-tiddit, cov-normal-tiddit                  | False       | tiddit, normal, coverage                | deliver               |
| tmb, research-tmb, snv, vardict                                | False       | research, vardict, tmb                  | storage               |
| tnscope, research-tmb, snv, tmb                                | False       | research, tnscope, tmb                  | storage               |
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                         | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                   | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                        | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal                  | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv                | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True        | tnscope-umi, vcf-umi-snv-index          | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | True        | tnscope-umi, vcf-umi-snv-research       | deliver               |
| research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi, snv | True        | tnscope-umi, vcf-umi-snv-research-index | deliver               |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical       | deliver, scout        |
| clinical-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi, snv | True        | tnscope-umi, vcf-umi-snv-clinical-index | deliver, scout        |
| tmb, research-tmb, snv, tnscope-umi                            | True        | research, tnscope-umi, tmb              | storage               |
