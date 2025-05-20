"""Tags that are used in the fluffy workflow."""

from cg_hermes.constants.tags import (
    AnalysisTags,
    BioinfoToolsTags,
    ReportTags,
    UsageTags,
    VariantTags,
)

FLUFFY_COMMON_TAGS = {
    frozenset(["multiqc"]): {
        "tags": [ReportTags.MULTIQC_HTML],
        "is_mandatory": True,
        "used_by": [UsageTags.NIPT],
    },
    frozenset(["nipt_csv"]): {
        "tags": [AnalysisTags.METRICS],
        "bundle_id": True,
        "is_mandatory": True,
        "used_by": [UsageTags.NIPT],
    },
    frozenset(["nipt_first_pass_csv"]): {
        "tags": [AnalysisTags.FIRST_PASS],
        "bundle_id": True,
        "is_mandatory": False,
        "used_by": [UsageTags.NIPT],
    },
    frozenset(["nipt_second_pass_csv"]): {
        "tags": [AnalysisTags.SECOND_PASS],
        "bundle_id": True,
        "is_mandatory": False,
        "used_by": [UsageTags.NIPT],
    },
    frozenset(["wcx2cytosure"]): {
        "tags": [BioinfoToolsTags.WCX2CYTOSURE],
        "is_mandatory": True,
        "used_by": [UsageTags.NIPT],
    },
    frozenset(["wisecondor_aberrations"]): {
        "tags": [BioinfoToolsTags.WISECONDOR, VariantTags.CNV],
        "is_mandatory": True,
        "used_by": [UsageTags.NIPT],
    },
}
