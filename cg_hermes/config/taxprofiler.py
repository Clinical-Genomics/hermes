"""Tags that are defined in Taxprofiler deliverables mapped to tags stored in Housekeeper."""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS
from cg_hermes.constants.tags import (
    TaxprofilerTags,
    AnalysisTags,
    ReportTags,
    QCTags,
    BioinfoToolsTags,
)

TAXPROFILER_COMMON_TAGS = {
    frozenset({"kraken2_combined_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.KRAKEN2, TaxprofilerTags.COMBINED_REPORT],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"kraken2_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.KRAKEN2, TaxprofilerTags.METAGENOMICS_REPORT],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"krona_kraken_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.KRAKEN2, TaxprofilerTags.KRONA, AnalysisTags.VISUALIZATION],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"krona_centrifuge_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.KRAKEN2, TaxprofilerTags.KRONA, AnalysisTags.VISUALIZATION],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"bracken_combined_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.BRACKEN, TaxprofilerTags.COMBINED_REPORT],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"bracken_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.BRACKEN, TaxprofilerTags.METAGENOMICS_REPORT],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"centrifuge_combined_report", "centrifuge"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.CENTRIFUGE, TaxprofilerTags.COMBINED_REPORT],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"centrifuge_report", "centrifuge"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [TaxprofilerTags.CENTRIFUGE, TaxprofilerTags.METAGENOMICS_REPORT],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [ReportTags.MULTIQC_HTML],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": True,
        "tags": [ReportTags.MULTIQC_JSON],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"qc-metrics"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS],
        "used_by": ["cg", "long-term-storage"],
    },
    frozenset({"multiqc-json", "multiqc-general-stats"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.GENERAL_STATS],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-json", "multiqc-fastp"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, BioinfoToolsTags.FASTP],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-json", "multiqc-samtools-stats"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, ReportTags.SAMTOOLS_STATS],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-json", "multiqc-kraken"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS, ReportTags.MULTIQC, TaxprofilerTags.KRAKEN2],
        "used_by": ["janus"],
    },
}

TAXPROFILER_TAGS = {**TAXPROFILER_COMMON_TAGS, **NEXTFLOW_TAGS}
