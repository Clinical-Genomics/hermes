| Balsamic tags                                                  | Mandatory   | HK tags                                   | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                           | audit, cg             |
| balsamic-dag                                                   | True        | balsamic-dag                              | audit                 |
| html, multiqc-html                                             | True        | multiqc-html                              | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                              | audit                 |
| alignmentsummarymetrics, multiqc, picard                       | True        | qc-metrics, multiqc, picard-alignment     | storage, janus        |
| multiqc, dups, picard                                          | True        | qc-metrics, multiqc, picard-duplicates    | storage, janus        |
| hsmetrics, multiqc, picard                                     | True        | qc-metrics, multiqc, picard-hs            | storage, janus        |
| insertsize, multiqc, picard                                    | True        | qc-metrics, multiqc, picard-insert-size   | storage, janus        |
| wgsmetrics, multiqc, picard                                    | False       | qc-metrics, multiqc, picard-wgs           | storage, janus        |
| multiqc, fastp                                                 | True        | qc-metrics, multiqc, fastp                | storage, janus        |
| samtools, stats, multiqc                                       | True        | qc-metrics, multiqc, samtools-stats       | storage, janus        |
| somalier, multiqc                                              | False       | qc-metrics, multiqc, somalier             | storage, janus        |
| qc-metrics-yaml, yaml                                          | True        | qc-metrics, deliverable                   | audit, cg             |
| cram, tumor-cram                                               | True        | tumor, cram                               | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                         | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                              | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                        | deliver, scout        |
| vcf-tumor, snv, dnascope, germline-vcf-tumor                   | True        | germline, vcf-snv-germline-tumor          | deliver               |
| vcf-tumor, snv, germline-vcf-tumor-index, dnascope             | True        | germline, vcf-snv-germline-tumor-index    | deliver               |
| snv, dnascope, vcf-normal, germline-vcf-normal                 | False       | germline, vcf-snv-germline-normal         | deliver               |
| snv, dnascope, vcf-normal, germline-vcf-normal-index           | False       | germline, vcf-snv-germline-normal-index   | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                            | False       | dnascope, normal, vcf                     | cg, genotype          |
| genotype-vcf-dnascope-index, vcf-dnascope                      | False       | dnascope, normal, vcf-index               | cg, genotype          |
| vcf-tumor, manta-germline, germline-vcf-tumor, sv              | True        | germline, vcf-sv-germline-tumor           | deliver               |
| vcf-tumor, germline-vcf-tumor-index, manta-germline, sv        | True        | germline, vcf-sv-germline-tumor-index     | deliver               |
| germline-vcf-normal, manta-germline, sv, vcf-normal            | False       | germline, vcf-sv-germline-normal          | deliver               |
| manta-germline, sv, germline-vcf-normal-index, vcf-normal      | False       | germline, vcf-sv-germline-normal-index    | deliver               |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv                              | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-index                        | deliver               |
| research-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-research                     | deliver               |
| research-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-research-index               | deliver               |
| clinical-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                     | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index               | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv                          | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-index                    | deliver               |
| snv, vcf-pass-tnscope, research-vcf-pass-tnscope               | False       | tnscope, vcf-snv-research                 | deliver               |
| snv, research-vcf-pass-tnscope-index, vcf-pass-tnscope         | False       | tnscope, vcf-snv-research-index           | deliver               |
| snv, clinical-vcf-pass-tnscope, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical                 | deliver, scout        |
| snv, clinical-vcf-pass-tnscope-index, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index           | deliver, scout        |
| clinical-ascat-copynumber, ascat-copynumber                    | False       | ascatngs, metrics                         | deliver               |
| rd-delly, clinical-rd-delly                                    | True        | delly, coverage                           | deliver               |
| cgh-tumor, cnv-somatic-cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure               | deliver, scout        |
| cnv-somatic-cgh-normal, cgh-normal                             | False       | tiddit, normal, vcf2cytosure              | deliver, scout        |
| cov, cnv-gens-bed, gens-bed                                    | False       | gens, coverage, bed                       | scout                 |
| cov, cnv-gens-bed-index, gens-bed                              | False       | gens, coverage, bed-index                 | scout                 |
| cnv-gens-bed, baf, gens-bed                                    | False       | gens, fracsnp, bed                        | scout                 |
| baf, cnv-gens-bed-index, gens-bed                              | False       | gens, fracsnp, bed-index                  | scout                 |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv                          | deliver               |
| research-vcf-vardict-index, vcf-vardict                        | False       | vardict, vcf-snv-index                    | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict               | False       | vardict, vcf-snv-research                 | deliver               |
| vcf-pass-vardict, snv, research-vcf-pass-vardict-index         | False       | vardict, vcf-snv-research-index           | deliver               |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict               | False       | vardict, vcf-snv-clinical                 | deliver, scout        |
| vcf-pass-vardict, snv, clinical-vcf-pass-vardict-index         | False       | vardict, vcf-snv-clinical-index           | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments                 | deliver               |
| cnv-cnr, cnr                                                   | False       | cnvkit, regions                           | storage               |
| gene-metrics, cnv-gene-metrics                                 | False       | cnvkit, metrics, genes                    | deliver               |
| clinical-cnv-report-pdf, cnv-report-pdf                        | True        | cnv-report                                | deliver, scout        |
| circular-cnvpytor, clinical-circular-cnvpytor                  | False       | circular-plot, cnvpytor, visualization    | storage               |
| scatter-cnvpytor, clinical-scatter-cnvpytor                    | False       | scatter-plot, cnvpytor, visualization     | storage               |
| clinical-plot-ascat-profile, plot-ascat-profile                | False       | profile-plot, ascatngs, visualization     | storage               |
| clinical-plot-raw-profile, plot-raw-profile                    | False       | raw-profile-plot, ascatngs, visualization | storage               |
| clinical-plot-aspcf, plot-aspcf                                | False       | aspcf-plot, ascatngs, visualization       | storage               |
| clinical-plot-tumor, plot-tumor                                | False       | tumor-plot, ascatngs, visualization       | storage               |
| plot-germline, clinical-plot-germline                          | False       | germline-plot, ascatngs, visualization    | storage               |
| clinical-plot-sunrise, plot-sunrise                            | False       | sunrise-plot, ascatngs, visualization     | storage               |
| clinical-cov-tumor-tiddit, cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                   | deliver               |
| clinical-cov-normal-tiddit, cov-normal-tiddit                  | False       | tiddit, normal, coverage                  | deliver               |
| snv, research-tmb, vardict, tmb                                | False       | research, vardict, tmb                    | storage               |
| snv, research-tmb, tmb, tnscope                                | False       | research, tnscope, tmb                    | storage               |
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                           | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                     | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                          | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal                    | deliver, scout        |
| vcf-tnscope-umi, research-vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv                  | deliver               |
| vcf-tnscope-umi, research-vcf-tnscope-umi-index                | True        | tnscope-umi, vcf-umi-snv-index            | deliver               |
| vcf-pass-tnscope-umi, snv, research-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-research         | deliver               |
| vcf-pass-tnscope-umi, snv, research-vcf-pass-tnscope-umi-index | True        | tnscope-umi, vcf-umi-snv-research-index   | deliver               |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical         | deliver, scout        |
| vcf-pass-tnscope-umi, snv, clinical-vcf-pass-tnscope-umi-index | True        | tnscope-umi, vcf-umi-snv-clinical-index   | deliver, scout        |
| tnscope-umi, snv, research-tmb, tmb                            | True        | research, tnscope-umi, tmb                | storage               |
