| Mip tags                            | Mandatory   | HK tags                     | Used by      |
|-------------------------------------|-------------|-----------------------------|--------------|
| chanjo_sexcheck                     | False       | chanjo, sex-check           | scout        |
| sites, chromograph_upd              | False       | chromograph, upd, sites     | scout        |
| regions, chromograph_upd            | False       | chromograph, upd, regions   | scout        |
| chromograph_cov, tcov               | False       | chromograph, tcov           | scout        |
| clinical, endvariantannotationblock | True        | vcf-snv-clinical            | scout        |
| research, endvariantannotationblock | True        | vcf-snv-research            | scout        |
| sv_str, expansionhunter             | False       | vcf-str                     | scout        |
| gatk_baserecalibration              | False       | cram                        | scout        |
| gatk_combinevariantcallsets         | True        | snv-gbcf, snv-bcf           | genotype     |
| config, mip_analyse                 | True        | mip-analyse, config         | cg, audit    |
| config_analysis, mip_analyse        | True        | mip-config                  | cg, audit    |
| log, mip_analyse                    | True        | mip-log                     | audit        |
| pedigree, mip_analyse               | True        | pedigree-yaml               | audit        |
| pedigree_fam, mip_analyse           | True        | pedigree                    | scout        |
| references_info, mip_analyse        | True        | mip-analyse, reference-info | audit        |
| sample_info, mip_analyse            | True        | sample-info                 | cg, audit    |
| html, multiqc_ar                    | True        | multiqc-html                | scout        |
| json, multiqc_ar                    | True        | multiqc-json                | vogue        |
| peddy_ar, ped_check                 | True        | peddy, ped-check            | audit, scout |
| peddy, peddy_ar                     | True        | peddy, ped                  | audit, scout |
| sex_check, peddy_ar                 | True        | peddy, sex-check            | audit, scout |
| qccollect_ar                        | True        | qc-metrics                  | audit        |
| rhocall_viz                         | False       | rhocall-viz                 | scout        |
| coverage, sambamba_depth            | True        | coverage, sambamba-depth    | chanjo       |
| samtools_subsample_mt               | False       | bam-mt                      | scout        |
| smncopynumbercaller                 | False       | smn-calling                 | scout        |
| star_caller                         | False       | cyrius                      | scout        |
| sv_combinevariantcallsets           | True        | sv-bcf                      | audit        |
| clinical, sv_reformat               | False       | vcf-sv-clinical             | scout        |
| research, sv_reformat               | False       | vcf-sv-research             | scout        |
| telomerecat_ar                      | False       | telomere-calling            | scout        |
| tiddit_coverage                     | False       | tiddit-coverage, bigwig     | scout        |
| upd_ar, regions                     | False       | upd, regions                | scout        |
| sites, upd_ar                       | False       | upd, sites                  | scout        |
| version_collect_ar                  | True        | exe-ver                     | audit        |
| vcf2cytosure_ar                     | False       | vcf2cytosure                | scout        |
