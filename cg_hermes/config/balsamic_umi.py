"""Tags that are defined in Balsamic UMI deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.balsamic import BALSAMIC_TAGS, RAW_TAGS

UMI_ALIGNMENT_TAGS = {
    # Alignment files
    frozenset(RAW_TAGS["tumor_umi_consensusfiltered.cram"]): {  # UMI cram (tumor)
        "tags": ["umi-cram", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["tumor_umi_consensusfiltered.cram.crai"]): {
        "tags": ["umi-cram-index", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["normal_umi_consensusfiltered.cram"]): {  # UMI cram (normal)
        "tags": ["umi-cram", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["normal_umi_consensusfiltered.cram.crai"]): {
        "tags": ["umi-cram-index", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
}

UMI_CALLERS_TAGS = {
    # SNVs/INDELs
    frozenset(RAW_TAGS["tnscope_umi.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope_umi.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope_umi.research.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-research-unfiltered"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope_umi.research.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-research-unfiltered-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope_umi.clinical.scored.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-clinical-scored"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["tnscope_umi.clinical.scored.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-clinical-scored-index"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["tnscope_umi.clinical.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-clinical"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["tnscope_umi.clinical.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-snv-clinical-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    # TMB
    frozenset(RAW_TAGS["tnscope_umi.balsamic_stat"]): {
        "tags": ["research", "tnscope-umi", "tmb"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
}

BALSAMIC_UMI_TAGS = {**BALSAMIC_TAGS, **UMI_ALIGNMENT_TAGS, **UMI_CALLERS_TAGS}

UMI_TUMOR_ONLY_PANEL_TAGS = {
    # SNVs/INDELs (PANEL)
    frozenset(RAW_TAGS["vardict.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.scored.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.scored.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(RAW_TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
    # TMB
    frozenset(RAW_TAGS["merged.balsamic_stat"]): {"is_mandatory": True},
}

UMI_TUMOR_NORMAL_PANEL_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["normal.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.cram.crai"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal_umi_consensusfiltered.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal_umi_consensusfiltered.cram.crai"]): {"is_mandatory": True},
    # Germline SNVs (PANEL & WGS)
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz.tbi"]): {"is_mandatory": True},
    # SNVs/INDELs (PANEL)
    frozenset(RAW_TAGS["vardict.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.scored.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.scored.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["merged.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(RAW_TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
    # TMB
    frozenset(RAW_TAGS["merged.balsamic_stat"]): {"is_mandatory": True},
    # MSI (PANEL UMI)
    frozenset(RAW_TAGS["msisensorpro.msi"]): {"is_mandatory": True},
}
