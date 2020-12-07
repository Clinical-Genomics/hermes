"""Tags that are used in the fluffy pipeline"""

FLUFFY_COMMON_TAGS = {
    frozenset(["multiqc"]): {
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "used_by": ["nipt"],
    },
    frozenset(["nipt_csv"]): {
        "tags": ["metrics"],
        "is_mandatory": True,
        "used_by": ["nipt"],
    },
    frozenset(["wisecondor_aberrations"]): {
        "tags": ["wisecondor"],
        "is_mandatory": True,
        "used_by": ["nipt"],
    },
}
