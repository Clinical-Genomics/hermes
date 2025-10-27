| Nallo tags                                          | Mandatory   | HK tags                             | Used by                                     |
|-----------------------------------------------------|-------------|-------------------------------------|---------------------------------------------|
| alignment_haplotags, alignment                      | True        | bam, haplotags                      | scout, clinical-delivery, long-term-storage |
| alignment_haplotags_index, alignment                | True        | bam-index, haplotags                | scout, clinical-delivery, long-term-storage |
| assembly, summary_hap1                              | True        | hap1, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| summary_hap2, assembly                              | True        | hap2, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| assembly_aligned, assembly                          | True        | bam, assembly                       | clinical-delivery, long-term-storage        |
| assembly, assembly_aligned_index                    | True        | bam-index, assembly                 | clinical-delivery, long-term-storage        |
| hap1, methylation_pileup                            | True        | bed, hap1, modkit-pileup            | clinical-delivery, long-term-storage        |
| hap1_index, methylation_pileup                      | True        | bed-index, hap1, modkit-pileup      | clinical-delivery, long-term-storage        |
| hap2, methylation_pileup                            | True        | bed, hap2, modkit-pileup            | clinical-delivery, long-term-storage        |
| hap2_index, methylation_pileup                      | True        | bed-index, hap2, modkit-pileup      | clinical-delivery, long-term-storage        |
| methylation_pileup, ungrouped                       | True        | bed, ungrouped, modkit-pileup       | clinical-delivery, long-term-storage        |
| ungrouped_index, methylation_pileup                 | True        | bed-index, ungrouped, modkit-pileup | clinical-delivery, long-term-storage        |
| mosdepth_d4, qc_bam                                 | True        | coverage, d4                        | scout, clinical-delivery, long-term-storage |
| multiqc-html, multiqc                               | True        | multiqc-html                        | scout, clinical-delivery, long-term-storage |
| pedigree_fam, pedigree                              | True        | pedigree                            | clinical-delivery, scout, long-term-storage |
| relate_html, somalier                               | True        | somalier, relate-html               | clinical-delivery, scout, long-term-storage |
| relate_pairs, somalier                              | True        | somalier, relate-pairs              | scout, long-term-storage                    |
| relate_samples, somalier                            | True        | somalier, relate-samples            | scout, long-term-storage                    |
| peddy                                               | True        | peddy, ped                          | audit, scout, clinical-delivery             |
| ped_check, peddy                                    | True        | peddy, ped-check                    | audit, scout, clinical-delivery             |
| peddy, sex_check                                    | True        | peddy, sex-check                    | audit, scout, clinical-delivery             |
| deepvariant, report                                 | True        | deepvariant-report                  | clinical-delivery, long-term-storage        |
| paraphase                                           | True        | bam, paraphase                      | clinical-delivery, long-term-storage        |
| paraphase_index, paraphase                          | True        | bam-index, paraphase                | clinical-delivery, long-term-storage        |
| json, paraphase                                     | True        | paraphase, json                     | clinical-delivery, long-term-storage        |
| vcf, paraphase                                      | False       | paraphase, vcf                      | clinical-delivery, long-term-storage        |
| vcf_index, paraphase                                | False       | paraphase, vcf-index                | clinical-delivery, long-term-storage        |
| sorted_repeats, vcf_str                             | True        | repeats, sorted, vcf                | long-term-storage                           |
| sorted_repeats, vcf_str_index                       | True        | repeats, sorted, vcf-index          | long-term-storage                           |
| spanning_repeats, bam                               | True        | repeats, spanning, bam              | long-term-storage                           |
| spanning_repeats, bam_index                         | True        | repeats, spanning, bam-index        | long-term-storage                           |
| repeats_annotated, vcf_str                          | True        | vcf-str                             | scout, clinical-delivery, long-term-storage |
| repeats_annotated, vcf_str_index                    | True        | vcf-str-index                       | scout, clinical-delivery, long-term-storage |
| vcf_snv_research, snv_annotated                     | True        | vcf-snv-research                    | scout, clinical-delivery, long-term-storage |
| vcf_snv_research_index, snv_annotated               | True        | vcf-snv-research-index              | scout, clinical-delivery, long-term-storage |
| vcf_snv_clinical, snv_annotated_filtered            | True        | vcf-snv-clinical                    | scout, clinical-delivery, long-term-storage |
| vcf_snv_clinical_index, snv_annotated_filtered      | True        | vcf-snv-clinical-index              | scout, clinical-delivery, long-term-storage |
| vcf_sv_research, sv_annotated_ranked                | True        | vcf-sv-research                     | scout, clinical-delivery, long-term-storage |
| vcf_sv_research_index, sv_annotated_ranked          | True        | vcf-sv-research-index               | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical, sv_annotated_ranked_filtered       | True        | vcf-sv-clinical                     | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical_index, sv_annotated_ranked_filtered | True        | vcf-sv-clinical-index               | scout, clinical-delivery, long-term-storage |
| svs_per_caller, vcf_hificnv                         | True        | hificnv, vcf                        | long-term-storage                           |
| svs_per_caller, vcf_hificnv_index                   | True        | hificnv, vcf-index                  | long-term-storage                           |
| svs_per_caller, vcf_severus                         | True        | severus, vcf                        | long-term-storage                           |
| svs_per_caller, vcf_severus_index                   | True        | severus, vcf-index                  | long-term-storage                           |
| svs_per_caller, vcf_sniffles                        | True        | sniffles1, vcf                      | long-term-storage                           |
| svs_per_caller, vcf_sniffles_index                  | True        | sniffles1, vcf-index                | long-term-storage                           |
| copy_number, bedgraph                               | True        | cnv, bedgraph                       | clinical-delivery, long-term-storage        |
| depth_track, bigwig                                 | True        | hificnv, bigwig                     | clinical-delivery, long-term-storage        |
| maf_depth_track, bigwig                             | True        | hificnv, bigwig, maf                | clinical-delivery, long-term-storage        |
| multiqc-json, multiqc                               | True        | multiqc-json                        | long-term-storage                           |
| nextflow-params                                     | True        | nextflow-params                     | cg, long-term-storage                       |
| nextflow-config                                     | True        | nextflow-config                     | cg, long-term-storage                       |
| samplesheet                                         | True        | nextflow-samplesheet                | cg, long-term-storage                       |
| software-versions                                   | True        | software-versions                   | cg, clinical-delivery, long-term-storage    |
| qc-metrics                                          | True        | qc-metrics, deliverable             | cg, long-term-storage                       |
| whatshap, gtf                                       | True        | bam, paraphase                      | scout, clinical-delivery, long-term-storage |
| whatshap, gtf_index                                 | True        | bam, paraphase                      | scout, clinical-delivery, long-term-storage |
| manifest                                            | False       | manifest                            | scout, long-term-storage                    |
