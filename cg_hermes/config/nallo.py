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
    NextflowTags,
    NalloTags,
    QCTags,
    ReportTags,
    VariantTags,
    UsageTags,
)

NALLO_COMMON_TAGS = {
    frozenset(["alignment", "alignment_haplotags"]): {
        "tags": [AlignmentTags.BAM, NalloTags.HAPLOTAGS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["alignment", "alignment_haplotags_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.HAPLOTAGS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["assembly", "summary_hap1"]): {
        "tags": [NalloTags.HAP1, NalloTags.ASSEMBLY, NalloTags.ASSEMBLY_SUMMARY],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["assembly", "summary_hap2"]): {
        "tags": [NalloTags.HAP2, NalloTags.ASSEMBLY, NalloTags.ASSEMBLY_SUMMARY],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["assembly", "assembly_aligned"]): {
        "tags": [AlignmentTags.BAM, NalloTags.ASSEMBLY],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["assembly", "assembly_aligned_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, NalloTags.ASSEMBLY],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "hap1"]): {
        "tags": [AnalysisTags.BED, NalloTags.HAP1, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "hap1_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.HAP1, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "hap2"]): {
        "tags": [AnalysisTags.BED, NalloTags.HAP2, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "hap2_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.HAP2, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "ungrouped"]): {
        "tags": [AnalysisTags.BED, NalloTags.UNGROUPED, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["methylation_pileup", "ungrouped_index"]): {
        "tags": [AnalysisTags.BED_INDEX, NalloTags.UNGROUPED, BioinfoToolsTags.MODKIT_PILEUP],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["qc_bam", "mosdepth_d4"]): {
        "tags": [AnalysisTags.COVERAGE, ReportTags.D4],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-html"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_HTML],
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["pedigree", "pedigree_fam"]): {
        "tags": [FamilyTags.PEDIGREE],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["somalier", "relate_html"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_HTML],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["somalier", "relate_pairs"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_PAIRS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["somalier", "relate_pairs"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_PAIRS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["somalier", "relate_samples"]): {
        "tags": [BioinfoToolsTags.SOMALIER, NalloTags.RELATE_SAMPLES],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["peddy", "peddy"]): {
        "tags": [BioinfoToolsTags.PEDDY, FamilyTags.PED],
        "is_mandatory": True,
        "used_by": [UsageTags.AUDIT, UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["peddy", "ped_check"]): {
        "tags": [BioinfoToolsTags.PEDDY, QCTags.PED_CHECK],
        "is_mandatory": True,
        "used_by": [UsageTags.AUDIT, UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["peddy", "sex_check"]): {
        "tags": [BioinfoToolsTags.PEDDY, QCTags.SEX_CHECK],
        "is_mandatory": True,
        "used_by": [UsageTags.AUDIT, UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["deepvariant", "report"]): {
        "tags": [NalloTags.DEEPVARIANT_REPORT],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["paraphase", "paraphase"]): {
        "tags": [AlignmentTags.BAM, BioinfoToolsTags.PARAPHASE],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["paraphase", "paraphase_index"]): {
        "tags": [AlignmentTags.BAM_INDEX, BioinfoToolsTags.PARAPHASE],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["paraphase", "json"]): {
        "tags": [BioinfoToolsTags.PARAPHASE, ReportTags.JSON],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["paraphase", "vcf"]): {
        "tags": [BioinfoToolsTags.PARAPHASE, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["paraphase", "vcf_index"]): {
        "tags": [BioinfoToolsTags.PARAPHASE, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sorted_repeats", "vcf_str"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SORTED, VariantTags.VCF],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sorted_repeats", "vcf_str_index"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SORTED, VariantTags.VCF_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["spanning_repeats", "bam"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SPANNING, AlignmentTags.BAM],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["spanning_repeats", "bam_index"]): {
        "tags": [NalloTags.REPEATS, NalloTags.SPANNING, AlignmentTags.BAM_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["repeats_annotated", "vcf_str"]): {
        "tags": [VariantTags.VCF_STR],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["repeats_annotated", "vcf_str_index"]): {
        "tags": [VariantTags.VCF_STR_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["snv_annotated", "vcf_snv_research"]): {
        "tags": [VariantTags.VCF_SNV_RESEARCH],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["snv_annotated", "vcf_snv_research_index"]): {
        "tags": [VariantTags.VCF_SNV_RESEARCH_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["snv_annotated_filtered", "vcf_snv_clinical"]): {
        "tags": [VariantTags.VCF_SNV_CLINICAL],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["snv_annotated_filtered", "vcf_snv_clinical_index"]): {
        "tags": [VariantTags.VCF_SNV_CLINICAL_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sv_annotated_ranked", "vcf_sv_research"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sv_annotated_ranked", "vcf_sv_research_index"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sv_annotated_ranked_filtered", "vcf_sv_clinical"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["sv_annotated_ranked_filtered", "vcf_sv_clinical_index"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_hificnv"]): {
        "tags": [BioinfoToolsTags.HIFICNV, VariantTags.VCF],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_hificnv_index"]): {
        "tags": [BioinfoToolsTags.HIFICNV, VariantTags.VCF_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_severus"]): {
        "tags": [BioinfoToolsTags.SEVERUS, VariantTags.VCF],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_severus_index"]): {
        "tags": [BioinfoToolsTags.SEVERUS, VariantTags.VCF_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_sniffles"]): {
        "tags": [BioinfoToolsTags.SNIFFLES1, VariantTags.VCF],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["svs_per_caller", "vcf_sniffles_index"]): {
        "tags": [BioinfoToolsTags.SNIFFLES1, VariantTags.VCF_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["qc_bam", "mosdepth_d4"]): {
        "tags": [AnalysisTags.COVERAGE, ReportTags.D4],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["copy_number", "bedgraph"]): {
        "tags": [VariantTags.CNV, NalloTags.BEDGRAPH],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["depth_track", "bigwig"]): {
        "tags": [BioinfoToolsTags.HIFICNV, AnalysisTags.BIGWIG],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["maf_depth_track", "bigwig"]): {
        "tags": [BioinfoToolsTags.HIFICNV, AnalysisTags.BIGWIG, NalloTags.MAF],
        "is_mandatory": True,
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-json"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_JSON],
        "used_by": [UsageTags.LONG_TERM_STORAGE],
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
