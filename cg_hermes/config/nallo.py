"""Tags that are defined in deliverables file mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However, the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS
from cg_hermes.constants.tags import (
    AlignmentTags,
    AnalysisTags,
    BioinfoToolsTags,
    FamilyTags,
    MipTags,
    NextflowTags,
    QCTags,
    NalloTags,
    ReportTags,
    VariantTags,
    UsageTags,
)

NALLO_COMMON_TAGS = {
    frozenset(["alignment", "alignment_haplotags"]): {
        "tags": [AlignmentTags.BAM, NalloTags.HAPLOTAGS],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["alignment", "alignment_haplotags_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.HAPLOTAGS],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "summary_hap1"]): {
        "tags": [NalloTags.HAP1, NalloTags.ASSEMBLY, NalloTags.ASSEMBLY_SUMMARY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "summary_hap2"]): {
        "tags": [NalloTags.HAP2, NalloTags.ASSEMBLY, NalloTags.ASSEMBLY_SUMMARY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap1_mapped"]): {
        "tags": [AlignmentTags.BAM, NalloTags.HAP1, NalloTags.ASSEMBLY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap1_mapped_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.HAP1, NalloTags.ASSEMBLY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap2_mapped"]): {
        "tags": [AlignmentTags.BAM, NalloTags.HAP2, NalloTags.ASSEMBLY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap2_mapped_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.HAP2, NalloTags.ASSEMBLY],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap1_mapped"]): {
        "tags": [AnalysisTags.BED, NalloTags.HAP1, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["assembly", "assembly_hap1_mapped_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.HAP1, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "hap1"]): {
        "tags": [AnalysisTags.BED, NalloTags.HAP1, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "hap1_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.HAP1, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "hap2"]): {
        "tags": [AnalysisTags.BED, NalloTags.HAP2, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "hap2_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.HAP2, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "ungrouped"]): {
        "tags": [AnalysisTags.BED, NalloTags.UNGROUPED, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["summary_counts", "ungrouped_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.UNGROUPED, NalloTags.MODKIT_PILEUP],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["qc_bam", "mosdepth_d4"]): {
        "tags": [AnalysisTags.COVERAGE, ReportTags.D4],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset({"multiqc", "multiqc-html"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_HTML],
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-json"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_JSON],
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["pedigree", "pedigree_fam"]): {
        "tags": [FamilyTags.PEDIGREE],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["somalier", "relate_html"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_HTML],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["somalier", "relate_pairs"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_PAIRS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["somalier", "relate_pairs"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_PAIRS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["somalier", "relate_samples"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_SAMPLES],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["deepvariant", "report"]): {
        "tags": [NalloTags.DEEPVARIANT_REPORT],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["paraphase", "paraphase"]): {
        "tags": [AlignmentTags.BAM, NalloTags.PARAPHASE],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["paraphase", "paraphase_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.PARAPHASE],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["paraphase", "json"]): {
        "tags": [NalloTags.PARAPHASE, ReportTags.JSON],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["paraphase", "vcf"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.PARAPHASE, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["paraphase", "vcf_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.PARAPHASE, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sorted_repeats", "vcf_str"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SORTED, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sorted_repeats", "vcf_str_index"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SORTED, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["spanning_repeats", "bam"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SPANNING, AlignmentTags.BAM],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["spanning_repeats", "bam_index"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SPANNING, AlignmentTags.BAM_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["repeats_annotated", "vcf_str"]): {
        "tags": [NalloTags.REPEATS, VariantTags.VCF_STR],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["repeats_annotated", "vcf_str_index"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SORTED, VariantTags.VCF_STR_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["snv_annotated", "vcf_snv_research"]): {
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF_SNV, ],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["repeats_annotated", "vcf_snv_research_index"]): {
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF_SNV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["snv_annotated_filtered", "vcf_snv_clinical"]): {
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF_SNV, ],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["snv_annotated_filtered", "vcf_snv_clinical_index"]): {
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF_SNV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sv_annotated_ranked", "vcf_sv_research"]): {
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF_SV, ],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sv_annotated_ranked", "vcf_sv_research_index"]): {
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF_SV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sv_annotated_ranked_filtered", "vcf_sv_clinical"]): {
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF_SV, ],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["sv_annotated_ranked_filtered", "vcf_sv_clinical_index"]): {
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF_SV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["qc_bam", "mosdepth_d4"]): {
        "tags": [AnalysisTags.COVERAGE, ReportTags.D4],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["copy_number", "bedgraph"]): {
        "tags": [VariantTags.CNV, NalloTags.BEDGRAPH],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["depth_track", "bigwig"]): {
        "tags": [NalloTags.HIFICNV, AnalysisTags.BIGWIG],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["maf_depth_track", "bigwig"]): {
        "tags": [NalloTags.HIFICNV, AnalysisTags.BIGWIG, NalloTags.MAF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset({"nextflow-params"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.NEXTFLOW_PARAMS],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"nextflow-config"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.NEXTFLOW_CONFIG],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"samplesheet"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.SAMPLESHEET],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
}

NALLO_TAGS = {**NALLO_COMMON_TAGS, **NEXTFLOW_TAGS}
