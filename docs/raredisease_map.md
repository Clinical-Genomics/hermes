| Raredisease tags                                 | Mandatory   | HK tags                                  | Used by                                        |
|--------------------------------------------------|-------------|------------------------------------------|------------------------------------------------|
| alignment_markduplicates, alignment              | False       | cram, picard-duplicates                  | scout, clinical-delivery                       |
| alignment_markduplicates_index, alignment        | False       | cram-index, picard-duplicates            | scout, clinical-delivery                       |
| alignment_mt, alignment                          | False       | bam-mt                                   | scout                                          |
| alignment_mt_index, alignment                    | False       | bam-mt-index                             | scout                                          |
| tiddit_coverage                                  | False       | tiddit-coverage, bigwig                  | scout                                          |
| tcov, chromograph_cov                            | False       | chromograph, tcov                        | scout                                          |
| smncopynumbercaller, tsv                         | False       | smn-calling                              | scout, clinical-delivery, long-term-storage    |
| expansionhunter, variant_catalog                 | False       | expansionhunter, variant-catalog         | scout, long-term-storage                       |
| case_sv_str, expansionhunter_stranger            | False       | vcf-str                                  | scout, long-term-storage, clinical-delivery    |
| case_sv_str_index, expansionhunter_stranger      | False       | vcf-str-index                            | scout, long-term-storage, clinical-delivery    |
| expansionhunter, str_variants                    | False       | expansionhunter, vcf-str                 | scout                                          |
| str_variants_index, expansionhunter              | False       | expansionhunter, vcf-str-index           | scout                                          |
| expansionhunter, str_alignment                   | False       | expansionhunter, bam                     | scout                                          |
| expansionhunter, str_alignment_index             | False       | expansionhunter, bam-index               | scout                                          |
| vcf2cytosure                                     | False       | vcf2cytosure                             | scout, long-term-storage                       |
| gens_generatedata, baf                           | False       | gens, fracsnp, bed                       | scout                                          |
| gens_generatedata, baf_index                     | False       | gens, fracsnp, bed-index                 | scout                                          |
| cov, gens_generatedata                           | False       | gens, coverage, bed                      | scout                                          |
| cov_index, gens_generatedata                     | False       | gens, coverage, bed-index                | scout                                          |
| call_mobile_elements                             | False       | mobile-elements, vcf                     | scout, long-term-storage                       |
| call_mobile_elements, call_mobile_elements_index | False       | mobile-elements, vcf-index               | scout, long-term-storage                       |
| annotate_mobile_elements, clinical               | False       | mobile-elements, clinical, vcf           | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, clinical_index         | False       | mobile-elements, clinical, vcf-index     | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, research               | False       | mobile-elements, research, vcf           | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, research_index         | False       | mobile-elements, research, vcf-index     | scout, clinical-delivery, long-term-storage    |
| call_snv                                         | True        | vcf-snv                                  | genotype, clinical-delivery, long-term-storage |
| call_snv_index, call_snv                         | False       | vcf-snv-index                            | cg, clinical-delivery, long-term-storage       |
| call_snv_mt, call_snv                            | False       | vcf-snv, mitochondria                    | cg                                             |
| call_snv_mt_index, call_snv                      | False       | vcf-snv-index, mitochondria              | cg                                             |
| call_sv                                          | False       | vcf-sv                                   | cg, clinical-delivery, long-term-storage       |
| call_sv, call_sv_index                           | False       | vcf-sv-index                             | cg, clinical-delivery, long-term-storage       |
| call_sv_mt                                       | False       | vcf-sv, mitochondria                     | cg                                             |
| call_sv_mt_index, call_sv_mt                     | False       | vcf-sv-index, mitochondria               | cg                                             |
| call_sv_mt_del, call_sv_mt                       | False       | mitochondria, mitodel                    | scout                                          |
| call_sv_mt, eklipse_del                          | False       | eklipse-del, csv, mitochondria           | scout, clinical-delivery, long-term-storage    |
| call_sv_mt, eklipse_png                          | False       | eklipse-png, mitochondria                | scout                                          |
| eklipse_genes, call_sv_mt                        | False       | eklipse-gene, csv, mitochondria          | scout                                          |
| snv_clinical, rank_and_filter                    | True        | vcf-snv-clinical                         | scout, clinical-delivery, long-term-storage    |
| snv_clinical_index, rank_and_filter              | True        | vcf-snv-clinical-index                   | scout, clinical-delivery, long-term-storage    |
| snv_research, rank_and_filter                    | True        | vcf-snv-research                         | scout, clinical-delivery, long-term-storage    |
| snv_research_index, rank_and_filter              | True        | vcf-snv-research-index                   | scout, clinical-delivery, long-term-storage    |
| sv_clinical, rank_and_filter                     | True        | vcf-sv-clinical                          | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_clinical_index               | True        | vcf-sv-clinical-index                    | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_research                     | True        | vcf-sv-research                          | scout, clinical-delivery, long-term-storage    |
| sv_research_index, rank_and_filter               | True        | vcf-sv-research-index                    | scout, clinical-delivery, long-term-storage    |
| mt_clinical, rank_and_filter                     | True        | vcf-sv-clinical, mitochondria            | scout, clinical-delivery, long-term-storage    |
| mt_clinical_index, rank_and_filter               | True        | vcf-sv-clinical-index, mitochondria      | scout, clinical-delivery, long-term-storage    |
| mt_research, rank_and_filter                     | True        | vcf-sv-research, mitochondria            | scout, clinical-delivery, long-term-storage    |
| mt_research_index, rank_and_filter               | True        | vcf-sv-research-index, mitochondria      | scout, clinical-delivery, long-term-storage    |
| ngsbits_samplegender                             | True        | ngsbits-samplegender                     | scout                                          |
| peddy                                            | True        | peddy, ped                               | audit, scout, clinical-delivery                |
| peddy, ped_check                                 | True        | peddy, ped-check                         | audit, scout, clinical-delivery                |
| sex_check, peddy                                 | True        | peddy, sex-check                         | audit, scout, clinical-delivery                |
| pedigree_fam, pedigree                           | True        | pedigree                                 | scout                                          |
| rhocallviz, annotate_snv                         | False       | rhocall-viz                              | scout                                          |
| annotate_snv_mt, haplogrep                       | False       | haplogrep                                | scout, clinical-delivery                       |
| chromograph_rhoviz, autozyg                      | False       | chromograph, autozyg                     | scout                                          |
| regions, chromograph_upd                         | False       | chromograph, upd, regions                | scout                                          |
| chromograph_upd, sites                           | False       | chromograph, upd, sites                  | scout                                          |
| multiqc, multiqc-html                            | True        | multiqc-html                             | scout, clinical-delivery, long-term-storage    |
| multiqc-json, multiqc                            | True        | multiqc-json                             | long-term-storage                              |
| multiqc-general-stats, multiqc                   | True        | qc-metrics, multiqc, general-stats       | janus                                          |
| multiqc-picard-alignment, multiqc                | True        | qc-metrics, multiqc, picard-alignment    | janus                                          |
| multiqc-picard-bamqc, multiqc                    | True        | qc-metrics, multiqc, picard-bamqc        | janus                                          |
| multiqc, multiqc-picard-insertsize               | True        | qc-metrics, multiqc, picard-insert-size  | janus                                          |
| multiqc-mosdepth-covdist, multiqc                | True        | qc-metrics, multiqc, mosdepth-covdist    | janus                                          |
| multiqc, multiqc-mosdepth-cumcov                 | True        | qc-metrics, multiqc, mosdepth-cumcov     | janus                                          |
| multiqc, multiqc-mosdepth-perchrom               | True        | qc-metrics, multiqc, mosdepth-perchrom   | janus                                          |
| multiqc-picard-qualitycycle, multiqc             | True        | qc-metrics, multiqc, picard-qualitycycle | janus                                          |
| multiqc-picard-qualitydistr, multiqc             | True        | qc-metrics, multiqc, picard-qualitydistr | janus                                          |
| multiqc, multiqc-peddy                           | True        | qc-metrics, multiqc, peddy               | janus                                          |
| multiqc-picard-hs, multiqc                       | True        | qc-metrics, multiqc, picard-hs           | janus                                          |
| multiqc-picard-histogram1, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc-picard-histogram2, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc-picard-histogram3, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc, multiqc-picard-wgs                      | True        | qc-metrics, multiqc, picard-wgs          | janus                                          |
| nextflow-params                                  | True        | nextflow-params                          | cg, long-term-storage                          |
| nextflow-config                                  | True        | nextflow-config                          | cg, long-term-storage                          |
| samplesheet                                      | True        | nextflow-samplesheet                     | cg, long-term-storage                          |
| software-versions                                | True        | software-versions                        | cg, clinical-delivery, long-term-storage       |
| qc-metrics                                       | True        | qc-metrics                               | cg, long-term-storage                          |