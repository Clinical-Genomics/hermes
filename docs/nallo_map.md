| Nallo tags                                          | Mandatory   | HK tags                             | Used by                                     |
|-----------------------------------------------------|-------------|-------------------------------------|---------------------------------------------|
| alignment, alignment_haplotags                      | True        | bam, haplotags                      | scout, clinical-delivery, long-term-storage |
| alignment, alignment_haplotags_index                | True        | bam-index, haplotags                | scout, clinical-delivery, long-term-storage |
| summary_hap1, assembly                              | True        | hap1, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| summary_hap2, assembly                              | True        | hap2, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| assembly_aligned, assembly                          | True        | bam, assembly                       | clinical-delivery, long-term-storage        |
| assembly_aligned_index, assembly                    | True        | bam-index, assembly                 | clinical-delivery, long-term-storage        |
| hap1, methylation_pileup                            | True        | bed, hap1, modkit-pileup            | clinical-delivery, long-term-storage        |
| methylation_pileup, hap1_index                      | True        | bed-index, hap1, modkit-pileup      | clinical-delivery, long-term-storage        |
| methylation_pileup, hap2                            | True        | bed, hap2, modkit-pileup            | clinical-delivery, long-term-storage        |
| methylation_pileup, hap2_index                      | True        | bed-index, hap2, modkit-pileup      | clinical-delivery, long-term-storage        |
| ungrouped, methylation_pileup                       | True        | bed, ungrouped, modkit-pileup       | clinical-delivery, long-term-storage        |
| ungrouped_index, methylation_pileup                 | True        | bed-index, ungrouped, modkit-pileup | clinical-delivery, long-term-storage        |
| qc_bam, mosdepth_d4                                 | True        | coverage, d4                        | scout, clinical-delivery, long-term-storage |
| multiqc, multiqc-html                               | True        | multiqc-html                        | scout, clinical-delivery, long-term-storage |
| pedigree, pedigree_fam                              | True        | pedigree                            | clinical-delivery, scout, long-term-storage |
| somalier, relate_html                               | True        | somalier, relate-html               | clinical-delivery, scout, long-term-storage |
| somalier, relate_pairs                              | True        | somalier, relate-pairs              | scout, long-term-storage                    |
| somalier, relate_samples                            | True        | somalier, relate-samples            | scout, long-term-storage                    |
| report, deepvariant                                 | True        | deepvariant-report                  | clinical-delivery, long-term-storage        |
| paraphase                                           | True        | bam, paraphase                      | clinical-delivery, long-term-storage        |
| paraphase_index, paraphase                          | True        | bam-index, paraphase                | clinical-delivery, long-term-storage        |
| json, paraphase                                     | True        | paraphase, json                     | clinical-delivery, long-term-storage        |
| vcf, paraphase                                      | False       | paraphase, vcf                      | clinical-delivery, long-term-storage        |
| vcf_index, paraphase                                | False       | paraphase, vcf-index                | clinical-delivery, long-term-storage        |
| sorted_repeats, vcf_str                             | True        | repeats, sorted, vcf                | long-term-storage                           |
| vcf_str_index, sorted_repeats                       | True        | repeats, sorted, vcf-index          | long-term-storage                           |
| bam, spanning_repeats                               | True        | repeats, spanning, bam              | long-term-storage                           |
| spanning_repeats, bam_index                         | True        | repeats, spanning, bam-index        | long-term-storage                           |
| vcf_str, repeats_annotated                          | True        | vcf-str                             | scout, clinical-delivery, long-term-storage |
| vcf_str_index, repeats_annotated                    | True        | vcf-str-index                       | scout, clinical-delivery, long-term-storage |
| snv_annotated, vcf_snv_research                     | True        | vcf-snv-research                    | scout, clinical-delivery, long-term-storage |
| snv_annotated, vcf_snv_research_index               | True        | vcf-snv-research-index              | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical            | True        | vcf-snv-clinical                    | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical_index      | True        | vcf-snv-clinical-index              | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked, vcf_sv_research                | True        | vcf-sv-research                     | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked, vcf_sv_research_index          | True        | vcf-sv-research-index               | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked_filtered, vcf_sv_clinical       | True        | vcf-sv-clinical                     | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical_index, sv_annotated_ranked_filtered | True        | vcf-sv-clinical-index               | scout, clinical-delivery, long-term-storage |
| bedgraph, copy_number                               | True        | cnv, bedgraph                       | clinical-delivery, long-term-storage        |
| depth_track, bigwig                                 | True        | hificnv, bigwig                     | clinical-delivery, long-term-storage        |
| bigwig, maf_depth_track                             | True        | hificnv, bigwig, maf                | clinical-delivery, long-term-storage        |
| multiqc, multiqc-json                               | True        | multiqc-json                        | long-term-storage                           |
| nextflow-params                                     | True        | nextflow-params                     | cg, long-term-storage                       |
| nextflow-config                                     | True        | nextflow-config                     | cg, long-term-storage                       |
| samplesheet                                         | True        | nextflow-samplesheet                | cg, long-term-storage                       |
| software-versions                                   | True        | software-versions                   | cg, clinical-delivery, long-term-storage    |
| qc-metrics                                          | True        | qc-metrics, deliverable             | cg, long-term-storage                       |
| manifest                                            | False       | manifest                            | scout, long-term-storage                    |