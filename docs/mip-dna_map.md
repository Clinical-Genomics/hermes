| Mip-dna tags                        | Mandatory   | HK tags                          | Used by      |
|-------------------------------------|-------------|----------------------------------|--------------|
| chanjo_sexcheck                     | False       | chanjo, sex-check                | scout        |
| sites, chromograph_upd              | False       | chromograph, upd, sites          | scout        |
| chromograph_upd, regions            | False       | chromograph, upd, regions        | scout        |
| tcov, chromograph_cov               | False       | chromograph, tcov                | scout        |
| chromograph_rhoviz, autozyg         | False       | chromograph, autozyg             | scout        |
| chromograph_rhoviz, fracsnp         | False       | chromograph, fracsnp             | scout        |
| endvariantannotationblock, clinical | True        | vcf-snv-clinical                 | scout        |
| endvariantannotationblock, research | True        | vcf-snv-research                 | scout        |
| expansionhunter, sv_str             | False       | vcf-str                          | scout        |
| expansionhunter, str_variants       | False       | expansionhunter, vcf-str         | scout        |
| str_alignment, expansionhunter      | False       | expansionhunter, bam             | scout        |
| expansionhunter, variant_catalog    | False       | expansionhunter, variant-catalog | scout        |
| glnexus_merge                       | False       | deepvariant, snv, vcf            | storage      |
| markduplicates                      | False       | cram                             | scout        |
| gatk_combinevariantcallsets         | True        | snv-gbcf, snv-bcf                | genotype     |
| gens_generatedata, baf              | False       | gens, fracsnp, bed               | scout        |
| cov, gens_generatedata              | False       | gens, coverage, bed              | scout        |
| me_merge_vcfs                       | False       | retroseq, vcf                    | audit        |
| clinical, me_filter                 | False       | mobile-elements, clinical, vcf   | scout        |
| me_filter, research                 | False       | mobile-elements, research, vcf   | scout        |
| mip_analyse, config                 | True        | mip-analyse, config              | cg, audit    |
| mip_analyse, config_analysis        | True        | mip-config                       | cg, audit    |
| mip_analyse, log                    | True        | mip-log                          | audit        |
| mip_analyse, pedigree               | True        | pedigree-yaml                    | audit        |
| mip_analyse, pedigree_fam           | True        | pedigree                         | scout        |
| mip_analyse, references_info        | True        | mip-analyse, reference-info      | audit        |
| mip_analyse, sample_info            | True        | sample-info                      | cg, audit    |
| html, multiqc_ar                    | True        | multiqc-html                     | scout        |
| json, multiqc_ar                    | True        | multiqc-json                     | storage      |
| deepvariant                         | True        | deepvariant-report               | storage      |
| mitodel                             | False       | mitodel                          | scout        |
| ped_check, peddy_ar                 | True        | peddy, ped-check                 | audit, scout |
| peddy_ar, peddy                     | True        | peddy, ped                       | audit, scout |
| sex_check, peddy_ar                 | True        | peddy, sex-check                 | audit, scout |
| qccollect_ar, deliverable           | True        | qc-metrics, deliverable          | audit        |
| audit, qccollect_ar                 | True        | qc-metrics, audit                | audit        |
| rhocall_viz                         | False       | rhocall-viz                      | scout        |
| sambamba_depth, coverage            | True        | coverage, sambamba-depth         | chanjo       |
| samtools_subsample_mt               | False       | bam-mt                           | scout        |
| smncopynumbercaller                 | False       | smn-calling                      | scout        |
| star_caller                         | False       | cyrius                           | scout        |
| sv_combinevariantcallsets           | True        | sv-bcf                           | audit        |
| clinical, sv_reformat               | False       | vcf-sv-clinical                  | scout        |
| sv_reformat, research               | False       | vcf-sv-research                  | scout        |
| telomerecat_ar                      | False       | telomere-calling                 | scout        |
| tiddit_coverage                     | False       | tiddit-coverage, bigwig          | scout        |
| upd_ar, regions                     | False       | upd, regions                     | scout        |
| sites, upd_ar                       | False       | upd, sites                       | scout        |
| version_collect_ar                  | True        | exe-ver                          | audit        |
| vcf2cytosure_ar                     | False       | vcf2cytosure                     | scout        |
