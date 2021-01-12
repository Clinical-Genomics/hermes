"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not mandatory by default.
However the tags that are available to a particular analysis is mandatory for that analysis.
"""
import copy
from typing import Dict, FrozenSet

BALSAMIC_COMMON_TAGS = {
    frozenset({"cns", "cnv-cns"}): {
        "tags": ["cnvkit", "segments"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"cnv-cnr", "cnr"}): {
        "tags": ["cnvkit", "regions"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"cnv-scatter", "scatter"}): {
        "tags": ["cnvkit", "visualization"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"cnv-diagram", "diagram"}): {
        "tags": ["cnvkit", "visualization", "diagram"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"cnv-gene-breaks", "gene-breaks"}): {
        "tags": ["cnvkit", "genes"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"gene-metrics", "cnv-gene-metrics"}): {
        "tags": ["cnvkit", "genes", "metrics"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"multiqc-html", "html"}): {
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": ["scout", "deliver", "audit"],
    },
    frozenset({"multiqc-json", "json"}): {
        "tags": ["multiqc-json"],
        "is_mandatory": True,
        "used_by": ["vogue", "audit"],
    },
    frozenset({"scout-bam", "bam"}): {"tags": ["bam"], "is_mandatory": False, "used_by": ["scout"]},
    frozenset({"scout-bam-index", "bam"}): {
        "tags": ["bam-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset({"vcf-all", "tnhaplotyper", "snv", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "tumor", "haplotype-caller"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "tnhaplotyper", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "tumor", "haplotype-caller"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "tnscope", "snv", "annotated-somatic-vcf-all"}): {
        "tags": ["tumor", "scope", "vcf-snv-research"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "tnscope", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["tumor", "scope", "vcf-snv-research-index"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "snv", "tnsnv", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "tumor", "genotyper"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "snv", "tnsnv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "tumor", "genotyper"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "manta", "annotated-somatic-vcf-all", "sv"}): {
        "tags": ["vcf-sv-research", "manta", "tumor"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "annotated-somatic-vcf-all-index", "manta", "sv"}): {
        "tags": ["vcf-sv-research-index", "manta", "tumor"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "cnvkit", "cnv", "annotated-somatic-vcf-all"}): {
        "tags": ["cnvkit", "sv-vcf", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"vcf-all", "cnvkit", "annotated-somatic-vcf-all-index", "cnv"}): {
        "tags": ["cnvkit", "sv-vcf-index", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"tnscope", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["sention", "scope", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"tnhaplotyper", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["sention", "haplotype-caller", "vcf-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"vcf-summary", "manta", "annotated-somatic-vcf-summary", "sv"}): {
        "tags": ["sention", "manta", "vcf-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"vcf-summary", "snv", "annotated-somatic-vcf-summary", "tnsnv"}): {
        "tags": ["sention", "genotyper", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"vcf-summary", "cnvkit", "cnv", "annotated-somatic-vcf-summary"}): {
        "tags": ["cnvkit", "vcf-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"tnhaplotyper", "vcf-pass", "annotated-somatic-vcf-pass", "snv"}): {
        "tags": ["vcf", "sention", "haplotype-caller", "filtered"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"tnhaplotyper", "vcf-pass", "snv", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["vcf-index", "sention", "haplotype-caller", "filtered"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-pass", "annotated-somatic-vcf-pass", "snv", "tnsnv"}): {
        "tags": ["vcf", "sention", "genotyper", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-somatic-vcf-pass-index", "vcf-pass", "snv", "tnsnv"}): {
        "tags": ["vcf-index", "sention", "genotyper", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"cnvkit", "vcf-pass", "annotated-somatic-vcf-pass", "cnv"}): {
        "tags": ["cnvkit", "sv-vcf", "filtered"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"cnvkit", "vcf-pass", "cnv", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["cnvkit", "sv-vcf-index", "filtered"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-pass", "annotated-somatic-vcf-pass", "manta", "sv"}): {
        "tags": ["vcf-sv-clinical", "manta", "filtered"],
        "is_mandatory": True,
        "used_by": ["scout"],
    },
    frozenset({"annotated-somatic-vcf-pass-index", "vcf-pass", "manta", "sv"}): {
        "tags": ["vcf-sv-clinical-index", "manta", "filtered"],
        "is_mandatory": True,
        "used_by": ["scout"],
    },
    frozenset({"tnscope", "vcf-pass", "annotated-somatic-vcf-pass", "snv"}): {
        "tags": ["vcf-snv-clinical", "scope", "filtered", "sention"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"tnscope", "vcf-pass", "snv", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["vcf-snv-clinical-index", "scope", "filtered", "sention"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"read1", "quality-trimmed-fastq-read1"}): {
        "tags": ["fastq"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"quality-trimmed-fastq-read2", "read2"}): {
        "tags": ["fastq"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"quality-trimmed-fastq-json", "json"}): {
        "tags": ["fastq", "metrics"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"quality-trimmed-fastq-html", "html"}): {
        "tags": ["fastq", "visualization"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"balsamic-report"}): {
        "tags": ["balsamic-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"balsamic-config"}): {
        "tags": ["balsamic-config"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"balsamic-dag"}): {
        "tags": ["balsamic-dag"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"normal-bam", "bam"}): {
        "tags": ["bam", "normal"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"normal-bam-index", "bam"}): {
        "tags": ["bam-index", "normal"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"cram", "normal-cram"}): {
        "tags": ["cram", "normal"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"cram", "normal-cram-index"}): {
        "tags": ["cram-index"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "snv", "vardict", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "vardict"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "snv", "vardict", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "vardict"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "strelka", "snv", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "strelka"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "strelka", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "strelka"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "mutect", "snv", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "mutect"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "mutect", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "mutect"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vardict", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["vardict", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"mutect", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["mutect", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"strelka", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["strelka", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"mutect", "vcf-pass", "annotated-somatic-vcf-pass", "snv"}): {
        "tags": ["vcf", "mutect", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"mutect", "vcf-pass", "snv", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["vcf-index", "mutect", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-pass", "annotated-somatic-vcf-pass", "snv", "vardict"}): {
        "tags": ["vcf-snv-clinical", "vardict", "filtered"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-pass", "snv", "vardict", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["vcf-snv-clinical-index", "vardict", "filtered"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"strelka", "vcf-pass", "annotated-somatic-vcf-pass", "snv"}): {
        "tags": ["vcf", "strelka", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"strelka", "vcf-pass", "snv", "annotated-somatic-vcf-pass-index"}): {
        "tags": ["vcf-index", "strelka", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"tmb", "stat-somatic-tmb", "vardict"}): {
        "tags": ["vardict", "tmb"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"vcf-all", "strelka-germline", "snv", "annotated-germline-vcf-all"}): {
        "tags": ["vcf", "strelka", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "strelka-germline", "vcf-all", "snv"}): {
        "tags": ["vcf-index", "strelka", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "haplotypecaller", "snv", "annotated-germline-vcf-all"}): {
        "tags": ["vcf", "haplotype-caller", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "haplotypecaller", "snv"}): {
        "tags": ["vcf-index", "haplotype-caller", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "manta-germline", "annotated-germline-vcf-all", "sv"}): {
        "tags": ["sv-vcf", "manta", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "manta-germline", "vcf-all", "sv"}): {
        "tags": ["sv-vcf-index", "manta", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"dnascope", "vcf-all", "snv", "annotated-germline-vcf-all"}): {
        "tags": ["vcf", "scope", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "snv", "dnascope"}): {
        "tags": ["vcf-index", "scope", "normal"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-summary", "strelka-germline", "vcf-summary", "snv"}): {
        "tags": ["strelka", "normal", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"annotated-germline-vcf-summary", "haplotypecaller", "snv", "vcf-summary"}): {
        "tags": ["haplotype-caller", "normal", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"dnascope", "annotated-germline-vcf-summary", "vcf-summary", "snv"}): {
        "tags": ["scope", "normal", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"annotated-germline-vcf-summary", "manta-germline", "vcf-summary", "sv"}): {
        "tags": ["manta", "normal", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"tumor-bam", "bam"}): {
        "tags": ["bam", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset({"tumor-bam-index", "bam"}): {
        "tags": ["bam-index", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset({"cram", "tumor-cram"}): {
        "tags": ["cram", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset({"cram", "tumor-cram-index"}): {
        "tags": ["cram-index", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset({"vcf-filtered", "snv", "clinical-vcf-filtered"}): {
        "tags": ["vcf-snv-clinical", "filtered"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"clinical-vcf-filtered-index", "vcf-filtered", "snv"}): {
        "tags": ["vcf-snv-clinical-index", "filtered"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-pass", "snv", "clinical-vcf-pass"}): {
        "tags": ["vcf", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"clinical-vcf-pass-index", "vcf-pass", "snv"}): {
        "tags": ["vcf-index", "filtered"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
}

TUMOR_ONLY_WGS_TAGS = {
    frozenset({"snv", "vcf-all", "tnscope", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "vcf-all", "tnscope"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "vcf-all", "tnsnv", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "vcf-all", "tnsnv"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-summary", "snv", "tnscope", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-summary", "snv", "tnsnv", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "tnsnv", "annotated-somatic-vcf-pass", "vcf-pass"}): {"is_mandatory": True},
    frozenset({"snv", "tnsnv", "annotated-somatic-vcf-pass-index", "vcf-pass"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "tnscope", "annotated-somatic-vcf-pass", "vcf-pass"}): {"is_mandatory": True},
    frozenset({"snv", "tnscope", "annotated-somatic-vcf-pass-index", "vcf-pass"}): {
        "is_mandatory": True
    },
    frozenset({"bam", "scout-bam"}): {"is_mandatory": True},
    frozenset({"scout-bam-index", "bam"}): {"is_mandatory": True},
}

TUMOR_NORMAL_WGS_TAGS = {
    frozenset({"bam", "scout-bam"}): {"is_mandatory": True},
    frozenset({"scout-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-all", "vcf-all"}): {"is_mandatory": True},
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-all-index", "vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "annotated-somatic-vcf-all", "tnsnv", "vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "tnsnv", "vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"tnscope", "snv", "vcf-summary", "annotated-somatic-vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"vcf-summary", "snv", "tnsnv", "annotated-somatic-vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "annotated-somatic-vcf-pass", "tnsnv", "vcf-pass"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-pass-index", "snv", "tnsnv", "vcf-pass"}): {
        "is_mandatory": True
    },
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-pass", "vcf-pass"}): {"is_mandatory": True},
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-pass-index", "vcf-pass"}): {
        "is_mandatory": True
    },
}

TUMOR_ONLY_PANEL_TAGS = {
    frozenset({"tumor-bam", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-cram", "cram"}): {"is_mandatory": True},
    frozenset({"tumor-cram-index", "cram"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered-index", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass-index", "snv"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all", "vcf-all", "snv", "vardict"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "vcf-all", "snv", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"mutect", "vcf-all", "snv", "annotated-somatic-vcf-all"}): {"is_mandatory": False},
    frozenset({"mutect", "annotated-somatic-vcf-all-index", "vcf-all", "snv"}): {
        "is_mandatory": False
    },
    frozenset({"mutect", "annotated-somatic-vcf-summary", "vcf-summary", "snv"}): {
        "is_mandatory": False
    },
    frozenset({"annotated-somatic-vcf-summary", "vcf-summary", "snv", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-pass", "vcf-pass", "snv", "vardict"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "annotated-somatic-vcf-pass-index", "snv", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"mutect", "vcf-pass", "annotated-somatic-vcf-pass", "snv"}): {"is_mandatory": False},
    frozenset({"mutect", "vcf-pass", "annotated-somatic-vcf-pass-index", "snv"}): {
        "is_mandatory": False
    },
    frozenset({"stat-somatic-tmb", "tmb", "vardict"}): {"is_mandatory": True},
    frozenset({"haplotypecaller", "annotated-germline-vcf-all", "vcf-all", "snv"}): {
        "is_mandatory": True
    },
    frozenset({"haplotypecaller", "vcf-all", "snv", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"sv", "vcf-all", "manta-germline", "annotated-germline-vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"sv", "vcf-all", "manta-germline", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-all", "vcf-all", "snv", "strelka-germline"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "snv", "strelka-germline"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-all", "dnascope", "vcf-all", "snv"}): {"is_mandatory": True},
    frozenset({"dnascope", "vcf-all", "snv", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "vcf-summary", "snv", "strelka-germline"}): {
        "is_mandatory": True
    },
    frozenset({"haplotypecaller", "annotated-germline-vcf-summary", "vcf-summary", "snv"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "dnascope", "vcf-summary", "snv"}): {
        "is_mandatory": True
    },
    frozenset({"sv", "annotated-germline-vcf-summary", "vcf-summary", "manta-germline"}): {
        "is_mandatory": True
    },
}

TUMOR_NORMAL_PANEL_TAGS = {
    frozenset({"normal-bam", "bam"}): {"is_mandatory": True},
    frozenset({"normal-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"normal-cram", "cram"}): {"is_mandatory": True},
    frozenset({"cram", "normal-cram-index"}): {"is_mandatory": True},
    frozenset({"snv", "vcf-all", "vardict", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "vcf-all", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"strelka", "snv", "vcf-all", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "strelka", "snv", "vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"mutect", "snv", "vcf-all", "annotated-somatic-vcf-all"}): {"is_mandatory": False},
    frozenset({"mutect", "annotated-somatic-vcf-all-index", "snv", "vcf-all"}): {
        "is_mandatory": False
    },
    frozenset({"vcf-summary", "snv", "annotated-somatic-vcf-summary", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"mutect", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "is_mandatory": False
    },
    frozenset({"strelka", "snv", "vcf-summary", "annotated-somatic-vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"mutect", "vcf-pass", "snv", "annotated-somatic-vcf-pass"}): {"is_mandatory": False},
    frozenset({"mutect", "vcf-pass", "snv", "annotated-somatic-vcf-pass-index"}): {
        "is_mandatory": False
    },
    frozenset({"vcf-pass", "snv", "annotated-somatic-vcf-pass", "vardict"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "snv", "annotated-somatic-vcf-pass-index", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"vcf-pass", "strelka", "snv", "annotated-somatic-vcf-pass"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "strelka", "snv", "annotated-somatic-vcf-pass-index"}): {
        "is_mandatory": True
    },
    frozenset({"stat-somatic-tmb", "tmb", "vardict"}): {"is_mandatory": True},
    frozenset({"strelka-germline", "snv", "vcf-all", "annotated-germline-vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"strelka-germline", "snv", "vcf-all", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"haplotypecaller", "snv", "vcf-all", "annotated-germline-vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"haplotypecaller", "snv", "vcf-all", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"vcf-all", "manta-germline", "annotated-germline-vcf-all", "sv"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "manta-germline", "sv"}): {
        "is_mandatory": True
    },
    frozenset({"snv", "vcf-all", "dnascope", "annotated-germline-vcf-all"}): {"is_mandatory": True},
    frozenset({"snv", "vcf-all", "dnascope", "annotated-germline-vcf-all-index"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "strelka-germline", "snv", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "haplotypecaller", "snv", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "vcf-summary", "snv", "dnascope"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "vcf-summary", "manta-germline", "sv"}): {
        "is_mandatory": True
    },
    frozenset({"tumor-bam", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"cram", "tumor-cram"}): {"is_mandatory": True},
    frozenset({"cram", "tumor-cram-index"}): {"is_mandatory": True},
}
