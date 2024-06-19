"""Tags that are defined in Tomte deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However, the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS
from cg_hermes.constants.tags import (
    AlignmentTags,
    UsageTags,
    QCTags,
    ReportTags,
    BioinfoToolsTags,
    RawDataTags,
    NextflowTags,
    AnalysisTags,
    TomteTags,
    VariantTags,
)

TOMTE_COMMON_TAGS = {
    frozenset({"transcript-counts", "salmon"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.SALMON_QUANT],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"research-vcf", "snv"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF, VariantTags.SNV],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"research-vcf-index", "snv"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.RESEARCH, VariantTags.VCF_INDEX, VariantTags.SNV],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"clinical-vcf", "snv"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF, VariantTags.SNV],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"clinical-vcf-index", "snv"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.CLINICAL, VariantTags.VCF_INDEX, VariantTags.SNV],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fraser", "fraser-clinical"}): {
        "is_mandatory": False,
        "tags": [TomteTags.FRASER, AnalysisTags.CLINICAL],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"fraser", "fraser-research"}): {
        "is_mandatory": False,
        "tags": [TomteTags.FRASER, AnalysisTags.RESEARCH],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"outrider", "outrider-clinical"}): {
        "is_mandatory": False,
        "tags": [TomteTags.OUTRIDER, AnalysisTags.CLINICAL],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"outrider", "outrider-research"}): {
        "is_mandatory": False,
        "tags": [TomteTags.OUTRIDER, AnalysisTags.RESEARCH],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"star", "star-cram"}): {
        "is_mandatory": True,
        "tags": [AlignmentTags.CRAM],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT],
    },
    frozenset({"star", "star-cram-index"}): {
        "is_mandatory": True,
        "tags": [AlignmentTags.CRAM_INDEX],
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset({"coverage", "bigwig"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.COVERAGE, AnalysisTags.BIGWIG],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"junction", "bed"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.JUNCTION, AnalysisTags.BED],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"junction", "bed-index"}): {
        "is_mandatory": True,
        "tags": [AnalysisTags.JUNCTION, AnalysisTags.BED_INDEX],
        "used_by": [UsageTags.CLINICAL_DELIVERY],
    },
    frozenset({"stringtie", "assembly"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.STRINGTIE, AnalysisTags.ASSEMBLY],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"gffcompare"}): {
        "is_mandatory": True,
        "tags": [BioinfoToolsTags.GFFCOMPARE],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"star", "raw-gene-counts"}): {
        "is_mandatory": True,
        "tags": [ReportTags.GENE_COUNTS],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"nextflow-config"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.NEXTFLOW_CONFIG],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"nextflow-params"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.NEXTFLOW_PARAMS],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-html"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_HTML, RawDataTags.RNA],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.SCOUT, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-json"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_JSON],
        "used_by": [UsageTags.CLINICAL_DELIVERY, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"multiqc", "multiqc-fastp"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.FASTP],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-fastqc"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.FASTQC],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-bcftools-stats"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.BCFTOOLS_STATS],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-gffcompare"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.GFFCOMPARE],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-rnaseq"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_RNASEQ],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-star"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.STAR],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-general-stats"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.GENERAL_STATS],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"multiqc", "multiqc-picard-insert-size"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.PICARD_INSERT_SIZE],
        "used_by": [UsageTags.JANUS],
    },
    frozenset({"samplesheet"}): {
        "is_mandatory": True,
        "tags": [NextflowTags.SAMPLESHEET],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
}

TOMTE_TAGS = {**TOMTE_COMMON_TAGS, **NEXTFLOW_TAGS}
