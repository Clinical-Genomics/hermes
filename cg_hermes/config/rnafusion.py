"""Tags that are defined in rnafusion deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_COMMON_TAGS

RNAFUSION_COMMON_TAGS = {
    frozenset({"arriba"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["arriba", "fusion"],
        "used_by": ["deliver"],
    },
    frozenset({"arriba-visualisation", "arriba"}): {
        "is_mandatory": False,
        "bundle_id": True,
        "tags": ["arriba-visualisation", "visualization", "arriba", "research"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"fusioncatcher"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher", "fusion"],
        "used_by": ["deliver"],
    },
    frozenset({"fusioncatcher-summary", "fusioncatcher"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher-summary"],
        "used_by": ["deliver"],
    },
    frozenset({"star-fusion"}): {
        "is_mandatory": True,
        "tags": ["star-fusion", "fusion"],
        "used_by": ["deliver"],
    },
    frozenset({"fusionreport", "report"}): {
        "is_mandatory": True,
        "tags": ["fusionreport", "research"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"fusioninspector", "report"}): {
        "is_mandatory": False,
        "tags": ["fusioninspector"],
        "used_by": ["deliver"],
    },
    frozenset({"fusioninspector-html", "report"}): {
        "is_mandatory": False,
        "tags": ["fusioninspector-html", "research"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "tags": ["multiqc-html", "rna"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"star-fusion-cram", "star-fusion"}): {
        "is_mandatory": True,
        "tags": ["cram"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"star-fusion-cram-index", "star-fusion"}): {
        "is_mandatory": True,
        "tags": ["cram-index"],
        "used_by": ["deliver", "scout"],
    },
    frozenset({"star-align-gene-counts", "star-align"}): {
        "is_mandatory": True,
        "tags": ["gene-counts"],
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
    frozenset({"vcf-fusion", "vcf-collect"}): {
        "is_mandatory": False,
        "tags": ["vcf-fusion"],
        "used_by": ["deliver", "scout"],
    },
}

NXF_RNAFUSION_COMMON_TAGS = {**RNAFUSION_COMMON_TAGS, **NEXTFLOW_COMMON_TAGS}
