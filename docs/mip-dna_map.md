| Mip-dna tags                        | Mandatory   | HK tags                     | Used by      |
|-------------------------------------|-------------|-----------------------------|--------------|
| chanjo_sexcheck                     | False       | chanjo, sex-check           | scout        |
| chromograph_cov, tcov               | False       | chromograph, tcov           | scout        |
| clinical, endvariantannotationblock | True        | vcf-snv-clinical            | scout        |
| clinical, sv_reformat               | False       | vcf-sv-clinical             | scout        |
| config, mip_analyse                 | True        | mip-analyse, config         | cg, audit    |
| config_analysis, mip_analyse        | True        | mip-config                  | cg, audit    |
| coverage, sambamba_depth            | True        | coverage, sambamba-depth    | chanjo       |
| expansionhunter, str_alignments     | False       | expansionhunter, bam        | scout        |
| expansionhunter, str_variants       | False       | expansionhunter, vcf-str    | scout        |
| expansionhunter, variant_catalog    | False       | expansionhunter, variant-catalog    | scout        |
| gatk_baserecalibration              | False       | cram                        | scout        |
| gatk_combinevariantcallsets         | True        | snv-gbcf, snv-bcf           | genotype     |
| gens_generatedata, baf              | False       | gens, fracsnp               | scout        |
| gens_generatedata, cov              | False       | gens, coverage              | scout        |
| glnexus_merge                       | False       | deepvariant, snv, vcf       | storage      |
| html, multiqc_ar                    | True        | multiqc-html                | scout        |
| json, multiqc_ar                    | True        | multiqc-json                | vogue        |
| log, mip_analyse                    | True        | mip-log                     | audit        |
| mitodel                             | False       | mitodel                     | scout        |
| peddy, peddy_ar                     | True        | peddy, ped                  | audit, scout |
| peddy_ar, ped_check                 | True        | peddy, ped-check            | audit, scout |
| pedigree, mip_analyse               | True        | pedigree-yaml               | audit        |
| pedigree_fam, mip_analyse           | True        | pedigree                    | scout        |
| qccollect_ar, audit                 | True        | qc-metrics, audit           | audit        |
| qccollect_ar, deliverable           | True        | qc-metrics, deliverable    | audit        |
| references_info, mip_analyse        | True        | mip-analyse, reference-info | audit        |
| regions, chromograph_upd            | False       | chromograph, upd, regions   | scout        |
| research, endvariantannotationblock | True        | vcf-snv-research            | scout        |
| research, sv_reformat               | False       | vcf-sv-research             | scout        |
| rhocall_viz                         | False       | rhocall-viz                 | scout        |
| sample_info, mip_analyse            | True        | sample-info                 | cg, audit    |
| samtools_subsample_mt               | False       | bam-mt                      | scout        |
| sex_check, peddy_ar                 | True        | peddy, sex-check            | audit, scout |
| sites, chromograph_upd              | False       | chromograph, upd, sites     | scout        |
| sites, upd_ar                       | False       | upd, sites                  | scout        |
| smncopynumbercaller                 | False       | smn-calling                 | scout        |
| star_caller                         | False       | cyrius                      | scout        |
| sv_combinevariantcallsets           | True        | sv-bcf                      | audit        |
| sv_str, expansionhunter             | False       | vcf-str                     | scout        |
| telomerecat_ar                      | False       | telomere-calling            | scout        |
| tiddit_coverage                     | False       | tiddit-coverage, bigwig     | scout        |
| upd_ar, regions                     | False       | upd, regions                | scout        |
| vcf2cytosure_ar                     | False       | vcf2cytosure                | scout        |
| version_collect_ar                  | True        | exe-ver                     | audit        |
