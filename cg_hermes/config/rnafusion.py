"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

# TODO
RNAFUSION_COMMON_TAGS = {
    frozenset({"sampleinfo", "runinfo"}): {
        "is_mandatory": False,
        "bundle_id": True,
        "tags": ["arriba_fusions"],
        "used_by": ["cg", "storage"],
    },
}
#