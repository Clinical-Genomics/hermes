| Mip-dna tags                        | Mandatory | HK tags                          | Used by      |
|-------------------------------------|-----------|----------------------------------|--------------|
| chanjo_sexcheck                     | False     | chanjo, sex-check                | scout        |
| sites, chromograph_upd              | False     | chromograph, upd, sites          | scout        |
| regions, chromograph_upd            | False     | chromograph, upd, regions        | scout        |
| tcov, chromograph_cov               | False     | chromograph, tcov                | scout        |
| autozyg, chromograph_rhoviz         | False     | chromograph, autozyg             | scout        |
| fracsnp, chromograph_rhoviz         | False     | chromograph, fracsnp             | scout        |
| clinical, endvariantannotationblock | True      | vcf-snv-clinical                 | scout        |
| research, endvariantannotationblock | True      | vcf-snv-research                 | scout        |
| sv_str, expansionhunter             | False     | vcf-str                          | scout        |
| str_variants, expansionhunter       | False     | expansionhunter, vcf-str         | scout        |
| str_alignment, expansionhunter      | False     | expansionhunter, bam             | scout        |
| variant_catalog, expansionhunter    | False     | expansionhunter, variant-catalog | scout        |
| glnexus_merge                       | False     | deepvariant, snv, vcf            | storage      |
| markduplicates                      | False     | cram                             | scout        |
| gatk_combinevariantcallsets         | True      | snv-gbcf, snv-bcf                | genotype     |
| gens_generatedata, baf              | False     | gens, fracsnp, bed               | scout        |
| gens_generatedata, cov              | False     | gens, coverage, bed              | scout        |
| me_merge_vcfs                       | False     | retroseq, vcf                    | audit        |
| clinical, me_filter                 | False     | mobile-elements, clinical, vcf   | scout        |
| research, me_filter                 | False     | mobile-elements, research, vcf   | scout        |
| mip_analyse, config                 | True      | mip-analyse, config              | cg, audit    |
| mip_analyse, config_analysis        | True      | mip-config                       | cg, audit    |
| mip_analyse, log                    | True      | mip-log                          | audit        |
| pedigree, mip_analyse               | True      | pedigree-yaml                    | audit        |
| pedigree_fam, mip_analyse           | True      | pedigree                         | scout        |
| mip_analyse, references_info        | True      | mip-analyse, reference-info      | audit        |
| sample_info, mip_analyse            | True      | sample-info                      | cg, audit    |
| html, multiqc_ar                    | True      | multiqc-html                     | scout        |
| json, multiqc_ar                    | True      | multiqc-json                     | storage      |
| mitodel                             | False     | mitodel                          | scout        |
| peddy_ar, ped_check                 | True      | peddy, ped-check                 | audit, scout |
| peddy_ar, peddy                     | True      | peddy, ped                       | audit, scout |
| peddy_ar, sex_check                 | True      | peddy, sex-check                 | audit, scout |
| qccollect_ar, deliverable           | True      | qc-metrics, deliverable          | audit        |
| qccollect_ar, audit                 | True      | qc-metrics, audit                | audit        |
| rhocall_viz                         | False     | rhocall-viz                      | scout        |
| sambamba_depth, coverage            | True      | coverage, sambamba-depth         | chanjo       |
| samtools_subsample_mt               | False     | bam-mt                           | scout        |
| smncopynumbercaller                 | False     | smn-calling                      | scout        |
| star_caller                         | False     | cyrius                           | scout        |
| sv_combinevariantcallsets           | True      | sv-bcf                           | audit        |
| sv_reformat, clinical               | False     | vcf-sv-clinical                  | scout        |
| sv_reformat, research               | False     | vcf-sv-research                  | scout        |
| telomerecat_ar                      | False     | telomere-calling                 | scout        |
| tiddit_coverage                     | False     | tiddit-coverage, bigwig          | scout        |
| regions, upd_ar                     | False     | upd, regions                     | scout        |
| sites, upd_ar                       | False     | upd, sites                       | scout        |
| version_collect_ar                  | True      | exe-ver                          | audit        |
| vcf2cytosure_ar                     | False     | vcf2cytosure                     | scout        |
