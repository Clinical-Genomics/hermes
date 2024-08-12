| Mip-rna tags                   | Mandatory   | HK tags                     | Used by   |
|--------------------------------|-------------|-----------------------------|-----------|
| config, mip_analyse            | True        | mip-analyse, config         | cg, audit |
| config_analysis, mip_analyse   | True        | mip-config                  | cg, audit |
| log, mip_analyse               | True        | mip-log                     | audit     |
| pedigree, mip_analyse          | True        | pedigree-yaml               | audit     |
| references_info, mip_analyse   | True        | mip-analyse, reference-info | audit     |
| sample_info, mip_analyse       | True        | sample-info                 | cg, audit |
| pedigree_fam, mip_analyse      | True        | pedigree                    | storage   |
| multiqc_ar, html               | True        | multiqc-html                | audit     |
| multiqc_ar, json               | True        | multiqc-json                | storage   |
| qccollect_ar, deliverable      | True        | qc-metrics, deliverable     | audit     |
| qccollect_ar, audit            | True        | qc-metrics, audit           | audit     |
| version_collect_ar             | True        | exe-ver                     | audit     |
| salmon_quant                   | True        | salmon-quant                | storage   |
| blobfish                       | False       | deseq2                      | storage   |
| star_fusion                    | False       | fusion, star-fusion         | storage   |
| arriba_ar                      | False       | fusion, arriba              | storage   |
| megafusion_ar                  | False       | fusion, vcf                 | storage   |
| svdb_merge_fusion              | False       | fusion, vcf                 | storage   |
| research, merge_fusion_reports | False       | fusion, research, pdf       | scout     |
| clinical, merge_fusion_reports | False       | fusion, pdf, clinical       | scout     |
| coverage, build_sj_tracks      | True        | coverage, bigwig            | scout     |
| junction, build_sj_tracks      | True        | junction, bed               | scout     |
| markduplicates                 | True        | cram                        | scout     |
| stringtie_ar                   | False       | stringtie, assembly         | storage   |
| gffcompare_ar                  | False       | gffcompare                  | storage   |
| gatk_asereadcounter            | True        | asereadcounter              | storage   |
| research, vcfparser_ar         | True        | vcf-snv-research            | storage   |
| clinical, vcfparser_ar         | True        | vcf-snv-clinical            | storage   |
