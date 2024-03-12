"""Tags that are defined in Taxprofiler deliverables mapped to tags stored in Housekeeper."""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS

TAXPROFILER_COMMON_TAGS = {
    frozenset({"kraken2_combined_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "kraken2report"],
        "used_by": ["deliver", "storage"],
    },
    frozenset({"kraken2_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "kraken2report"],
        "used_by": ["deliver"],
    },
    frozenset({"krona_kraken_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "krona", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"krona_centrifuge_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["centrifuge", "krona", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"bracken_combined_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["bracken", "brackenreport"],
        "used_by": ["deliver"],
    },
    frozenset({"bracken_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["bracken", "brackenreport"],
        "used_by": ["deliver"],
    },
    frozenset({"centrifuge_combined_report", "centrifuge"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["centrifuge", "centrifugereport"],
        "used_by": ["deliver"],
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["multiqc-html"],
        "used_by": ["deliver"],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": True,
        "tags": ["multiqc-json"],
        "used_by": ["deliver"],
    },
    frozenset({"qc-metrics"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics"],
        "used_by": ["cg"],
    },
}

TAXPROFILER_TAGS = {**TAXPROFILER_COMMON_TAGS, **NEXTFLOW_TAGS}
