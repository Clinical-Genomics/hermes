"""Tags that are defined in Taxprofiler deliverables mapped to tags stored in Housekeeper."""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS

TAXPROFILER_COMMON_TAGS = {
    frozenset({"kraken2_combined_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "combined-report"],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"kraken2_report", "kraken2"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "metagenomics-report"],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"krona_kraken_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "krona", "visualization"],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"krona_centrifuge_plot", "krona"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["centrifuge", "krona", "visualization"],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"bracken_combined_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["bracken", "combined-report"],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"bracken_report", "bracken"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["bracken", "metagenomics-report"],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"centrifuge_combined_report", "centrifuge"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["centrifuge", "combined-report"],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"centrifuge_report", "centrifuge"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["centrifuge", "metagenomics-report"],
        "used_by": ["clinical-delivery"],
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["multiqc-html"],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": True,
        "tags": ["multiqc-json"],
        "used_by": ["clinical-delivery", "long-term-storage"],
    },
    frozenset({"qc-metrics"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics"],
        "used_by": ["cg", "long-term-storage"],
    },
    frozenset({"multiqc-general-stats", "multiqc"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "general-stats"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-fastp", "multiqc"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "fastp"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-samtools-stats", "multiqc"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "samtools-stats"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc-kraken", "multiqc"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "kraken2"],
        "used_by": ["janus"],
    },
}

TAXPROFILER_TAGS = {**TAXPROFILER_COMMON_TAGS, **NEXTFLOW_TAGS}
