"""Tags that are defined in Balsamic UMI deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

import copy

from cg_hermes.config.balsamic import (
    BALSAMIC_TAGS,
    TUMOR_ONLY_PANEL_TAGS,
    TUMOR_NORMAL_PANEL_TAGS,
)

UMI_RAW_TAGS = {
    # Alignment files
    "tumor_umi_consensusfiltered.merged.cram": ["cram", "umi-tumor-cram"],
    "tumor_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-tumor-cram-index"],
    "normal_umi_consensusfiltered.merged.cram": ["cram", "umi-normal-cram"],
    "normal_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-normal-cram-index"],
    # SNVs/INDELs
    "TNscope_umi.vcf.gz": [
        "vcf-tnscope-umi",
        "research-vcf-tnscope-umi",
    ],
    "TNscope_umi.vcf.gz.tbi": [
        "vcf-tnscope-umi",
        "research-vcf-tnscope-umi-index",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope-umi",
        "snv",
        "research-vcf-pass-tnscope-umi",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope-umi",
        "snv",
        "research-vcf-pass-tnscope-umi-index",
    ],
}

BALSAMIC_UMI_TAGS = {
    # Alignment files
    frozenset(UMI_RAW_TAGS["tumor_umi_consensusfiltered.merged.cram"]): {  # UMI cram (tumor)
        "tags": ["umi-cram", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(UMI_RAW_TAGS["tumor_umi_consensusfiltered.merged.cram.crai"]): {
        "tags": ["umi-cram-index", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(UMI_RAW_TAGS["normal_umi_consensusfiltered.merged.cram"]): {  # UMI cram (normal)
        "tags": ["umi-cram", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(UMI_RAW_TAGS["normal_umi_consensusfiltered.merged.cram.crai"]): {
        "tags": ["umi-cram-index", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # SNVs/INDELs
    frozenset(UMI_RAW_TAGS["TNscope_umi.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-research"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(UMI_RAW_TAGS["TNscope_umi.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-research-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(UMI_RAW_TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-clinical"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(UMI_RAW_TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-clinical-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
}

BALSAMIC_UMI_TAGS.update(BALSAMIC_TAGS)

UMI_TUMOR_ONLY_PANEL_TAGS = copy.deepcopy(TUMOR_ONLY_PANEL_TAGS)

UMI_TUMOR_NORMAL_PANEL_TAGS = {
    frozenset(UMI_RAW_TAGS["normal_umi_consensusfiltered.merged.cram"]): {"is_mandatory": True},
    frozenset(UMI_RAW_TAGS["normal_umi_consensusfiltered.merged.cram.crai"]): {
        "is_mandatory": True
    },
}

UMI_TUMOR_NORMAL_PANEL_TAGS.update(TUMOR_NORMAL_PANEL_TAGS)
