"""Tags that are defined in Tomte deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However, the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS

TOMTE_COMMON_TAGS = {
    frozenset({"fraser", "fraser-clinical"}): {
        "is_mandatory": False,
        "tags": ["fraser", "clinical"],
        "used_by": ["deliver"],
    },
    frozenset({"fraser", "fraser-research"}): {
        "is_mandatory": False,
        "tags": ["fraser", "research"],
        "used_by": ["deliver"],
    },
    frozenset({"outrider", "outrider-clinical"}): {
        "is_mandatory": False,
        "tags": ["outrider", "clinical"],
        "used_by": ["deliver"],
    },
    frozenset({"outrider", "outrider-research"}): {
        "is_mandatory": False,
        "tags": ["outrider", "research"],
        "used_by": ["deliver"],
    },
    frozenset({"star", "star-cram"}): {
        "is_mandatory": True,
        "tags": ["cram"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"star", "star-cram-index"}): {
        "is_mandatory": True,
        "tags": ["cram-index"],
        "used_by": ["deliver"],
    },
    frozenset({"coverage", "bigwig"}): {
        "is_mandatory": True,
        "tags": ["coverage", "bigwig"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"junction", "bed"}): {
        "is_mandatory": True,
        "tags": ["junction", "bed"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"junction", "bed-index"}): {
        "is_mandatory": True,
        "tags": ["junction", "bed-index"],
        "used_by": ["deliver"],
    },
    frozenset({"stringtie", "assembly"}): {
        "is_mandatory": True,
        "tags": ["stringtie", "assembly"],
        "used_by": ["deliver"],
    },
    frozenset({"gffcompare"}): {
        "is_mandatory": True,
        "tags": ["gffcompare"],
        "used_by": ["deliver"],
    },
    frozenset({"star", "raw-gene-counts"}): {
        "is_mandatory": True,
        "tags": ["gene-counts"],
        "used_by": ["deliver"],
    },
    frozenset({"samplesheet"}): {
        "is_mandatory": True,
        "tags": ["samplesheet"],
        "used_by": ["cg"],
    },
    frozenset({"nextflow-config"}): {
        "is_mandatory": True,
        "tags": ["nextflow-config"],
        "used_by": ["cg"],
    },
    frozenset({"qc-metrics"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics"],
        "used_by": ["cg"],
    },
    frozenset({"multiqc", "multiqc-html"}): {
        "is_mandatory": True,
        "tags": ["multiqc-html", "rna"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"multiqc", "multiqc-json"}): {
        "is_mandatory": True,
        "tags": ["multiqc-json"],
        "used_by": ["deliver"],
    },
    frozenset({"multiqc", "multiqc-fastp"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "fastp"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-fastqc"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "fastqc"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-bcftools-stats"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "bcftools-stats"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-gffcompare"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "gffcompare"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-picard-rnaseq"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "picard-rnaseq"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-star"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "star"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-general-stats"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "general-stats"],
        "used_by": ["janus"],
    },
    frozenset({"multiqc", "multiqc-picard-insert-size"}): {
        "is_mandatory": True,
        "tags": ["qc-metrics", "multiqc", "picard-insert-size"],
        "used_by": ["janus"],
    },
}

TOMTE_TAGS = {**TOMTE_COMMON_TAGS, **NEXTFLOW_TAGS}
