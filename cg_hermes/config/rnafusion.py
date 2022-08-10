"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

# TODO
RNAFUSION_COMMON_TAGS = {
    frozenset({"arriba"}): {
        "is_mandatory": True,
        "tags": ["arriba"],
        "used_by": ["cg"],
    },
    frozenset({"fusioncatcher"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher"],
        "used_by": ["cg"],
    },
    frozenset({"fusioncatcher_summary"}): {
        "is_mandatory": True,
        "tags": ["fusioncatcher_summary"],
        "used_by": ["cg"],
    },
    frozenset({"pizzly"}): {
        "is_mandatory": True,
        "tags": ["pizzly"],
        "used_by": ["cg"],
    },
    frozenset({"starfusions"}): {
        "is_mandatory": True,
        "tags": ["star-fusion"],
        "used_by": ["cg"],
    },
    frozenset({"squid"}): {
        "is_mandatory": True,
        "tags": ["squid"],
        "used_by": ["cg"],
    },
}
#