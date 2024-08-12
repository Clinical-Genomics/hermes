"""Tags that are defined in rnafusion deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS
from cg_hermes.constants.tags import (
    AlignmentTags,
    AnalysisTags,
    BioinfoToolsTags,
    NextflowTags,
    QCTags,
    RawDataTags,
    ReportTags,
    RnafusionTags,
    UsageTags,
)

RNAFUSION_COMMON_TAGS = {
    frozenset({"arriba"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [BioinfoToolsTags.ARRIBA, AnalysisTags.FUSION],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"arriba-visualisation", "arriba"}): {
        "is_mandatory": False,
        "bundle_id": True,
        "tags": [
            RnafusionTags.ARRIBA_VISUALISATION,
            AnalysisTags.VISUALIZATION,
            BioinfoToolsTags.ARRIBA,
            AnalysisTags.RESEARCH,
        ],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fusioncatcher"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.FUSIONCATCHER, AnalysisTags.FUSION],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fusioncatcher-summary", "fusioncatcher"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.FUSIONCATCHER_SUMMARY],
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset({"star-fusion"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.STAR_FUSION, AnalysisTags.FUSION],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fusionreport", "report"}): {
        "is_mandatory": True,
        "tags": [RnafusionTags.FUSIONREPORT, AnalysisTags.RESEARCH],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fusioninspector", "report"}): {
        "is_mandatory": False,
        "tags": [BioinfoToolsTags.FUSIONINSPECTOR],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fusioninspector-html", "report"}): {
        "is_mandatory": False,
        "tags": [RnafusionTags.FUSIONINSPECTOR_HTML, AnalysisTags.RESEARCH],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_HTML, RawDataTags.RNA],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"star-fusion-cram", "star-fusion"}): {
        "is_mandatory": True,
        "tags": [AlignmentTags.CRAM],
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset({"star-fusion-cram-index", "star-fusion"}): {
        "is_mandatory": True,
        "tags": [AlignmentTags.CRAM_INDEX],
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset({"star-align-gene-counts", "star-align"}): {
        "is_mandatory": True,
        "tags": [ReportTags.GENE_COUNTS],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_JSON],
        "used_by": [UsageTags.CG],
    },
    frozenset({"vcf-fusion", "vcf-collect"}): {
        "is_mandatory": False,
        "tags": [AnalysisTags.VCF_FUSION],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc-fastp", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.FASTP],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc-picard-duplicates", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_DUPLICATES],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc-picard-insert-size", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_INSERT_SIZE],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc-picard-rnaseq", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_RNASEQ],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc-general-stats", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.GENERAL_STATS],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc-star", "multiqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.STAR],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"samplesheet-valid"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [NextflowTags.SAMPLESHEET_VALID],
        "used_by": [UsageTags.CG],
    },
}

RNAFUSION_TAGS = {**RNAFUSION_COMMON_TAGS, **NEXTFLOW_TAGS}
