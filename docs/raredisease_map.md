| Raredisease tags                                 | Mandatory   | HK tags                              | Used by                                        |
|--------------------------------------------------|-------------|--------------------------------------|------------------------------------------------|
| alignment, alignment_markduplicates              | False       | cram, picard-duplicates              | scout, clinical-delivery                       |
| alignment_markduplicates_index, alignment        | False       | cram-index, picard-duplicates        | scout, clinical-delivery                       |
| alignment, alignment_mt                          | False       | bam-mt                               | scout                                          |
| alignment_mt_index, alignment                    | False       | bam-mt-index                         | scout                                          |
| tiddit_coverage                                  | False       | tiddit-coverage, bigwig              | scout                                          |
| d4tools_d4, qc_bam                              | False       | coverage, d4                         | scout                                          |
| sambamba_depth, qc_bam                           | False       | coverage, sambamba_depth             | cg, long-term-storage                          |
| tcov, chromograph_cov                            | False       | chromograph, tcov                    | scout                                          |
| smncopynumbercaller, tsv                         | False       | smn-calling                          | scout, clinical-delivery, long-term-storage    |
| variant_catalog, expansionhunter                 | False       | expansionhunter, variant-catalog     | scout, long-term-storage                       |
| case_sv_str, expansionhunter_stranger            | False       | vcf-str                              | scout, long-term-storage, clinical-delivery    |
| case_sv_str_index, expansionhunter_stranger      | False       | vcf-str-index                        | scout, long-term-storage, clinical-delivery    |
| str_variants, expansionhunter                    | False       | expansionhunter, vcf-str             | scout                                          |
| str_alignment, expansionhunter                   | False       | expansionhunter, bam                 | scout                                          |
| str_alignment_index, expansionhunter             | False       | expansionhunter, bam-index           | scout                                          |
| vcf2cytosure                                     | False       | vcf2cytosure                         | scout, long-term-storage                       |
| baf, gens_generatedata                           | False       | gens, fracsnp, bed                   | scout                                          |
| baf_index, gens_generatedata                     | False       | gens, fracsnp, bed-index             | scout                                          |
| gens_generatedata, cov                           | False       | gens, coverage, bed                  | scout                                          |
| cov_index, gens_generatedata                     | False       | gens, coverage, bed-index            | scout                                          |
| call_mobile_elements                             | False       | mobile-elements, vcf                 | scout, long-term-storage                       |
| call_mobile_elements, call_mobile_elements_index | False       | mobile-elements, vcf-index           | scout, long-term-storage                       |
| clinical, annotate_mobile_elements               | False       | mobile-elements, clinical, vcf       | scout, clinical-delivery, long-term-storage    |
| annotate_mobile_elements, clinical_index         | False       | mobile-elements, clinical, vcf-index | scout, clinical-delivery, long-term-storage    |
| research, annotate_mobile_elements               | False       | mobile-elements, research, vcf       | scout, clinical-delivery, long-term-storage    |
| research_index, annotate_mobile_elements         | False       | mobile-elements, research, vcf-index | scout, clinical-delivery, long-term-storage    |
| call_snv                                         | True        | vcf-snv                              | genotype, clinical-delivery, long-term-storage |
| call_snv_index, call_snv                         | False       | vcf-snv-index                        | cg, clinical-delivery, long-term-storage       |
| call_snv_mt, call_snv                            | False       | vcf-snv, mitochondria                | cg                                             |
| call_snv, call_snv_mt_index                      | False       | vcf-snv-index, mitochondria          | cg                                             |
| call_sv                                          | False       | vcf-sv                               | cg, clinical-delivery, long-term-storage       |
| call_sv_index, call_sv                           | False       | vcf-sv-index                         | cg, clinical-delivery, long-term-storage       |
| call_sv_mt                                       | False       | vcf-sv, mitochondria                 | cg                                             |
| call_sv_mt_index, call_sv_mt                     | False       | vcf-sv-index, mitochondria           | cg                                             |
| call_sv_mt_del, call_sv_mt                       | False       | mitochondria, mitodel                | scout                                          |
| eklipse_del, call_sv_mt                          | False       | eklipse-del, csv, mitochondria       | long-term-storage                              |
| eklipse_png, call_sv_mt                          | False       | eklipse-png, mitochondria            | long-term-storage                              |
| eklipse_genes, call_sv_mt                        | False       | eklipse-gene, csv, mitochondria      | scout                                          |
| snv_clinical, rank_and_filter                    | True        | vcf-snv-clinical                     | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, snv_clinical_index              | True        | vcf-snv-clinical-index               | scout, clinical-delivery, long-term-storage    |
| snv_research, rank_and_filter                    | True        | vcf-snv-research                     | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, snv_research_index              | True        | vcf-snv-research-index               | scout, clinical-delivery, long-term-storage    |
| rank_and_filter, sv_clinical                     | True        | vcf-sv-clinical                      | scout, clinical-delivery, long-term-storage    |
| sv_clinical_index, rank_and_filter               | True        | vcf-sv-clinical-index                | scout, clinical-delivery, long-term-storage    |
| sv_research, rank_and_filter                     | True        | vcf-sv-research                      | scout, clinical-delivery, long-term-storage    |
| sv_research_index, rank_and_filter               | True        | vcf-sv-research-index                | scout, clinical-delivery, long-term-storage    |
| mt_clinical, rank_and_filter                     | False       | vcf-sv-clinical, mitochondria        | scout, clinical-delivery, long-term-storage    |
| mt_clinical_index, rank_and_filter               | False       | vcf-sv-clinical-index, mitochondria  | scout, clinical-delivery, long-term-storage    |
| mt_research, rank_and_filter                     | False       | vcf-sv-research, mitochondria        | scout, clinical-delivery, long-term-storage    |
| mt_research_index, rank_and_filter               | False       | vcf-sv-research-index, mitochondria  | scout, clinical-delivery, long-term-storage    |
| ngsbits_samplegender                             | True        | ngsbits-samplegender                 | scout                                          |
| peddy                                            | True        | peddy, ped                           | audit, scout, clinical-delivery                |
| ped_check, peddy                                 | True        | peddy, ped-check                     | audit, scout, clinical-delivery                |
| sex_check, peddy                                 | True        | peddy, sex-check                     | audit, scout, clinical-delivery                |
| pedigree_fam, pedigree                           | True        | pedigree                             | scout                                          |
| rhocallviz, annotate_snv                         | False       | rhocall-viz                          | scout                                          |
| annotate_snv_mt, haplogrep                       | False       | haplogrep                            | scout, clinical-delivery                       |
| chromograph_rhoviz, autozyg                      | False       | chromograph, autozyg                 | scout                                          |
| chromograph_upd, regions                         | False       | chromograph, upd, regions            | scout                                          |
| chromograph_upd, sites                           | False       | chromograph, upd, sites              | scout                                          |
| multiqc-html, multiqc                            | True        | multiqc-html                         | scout, clinical-delivery, long-term-storage    |
| multiqc-json, multiqc                            | True        | multiqc-json                         | long-term-storage                              |
| nextflow-params                                  | True        | nextflow-params                      | cg, long-term-storage                          |
| nextflow-config                                  | True        | nextflow-config                      | cg, long-term-storage                          |
| samplesheet                                      | True        | nextflow-samplesheet                 | cg, long-term-storage                          |
| software-versions                                | True        | software-versions                    | cg, clinical-delivery, long-term-storage       |
| qc-metrics                                       | True        | qc-metrics, deliverable              | cg, long-term-storage                          |
| manifest                                         | False       | manifest                             | scout, long-term-storage                       |