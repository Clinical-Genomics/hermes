| Balsamic tags                                                     | Mandatory   | HK tags                                                     | Used by               |
|-------------------------------------------------------------------|-------------|-------------------------------------------------------------|-----------------------|
| html, multiqc-html                                                | True        | multiqc-html                                                | deliver, scout, audit |
| multiqc-json, json                                                | True        | multiqc-json                                                | vogue, audit          |
| balsamic-report                                                   | True        | balsamic-report                                             | audit                 |
| balsamic-config                                                   | True        | balsamic-config                                             | audit                 |
| balsamic-dag                                                      | True        | balsamic-dag                                                | audit                 |
| qc-metrics-yaml                                                   | True        | qc-metrics, deliverable                                     | vogue                 |
| quality-trimmed-fastq-html, html                                  | True        | fastq, visualization                                        | audit                 |
| quality-trimmed-fastq-json, json                                  | True        | fastq, metrics                                              | audit                 |
| quality-trimmed-fastq-read1, read1                                | True        | fastq                                                       | deliver               |
| quality-trimmed-fastq-read2, read2                                | True        | fastq                                                       | deliver               |
| cram, tumor-cram                                                  | True        | cram, tumor                                                 | deliver, scout        |
| tumor-cram-index, cram                                            | True        | cram-index, tumor                                           | deliver, scout        |
| cram, normal-cram                                                 | False       | cram, normal                                                | deliver, scout        |
| cram, normal-cram-index                                           | False       | cram-index, normal                                          | deliver, scout        |
| tnscope, snv, annotated-somatic-vcf-all, vcf-all                  | False       | tnscope, vcf-snv-research, somatic                          | deliver, scout        |
| annotated-somatic-vcf-all-index, tnscope, snv, vcf-all            | False       | tnscope, vcf-snv-research-index, somatic                    | deliver, scout        |
| tnscope, annotated-somatic-vcf-summary, snv, vcf-summary          | False       | sention, tnscope, vcf-report, somatic                       | audit                 |
| vardict, snv, annotated-somatic-vcf-all, vcf-all                  | False       | vcf, vardict, somatic                                       | storage               |
| vardict, snv, vcf-all, annotated-somatic-vcf-all-index            | False       | vcf-index, vardict, somatic                                 | storage               |
| vardict, annotated-somatic-vcf-summary, snv, vcf-summary          | False       | vardict, vcf-report, somatic                                | audit                 |
| snv, clinical-vcf-filtered, vcf-filtered                          | True        | vcf, vcf-snv-filtered, somatic                              | storage               |
| clinical-vcf-filtered-index, snv, vcf-filtered                    | True        | vcf-index, vcf-snv-filtered-index, somatic                  | storage               |
| vcf-pass, snv, clinical-vcf-pass                                  | True        | vcf, vcf-snv-clinical, somatic                              | deliver, scout        |
| snv, clinical-vcf-pass-index, vcf-pass                            | True        | vcf-index, vcf-snv-clinical-index, somatic                  | deliver, scout        |
| snv, annotated-somatic-vcf-all, vcf-all, tnhaplotyper             | True        | vcf, tumor, haplotype-caller, somatic                       | storage               |
| annotated-somatic-vcf-all-index, snv, vcf-all, tnhaplotyper       | True        | vcf-index, tumor, haplotype-caller, somatic                 | storage               |
| annotated-somatic-vcf-summary, snv, tnhaplotyper, vcf-summary     | True        | sention, haplotype-caller, vcf-report, somatic              | audit                 |
| snv, vcf-filtered, research-vcf-filtered                          | True        | vcf-snv-research, filtered, somatic, haplotype-caller       | storage               |
| snv, vcf-filtered, research-vcf-filtered-index                    | True        | vcf-snv-research-index, filtered, somatic, haplotype-caller | storage               |
| snv, research-vcf-pass, vcf-pass                                  | True        | vcf, filtered, somatic, haplotype-caller                    | storage               |
| snv, research-vcf-pass-index, vcf-pass                            | True        | vcf-index, filtered, somatic, haplotype-caller              | storage               |
| snv, annotated-germline-vcf-all, vcf-all, dnascope                | True        | vcf, dnascope, germline                                     | storage               |
| annotated-germline-vcf-all-index, snv, dnascope, vcf-all          | True        | vcf-index, dnascope, germline                               | storage               |
| snv, dnascope, vcf-summary, annotated-germline-vcf-summary        | True        | dnascope, germline, vcf-report                              | audit                 |
| haplotypecaller, snv, annotated-germline-vcf-all, vcf-all         | False       | vcf, haplotype-caller, germline                             | storage               |
| annotated-germline-vcf-all-index, haplotypecaller, snv, vcf-all   | False       | vcf-index, haplotype-caller, germline                       | storage               |
| snv, haplotypecaller, vcf-summary, annotated-germline-vcf-summary | False       | haplotype-caller, germline, vcf-report                      | audit                 |
| manta, annotated-somatic-vcf-all, vcf-all, sv                     | True        | vcf-sv-research, manta, tumor, somatic                      | deliver, scout        |
| manta, vcf-all, sv, annotated-somatic-vcf-all-index               | True        | vcf-sv-research-index, manta, tumor, somatic                | deliver, scout        |
| manta, annotated-somatic-vcf-summary, sv, vcf-summary             | True        | sention, manta, vcf-report, somatic                         | audit                 |
| clinical-vcf-sv-pass, vcf-sv-pass                                 | False       | vcf-sv-clinical, manta, filtered                            | deliver, scout        |
| vcf-sv-pass, clinical-vcf-sv-pass-index                           | False       | vcf-sv-clinical-index, manta, filtered                      | deliver, scout        |
| clinical-vcf-sv-pass, vcf-sv-pass, sv                             | False       | vcf-sv-clinical, manta, filtered                            | deliver, scout        |
| vcf-sv-pass, clinical-vcf-sv-pass-index, sv                       | False       | vcf-sv-clinical-index, manta, filtered                      | deliver, scout        |
| manta-germline, annotated-germline-vcf-all, vcf-all, sv           | True        | sv-vcf, manta, germline                                     | storage               |
| annotated-germline-vcf-all-index, manta-germline, vcf-all, sv     | True        | sv-vcf-index, manta, germline                               | storage               |
| manta-germline, vcf-summary, sv, annotated-germline-vcf-summary   | True        | manta, germline, vcf-report                                 | audit                 |
| annotated-somatic-vcf-all, vcf-all, delly, sv                     | True        | delly, vcf, somatic                                         | deliver               |
| annotated-somatic-vcf-all-index, vcf-all, delly, sv               | True        | delly, vcf-index, somatic                                   | deliver               |
| annotated-somatic-vcf-summary, delly, sv, vcf-summary             | True        | delly, vcf-report, somatic                                  | audit                 |
| vcf-sv-pass, research-vcf-sv-pass                                 | False       | ascatngs, vcf, filtered                                     | deliver               |
| research-vcf-sv-pass-index, vcf-sv-pass                           | False       | ascatngs, vcf-index, filtered                               | deliver               |
| vcf-sv-pass, research-vcf-sv-pass, sv                             | False       | delly, vcf, filtered, somatic                               | deliver               |
| research-vcf-sv-pass-index, vcf-sv-pass, sv                       | False       | delly, vcf-index, filtered, somatic                         | deliver               |
| cnvkit, annotated-somatic-vcf-all, vcf-all, cnv                   | False       | cnvkit, sv-vcf, tumor, somatic                              | deliver               |
| cnvkit, vcf-all, cnv, annotated-somatic-vcf-all-index             | False       | cnvkit, sv-vcf-index, tumor, somatic                        | deliver               |
| cnvkit, annotated-somatic-vcf-summary, cnv, vcf-summary           | False       | cnvkit, vcf-report, somatic                                 | audit                 |
| vcf-sv-pass, research-vcf-sv-pass, cnv                            | False       | cnvkit, vcf-sv-research, filtered                           | deliver               |
| research-vcf-sv-pass-index, vcf-sv-pass, cnv                      | False       | cnvkit, vcf-sv-research-index, filtered                     | deliver               |
| cnv-cns, cns                                                      | False       | cnvkit, segments                                            | deliver               |
| cnv-cnr, cnr                                                      | False       | cnvkit, regions                                             | deliver               |
| scatter, cnv-scatter                                              | False       | cnvkit, visualization                                       | deliver               |
| cnv-diagram, diagram                                              | False       | cnvkit, visualization, diagram                              | deliver               |
| gene-metrics, cnv-gene-metrics                                    | False       | cnvkit, genes, metrics                                      | deliver               |
| gene-breaks, cnv-gene-breaks                                      | False       | cnvkit, genes                                               | storage               |
| tnscope-umi, snv, annotated-somatic-vcf-all, vcf-all              | False       | vcf, tnscope-umi, somatic                                   | storage               |
| annotated-somatic-vcf-all-index, tnscope-umi, snv, vcf-all        | False       | vcf-index, tnscope-umi, somatic                             | storage               |
| tnscope-umi, snv, annotated-somatic-vcf-summary, vcf-summary      | False       | vcf-report, tnscope-umi, somatic                            | audit                 |
| annotated-somatic-vcf-all, vcf-all, ascat, cnv                    | False       | ascatngs, vcf, somatic                                      | deliver               |
| annotated-somatic-vcf-all-index, vcf-all, ascat, cnv              | False       | ascatngs, vcf-index, somatic                                | deliver               |
| annotated-somatic-vcf-summary, ascat, cnv, vcf-summary            | False       | ascatngs, vcf-report, somatic                               | audit                 |
| research-ascat-output-pdf, ascat-output-pdf                       | False       | ascatngs, visualization                                     | deliver, scout        |
