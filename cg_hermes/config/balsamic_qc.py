"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.balsamic import QC_TAGS, RAW_TAGS


QC_ALIGNMENT_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["tumor.merged.cram"]): {  # cram (tumor)
        "tags": ["tumor", "qc-cram"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tumor.merged.cram.crai"]): {
        "tags": ["tumor", "qc-cram-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["normal.merged.cram"]): {  # cram (normal)
        "tags": ["normal", "qc-cram"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {
        "tags": ["normal", "qc-cram-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
}

BALSAMIC_QC_TAGS = {**QC_TAGS, **QC_ALIGNMENT_TAGS}

QC_TUMOR_NORMAL_WGS_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
}

QC_TUMOR_NORMAL_PANEL_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
}
