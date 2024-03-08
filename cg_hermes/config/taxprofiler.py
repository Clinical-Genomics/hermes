"""Tags that are defined in taxprofiler deliverables mapped to tags used in CG"""

from cg_hermes.config.nextflow import NEXTFLOW_COMMON_TAGS

TAXPROFILER_COMMON_TAGS = {
    frozenset({"test"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["kraken2", "report"],
        "used_by": ["deliver"],
    },
}

NXF_TAXPROFILER_COMMON_TAGS = {**TAXPROFILER_COMMON_TAGS, **NEXTFLOW_COMMON_TAGS}
