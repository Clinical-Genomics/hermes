Balsamic tags                                                       Mandatory    HK tags                                           Used by
------------------------------------------------------------------  -----------  ------------------------------------------------  ---------------------
cnv-cns, cns                                                        True         cnvkit, segments                                  deliver
cnr, cnv-cnr                                                        True         cnvkit, regions                                   deliver
scatter, cnv-scatter                                                True         cnvkit, visualization                             deliver
cnv-diagram, diagram                                                True         cnvkit, visualization, diagram                    deliver
gene-breaks, cnv-gene-breaks                                        True         cnvkit, genes                                     storage
cnv-gene-metrics, gene-metrics                                      True         cnvkit, genes, metrics                            deliver
multiqc-html, html                                                  True         multiqc-html                                      scout, deliver, audit
multiqc-json, json                                                  True         multiqc-json                                      vogue, audit
scout-bam, bam                                                      False        bam                                               scout
scout-bam-index, bam                                                False        bam-index                                         scout
tnhaplotyper, vcf-all, annotated-somatic-vcf-all, snv               True         vcf, tumor, haplotype-caller                      storage
tnhaplotyper, vcf-all, annotated-somatic-vcf-all-index, snv         True         vcf-index, tumor, haplotype-caller                storage
snv, vcf-all, annotated-somatic-vcf-all, tnscope                    False        tumor, scope, vcf-snv-research                    scout, deliver
snv, vcf-all, annotated-somatic-vcf-all-index, tnscope              False        tumor, scope, vcf-snv-research-index              scout, deliver
snv, tnsnv, vcf-all, annotated-somatic-vcf-all                      False        vcf, tumor, genotyper                             storage
snv, tnsnv, vcf-all, annotated-somatic-vcf-all-index                False        vcf-index, tumor, genotyper                       storage
sv, manta, vcf-all, annotated-somatic-vcf-all                       True         vcf-sv-research, manta, tumor                     scout, deliver
annotated-somatic-vcf-all-index, manta, vcf-all, sv                 True         vcf-sv-research-index, manta, tumor               scout, deliver
cnvkit, vcf-all, cnv, annotated-somatic-vcf-all                     True         cnvkit, sv-vcf, tumor                             deliver
annotated-somatic-vcf-all-index, cnvkit, vcf-all, cnv               True         cnvkit, sv-vcf-index, tumor                       deliver
snv, annotated-somatic-vcf-summary, vcf-summary, tnscope            False        sention, scope, vcf-report                        audit
snv, tnhaplotyper, annotated-somatic-vcf-summary, vcf-summary       True         sention, haplotype-caller, vcf-report             audit
annotated-somatic-vcf-summary, manta, sv, vcf-summary               True         sention, manta, vcf-report                        audit
snv, tnsnv, annotated-somatic-vcf-summary, vcf-summary              False        sention, genotyper, vcf-report                    audit
annotated-somatic-vcf-summary, cnvkit, cnv, vcf-summary             True         cnvkit, vcf-report                                audit
vcf-pass, tnhaplotyper, annotated-somatic-vcf-pass, snv             True         vcf, sention, haplotype-caller, filtered          storage
vcf-pass, tnhaplotyper, annotated-somatic-vcf-pass-index, snv       True         vcf-index, sention, haplotype-caller, filtered    storage
vcf-pass, tnsnv, annotated-somatic-vcf-pass, snv                    False        vcf, sention, genotyper, filtered                 storage
vcf-pass, tnsnv, annotated-somatic-vcf-pass-index, snv              False        vcf-index, sention, genotyper, filtered           storage
vcf-pass, cnvkit, cnv, annotated-somatic-vcf-pass                   True         cnvkit, sv-vcf, filtered                          storage
vcf-pass, cnvkit, cnv, annotated-somatic-vcf-pass-index             True         cnvkit, sv-vcf-index, filtered                    storage
vcf-pass, manta, annotated-somatic-vcf-pass, sv                     True         vcf-sv-clinical, manta, filtered                  scout
vcf-pass, manta, annotated-somatic-vcf-pass-index, sv               True         vcf-sv-clinical-index, manta, filtered            scout
vcf-pass, snv, annotated-somatic-vcf-pass, tnscope                  False        vcf-snv-clinical, scope, filtered, sention        scout, deliver
vcf-pass, snv, annotated-somatic-vcf-pass-index, tnscope            False        vcf-snv-clinical-index, scope, filtered, sention  scout, deliver
quality-trimmed-fastq-read1, read1                                  True         fastq                                             deliver
quality-trimmed-fastq-read2, read2                                  True         fastq                                             deliver
json, quality-trimmed-fastq-json                                    True         fastq, metrics                                    audit
quality-trimmed-fastq-html, html                                    True         fastq, visualization                              audit
balsamic-report                                                     True         balsamic-report                                   audit
balsamic-config                                                     True         balsamic-config                                   audit
balsamic-dag                                                        True         balsamic-dag                                      audit
bam, normal-bam                                                     False        bam, normal                                       scout, deliver
normal-bam-index, bam                                               False        bam-index, normal                                 scout, deliver
normal-cram, cram                                                   False        cram, normal                                      scout, deliver
cram, normal-cram-index                                             False        cram-index                                        scout, deliver
snv, vardict, vcf-all, annotated-somatic-vcf-all                    False        vcf, vardict                                      storage
snv, vardict, vcf-all, annotated-somatic-vcf-all-index              False        vcf-index, vardict                                storage
strelka, vcf-all, annotated-somatic-vcf-all, snv                    False        vcf, strelka                                      storage
strelka, vcf-all, annotated-somatic-vcf-all-index, snv              False        vcf-index, strelka                                storage
snv, vcf-all, mutect, annotated-somatic-vcf-all                     False        vcf, mutect                                       storage
snv, vcf-all, annotated-somatic-vcf-all-index, mutect               False        vcf-index, mutect                                 storage
snv, vardict, annotated-somatic-vcf-summary, vcf-summary            False        vardict, vcf-report                               audit
snv, mutect, annotated-somatic-vcf-summary, vcf-summary             False        mutect, vcf-report                                audit
strelka, snv, annotated-somatic-vcf-summary, vcf-summary            False        strelka, vcf-report                               audit
vcf-pass, mutect, annotated-somatic-vcf-pass, snv                   False        vcf, mutect, filtered                             storage
vcf-pass, mutect, annotated-somatic-vcf-pass-index, snv             False        vcf-index, mutect, filtered                       storage
vcf-pass, vardict, annotated-somatic-vcf-pass, snv                  False        vcf-snv-clinical, vardict, filtered               scout, deliver
vcf-pass, vardict, annotated-somatic-vcf-pass-index, snv            False        vcf-snv-clinical-index, vardict, filtered         scout, deliver
strelka, vcf-pass, annotated-somatic-vcf-pass, snv                  False        vcf, strelka, filtered                            storage
strelka, vcf-pass, annotated-somatic-vcf-pass-index, snv            False        vcf-index, strelka, filtered                      storage
vardict, tmb, stat-somatic-tmb                                      False        vardict, tmb                                      audit
snv, vcf-all, annotated-germline-vcf-all, strelka-germline          False        vcf, strelka, normal                              storage
snv, vcf-all, annotated-germline-vcf-all-index, strelka-germline    False        vcf-index, strelka, normal                        storage
haplotypecaller, vcf-all, annotated-germline-vcf-all, snv           False        vcf, haplotype-caller, normal                     storage
haplotypecaller, vcf-all, annotated-germline-vcf-all-index, snv     False        vcf-index, haplotype-caller, normal               storage
vcf-all, annotated-germline-vcf-all, sv, manta-germline             False        sv-vcf, manta, normal                             storage
vcf-all, annotated-germline-vcf-all-index, sv, manta-germline       False        sv-vcf-index, manta, normal                       storage
snv, vcf-all, annotated-germline-vcf-all, dnascope                  False        vcf, scope, normal                                storage
snv, vcf-all, annotated-germline-vcf-all-index, dnascope            False        vcf-index, scope, normal                          storage
snv, strelka-germline, annotated-germline-vcf-summary, vcf-summary  False        strelka, normal, vcf-report                       audit
haplotypecaller, vcf-summary, annotated-germline-vcf-summary, snv   False        haplotype-caller, normal, vcf-report              audit
snv, annotated-germline-vcf-summary, dnascope, vcf-summary          False        scope, normal, vcf-report                         audit
vcf-summary, annotated-germline-vcf-summary, sv, manta-germline     False        manta, normal, vcf-report                         audit
bam, tumor-bam                                                      False        bam, tumor                                        scout
tumor-bam-index, bam                                                False        bam-index, tumor                                  scout
cram, tumor-cram                                                    False        cram, tumor                                       scout
cram, tumor-cram-index                                              False        cram-index, tumor                                 scout
vcf-filtered, clinical-vcf-filtered, snv                            False        vcf-snv-clinical, filtered                        scout, deliver
vcf-filtered, clinical-vcf-filtered-index, snv                      False        vcf-snv-clinical-index, filtered                  scout, deliver
vcf-pass, clinical-vcf-pass, snv                                    False        vcf, filtered                                     storage
vcf-pass, clinical-vcf-pass-index, snv                              False        vcf-index, filtered                               storage
