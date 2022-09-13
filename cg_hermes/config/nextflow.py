"""Tags that are defined in nextflow deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

NEXTFLOW_COMMON_TAGS = {
    frozenset({"samplesheet-valid"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["samplesheet-valid"],
        "used_by": ["cg"],
    },
    frozenset({"software-versions"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["software-versions"],
        "used_by": ["cg"],
    },
}
#
