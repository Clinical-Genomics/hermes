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
        "used_by": ["cg"],
    },
    frozenset({"arriba-visualisation", "arriba"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["arriba-visualisation", "visualization", "arriba"],
        "used_by": ["cg"],
    },
    frozenset({"fusioncatcher"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher", "fusion"],
        "used_by": ["cg"],
    },
    frozenset({"fusioncatcher-summary", "fusioncatcher"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher-summary"],
        "used_by": ["cg"],
    },
    frozenset({"pizzly"}): {
        "is_mandatory": True,
        "tags": ["pizzly", "fusion"],
        "used_by": ["cg"],
    },
    frozenset({"star-fusion"}): {
        "is_mandatory": True,
        "tags": ["star-fusion", "fusion"],
        "used_by": ["cg"],
    },
    frozenset({"squid"}): {
        "is_mandatory": True,
        "tags": ["squid", "fusion"],
        "used_by": ["cg"],
    },
    frozenset({"fusionreport", "report"}): {
        "is_mandatory": True,
        "tags": ["fusionreport"],
        "used_by": ["cg"],
    },
    frozenset({"fusioninspector", "report"}): {
        "is_mandatory": True,
        "tags": ["fusioninspector"],
        "used_by": ["cg"]
    },
    frozenset({"multiqc-html", "report"}): {
        "is_mandatory": True,
        "tags": ["multiqc-html"],
        "used_by": ["deliver"],
    },
}

NXF_RNAFUSION_COMMON_TAGS = {**RNAFUSION_COMMON_TAGS, **NEXTFLOW_COMMON_TAGS}


#
