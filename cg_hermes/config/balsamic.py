"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not mandatory by default.
However the tags that are available to a particular analysis is mandatory for that analysis.
"""

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
    frozenset({"coverage-qc-report"}): {
        "tags": ["delivery-report"],
        "is_mandatory": False,
        "used_by": ["scout"],
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
        "tags": ["vcf", "tumor", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "tnhaplotyper", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "tumor", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "tnscope", "snv", "annotated-somatic-vcf-all"}): {
        "tags": ["tumor", "tnscope", "vcf-snv-research", "somatic"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "tnscope", "snv", "annotated-somatic-vcf-all-index"}): {
        "tags": ["tumor", "tnscope", "vcf-snv-research-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "manta", "annotated-somatic-vcf-all", "sv"}): {
        "tags": ["vcf-sv-research", "manta", "tumor", "somatic"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "annotated-somatic-vcf-all-index", "manta", "sv"}): {
        "tags": ["vcf-sv-research-index", "manta", "tumor", "somatic"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-all", "cnvkit", "cnv", "annotated-somatic-vcf-all"}): {
        "tags": ["cnvkit", "sv-vcf", "tumor", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"vcf-all", "cnvkit", "annotated-somatic-vcf-all-index", "cnv"}): {
        "tags": ["cnvkit", "sv-vcf-index", "tumor", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset({"tnscope", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["sention", "tnscope", "vcf-report", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"tnhaplotyper", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["sention", "haplotype-caller", "vcf-report", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"vcf-summary", "manta", "annotated-somatic-vcf-summary", "sv"}): {
        "tags": ["sention", "manta", "vcf-report", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset({"vcf-summary", "cnvkit", "cnv", "annotated-somatic-vcf-summary"}): {
        "tags": ["cnvkit", "vcf-report", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
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
        "tags": ["vcf", "vardict", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "snv", "vardict", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "vardict", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vardict", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["vardict", "vcf-report", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"vcf-all", "snv", "tnscope-umi", "annotated-somatic-vcf-all"}): {
        "tags": ["vcf", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage", "deliver"],
    },
    frozenset({"vcf-all", "snv", "tnscope-umi", "annotated-somatic-vcf-all-index"}): {
        "tags": ["vcf-index", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage", "deliver"],
    },
    frozenset({"tnscope-umi", "vcf-summary", "snv", "annotated-somatic-vcf-summary"}): {
        "tags": ["tnscope-umi", "vcf-report", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"tmb", "stat-somatic-tmb", "vardict"}): {
        "tags": ["vardict", "tmb"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"vcf-all", "haplotypecaller", "snv", "annotated-germline-vcf-all"}): {
        "tags": ["vcf", "haplotype-caller", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "haplotypecaller", "snv"}): {
        "tags": ["vcf-index", "haplotype-caller", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"vcf-all", "manta-germline", "annotated-germline-vcf-all", "sv"}): {
        "tags": ["sv-vcf", "manta", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "manta-germline", "vcf-all", "sv"}): {
        "tags": ["sv-vcf-index", "manta", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"dnascope", "vcf-all", "snv", "annotated-germline-vcf-all"}): {
        "tags": ["vcf", "dnascope", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-all-index", "vcf-all", "snv", "dnascope"}): {
        "tags": ["vcf-index", "dnascope", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset({"annotated-germline-vcf-summary", "haplotypecaller", "snv", "vcf-summary"}): {
        "tags": ["haplotype-caller", "germline", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"dnascope", "annotated-germline-vcf-summary", "vcf-summary", "snv"}): {
        "tags": ["dnascope", "germline", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"annotated-germline-vcf-summary", "manta-germline", "vcf-summary", "sv"}): {
        "tags": ["manta", "germline", "vcf-report"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset({"tumor-bam", "bam"}): {
        "tags": ["bam", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"tumor-bam-index", "bam"}): {
        "tags": ["bam-index", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"cram", "tumor-cram"}): {
        "tags": ["cram", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"cram", "tumor-cram-index"}): {
        "tags": ["cram-index", "tumor"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-filtered", "snv", "clinical-vcf-filtered"}): {
        "tags": ["vcf", "vcf-snv-filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"clinical-vcf-filtered-index", "vcf-filtered", "snv"}): {
        "tags": ["vcf-index", "vcf-snv-filtered-index", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset({"vcf-pass", "snv", "clinical-vcf-pass"}): {
        "tags": ["vcf", "vcf-snv-clinical", "somatic"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"clinical-vcf-pass-index", "vcf-pass", "snv"}): {
        "tags": ["vcf-index", "vcf-snv-clinical-index", "somatic"],
        "is_mandatory": True,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"vcf-sv-pass", "sv", "clinical-vcf-sv-pass"}): {
        "tags": ["vcf", "vcf-sv-clinical", "somatic"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
    frozenset({"clinical-vcf-sv-pass-index", "vcf-sv-pass", "sv"}): {
        "tags": ["vcf-index", "vcf-sv-clinical-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["scout", "deliver"],
    },
}

TUMOR_ONLY_WGS_TAGS = {
    frozenset({"snv", "vcf-all", "tnscope", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "vcf-all", "tnscope"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-summary", "snv", "tnscope", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"tumor-bam", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-cram", "cram"}): {"is_mandatory": True},
    frozenset({"tumor-cram-index", "cram"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered-index", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass-index", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass", "sv"}): {"is_mandatory": False},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass-index", "sv"}): {"is_mandatory": False},
}

TUMOR_NORMAL_WGS_TAGS = {
    frozenset({"normal-bam", "bam"}): {"is_mandatory": True},
    frozenset({"normal-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"normal-cram", "cram"}): {"is_mandatory": True},
    frozenset({"cram", "normal-cram-index"}): {"is_mandatory": True},
    frozenset({"tumor-bam", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-cram", "cram"}): {"is_mandatory": True},
    frozenset({"tumor-cram-index", "cram"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered-index", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass-index", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass", "sv"}): {"is_mandatory": False},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass-index", "sv"}): {"is_mandatory": False},
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-all", "vcf-all"}): {"is_mandatory": True},
    frozenset({"tnscope", "snv", "annotated-somatic-vcf-all-index", "vcf-all"}): {
        "is_mandatory": True
    },
    frozenset({"tnscope", "snv", "vcf-summary", "annotated-somatic-vcf-summary"}): {
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
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass", "sv"}): {"is_mandatory": False},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass-index", "sv"}): {"is_mandatory": False},
    frozenset({"vcf-all", "snv", "tnscope-umi", "annotated-somatic-vcf-all"},): {"is_mandatory": True},
    frozenset({"vcf-all", "snv", "tnscope-umi", "annotated-somatic-vcf-all-index"},): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-summary", "tnscope-umi", "snv", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-all", "vcf-all", "snv", "vardict"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "vcf-all", "snv", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-somatic-vcf-summary", "vcf-summary", "snv", "vardict"}): {
        "is_mandatory": True
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
    frozenset({"annotated-germline-vcf-all", "dnascope", "vcf-all", "snv"}): {"is_mandatory": True},
    frozenset({"dnascope", "vcf-all", "snv", "annotated-germline-vcf-all-index"}): {
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
    frozenset({"tumor-bam", "bam"}): {"is_mandatory": True},
    frozenset({"tumor-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"cram", "tumor-cram"}): {"is_mandatory": True},
    frozenset({"cram", "tumor-cram-index"}): {"is_mandatory": True},
    frozenset({"normal-bam", "bam"}): {"is_mandatory": True},
    frozenset({"normal-bam-index", "bam"}): {"is_mandatory": True},
    frozenset({"normal-cram", "cram"}): {"is_mandatory": True},
    frozenset({"cram", "normal-cram-index"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"clinical-vcf-filtered-index", "snv", "vcf-filtered"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-pass", "clinical-vcf-pass-index", "snv"}): {"is_mandatory": True},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass", "sv"}): {"is_mandatory": False},
    frozenset({"vcf-sv-pass", "clinical-vcf-sv-pass-index", "sv"}): {"is_mandatory": False},
    frozenset({"snv", "vcf-all", "vardict", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-all-index", "snv", "vcf-all", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"vcf-summary", "snv", "annotated-somatic-vcf-summary", "vardict"}): {
        "is_mandatory": True
    },
    frozenset({"stat-somatic-tmb", "tmb", "vardict"}): {"is_mandatory": True},
    frozenset({"snv", "vcf-all", "tnscope-umi", "annotated-somatic-vcf-all"}): {"is_mandatory": True},
    frozenset({"vcf-all", "snv", "tnscope-umi", "annotated-somatic-vcf-all-index"},): {"is_mandatory": True},
    frozenset({"annotated-somatic-vcf-summary", "tnscope-umi", "snv", "vcf-summary"}): {
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
    frozenset({"annotated-germline-vcf-summary", "haplotypecaller", "snv", "vcf-summary"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "vcf-summary", "snv", "dnascope"}): {
        "is_mandatory": True
    },
    frozenset({"annotated-germline-vcf-summary", "vcf-summary", "manta-germline", "sv"}): {
        "is_mandatory": True
    },
}
