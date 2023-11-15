| Balsamic tags                                                  | Mandatory   | HK tags                                 | Used by               |
|----------------------------------------------------------------|-------------|-----------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                         | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                         | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                            | audit                 |
| html, multiqc-html                                             | True        | multiqc-html                            | audit, deliver, scout |
| multiqc-json, json                                             | True        | multiqc-json                            | audit                 |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                              | audit, cg, vogue      |
| cram, tumor-cram                                               | True        | tumor, cram                             | deliver, scout        |
| tumor-cram-index, cram                                         | True        | tumor, cram-index                       | deliver, scout        |
| normal-cram, cram                                              | False       | normal, cram                            | deliver, scout        |
| normal-cram-index, cram                                        | False       | normal, cram-index                      | deliver, scout        |
| germline-vcf-tumor, dnascope, snv, vcf-tumor                   | True        | germline, vcf-snv-germline-tumor        | deliver               |
| dnascope, germline-vcf-tumor-index, snv, vcf-tumor             | True        | germline, vcf-snv-germline-tumor-index  | deliver               |
| dnascope, snv, germline-vcf-normal, vcf-normal                 | False       | germline, vcf-snv-germline-normal       | deliver               |
| dnascope, germline-vcf-normal-index, snv, vcf-normal           | False       | germline, vcf-snv-germline-normal-index | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                            | False       | dnascope, normal, vcf                   | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                      | False       | dnascope, normal, vcf-index             | cg, genotype          |
| germline-vcf-tumor, manta-germline, sv, vcf-tumor              | True        | germline, vcf-sv-germline-tumor         | deliver               |
| germline-vcf-tumor-index, manta-germline, sv, vcf-tumor        | True        | germline, vcf-sv-germline-tumor-index   | deliver               |
| sv, manta-germline, germline-vcf-normal, vcf-normal            | False       | germline, vcf-sv-germline-normal        | deliver               |
| sv, germline-vcf-normal-index, manta-germline, vcf-normal      | False       | germline, vcf-sv-germline-normal-index  | deliver               |
| research-vcf-svdb, vcf-svdb                                    | True        | svdb, vcf-sv                            | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-index                      | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb                          | True        | svdb, vcf-sv-research                   | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-research-index             | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                   | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index             | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv                        | deliver               |
| research-vcf-tnscope-index, vcf-tnscope                        | False       | tnscope, vcf-snv-index                  | deliver               |
| snv, research-vcf-pass-tnscope, vcf-pass-tnscope               | False       | tnscope, vcf-snv-research               | deliver               |
| vcf-pass-tnscope, snv, research-vcf-pass-tnscope-index         | False       | tnscope, vcf-snv-research-index         | deliver               |
| snv, clinical-vcf-pass-tnscope, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical               | deliver, scout        |
| clinical-vcf-pass-tnscope-index, snv, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index         | deliver, scout        |
| clinical-cnv-report-pdf, cnv-report-pdf                        | False       | cnv-report, visualization               | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                    | False       | ascatngs, metrics                       | deliver               |
| clinical-rd-delly, rd-delly                                    | True        | delly, coverage                         | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure             | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                             | False       | tiddit, normal, vcf2cytosure            | deliver, scout        |
| gens-bed, cnv-gens-bed, cov                                    | False       | gens, coverage, bed                     | scout                 |
| gens-bed, cnv-gens-bed-index, cov                              | False       | gens, coverage, bed-index               | scout                 |
| baf, gens-bed, cnv-gens-bed                                    | False       | gens, fracsnp, bed                      | scout                 |
| baf, gens-bed, cnv-gens-bed-index                              | False       | gens, fracsnp, bed-index                | scout                 |
| vcf-vardict, research-vcf-vardict                              | False       | vardict, vcf-snv                        | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-index                  | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict               | False       | vardict, vcf-snv-research               | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict-index         | False       | vardict, vcf-snv-research-index         | deliver               |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical               | deliver, scout        |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index         | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments               | deliver               |
| cnv-cnr, cnr                                                   | False       | cnvkit, regions                         | storage               |
| cnv-scatter, scatter                                           | False       | cnvkit, visualization, scatter          | deliver               |
| diagram, cnv-diagram                                           | False       | cnvkit, visualization, diagram          | deliver               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes                  | deliver               |
| cov-tumor-tiddit, clinical-cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                 | deliver               |
| cov-normal-tiddit, clinical-cov-normal-tiddit                  | False       | tiddit, normal, coverage                | deliver               |
| tmb, vardict, research-tmb, snv                                | False       | research, vardict, tmb                  | storage               |
| tmb, tnscope, research-tmb, snv                                | False       | research, tnscope, tmb                  | storage               |
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                         | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                   | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                        | deliver, scout        |
| umi-normal-cram-index, cram                                    | False       | umi-cram-index, normal                  | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv                | deliver               |
| vcf-tnscope-umi, research-vcf-tnscope-umi-index                | True        | tnscope-umi, vcf-umi-snv-index          | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | True        | tnscope-umi, vcf-umi-snv-research       | deliver               |
| research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi, snv | True        | tnscope-umi, vcf-umi-snv-research-index | deliver               |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical       | deliver, scout        |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi-index | True        | tnscope-umi, vcf-umi-snv-clinical-index | deliver, scout        |
| tmb, research-tmb, snv, tnscope-umi                            | True        | research, tnscope-umi, tmb              | storage               |
