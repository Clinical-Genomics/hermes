| Balsamic tags                                                  | Mandatory | HK tags                                   | Used by               |
|----------------------------------------------------------------|-----------|-------------------------------------------|-----------------------|
| balsamic-config                                                | True      | balsamic-config                           | audit, cg             |
| balsamic-report                                                | True      | balsamic-report                           | audit                 |
| balsamic-dag                                                   | True      | balsamic-dag                              | audit                 |
| html, multiqc-html                                             | True      | multiqc-html                              | audit, deliver, scout |
| json, multiqc-json                                             | True      | multiqc-json                              | audit                 |
| yaml, qc-metrics-yaml                                          | True      | qc-metrics                                | audit, cg             |
| tumor-cram, cram                                               | True      | tumor, cram                               | deliver, scout        |
| cram, tumor-cram-index                                         | True      | tumor, cram-index                         | deliver, scout        |
| cram, normal-cram                                              | False     | normal, cram                              | deliver, scout        |
| cram, normal-cram-index                                        | False     | normal, cram-index                        | deliver, scout        |
| dnascope, germline-vcf-tumor, vcf-tumor, snv                   | True      | germline, vcf-snv-germline-tumor          | deliver               |
| dnascope, germline-vcf-tumor-index, vcf-tumor, snv             | True      | germline, vcf-snv-germline-tumor-index    | deliver               |
| dnascope, germline-vcf-normal, vcf-normal, snv                 | False     | germline, vcf-snv-germline-normal         | deliver               |
| dnascope, germline-vcf-normal-index, vcf-normal, snv           | False     | germline, vcf-snv-germline-normal-index   | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                            | False     | dnascope, normal, vcf                     | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                      | False     | dnascope, normal, vcf-index               | cg, genotype          |
| sv, germline-vcf-tumor, manta-germline, vcf-tumor              | True      | germline, vcf-sv-germline-tumor           | deliver               |
| manta-germline, sv, germline-vcf-tumor-index, vcf-tumor        | True      | germline, vcf-sv-germline-tumor-index     | deliver               |
| vcf-normal, germline-vcf-normal, sv, manta-germline            | False     | germline, vcf-sv-germline-normal          | deliver               |
| germline-vcf-normal-index, manta-germline, sv, vcf-normal      | False     | germline, vcf-sv-germline-normal-index    | deliver               |
| vcf-svdb, research-vcf-svdb                                    | True      | svdb, vcf-sv                              | deliver               |
| vcf-svdb, research-vcf-svdb-index                              | True      | svdb, vcf-sv-index                        | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb                          | True      | svdb, vcf-sv-research                     | deliver               |
| research-vcf-pass-svdb-index, vcf-pass-svdb                    | True      | svdb, vcf-sv-research-index               | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                          | True      | svdb, vcf-sv-clinical                     | deliver, scout        |
| vcf-pass-svdb, clinical-vcf-pass-svdb-index                    | True      | svdb, vcf-sv-clinical-index               | deliver, scout        |
| research-vcf-tnscope, vcf-tnscope                              | False     | tnscope, vcf-snv                          | deliver               |
| research-vcf-tnscope-index, vcf-tnscope                        | False     | tnscope, vcf-snv-index                    | deliver               |
| vcf-pass-tnscope, research-vcf-pass-tnscope, snv               | False     | tnscope, vcf-snv-research                 | deliver               |
| research-vcf-pass-tnscope-index, vcf-pass-tnscope, snv         | False     | tnscope, vcf-snv-research-index           | deliver               |
| clinical-vcf-pass-tnscope, vcf-pass-tnscope, snv               | False     | tnscope, vcf-snv-clinical                 | deliver, scout        |
| clinical-vcf-pass-tnscope-index, vcf-pass-tnscope, snv         | False     | tnscope, vcf-snv-clinical-index           | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                    | False     | ascatngs, metrics                         | deliver               |
| rd-delly, clinical-rd-delly                                    | True      | delly, coverage                           | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                               | False     | cnvkit, tumor, vcf2cytosure               | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                             | False     | tiddit, normal, vcf2cytosure              | deliver, scout        |
| cov, cnv-gens-bed, gens-bed                                    | False     | gens, coverage, bed                       | scout                 |
| cnv-gens-bed-index, cov, gens-bed                              | False     | gens, coverage, bed-index                 | scout                 |
| baf, cnv-gens-bed, gens-bed                                    | False     | gens, fracsnp, bed                        | scout                 |
| cnv-gens-bed-index, baf, gens-bed                              | False     | gens, fracsnp, bed-index                  | scout                 |
| research-vcf-vardict, vcf-vardict                              | False     | vardict, vcf-snv                          | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False     | vardict, vcf-snv-index                    | deliver               |
| vcf-pass-vardict, research-vcf-pass-vardict, snv               | False     | vardict, vcf-snv-research                 | deliver               |
| vcf-pass-vardict, research-vcf-pass-vardict-index, snv         | False     | vardict, vcf-snv-research-index           | deliver               |
| vcf-pass-vardict, clinical-vcf-pass-vardict, snv               | False     | vardict, vcf-snv-clinical                 | deliver, scout        |
| vcf-pass-vardict, clinical-vcf-pass-vardict-index, snv         | False     | vardict, vcf-snv-clinical-index           | deliver, scout        |
| cnv-cns, cns                                                   | False     | cnvkit, metrics, segments                 | deliver               |
| cnr, cnv-cnr                                                   | False     | cnvkit, regions                           | storage               |
| cnv-gene-metrics, gene-metrics                                 | False     | cnvkit, metrics, genes                    | deliver               |
| clinical-cnv-report-pdf, cnv-report-pdf                        | True      | cnv-report                                | deliver, scout        |
| circular-cnvpytor, clinical-circular-cnvpytor                  | False     | circular-plot, cnvpytor, visualization    | storage               |
| clinical-scatter-cnvpytor, scatter-cnvpytor                    | False     | scatter-plot, cnvpytor, visualization     | storage               |
| plot-ascat-profile, clinical-plot-ascat-profile                | False     | profile-plot, ascatngs, visualization     | storage               |
| clinical-plot-raw-profile, plot-raw-profile                    | False     | raw-profile-plot, ascatngs, visualization | storage               |
| plot-aspcf, clinical-plot-aspcf                                | False     | aspcf-plot, ascatngs, visualization       | storage               |
| plot-tumor, clinical-plot-tumor                                | False     | tumor-plot, ascatngs, visualization       | storage               |
| plot-germline, clinical-plot-germline                          | False     | germline-plot, ascatngs, visualization    | storage               |
| plot-sunrise, clinical-plot-sunrise                            | False     | sunrise-plot, ascatngs, visualization     | storage               |
| cov-tumor-tiddit, clinical-cov-tumor-tiddit                    | False     | tiddit, tumor, coverage                   | deliver               |
| clinical-cov-normal-tiddit, cov-normal-tiddit                  | False     | tiddit, normal, coverage                  | deliver               |
| vardict, research-tmb, tmb, snv                                | False     | research, vardict, tmb                    | storage               |
| tmb, tnscope, research-tmb, snv                                | False     | research, tnscope, tmb                    | storage               |
| umi-tumor-cram, cram                                           | True      | umi-cram, tumor                           | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True      | umi-cram-index, tumor                     | deliver, scout        |
| umi-normal-cram, cram                                          | False     | umi-cram, normal                          | deliver, scout        |
| cram, umi-normal-cram-index                                    | False     | umi-cram-index, normal                    | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                      | True      | tnscope-umi, vcf-umi-snv                  | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True      | tnscope-umi, vcf-umi-snv-index            | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | True      | tnscope-umi, vcf-umi-snv-research         | deliver               |
| research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi, snv | True      | tnscope-umi, vcf-umi-snv-research-index   | deliver               |
| vcf-pass-tnscope-umi, clinical-vcf-pass-tnscope-umi, snv       | True      | tnscope-umi, vcf-umi-snv-clinical         | deliver, scout        |
| vcf-pass-tnscope-umi, clinical-vcf-pass-tnscope-umi-index, snv | True      | tnscope-umi, vcf-umi-snv-clinical-index   | deliver, scout        |
| tmb, tnscope-umi, research-tmb, snv                            | True      | research, tnscope-umi, tmb                | storage               |
