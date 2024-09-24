| Raredisease tags                                 | Mandatory   | HK tags                                  | Used by                                        |
|--------------------------------------------------|-------------|------------------------------------------|------------------------------------------------|
| alignment, alignment_markduplicates              | False       | cram, picard-duplicates                  | scout, clinical-delivery                       |
| alignment_markduplicates_index, alignment        | False       | cram-index, picard-duplicates            | scout, clinical-delivery                       |
| alignment, alignment_mt                          | False       | bam-mt                                   | scout                                          |
| alignment, alignment_mt_index                    | False       | bam-mt-index                             | scout                                          |
| tiddit_coverage                                  | False       | tiddit-coverage, bigwig                  | scout                                          |
| qc_bam, mosdepth_d4                              | False       | coverage, d4                             | scout                                          |
| tcov, chromograph_cov                            | False       | chromograph, tcov                        | scout                                          |
| tsv, smncopynumbercaller                         | False       | smn-calling                              | scout, clinical-delivery, long-term-storage    |
| variant_catalog, expansionhunter                 | False       | expansionhunter, variant-catalog         | scout, long-term-storage                       |
| case_sv_str, expansionhunter_stranger            | False       | vcf-str                                  | scout, long-term-storage, clinical-delivery    |
| case_sv_str_index, expansionhunter_stranger      | False       | vcf-str-index                            | scout, long-term-storage, clinical-delivery    |
| str_variants, expansionhunter                    | False       | expansionhunter, vcf-str                 | scout                                          |
| str_alignment, expansionhunter                   | False       | expansionhunter, bam                     | scout                                          |
| str_alignment_index, expansionhunter             | False       | expansionhunter, bam-index               | scout                                          |
| vcf2cytosure                                     | False       | vcf2cytosure                             | scout, long-term-storage                       |
| baf, gens_generatedata                           | False       | gens, fracsnp, bed                       | scout                                          |
| gens_generatedata, baf_index                     | False       | gens, fracsnp, bed-index                 | scout                                          |
| cov, gens_generatedata                           | False       | gens, coverage, bed                      | scout                                          |
| gens_generatedata, cov_index                     | False       | gens, coverage, bed-index                | scout                                          |
| call_mobile_elements                             | False       | mobile-elements, vcf                     | scout, long-term-storage                       |
| call_mobile_elements_index, call_mobile_elements | False       | mobile-elements, vcf-index               | scout, long-term-storage                       |
| clinical, annotate_mobile_elements               | False       | mobile-elements, clinical, vcf           | scout, clinical-delivery, long-term-storage    |
| clinical_index, annotate_mobile_elements         | False       | mobile-elements, clinical, vcf-index     | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, research               | False       | mobile-elements, research, vcf           | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, research_index         | False       | mobile-elements, research, vcf-index     | scout, clinical-delivery, long-term-storage    |
| call_snv                                         | True        | vcf-snv                                  | genotype, clinical-delivery, long-term-storage |
| call_snv_index, call_snv                         | False       | vcf-snv-index                            | cg, clinical-delivery, long-term-storage       |
| call_snv_mt, call_snv                            | False       | vcf-snv, mitochondria                    | cg                                             |
| call_snv_mt_index, call_snv                      | False       | vcf-snv-index, mitochondria              | cg                                             |
| call_sv                                          | False       | vcf-sv                                   | cg, clinical-delivery, long-term-storage       |
| call_sv_index, call_sv                           | False       | vcf-sv-index                             | cg, clinical-delivery, long-term-storage       |
| call_sv_mt                                       | False       | vcf-sv, mitochondria                     | cg                                             |
| call_sv_mt, call_sv_mt_index                     | False       | vcf-sv-index, mitochondria               | cg                                             |
| call_sv_mt, call_sv_mt_del                       | False       | mitochondria, mitodel                    | scout                                          |
| call_sv_mt, eklipse_del                          | False       | eklipse-del, csv, mitochondria           | long-term-storage                              |
| call_sv_mt, eklipse_png                          | False       | eklipse-png, mitochondria                | long-term-storage                              |
| eklipse_genes, call_sv_mt                        | False       | eklipse-gene, csv, mitochondria          | scout                                          |
| rank_and_filter, snv_clinical                    | True        | vcf-snv-clinical                         | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, snv_clinical_index              | True        | vcf-snv-clinical-index                   | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, snv_research                    | True        | vcf-snv-research                         | scout, clinical-delivery, long-term-storage    |
| snv_research_index, rank_and_filter              | True        | vcf-snv-research-index                   | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_clinical                     | True        | vcf-sv-clinical                          | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_clinical_index               | True        | vcf-sv-clinical-index                    | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_research                     | True        | vcf-sv-research                          | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_research_index               | True        | vcf-sv-research-index                    | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, mt_clinical                     | True        | vcf-sv-clinical, mitochondria            | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, mt_clinical_index               | True        | vcf-sv-clinical-index, mitochondria      | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, mt_research                     | True        | vcf-sv-research, mitochondria            | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, mt_research_index               | True        | vcf-sv-research-index, mitochondria      | scout, clinical-delivery, long-term-storage    |
| ngsbits_samplegender                             | True        | ngsbits-samplegender                     | scout                                          |
| peddy                                            | True        | peddy, ped                               | audit, scout, clinical-delivery                |
| ped_check, peddy                                 | True        | peddy, ped-check                         | audit, scout, clinical-delivery                |
| sex_check, peddy                                 | True        | peddy, sex-check                         | audit, scout, clinical-delivery                |
| pedigree_fam, pedigree                           | True        | pedigree                                 | scout                                          |
| rhocallviz, annotate_snv                         | False       | rhocall-viz                              | scout                                          |
| haplogrep, annotate_snv_mt                       | False       | haplogrep                                | scout, clinical-delivery                       |
| autozyg, chromograph_rhoviz                      | False       | chromograph, autozyg                     | scout                                          |
| regions, chromograph_upd                         | False       | chromograph, upd, regions                | scout                                          |
| sites, chromograph_upd                           | False       | chromograph, upd, sites                  | scout                                          |
| multiqc-html, multiqc                            | True        | multiqc-html                             | scout, clinical-delivery, long-term-storage    |
| multiqc-json, multiqc                            | True        | multiqc-json                             | long-term-storage                              |
| multiqc-general-stats, multiqc                   | True        | qc-metrics, multiqc, general-stats       | janus                                          |
| multiqc-picard-alignment, multiqc                | True        | qc-metrics, multiqc, picard-alignment    | janus                                          |
| multiqc-picard-bamqc, multiqc                    | True        | qc-metrics, multiqc, picard-bamqc        | janus                                          |
| multiqc-picard-insertsize, multiqc               | True        | qc-metrics, multiqc, picard-insert-size  | janus                                          |
| multiqc-mosdepth-covdist, multiqc                | True        | qc-metrics, multiqc, mosdepth-covdist    | janus                                          |
| multiqc-mosdepth-cumcov, multiqc                 | True        | qc-metrics, multiqc, mosdepth-cumcov     | janus                                          |
| multiqc-mosdepth-perchrom, multiqc               | True        | qc-metrics, multiqc, mosdepth-perchrom   | janus                                          |
| multiqc-picard-qualitycycle, multiqc             | True        | qc-metrics, multiqc, picard-qualitycycle | janus                                          |
| multiqc-picard-qualitydistr, multiqc             | True        | qc-metrics, multiqc, picard-qualitydistr | janus                                          |
| multiqc-peddy, multiqc                           | True        | qc-metrics, multiqc, peddy               | janus                                          |
| multiqc, multiqc-picard-hs                       | True        | qc-metrics, multiqc, picard-hs           | janus                                          |
| multiqc-picard-histogram1, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc-picard-histogram2, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc-picard-histogram3, multiqc               | False       | qc-metrics, multiqc, picard-histogram    | janus                                          |
| multiqc-picard-wgs, multiqc                      | True        | qc-metrics, multiqc, picard-wgs          | janus                                          |
| nextflow-params                                  | True        | nextflow-params                          | cg, long-term-storage                          |
| nextflow-config                                  | True        | nextflow-config                          | cg, long-term-storage                          |
| samplesheet                                      | True        | nextflow-samplesheet                     | cg, long-term-storage                          |
| software-versions                                | True        | software-versions                        | cg, clinical-delivery, long-term-storage       |
| qc-metrics                                       | True        | qc-metrics, deliverable                  | cg, long-term-storage                          |
| manifest                                         | False       | manifest                                 | scout, long-term-storage                       |

