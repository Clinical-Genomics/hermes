| Nallo tags                                          | Mandatory   | HK tags                             | Used by                                     |
|-----------------------------------------------------|-------------|-------------------------------------|---------------------------------------------|
| alignment, alignment_haplotags                      | True        | bam, haplotags                      | scout, clinical-delivery, long-term-storage |
| alignment_haplotags_index, alignment                | True        | bam-index, haplotags                | scout, clinical-delivery, long-term-storage |
| summary_hap1, assembly                              | True        | hap1, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| summary_hap2, assembly                              | True        | hap2, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| assembly_aligned, assembly                          | True        | bam, assembly                       | clinical-delivery, long-term-storage        |
| assembly_aligned_index, assembly                    | True        | bam-index, assembly                 | clinical-delivery, long-term-storage        |
| methylation_pileup, hap1                            | True        | bed, hap1, modkit-pileup            | clinical-delivery, long-term-storage        |
| methylation_pileup, hap1_index                      | True        | bed-index, hap1, modkit-pileup      | clinical-delivery, long-term-storage        |
| methylation_pileup, hap2                            | True        | bed, hap2, modkit-pileup            | clinical-delivery, long-term-storage        |
| methylation_pileup, hap2_index                      | True        | bed-index, hap2, modkit-pileup      | clinical-delivery, long-term-storage        |
| methylation_pileup, ungrouped                       | True        | bed, ungrouped, modkit-pileup       | clinical-delivery, long-term-storage        |
| methylation_pileup, ungrouped_index                 | True        | bed-index, ungrouped, modkit-pileup | clinical-delivery, long-term-storage        |
| mosdepth_d4, qc_bam                                 | True        | coverage, d4                        | scout, clinical-delivery, long-term-storage |
| multiqc-html, multiqc                               | True        | multiqc-html                        | scout, clinical-delivery, long-term-storage |
| pedigree_fam, pedigree                              | True        | pedigree                            | clinical-delivery, scout, long-term-storage |
| relate_html, somalier                               | True        | somalier, relate-html               | clinical-delivery, scout, long-term-storage |
| relate_pairs, somalier                              | True        | somalier, relate-pairs              | scout, long-term-storage                    |
| relate_samples, somalier                            | True        | somalier, relate-samples            | scout, long-term-storage                    |
| deepvariant, report                                 | True        | deepvariant-report                  | clinical-delivery, long-term-storage        |
| paraphase                                           | True        | bam, paraphase                      | clinical-delivery, long-term-storage        |
| paraphase, paraphase_index                          | True        | bam-index, paraphase                | clinical-delivery, long-term-storage        |
| paraphase, json                                     | True        | paraphase, json                     | clinical-delivery, long-term-storage        |
| vcf, paraphase                                      | False       | paraphase, vcf                      | clinical-delivery, long-term-storage        |
| paraphase, vcf_index                                | False       | paraphase, vcf-index                | clinical-delivery, long-term-storage        |
| vcf_str, sorted_repeats                             | True        | repeats, sorted, vcf                | long-term-storage                           |
| vcf_str_index, sorted_repeats                       | True        | repeats, sorted, vcf-index          | long-term-storage                           |
| spanning_repeats, bam                               | True        | repeats, spanning, bam              | long-term-storage                           |
| spanning_repeats, bam_index                         | True        | repeats, spanning, bam-index        | long-term-storage                           |
| vcf_str, repeats_annotated                          | True        | vcf-str                             | scout, clinical-delivery, long-term-storage |
| vcf_str_index, repeats_annotated                    | True        | vcf-str-index                       | scout, clinical-delivery, long-term-storage |
| snv_annotated, vcf_snv_research                     | True        | vcf-snv-research                    | scout, clinical-delivery, long-term-storage |
| snv_annotated, vcf_snv_research_index               | True        | vcf-snv-research-index              | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical            | True        | vcf-snv-clinical                    | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical_index      | True        | vcf-snv-clinical-index              | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked, vcf_sv_research                | True        | vcf-sv-research                     | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked, vcf_sv_research_index          | True        | vcf-sv-research-index               | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical, sv_annotated_ranked_filtered       | True        | vcf-sv-clinical                     | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked_filtered, vcf_sv_clinical_index | True        | vcf-sv-clinical-index               | scout, clinical-delivery, long-term-storage |
| vcf_hificnv, svs_per_caller                         | True        | hificnv, vcf                        | long-term-storage                           |
| vcf_hificnv_index, svs_per_caller                   | True        | hificnv, vcf-index                  | long-term-storage                           |
| vcf_severus, svs_per_caller                         | True        | severus, vcf                        | long-term-storage                           |
| vcf_severus_index, svs_per_caller                   | True        | severus, vcf-index                  | long-term-storage                           |
| vcf_sniffles, svs_per_caller                        | True        | sniffles1, vcf                      | long-term-storage                           |
| vcf_sniffles_index, svs_per_caller                  | True        | sniffles1, vcf-index                | long-term-storage                           |
| bedgraph, copy_number                               | True        | cnv, bedgraph                       | clinical-delivery, long-term-storage        |
| bigwig, depth_track                                 | True        | hificnv, bigwig                     | clinical-delivery, long-term-storage        |
| maf_depth_track, bigwig                             | True        | hificnv, bigwig, maf                | clinical-delivery, long-term-storage        |
| multiqc-json, multiqc                               | True        | multiqc-json                        | long-term-storage                           |
| nextflow-params                                     | True        | nextflow-params                     | cg, long-term-storage                       |
| nextflow-config                                     | True        | nextflow-config                     | cg, long-term-storage                       |
| samplesheet                                         | True        | nextflow-samplesheet                | cg, long-term-storage                       |
| software-versions                                   | True        | software-versions                   | cg, clinical-delivery, long-term-storage    |
| qc-metrics                                          | True        | qc-metrics, deliverable             | cg, long-term-storage                       |
| manifest                                            | False       | manifest                            | scout, long-term-storage                    |