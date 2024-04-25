| Raredisease tags                                  | Mandatory   | HK tags                                 | Used by      |
|---------------------------------------------------|-------------|-----------------------------------------|--------------|
| alignment, alignment_markduplicates               | False       | cram                                    | scout        |
| alignment, alignment_markduplicates               | False       | cram_index                              | scout        |
| alignment, alignment_mt                           | False       | cram-mt                                 | scout        |
| alignment, alignment_mt_index                     | False       | cram-mt                                 | scout        |
| tiddit_coverage,tiddit_coverage                   | False       | tiddit-coverage, bigwig                 | scout        |
| chromograph_cov, tcov                             | False       | chromograph, tcov                       | scout        |
| smncopynumbercaller, tsv                          | False       | smn-calling                             | scout        |
| expansionhunter, variant_catalog                  | False       | expansionhunter, variant-catalog        | scout        |
| expansionhunter, case_sv_str                      | False       | vcf-str                                 | scout        |
| expansionhunter, case_sv_str_index                | False       | vcf-str_index                           | scout        |
| expansionhunter, str_variants                     | False       | expansionhunter, vcf-str                | scout        |
| expansionhunter, str_variants_index               | False       | expansionhunter, vcf-str-index          | scout        |
| expansionhunter, str_alignment                    | False       | expansionhunter, bam                    | scout        |
| expansionhunter, str_alignment_index              | False       | expansionhunter, bam-index              | scout        |
| vcf2cytosure, vcf2cytosure                        | False       | vcf2cytosure                            | scout        |
| gens_generatedata, baf                            | False       | gens, fracsnp, bed                      | scout        |
| gens_generatedata, baf_index                      | False       | gens, fracsnp, bed-index                | scout        |
| gens_generatedata, cov                            | False       | gens, coverage, bed                     | scout        |
| gens_generatedata, cov_index                      | False       | gens, coverage, bed-index               | scout        |
| call_mobile_elements, call_mobile_elements        | False       | gens, coverage, bed-index               | scout        |
| call_mobile_elements, call_mobile_elements_index  | False       | gens, coverage, bed-index               | scout        |
| annotate_mobile_elements, clinical                | False       | mobile-elements, clinical, vcf          | scout        |
| annotate_mobile_elements, clinical_index          | False       | mobile-elements, clinical, vcf_index    | scout        |
| annotate_mobile_elements, research                | False       | mobile-elements, research, vcf          | scout        |
| annotate_mobile_elements, research_index          | False       | mobile-elements, research, vcf_index    | scout        |
| call_snv, call_snv                                | True        | vcf_snv                                 | genotype     |
| call_snv, call_snv_index                          | False       | vcf_snv_index                           | scout        |
| call_snv, call_snv_mt                             | False       | vcf_snv, mitochondria                   | scout        |
| call_snv, call_snv_mt_index                       | False       | vcf_snv_index, mitochondria             | scout        |
| call_sv, call_sv                                  | False       | vcf_sv                                  | scout        |
| call_sv, call_sv_index                            | False       | vcf_sv_index                            | scout        |
| call_sv, call_sv_mt                               | False       | vcf_sv, mitochondria                    | scout        |
| call_sv, call_sv_mt_index                         | False       | vcf_sv_index, mitochondria              | scout        |
| call_sv_mt, call_sv_mt_del                        | False       | mitodel, mitochondria                   | scout        |
| call_sv_mt, eklipse_del                           | False       | eklipse_del, csv, mitochondria          | scout        |
| call_sv_mt, eklipse_png                           | False       | eklipse_png, mitochondria               | scout        |
| call_sv_mt, eklipse_genes                         | False       | eklipse_genes, mitochondria             | scout        |
| annotate_sv, svdbquery                            | False       | svdbquery, vcf                          | scout        |
| annotate_sv, svdbquery_index                      | False       | svdbquery, vcf_index                    | scout        |
| rank_and_filter, snv_clinical                     | True        | vcf-snv-clinical                        | scout        |
| rank_and_filter, snv_clinical_index               | True        | vcf-snv-clinical_index                  | scout        |
| rank_and_filter, snv_research                     | True        | vcf-snv-research                        | scout        |
| rank_and_filter, snv_research_index               | True        | vcf-snv-research_index                  | scout        |
| rank_and_filter, sv_clinical                      | True        | vcf-sv-clinical                         | scout        |
| rank_and_filter, sv_clinical_index                | True        | vcf-sv-clinical_index                   | scout        |
| rank_and_filter, sv_research                      | True        | vcf-sv-research                         | scout        |
| rank_and_filter, sv_research_index                | True        | vcf-sv-research_index                   | scout        |
| rank_and_filter, mt_clinical                      | True        | vcf-sv-clinical, mitochondria           | scout        |
| rank_and_filter, mt_clinical_index                | True        | vcf-sv-clinical_index, mitochondria     | scout        |
| rank_and_filter, mt_research                      | True        | vcf-sv-research, mitochondria           | scout        |
| rank_and_filter, mt_research_index                | True        | vcf-sv-research_index, mitochondria     | scout        |
| ngsbits_samplegender, ngsbits_samplegender        | True        | ngsbits                                 | scout        |
| peddy, peddy                                      | True        | peddy, ped                              | audit, scout |
| ped_check, peddy_ar                               | True        | peddy, ped-check                        | audit, scout |
| peddy, sex_check,                                 | True        | peddy, sex-check                        | audit, scout |
| pedigree, pedigree_fam                            | True        | pedigree                                | scout        |
| annotate_snv, rhocallviz                          | False       | rhocall-viz                             | scout        |
| annotate_snv, annotate_snv                        | False       | vcf_snv, annotation                     | scout        |
| annotate_snv, annotate_snv_index                  | False       | vcf_snv_index, annotation               | scout        |
| annotate_snv_mt, annotate_snv_mt                  | False       | vcf_mt, annotation                      | scout        |
| annotate_snv_mt, annotate_snv_mt_index            | False       | vcf_mt_index, annotation                | scout        |
| annotate_snv_mt, halogrep                         | False       | halogrep                                | scout        |
| chromograph_rhoviz, autozyg                       | False       | chromograph, autozyg                    | scout        |
| chromograph_upd, regions                          | False       | chromograph, upd, regions               | scout        |
| multiqc, html                                     | True        | multiqc-html                            | scout        |
| multiqc, json                                     | True        | multiqc-json                            | storage      |
| multiqc, multiqc-mosdepth-covdist                 | True        | qc-metrics, multiqc, mosdepth-covdist   | janus        |
| multiqc, multiqc-mosdepth-cumcov                  | True        | qc-metrics, multiqc, mosdepth-cumcov    | janus        |
| multiqc, multiqc-mosdepth-perchrom                | True        | qc-metrics, multiqc, mosdepth-perchrom  | janus        |
| multiqc, multiqc-general-stats                    | True        | qc-metrics, multiqc, general-stats      | janus        |
| multiqc, multiqc-picard-alignment                 | True        | qc-metrics, multiqc, picard-alignment   | janus        |
| multiqc, multiqc-picard-bamqc                     | True        | qc-metrics, multiqc, picard-bamqc       | janus        |
| multiqc, multiqc-picard-insertsize                | True        | qc-metrics, multiqc, picard-insertsize  | janus        |
| multiqc, multiqc-picard-qualitycycle              | True        | qc-metrics, multiqc, picard-qualitycycle| janus        |
| multiqc, multiqc-picard-qualitydistr              | True        | qc-metrics, multiqc, picard-qualitydistr| janus        |
| multiqc, multiqc-peddy                            | True        | qc-metrics, multiqc, peddy              | janus        |
| multiqc, multiqc-picard-hs                        | True        | qc-metrics, multiqc, picard-hs          | janus        |
| multiqc, multiqc-picard-histogram*                | True        | qc-metrics, multiqc, picard-histogram   | janus        |
| multiqc, multiqc-picard-wgs                       | True        | qc-metrics, multiqc, picard-wgs         | janus        |
