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
    RarediseaseTags,
    ReportTags,
    VariantTags,
    UsageTags,
)

RAREDISEASE_COMMON_TAGS = {
    frozenset(["alignment", "alignment_markduplicates"]): {
        "tags": [AlignmentTags.CRAM, ReportTags.PICARD_DUPLICATES],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["alignment", "alignment_markduplicates_index"]): {
        "tags": [AlignmentTags.CRAM_INDEX, ReportTags.PICARD_DUPLICATES],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["alignment", "alignment_mt"]): {
        "tags": [AlignmentTags.BAM_MT],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["alignment", "alignment_mt_index"]): {
        "tags": [AlignmentTags.BAM_MT_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["tiddit_coverage"]): {
        "tags": [AnalysisTags.TIDDIT_COVERAGE, AnalysisTags.BIGWIG],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["qc_bam", "mosdepth_d4"]): {
        "tags": [AnalysisTags.COVERAGE, ReportTags.D4],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["chromograph_cov", "tcov"]): {
        "tags": [BioinfoToolsTags.CHROMOGRAPH, AnalysisTags.TCOV],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["smncopynumbercaller", "tsv"]): {
        "tags": [VariantTags.SMN_CALLING],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["expansionhunter", "variant_catalog"]): {
        "tags": [BioinfoToolsTags.EXPANSIONHUNTER, MipTags.VARIANT_CATALOG],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["expansionhunter_stranger", "case_sv_str"]): {
        "tags": [VariantTags.VCF_STR],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["expansionhunter_stranger", "case_sv_str_index"]): {
        "tags": [VariantTags.VCF_STR_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["expansionhunter", "str_variants"]): {
        "tags": [BioinfoToolsTags.EXPANSIONHUNTER, VariantTags.VCF_STR],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["expansionhunter", "str_alignment"]): {
        "tags": [BioinfoToolsTags.EXPANSIONHUNTER, AlignmentTags.BAM],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["expansionhunter", "str_alignment_index"]): {
        "tags": [BioinfoToolsTags.EXPANSIONHUNTER, AlignmentTags.BAM_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["vcf2cytosure", "vcf2cytosure"]): {
        "tags": [VariantTags.VCF2CYTOSURE],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["gens_generatedata", "baf"]): {
        "tags": [BioinfoToolsTags.GENS, AnalysisTags.FRACSNP, AnalysisTags.BED],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["gens_generatedata", "baf_index"]): {
        "tags": [BioinfoToolsTags.GENS, AnalysisTags.FRACSNP, AnalysisTags.BED_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["gens_generatedata", "cov"]): {
        "tags": [BioinfoToolsTags.GENS, AnalysisTags.COVERAGE, AnalysisTags.BED],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["gens_generatedata", "cov_index"]): {
        "tags": [BioinfoToolsTags.GENS, AnalysisTags.COVERAGE, AnalysisTags.BED_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["call_mobile_elements", "call_mobile_elements"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_mobile_elements", "call_mobile_elements_index"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["annotate_mobile_elements", "clinical"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, AnalysisTags.CLINICAL, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["annotate_mobile_elements", "clinical_index"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, AnalysisTags.CLINICAL, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["annotate_mobile_elements", "research"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, AnalysisTags.RESEARCH, VariantTags.VCF],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["annotate_mobile_elements", "research_index"]): {
        "tags": [VariantTags.MOBILE_ELEMENTS, AnalysisTags.RESEARCH, VariantTags.VCF_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_snv", "call_snv"]): {
        "tags": [VariantTags.VCF_SNV],
        "is_mandatory": True,
        "used_by": [UsageTags.GENOTYPE, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_snv", "call_snv_index"]): {
        "tags": [VariantTags.VCF_SNV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.CG, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_snv", "call_snv_mt"]): {
        "tags": [VariantTags.VCF_SNV, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.CG],
    },
    frozenset(["call_snv", "call_snv_mt_index"]): {
        "tags": [VariantTags.VCF_SNV_INDEX, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.CG],
    },
    frozenset(["call_sv", "call_sv"]): {
        "tags": [VariantTags.VCF_SV],
        "is_mandatory": False,
        "used_by": [UsageTags.CG, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_sv", "call_sv_index"]): {
        "tags": [VariantTags.VCF_SV_INDEX],
        "is_mandatory": False,
        "used_by": [UsageTags.CG, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_sv_mt", "call_sv_mt"]): {
        "tags": [VariantTags.VCF_SV, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.CG],
    },
    frozenset(["call_sv_mt", "call_sv_mt_index"]): {
        "tags": [VariantTags.VCF_SV_INDEX, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.CG],
    },
    frozenset(["call_sv_mt", "call_sv_mt_del"]): {
        "tags": [AnalysisTags.MITOCHONDRIA, BioinfoToolsTags.MITODEL],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["call_sv_mt", "eklipse_del"]): {
        "tags": [RarediseaseTags.EKLIPSE_DEL, ReportTags.CSV, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_sv_mt", "eklipse_png"]): {
        "tags": [RarediseaseTags.EKLIPSE_PNG, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["call_sv_mt", "eklipse_genes"]): {
        "tags": [RarediseaseTags.EKLIPSE_GENES, ReportTags.CSV, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["rank_and_filter", "snv_clinical"]): {
        "tags": [VariantTags.VCF_SNV_CLINICAL],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "snv_clinical_index"]): {
        "tags": [VariantTags.VCF_SNV_CLINICAL_INDEX],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "snv_research"]): {
        "tags": [VariantTags.VCF_SNV_RESEARCH],
        "index_tags": ["vcf-snv-research-index"],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "snv_research_index"]): {
        "tags": [VariantTags.VCF_SNV_RESEARCH_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "sv_clinical"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "sv_clinical_index"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL_INDEX],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "sv_research"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH],
        "index_tags": ["vcf-snv-research-index"],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "sv_research_index"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH_INDEX],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "mt_clinical"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "mt_clinical_index"]): {
        "tags": [VariantTags.VCF_SV_CLINICAL_INDEX, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "mt_research"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH, AnalysisTags.MITOCHONDRIA],
        "index_tags": ["vcf-snv-research-index"],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["rank_and_filter", "mt_research_index"]): {
        "tags": [VariantTags.VCF_SV_RESEARCH_INDEX, AnalysisTags.MITOCHONDRIA],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset(["ngsbits_samplegender", "ngsbits_samplegender"]): {
        "tags": [RarediseaseTags.NGSBITS],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
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
    frozenset(["pedigree", "pedigree_fam"]): {
        "tags": [FamilyTags.PEDIGREE],
        "is_mandatory": True,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["annotate_snv", "rhocallviz"]): {
        "tags": [VariantTags.RHOCALL_VIZ],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["annotate_snv_mt", "haplogrep"]): {
        "tags": [RarediseaseTags.HAPLOGREP],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT, UsageTags.CLINICAL_DELIVERY],
    },
    frozenset(["chromograph_rhoviz", "autozyg"]): {
        "tags": [BioinfoToolsTags.CHROMOGRAPH, AnalysisTags.AUTOZYG],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["chromograph_upd", "regions"]): {
        "tags": [BioinfoToolsTags.CHROMOGRAPH, VariantTags.UPD, AnalysisTags.REGIONS],
        "is_mandatory": False,
        "used_by": [UsageTags.SCOUT],
    },
    frozenset(["chromograph_upd", "sites"]): {
        "tags": [BioinfoToolsTags.CHROMOGRAPH, VariantTags.UPD, AnalysisTags.SITES],
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
    frozenset({"multiqc", "multiqc-general-stats"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.GENERAL_STATS],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-alignment"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_ALIGNMENT],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-bamqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_BAMQC],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-insertsize"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_INSERT_SIZE],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-mosdepth-covdist"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.MOSDEPTH_COVDIST],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-mosdepth-cumcov"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.MOSDEPTH_CUMCOV],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-mosdepth-perchrom"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.MOSDEPTH_PERCHROM],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-qualitycycle"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_QUALITYCYCLE],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-qualitydistr"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_QUALITYDISTR],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-peddy"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.PEDDY],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-hs"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_HS],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-histogram1"}): {
        "is_mandatory": False,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_HISTOGRAM],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-histogram2"}): {
        "is_mandatory": False,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_HISTOGRAM],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-histogram3"}): {
        "is_mandatory": False,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_HISTOGRAM],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-wgs"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_WGS],
        "used_by": [UsageTags.JANUS],
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

RAREDISEASE_TAGS = {**RAREDISEASE_COMMON_TAGS, **NEXTFLOW_TAGS}
