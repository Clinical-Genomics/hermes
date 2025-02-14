| Nallo tags                                          | Mandatory   | HK tags                             | Used by                                     |
|-----------------------------------------------------|-------------|-------------------------------------|---------------------------------------------|
| alignment_haplotags, alignment                      | True        | bam, haplotags                      | scout, clinical-delivery, long-term-storage |
| alignment, alignment_haplotags_index                | True        | bam-index, haplotags                | scout, clinical-delivery, long-term-storage |
| assembly, summary_hap1                              | True        | hap1, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| summary_hap2, assembly                              | True        | hap2, assembly, assembly-summary    | clinical-delivery, long-term-storage        |
| assembly, assembly_hap1_mapped                      | True        | bed, hap1, modkit-pileup            | clinical-delivery, long-term-storage        |
| assembly, assembly_hap1_mapped_index                | True        | bed-index, hap1, modkit-pileup      | clinical-delivery, long-term-storage        |
| assembly_hap2_mapped, assembly                      | True        | bam, hap2, assembly                 | clinical-delivery, long-term-storage        |
| assembly, assembly_hap2_mapped_index                | True        | bam-index, hap2, assembly           | clinical-delivery, long-term-storage        |
| summary_counts, hap1                                | True        | bed, hap1, modkit-pileup            | clinical-delivery, long-term-storage        |
| hap1_index, summary_counts                          | True        | bed-index, hap1, modkit-pileup      | clinical-delivery, long-term-storage        |
| summary_counts, hap2                                | True        | bed, hap2, modkit-pileup            | clinical-delivery, long-term-storage        |
| summary_counts, hap2_index                          | True        | bed-index, hap2, modkit-pileup      | clinical-delivery, long-term-storage        |
| summary_counts, ungrouped                           | True        | bed, ungrouped, modkit-pileup       | clinical-delivery, long-term-storage        |
| ungrouped_index, summary_counts                     | True        | bed-index, ungrouped, modkit-pileup | clinical-delivery, long-term-storage        |
| mosdepth_d4, qc_bam                                 | True        | coverage, d4                        | scout, clinical-delivery, long-term-storage |
| multiqc-html, multiqc                               | True        | multiqc-html                        | scout, clinical-delivery, long-term-storage |
| multiqc, multiqc-json                               | True        | multiqc-json                        | long-term-storage                           |
| pedigree_fam, pedigree                              | True        | pedigree                            | clinical-delivery, scout, long-term-storage |
| relate_html, somalier                               | True        | somalier, relate-html               | clinical-delivery, scout, long-term-storage |
| somalier, relate_pairs                              | True        | somalier, relate-pairs              | scout, long-term-storage                    |
| somalier, relate_samples                            | True        | somalier, relate-samples            | scout, long-term-storage                    |
| deepvariant, report                                 | True        | deepvariant-report                  | clinical-delivery, long-term-storage        |
| paraphase                                           | True        | bam, paraphase                      | clinical-delivery, long-term-storage        |
| paraphase_index, paraphase                          | True        | bam-index, paraphase                | clinical-delivery, long-term-storage        |
| json, paraphase                                     | True        | paraphase, json                     | clinical-delivery, long-term-storage        |
| vcf, paraphase                                      | False       | bam-index, paraphase, vcf           | clinical-delivery, long-term-storage        |
| vcf_index, paraphase                                | False       | bam-index, paraphase, vcf-index     | clinical-delivery, long-term-storage        |
| sorted_repeats, vcf_str                             | True        | repeats, sorted, vcf                | long-term-storage                           |
| sorted_repeats, vcf_str_index                       | True        | repeats, sorted, vcf-index          | long-term-storage                           |
| bam, spanning_repeats                               | True        | repeats, spanning, bam              | long-term-storage                           |
| bam_index, spanning_repeats                         | True        | repeats, spanning, bam-index        | long-term-storage                           |
| repeats_annotated, vcf_str                          | True        | vcf-str                             | scout, clinical-delivery, long-term-storage |
| repeats_annotated, vcf_str_index                    | True        | vcf-str-index                       | scout, clinical-delivery, long-term-storage |
| vcf_snv_research, snv_annotated                     | True        | vcf-snv-research                    | scout, clinical-delivery, long-term-storage |
| vcf_snv_research_index, snv_annotated               | True        | vcf-snv-research-index              | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical            | True        | vcf-snv-clinical                    | scout, clinical-delivery, long-term-storage |
| snv_annotated_filtered, vcf_snv_clinical_index      | True        | vcf-snv-clinical-index              | scout, clinical-delivery, long-term-storage |
| vcf_sv_research, sv_annotated_ranked                | True        | vcf-sv-research                     | scout, clinical-delivery, long-term-storage |
| sv_annotated_ranked, vcf_sv_research_index          | True        | vcf-sv-research-index               | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical, sv_annotated_ranked_filtered       | True        | vcf-sv-clinical                     | scout, clinical-delivery, long-term-storage |
| vcf_sv_clinical_index, sv_annotated_ranked_filtered | True        | vcf-sv-clinical-index               | scout, clinical-delivery, long-term-storage |
| copy_number, bedgraph                               | True        | cnv, bedgraph                       | clinical-delivery, long-term-storage        |
| bigwig, depth_track                                 | True        | hificnv, bigwig                     | clinical-delivery, long-term-storage        |
| bigwig, maf_depth_track                             | True        | hificnv, bigwig, maf                | clinical-delivery, long-term-storage        |
| nextflow-params                                     | True        | nextflow-params                     | cg, long-term-storage                       |
| nextflow-config                                     | True        | nextflow-config                     | cg, long-term-storage                       |
| samplesheet                                         | True        | nextflow-samplesheet                | cg, long-term-storage                       |
| software-versions                                   | True        | software-versions                   | cg, clinical-delivery, long-term-storage    |
| qc-metrics                                          | True        | qc-metrics, deliverable             | cg, long-term-storage                       |
| manifest                                            | False       | manifest                            | scout, long-term-storage                    |