| Mip-rna tags                            | Mandatory   | HK tags                     | Used by      |
|-------------------------------------|-------------|-----------------------------|--------------|
| arriba_ar                           | True        | fusion, arriba              | storage      |
| blobfish                            | False       | deseq2                      | storage      |
| build_sj_tracks, coverage           | True        | bigwig, coverage            | scout        |
| build_sj_tracks, junction           | True        | bed, junction               | scout        |
| config, mip_analyse                 | True        | mip-analyse, config         | cg, audit    |
| config_analysis, mip_analyse        | True        | mip-config                  | cg, audit    |
| gatk_asereadcounter                 | True        | asereadcounter              | storage      |
| html, multiqc_ar                    | True        | multiqc-html                | scout        |
| json, multiqc_ar                    | True        | multiqc-json                | vogue        |
| log, mip_analyse                    | True        | mip-log                     | audit        |
| markduplicates                      | True        | cram                        | storage      |
| megafusion_ar                       | True        | fusion, vcf                 | storage      |
| merege_fusion_reports, clinical     | True        | fusion, pdf, clinical       | scout        |
| merege_fusion_reports, research     | True        | fusion, pdf, research       | scout        |
| pedigree, mip_analyse               | True        | pedigree-yaml               | audit        |
| pedigree_fam, mip_analyse           | True        | pedigree                    | scout        |
| qccollect_ar, deliverable           | True        | qc-metrics, deliverables    | audit        |
| qccollect_ar, audit                 | True        | qc-metrics, audit           | audit        |
| references_info, mip_analyse        | True        | mip-analyse, reference-info | audit        |
| salmon_quant                        | True        | salmon-quant                | storage      |
| sample_info, mip_analyse            | True        | sample-info                 | cg, audit    |
| star_fusion                         | True        | fusion, star-fusion         | storage      |
| stringtie_ar                        | True        | assembly, stringtie         | storage      |
| svdb_merge_fusion                   | True        | fusion, vcf                 | storage      |
| vcfparser_ar, clinical              | True        | vcf-snv-clinical            | storage      |
| vcfparser_ar, research              | True        | vcf-snv-research            | storage      |
| version_collect_ar                  | True        | exe-ver                     | audit        |
