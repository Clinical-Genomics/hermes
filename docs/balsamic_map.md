| Balsamic tags                                                    | Mandatory   | HK tags                                 | Used by               |
|------------------------------------------------------------------|-------------|-----------------------------------------|-----------------------|
| balsamic-config                                                  | True        | balsamic-config                         | audit, cg             |
| balsamic-report                                                  | True        | balsamic-report                         | audit                 |
| balsamic-dag                                                     | True        | balsamic-dag                            | audit                 |
| multiqc-html, html                                               | True        | multiqc-html                            | audit, deliver, scout |
| multiqc-json, json                                               | True        | multiqc-json                            | audit                 |
| qc-metrics-yaml, yaml                                            | True        | qc-metrics                              | audit, cg, vogue      |
| cram, tumor-cram                                                 | True        | tumor, cram                             | deliver, scout        |
| cram, tumor-cram-index                                           | True        | tumor, cram-index                       | deliver, scout        |
| normal-cram, cram                                                | False       | normal, cram                            | deliver, scout        |
| normal-cram-index, cram                                          | False       | normal, cram-index                      | deliver, scout        |
| dnascope, snv, germline-vcf-tumor, vcf-tumor                     | True        | germline, vcf-snv-germline-tumor        | deliver               |
| dnascope, germline-vcf-tumor-index, snv, vcf-tumor               | True        | germline, vcf-snv-germline-tumor-index  | deliver               |
| dnascope, vcf-normal, snv, germline-vcf-normal                   | False       | germline, vcf-snv-germline-normal       | deliver               |
| dnascope, vcf-normal, snv, germline-vcf-normal-index             | False       | germline, vcf-snv-germline-normal-index | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                              | False       | dnascope, normal, vcf                   | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                        | False       | dnascope, normal, vcf-index             | cg, genotype          |
| manta-germline, germline-vcf-tumor, vcf-tumor, sv                | True        | germline, vcf-sv-germline-tumor         | deliver               |
| germline-vcf-tumor-index, manta-germline, vcf-tumor, sv          | True        | germline, vcf-sv-germline-tumor-index   | deliver               |
| germline-vcf-normal, vcf-normal, manta-germline, sv              | False       | germline, vcf-sv-germline-normal        | deliver               |
| vcf-normal, germline-vcf-normal-index, manta-germline, sv        | False       | germline, vcf-sv-germline-normal-index  | deliver               |
| research-vcf-svdb, vcf-svdb                                      | True        | svdb, vcf-sv                            | deliver               |
| vcf-svdb, research-vcf-svdb-index                                | True        | svdb, vcf-sv-index                      | deliver               |
| research-vcf-pass-svdb, vcf-pass-svdb                            | True        | svdb, vcf-sv-research                   | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb-index                      | True        | svdb, vcf-sv-research-index             | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                            | True        | svdb, vcf-sv-clinical                   | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                      | True        | svdb, vcf-sv-clinical-index             | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                                | False       | tnscope, vcf-snv                        | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                          | False       | tnscope, vcf-snv-index                  | deliver               |
| snv, vcf-pass-tnscope, research-vcf-pass-tnscope                 | False       | tnscope, vcf-snv-research               | deliver               |
| vcf-pass-tnscope, snv, research-vcf-pass-tnscope-index           | False       | tnscope, vcf-snv-research-index         | deliver               |
| snv, clinical-vcf-pass-tnscope, vcf-pass-tnscope                 | False       | tnscope, vcf-snv-clinical               | deliver, scout        |
| snv, clinical-vcf-pass-tnscope-index, vcf-pass-tnscope           | False       | tnscope, vcf-snv-clinical-index         | deliver, scout        |
| cnv-report-pdf, clinical-cnv-report-pdf                          | False       | cnv-report, visualization               | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                      | False       | ascatngs, metrics                       | deliver               |
| rd-delly, clinical-rd-delly                                      | True        | delly, coverage                         | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                                 | False       | cnvkit, tumor, vcf2cytosure             | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                               | False       | tiddit, normal, vcf2cytosure            | deliver, scout        |
| vcf-vardict, research-vcf-vardict                                | False       | vardict, vcf-snv                        | deliver               |
| vcf-vardict, research-vcf-vardict-index                          | False       | vardict, vcf-snv-index                  | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict                 | False       | vardict, vcf-snv-research               | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict-index           | False       | vardict, vcf-snv-research-index         | deliver               |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict                 | False       | vardict, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-vardict, clinical-vcf-pass-vardict-index, snv           | False       | vardict, vcf-snv-clinical-index         | deliver, scout        |
| cnv-cns, cns                                                     | False       | cnvkit, metrics, segments               | deliver               |
| cnv-cnr, cnr                                                     | False       | cnvkit, metrics, regions                | storage               |
| scatter, cnv-scatter                                             | False       | cnvkit, visualization, scatter          | deliver               |
| diagram, cnv-diagram                                             | False       | cnvkit, visualization, diagram          | deliver               |
| gene-metrics, cnv-gene-metrics                                   | False       | cnvkit, metrics, genes                  | deliver               |
| cov-tumor-tiddit, clinical-cov-tumor-tiddit                      | False       | tiddit, tumor, coverage                 | deliver               |
| clinical-cov-normal-tiddit, cov-normal-tiddit                    | False       | tiddit, normal, coverage                | deliver               |
| research-bcftools-counts, bcftools-counts                        | True        | research, sv, tmb                       | storage               |
| bcftools-counts-research, research-bcftools-counts-research, snv | True        | research, snv, tmb                      | storage               |
| cram, umi-tumor-cram                                             | True        | umi-cram, tumor                         | deliver, scout        |
| umi-tumor-cram-index, cram                                       | True        | umi-cram-index, tumor                   | deliver, scout        |
| umi-normal-cram, cram                                            | False       | umi-cram, normal                        | deliver, scout        |
| umi-normal-cram-index, cram                                      | False       | umi-cram-index, normal                  | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                        | True        | tnscope-umi, vcf-umi-snv                | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                  | True        | tnscope-umi, vcf-umi-snv-index          | deliver               |
| vcf-pass-tnscope-umi, snv, research-vcf-pass-tnscope-umi         | True        | tnscope-umi, vcf-umi-snv-research       | deliver               |
| vcf-pass-tnscope-umi, snv, research-vcf-pass-tnscope-umi-index   | True        | tnscope-umi, vcf-umi-snv-research-index | deliver               |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi         | True        | tnscope-umi, vcf-umi-snv-clinical       | deliver, scout        |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi-index   | True        | tnscope-umi, vcf-umi-snv-clinical-index | deliver, scout        |
