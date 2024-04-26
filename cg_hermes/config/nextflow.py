"""Tags that are defined in nextflow deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.constants.tags import (
    NextflowTags,
    QCTags,
    UsageTags,
)


NEXTFLOW_TAGS = {
    frozenset({"software-versions"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": [NextflowTags.SOFTWARE_VERSIONS],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
    frozenset({"qc-metrics"}): {
        "is_mandatory": True,
        "tags": [QCTags.QC_METRICS],
        "used_by": [UsageTags.CG, UsageTags.LONG_TERM_STORAGE],
    },
}
#
