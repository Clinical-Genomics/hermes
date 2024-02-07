| Mip-rna tags                   | Mandatory | HK tags                     | Used by   |
|--------------------------------|-----------|-----------------------------|-----------|
| mip_analyse, config            | True      | mip-analyse, config         | cg, audit |
| mip_analyse, config_analysis   | True      | mip-config                  | cg, audit |
| mip_analyse, log               | True      | mip-log                     | audit     |
| mip_analyse, pedigree          | True      | pedigree-yaml               | audit     |
| mip_analyse, references_info   | True      | mip-analyse, reference-info | audit     |
| mip_analyse, sample_info       | True      | sample-info                 | cg, audit |
| mip_analyse, pedigree_fam      | True      | pedigree                    | storage   |
| html, multiqc_ar               | True      | multiqc-html                | audit     |
| json, multiqc_ar               | True      | multiqc-json                | storage   |
| deliverable, qccollect_ar      | True      | qc-metrics, deliverable     | audit     |
| qccollect_ar, audit            | True      | qc-metrics, audit           | audit     |
| version_collect_ar             | True      | exe-ver                     | audit     |
| salmon_quant                   | True      | salmon-quant                | storage   |
| blobfish                       | False     | deseq2                      | storage   |
| star_fusion                    | False     | fusion, star-fusion         | storage   |
| arriba_ar                      | False     | fusion, arriba              | storage   |
| megafusion_ar                  | False     | fusion, vcf                 | storage   |
| svdb_merge_fusion              | False     | fusion, vcf                 | storage   |
| research, merge_fusion_reports | False     | fusion, research, pdf       | scout     |
| clinical, merge_fusion_reports | False     | fusion, pdf, clinical       | scout     |
| coverage, build_sj_tracks      | True      | coverage, bigwig            | scout     |
| junction, build_sj_tracks      | True      | junction, bed               | scout     |
| markduplicates                 | True      | cram                        | scout     |
| stringtie_ar                   | False     | stringtie, assembly         | storage   |
| gffcompare_ar                  | False     | gffcompare                  | storage   |
| gatk_asereadcounter            | True      | asereadcounter              | storage   |
| research, vcfparser_ar         | True      | vcf-snv-research            | storage   |
| vcfparser_ar, clinical         | True      | vcf-snv-clinical            | storage   |
