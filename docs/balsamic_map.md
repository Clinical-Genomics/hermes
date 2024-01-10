| Balsamic tags                                                  | Mandatory   | HK tags                                   | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                           | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                           | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                              | audit                 |
| html, multiqc-html                                             | True        | multiqc-html                              | audit, deliver, scout |
| multiqc-json, json                                             | True        | multiqc-json                              | audit                 |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                                | audit, cg, vogue      |
| tumor-cram, cram                                               | True        | tumor, cram                               | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                         | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                              | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                        | deliver, scout        |
| vcf-tumor, germline-vcf-tumor, dnascope, snv                   | True        | germline, vcf-snv-germline-tumor          | deliver               |
| vcf-tumor, germline-vcf-tumor-index, dnascope, snv             | True        | germline, vcf-snv-germline-tumor-index    | deliver               |
| vcf-normal, germline-vcf-normal, dnascope, snv                 | False       | germline, vcf-snv-germline-normal         | deliver               |
| vcf-normal, snv, dnascope, germline-vcf-normal-index           | False       | germline, vcf-snv-germline-normal-index   | deliver               |
| genotype-vcf-dnascope, vcf-dnascope                            | False       | dnascope, normal, vcf                     | cg, genotype          |
| genotype-vcf-dnascope-index, vcf-dnascope                      | False       | dnascope, normal, vcf-index               | cg, genotype          |
| vcf-tumor, manta-germline, sv, germline-vcf-tumor              | True        | germline, vcf-sv-germline-tumor           | deliver               |
| vcf-tumor, manta-germline, germline-vcf-tumor-index, sv        | True        | germline, vcf-sv-germline-tumor-index     | deliver               |
| vcf-normal, manta-germline, sv, germline-vcf-normal            | False       | germline, vcf-sv-germline-normal          | deliver               |
| vcf-normal, manta-germline, sv, germline-vcf-normal-index      | False       | germline, vcf-sv-germline-normal-index    | deliver               |
| research-vcf-svdb, vcf-svdb                                    | True        | svdb, vcf-sv                              | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-index                        | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb                          | True        | svdb, vcf-sv-research                     | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-research-index               | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                     | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index               | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv                          | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-index                    | deliver               |
| vcf-pass-tnscope, research-vcf-pass-tnscope, snv               | False       | tnscope, vcf-snv-research                 | deliver               |
| vcf-pass-tnscope, research-vcf-pass-tnscope-index, snv         | False       | tnscope, vcf-snv-research-index           | deliver               |
| vcf-pass-tnscope, snv, clinical-vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical                 | deliver, scout        |
| vcf-pass-tnscope, clinical-vcf-pass-tnscope-index, snv         | False       | tnscope, vcf-snv-clinical-index           | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                         | deliver               |
| rd-delly, clinical-rd-delly                                    | True        | delly, coverage                           | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure               | deliver, scout        |
| cgh-normal, cnv-somatic-cgh-normal                             | False       | tiddit, normal, vcf2cytosure              | deliver, scout        |
| gens-bed, cov, cnv-gens-bed                                    | False       | gens, coverage, bed                       | scout                 |
| gens-bed, cov, cnv-gens-bed-index                              | False       | gens, coverage, bed-index                 | scout                 |
| gens-bed, cnv-gens-bed, baf                                    | False       | gens, fracsnp, bed                        | scout                 |
| gens-bed, cnv-gens-bed-index, baf                              | False       | gens, fracsnp, bed-index                  | scout                 |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv                          | deliver               |
| vcf-vardict, research-vcf-vardict-index                        | False       | vardict, vcf-snv-index                    | deliver               |
| vcf-pass-vardict, research-vcf-pass-vardict, snv               | False       | vardict, vcf-snv-research                 | deliver               |
| vcf-pass-vardict, research-vcf-pass-vardict-index, snv         | False       | vardict, vcf-snv-research-index           | deliver               |
| vcf-pass-vardict, clinical-vcf-pass-vardict, snv               | False       | vardict, vcf-snv-clinical                 | deliver, scout        |
| vcf-pass-vardict, clinical-vcf-pass-vardict-index, snv         | False       | vardict, vcf-snv-clinical-index           | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments                 | deliver               |
| cnv-cnr, cnr                                                   | False       | cnvkit, regions                           | storage               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes                    | deliver               |
| clinical-cnv-report-pdf, cnv-report-pdf                        | True        | cnv-report                                | deliver, scout        |
| circular-cnvpytor, clinical-circular-cnvpytor                  | False       | circular-plot, cnvpytor, visualization    | storage               |
| scatter-cnvpytor, clinical-scatter-cnvpytor                    | False       | scatter-plot, cnvpytor, visualization     | storage               |
| clinical-plot-ascat-profile, plot-ascat-profile                | False       | profile-plot, ascatngs, visualization     | storage               |
| clinical-plot-raw-profile, plot-raw-profile                    | False       | raw-profile-plot, ascatngs, visualization | storage               |
| clinical-plot-aspcf, plot-aspcf                                | False       | aspcf-plot, ascatngs, visualization       | storage               |
| plot-tumor, clinical-plot-tumor                                | False       | tumor-plot, ascatngs, visualization       | storage               |
| plot-germline, clinical-plot-germline                          | False       | germline-plot, ascatngs, visualization    | storage               |
| clinical-plot-sunrise, plot-sunrise                            | False       | sunrise-plot, ascatngs, visualization     | storage               |
| cov-tumor-tiddit, clinical-cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                   | deliver               |
| cov-normal-tiddit, clinical-cov-normal-tiddit                  | False       | tiddit, normal, coverage                  | deliver               |
| tmb, vardict, research-tmb, snv                                | False       | research, vardict, tmb                    | storage               |
| tmb, tnscope, research-tmb, snv                                | False       | research, tnscope, tmb                    | storage               |
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                           | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                     | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                          | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal                    | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv                  | deliver               |
| vcf-tnscope-umi, research-vcf-tnscope-umi-index                | True        | tnscope-umi, vcf-umi-snv-index            | deliver               |
| research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi, snv       | True        | tnscope-umi, vcf-umi-snv-research         | deliver               |
| vcf-pass-tnscope-umi, research-vcf-pass-tnscope-umi-index, snv | True        | tnscope-umi, vcf-umi-snv-research-index   | deliver               |
| vcf-pass-tnscope-umi, clinical-vcf-pass-tnscope-umi, snv       | True        | tnscope-umi, vcf-umi-snv-clinical         | deliver, scout        |
| vcf-pass-tnscope-umi, clinical-vcf-pass-tnscope-umi-index, snv | True        | tnscope-umi, vcf-umi-snv-clinical-index   | deliver, scout        |
| tnscope-umi, tmb, research-tmb, snv                            | True        | research, tnscope-umi, tmb                | storage               |
