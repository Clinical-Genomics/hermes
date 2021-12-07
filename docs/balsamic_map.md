| Balsamic tags                                                      | Mandatory   | HK tags                                                      | Used by               |
|--------------------------------------------------------------------|-------------|--------------------------------------------------------------|-----------------------|
| cnv-cns, cns                                                       | True        | cnvkit, segments                                             | deliver               |
| cnv-cnr, cnr                                                       | True        | cnvkit, regions                                              | deliver               |
| cnv-scatter, scatter                                               | True        | cnvkit, visualization                                        | deliver               |
| diagram, cnv-diagram                                               | True        | cnvkit, visualization, diagram                               | deliver               |
| gene-breaks, cnv-gene-breaks                                       | True        | cnvkit, genes                                                | storage               |
| cnv-gene-metrics, gene-metrics                                     | True        | cnvkit, genes, metrics                                       | deliver               |
| ascat, vcf-all, annotated-somatic-vcf-all, cnv                     | True        | ascatngs, vcf, somatic                                       | deliver               |
| ascat, vcf-all, annotated-somatic-vcf-all-index, cnv               | True        | ascatngs, vcf-index, somatic                                 | deliver               |
| research-vcf-sv-pass, vcf-sv-pass                                  | True        | ascatngs, vcf, filtered, somatic                             | deliver               |
| research-vcf-sv-pass-index, vcf-sv-pass                            | True        | ascatngs, vcf-index, filtered, somatic                       | deliver               |
| ascat-output-pdf, research-ascat-output-pdf                        | True        | ascatngs, visualization                                      | scout, deliver        |
| delly, annotated-somatic-vcf-all, sv, vcf-all                      | True        | delly, vcf, somatic                                          | deliver               |
| delly, annotated-somatic-vcf-all-index, sv, vcf-all                | True        | delly, vcf-index, somatic                                    | deliver               |
| sv, vcf-sv-pass, research-vcf-sv-pass                              | True        | delly, vcf, filtered, somatic                                | deliver               |
| sv, vcf-sv-pass, research-vcf-sv-pass-index                        | True        | delly, vcf-index, filtered, somatic                          | deliver               |
| qc-metrics-yaml                                                    | True        | qc-metrics, deliverable                                      | vogue, deliver        |
| html, multiqc-html                                                 | True        | multiqc-html                                                 | scout, deliver, audit |
| multiqc-json, json                                                 | True        | multiqc-json                                                 | vogue, audit          |
| scout-bam, bam                                                     | False       | bam                                                          | scout                 |
| scout-bam-index, bam                                               | False       | bam-index                                                    | scout                 |
| tnhaplotyper, snv, annotated-somatic-vcf-all, vcf-all              | True        | vcf, tumor, haplotype-caller                                 | storage               |
| tnhaplotyper, annotated-somatic-vcf-all-index, snv, vcf-all        | True        | vcf-index, tumor, haplotype-caller                           | storage               |
| vcf-filtered, snv, research-vcf-filtered                           | True        | vcf-snv-research, filtered, somatic, haplotype-caller        | storage               |
| vcf-filtered, snv, research-vcf-filtered-index                     | True        | vcf-snv-research-index, filtered, somatic, haplotype-caller  | storage               |
| snv, research-vcf-pass, vcf-pass                                   | True        | vcf, filtered, somatic, haplotype-caller                     | storage               |
| snv, research-vcf-pass-index, vcf-pass                             | True        | vcf-index, filtered, somatic, haplotype-caller               | storage               |
| tnscope, annotated-somatic-vcf-all, snv, vcf-all                   | False       | tumor, scope, vcf-snv-research                               | scout, deliver        |
| tnscope, annotated-somatic-vcf-all-index, snv, vcf-all             | False       | tumor, scope, vcf-snv-research-index                         | scout, deliver        |
| annotated-somatic-vcf-all, tnsnv, snv, vcf-all                     | False       | vcf, tumor, genotyper                                        | storage               |
| annotated-somatic-vcf-all-index, tnsnv, snv, vcf-all               | False       | vcf-index, tumor, genotyper                                  | storage               |
| annotated-somatic-vcf-all, sv, manta, vcf-all                      | True        | vcf-sv-research, manta, tumor                                | scout, deliver        |
| annotated-somatic-vcf-all-index, sv, manta, vcf-all                | True        | vcf-sv-research-index, manta, tumor                          | scout, deliver        |
| cnv, cnvkit, annotated-somatic-vcf-all, vcf-all                    | True        | cnvkit, sv-vcf, tumor                                        | deliver               |
| annotated-somatic-vcf-all-index, cnv, cnvkit, vcf-all              | True        | cnvkit, sv-vcf-index, tumor                                  | deliver               |
| tnscope, vcf-summary, annotated-somatic-vcf-summary, snv           | False       | sention, scope, vcf-report                                   | audit                 |
| tnhaplotyper, annotated-somatic-vcf-summary, snv, vcf-summary      | True        | sention, haplotype-caller, vcf-report                        | audit                 |
| vcf-summary, annotated-somatic-vcf-summary, manta, sv              | True        | sention, manta, vcf-report                                   | audit                 |
| vcf-summary, tnsnv, annotated-somatic-vcf-summary, snv             | False       | sention, genotyper, vcf-report                               | audit                 |
| vcf-summary, cnv, cnvkit, annotated-somatic-vcf-summary            | True        | cnvkit, vcf-report                                           | audit                 |
| tnhaplotyper, annotated-somatic-vcf-pass, vcf-pass, snv            | True        | vcf, sention, haplotype-caller, filtered                     | storage               |
| tnhaplotyper, vcf-pass, snv, annotated-somatic-vcf-pass-index      | True        | vcf-index, sention, haplotype-caller, filtered               | storage               |
| annotated-somatic-vcf-pass, tnsnv, vcf-pass, snv                   | False       | vcf, sention, genotyper, filtered                            | storage               |
| tnsnv, vcf-pass, snv, annotated-somatic-vcf-pass-index             | False       | vcf-index, sention, genotyper, filtered                      | storage               |
| cnv, annotated-somatic-vcf-pass, cnvkit, vcf-pass                  | True        | cnvkit, sv-vcf, filtered                                     | storage               |
| cnv, cnvkit, vcf-pass, annotated-somatic-vcf-pass-index            | True        | cnvkit, sv-vcf-index, filtered                               | storage               |
| annotated-somatic-vcf-pass, vcf-pass, manta, sv                    | True        | vcf-sv-clinical, manta, filtered                             | scout                 |
| manta, vcf-pass, annotated-somatic-vcf-pass-index, sv              | True        | vcf-sv-clinical-index, manta, filtered                       | scout                 |
| tnscope, annotated-somatic-vcf-pass, vcf-pass, snv                 | False       | vcf-snv-clinical, scope, filtered, sention                   | scout, deliver        |
| tnscope, vcf-pass, snv, annotated-somatic-vcf-pass-index           | False       | vcf-snv-clinical-index, scope, filtered, sention             | scout, deliver        |
| quality-trimmed-fastq-read1, read1                                 | True        | fastq                                            | deliver               |
| read2, quality-trimmed-fastq-read2                                 | True        | fastq                                            | deliver               |
| quality-trimmed-fastq-json, json                                   | True        | fastq, metrics                                   | audit                 |
| html, quality-trimmed-fastq-html                                   | True        | fastq, visualization                             | audit                 |
| balsamic-report                                                    | True        | balsamic-report                                  | audit                 |
| balsamic-config                                                    | True        | balsamic-config                                  | audit                 |
| balsamic-dag                                                       | True        | balsamic-dag                                     | audit                 |
| normal-bam, bam                                                    | False       | bam, normal                                      | scout, deliver        |
| normal-bam-index, bam                                              | False       | bam-index, normal                                | scout, deliver        |
| normal-cram, cram                                                  | False       | cram, normal                                     | scout, deliver        |
| normal-cram-index, cram                                            | False       | cram-index                                       | scout, deliver        |
| vardict, annotated-somatic-vcf-all, snv, vcf-all                   | False       | vcf, vardict                                     | storage               |
| vardict, annotated-somatic-vcf-all-index, snv, vcf-all             | False       | vcf-index, vardict                               | storage               |
| vardict, vcf-summary, annotated-somatic-vcf-summary, snv           | False       | vardict, vcf-report                              | audit                 |
| vardict, annotated-somatic-vcf-pass, vcf-pass, snv                 | False       | vcf-snv-clinical, vardict, filtered              | scout, deliver        |
| vardict, vcf-pass, snv, annotated-somatic-vcf-pass-index           | False       | vcf-snv-clinical-index, vardict, filtered        | scout, deliver        |
| annotated-germline-vcf-all, snv, haplotypecaller, vcf-all          | False       | vcf, haplotype-caller, normal                    | storage               |
| annotated-germline-vcf-all-index, snv, haplotypecaller, vcf-all    | False       | vcf-index, haplotype-caller, normal              | storage               |
| manta-germline, annotated-germline-vcf-all, sv, vcf-all            | False       | sv-vcf, manta, normal                            | storage               |
| annotated-germline-vcf-all-index, sv, manta-germline, vcf-all      | False       | sv-vcf-index, manta, normal                      | storage               |
| dnascope, annotated-germline-vcf-all, snv, vcf-all                 | False       | vcf, scope, normal                               | storage               |
| annotated-germline-vcf-all-index, dnascope, snv, vcf-all           | False       | vcf-index, scope, normal                         | storage               |
| vcf-summary, annotated-germline-vcf-summary, snv, haplotypecaller  | False       | haplotype-caller, normal, vcf-report             | audit                 |
| dnascope, annotated-germline-vcf-summary, snv, vcf-summary         | False       | scope, normal, vcf-report                        | audit                 |
| manta-germline, annotated-germline-vcf-summary, sv, vcf-summary    | False       | manta, normal, vcf-report                        | audit                 |
| tumor-bam, bam                                                     | False       | bam, tumor                                       | scout                 |
| tumor-bam-index, bam                                               | False       | bam-index, tumor                                 | scout                 |
| tumor-cram, cram                                                   | False       | cram, tumor                                      | scout                 |
| tumor-cram-index, cram                                             | False       | cram-index, tumor                                | scout                 |
| clinical-vcf-filtered, vcf-filtered, snv                           | False       | vcf-snv-clinical, filtered                       | scout, deliver        |
| clinical-vcf-filtered-index, vcf-filtered, snv                     | False       | vcf-snv-clinical-index, filtered                 | scout, deliver        |
| clinical-vcf-pass, vcf-pass, snv                                   | False       | vcf, filtered                                    | storage               |
| vcf-pass, snv, clinical-vcf-pass-index                             | False       | vcf-index, filtered                              | storage               |
