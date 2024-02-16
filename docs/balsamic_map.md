| Balsamic tags                                                  | Mandatory   | HK tags                                   | Used by               |
|----------------------------------------------------------------|-------------|-------------------------------------------|-----------------------|
| balsamic-config                                                | True        | balsamic-config                           | audit, cg             |
| balsamic-report                                                | True        | balsamic-report                           | audit                 |
| balsamic-dag                                                   | True        | balsamic-dag                              | audit                 |
| html, multiqc-html                                             | True        | multiqc-html                              | audit, deliver, scout |
| json, multiqc-json                                             | True        | multiqc-json                              | audit                 |
| alignmentsummarymetrics, picard, multiqc                       | True        | qc-metrics, multiqc, picard-alignment     | storage, janus        |
| picard, multiqc, dups                                          | True        | qc-metrics, multiqc, picard-duplicates    | storage, janus        |
| picard, multiqc, hsmetrics                                     | True        | qc-metrics, multiqc, picard-hs            | storage, janus        |
| picard, multiqc, insertsize                                    | True        | qc-metrics, multiqc, picard-insert-size   | storage, janus        |
| wgsmetrics, picard, multiqc                                    | False       | qc-metrics, multiqc, picard-wgs           | storage, janus        |
| multiqc, fastp                                                 | True        | qc-metrics, multiqc, fastp                | storage, janus        |
| samtools, stats, multiqc                                       | True        | qc-metrics, multiqc, samtools-stats       | storage, janus        |
| multiqc, somalier                                              | False       | qc-metrics, multiqc, somalier             | storage, janus        |
| yaml, qc-metrics-yaml                                          | True        | qc-metrics                                | audit, cg             |
| cram, tumor-cram                                               | True        | tumor, cram                               | deliver, scout        |
| cram, tumor-cram-index                                         | True        | tumor, cram-index                         | deliver, scout        |
| cram, normal-cram                                              | False       | normal, cram                              | deliver, scout        |
| cram, normal-cram-index                                        | False       | normal, cram-index                        | deliver, scout        |
| snv, germline-vcf-tumor, dnascope, vcf-tumor                   | True        | germline, vcf-snv-germline-tumor          | deliver               |
| snv, dnascope, germline-vcf-tumor-index, vcf-tumor             | True        | germline, vcf-snv-germline-tumor-index    | deliver               |
| snv, vcf-normal, dnascope, germline-vcf-normal                 | False       | germline, vcf-snv-germline-normal         | deliver               |
| snv, vcf-normal, dnascope, germline-vcf-normal-index           | False       | germline, vcf-snv-germline-normal-index   | deliver               |
| vcf-dnascope, genotype-vcf-dnascope                            | False       | dnascope, normal, vcf                     | cg, genotype          |
| vcf-dnascope, genotype-vcf-dnascope-index                      | False       | dnascope, normal, vcf-index               | cg, genotype          |
| sv, germline-vcf-tumor, vcf-tumor, manta-germline              | True        | germline, vcf-sv-germline-tumor           | deliver               |
| sv, germline-vcf-tumor-index, vcf-tumor, manta-germline        | True        | germline, vcf-sv-germline-tumor-index     | deliver               |
| sv, vcf-normal, manta-germline, germline-vcf-normal            | False       | germline, vcf-sv-germline-normal          | deliver               |
| sv, vcf-normal, germline-vcf-normal-index, manta-germline      | False       | germline, vcf-sv-germline-normal-index    | deliver               |
| vcf-svdb, research-vcf-svdb                                    | True        | svdb, vcf-sv                              | deliver               |
| research-vcf-svdb-index, vcf-svdb                              | True        | svdb, vcf-sv-index                        | deliver               |
| research-vcf-pass-svdb, vcf-pass-svdb                          | True        | svdb, vcf-sv-research                     | deliver               |
| vcf-pass-svdb, research-vcf-pass-svdb-index                    | True        | svdb, vcf-sv-research-index               | deliver               |
| vcf-pass-svdb, clinical-vcf-pass-svdb                          | True        | svdb, vcf-sv-clinical                     | deliver, scout        |
| clinical-vcf-pass-svdb-index, vcf-pass-svdb                    | True        | svdb, vcf-sv-clinical-index               | deliver, scout        |
| vcf-tnscope, research-vcf-tnscope                              | False       | tnscope, vcf-snv                          | deliver               |
| vcf-tnscope, research-vcf-tnscope-index                        | False       | tnscope, vcf-snv-index                    | deliver               |
| research-vcf-pass-tnscope, snv, vcf-pass-tnscope               | False       | tnscope, vcf-snv-research                 | deliver               |
| snv, research-vcf-pass-tnscope-index, vcf-pass-tnscope         | False       | tnscope, vcf-snv-research-index           | deliver               |
| snv, clinical-vcf-pass-tnscope, vcf-pass-tnscope               | False       | tnscope, vcf-snv-clinical                 | deliver, scout        |
| snv, clinical-vcf-pass-tnscope-index, vcf-pass-tnscope         | False       | tnscope, vcf-snv-clinical-index           | deliver, scout        |
| ascat-copynumber, clinical-ascat-copynumber                    | False       | ascatngs, metrics                         | deliver               |
| clinical-rd-delly, rd-delly                                    | True        | delly, coverage                           | deliver               |
| cnv-somatic-cgh-tumor, cgh-tumor                               | False       | cnvkit, tumor, vcf2cytosure               | deliver, scout        |
| cgh-normal, cnv-somatic-cgh-normal                             | False       | tiddit, normal, vcf2cytosure              | deliver, scout        |
| cov, cnv-gens-bed, gens-bed                                    | False       | gens, coverage, bed                       | scout                 |
| cov, cnv-gens-bed-index, gens-bed                              | False       | gens, coverage, bed-index                 | scout                 |
| baf, cnv-gens-bed, gens-bed                                    | False       | gens, fracsnp, bed                        | scout                 |
| baf, cnv-gens-bed-index, gens-bed                              | False       | gens, fracsnp, bed-index                  | scout                 |
| research-vcf-vardict, vcf-vardict                              | False       | vardict, vcf-snv                          | deliver               |
| research-vcf-vardict-index, vcf-vardict                        | False       | vardict, vcf-snv-index                    | deliver               |
| snv, research-vcf-pass-vardict, vcf-pass-vardict               | False       | vardict, vcf-snv-research                 | deliver               |
| snv, research-vcf-pass-vardict-index, vcf-pass-vardict         | False       | vardict, vcf-snv-research-index           | deliver               |
| snv, clinical-vcf-pass-vardict, vcf-pass-vardict               | False       | vardict, vcf-snv-clinical                 | deliver, scout        |
| snv, clinical-vcf-pass-vardict-index, vcf-pass-vardict         | False       | vardict, vcf-snv-clinical-index           | deliver, scout        |
| cns, cnv-cns                                                   | False       | cnvkit, metrics, segments                 | deliver               |
| cnr, cnv-cnr                                                   | False       | cnvkit, regions                           | storage               |
| cnv-gene-metrics, gene-metrics                                 | False       | cnvkit, metrics, genes                    | deliver               |
| clinical-cnv-report-pdf, cnv-report-pdf                        | True        | cnv-report                                | deliver, scout        |
| clinical-circular-cnvpytor, circular-cnvpytor                  | False       | circular-plot, cnvpytor, visualization    | storage               |
| scatter-cnvpytor, clinical-scatter-cnvpytor                    | False       | scatter-plot, cnvpytor, visualization     | storage               |
| plot-ascat-profile, clinical-plot-ascat-profile                | False       | profile-plot, ascatngs, visualization     | storage               |
| clinical-plot-raw-profile, plot-raw-profile                    | False       | raw-profile-plot, ascatngs, visualization | storage               |
| plot-aspcf, clinical-plot-aspcf                                | False       | aspcf-plot, ascatngs, visualization       | storage               |
| clinical-plot-tumor, plot-tumor                                | False       | tumor-plot, ascatngs, visualization       | storage               |
| plot-germline, clinical-plot-germline                          | False       | germline-plot, ascatngs, visualization    | storage               |
| clinical-plot-sunrise, plot-sunrise                            | False       | sunrise-plot, ascatngs, visualization     | storage               |
| cov-tumor-tiddit, clinical-cov-tumor-tiddit                    | False       | tiddit, tumor, coverage                   | deliver               |
| cov-normal-tiddit, clinical-cov-normal-tiddit                  | False       | tiddit, normal, coverage                  | deliver               |
| research-tmb, snv, vardict, tmb                                | False       | research, vardict, tmb                    | storage               |
| research-tmb, snv, tmb, tnscope                                | False       | research, tnscope, tmb                    | storage               |
| cram, umi-tumor-cram                                           | True        | umi-cram, tumor                           | deliver, scout        |
| cram, umi-tumor-cram-index                                     | True        | umi-cram-index, tumor                     | deliver, scout        |
| cram, umi-normal-cram                                          | False       | umi-cram, normal                          | deliver, scout        |
| cram, umi-normal-cram-index                                    | False       | umi-cram-index, normal                    | deliver, scout        |
| research-vcf-tnscope-umi, vcf-tnscope-umi                      | True        | tnscope-umi, vcf-umi-snv                  | deliver               |
| research-vcf-tnscope-umi-index, vcf-tnscope-umi                | True        | tnscope-umi, vcf-umi-snv-index            | deliver               |
| snv, research-vcf-pass-tnscope-umi, vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-research         | deliver               |
| snv, research-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi | True        | tnscope-umi, vcf-umi-snv-research-index   | deliver               |
| snv, vcf-pass-tnscope-umi, clinical-vcf-pass-tnscope-umi       | True        | tnscope-umi, vcf-umi-snv-clinical         | deliver, scout        |
| snv, clinical-vcf-pass-tnscope-umi-index, vcf-pass-tnscope-umi | True        | tnscope-umi, vcf-umi-snv-clinical-index   | deliver, scout        |
| research-tmb, snv, tnscope-umi, tmb                            | True        | research, tnscope-umi, tmb                | storage               |
