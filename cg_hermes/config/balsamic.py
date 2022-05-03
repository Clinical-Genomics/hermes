"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

TAGS = {
    # Config, QC and reports (PANEL & WGS)
    "config.json": ["balsamic-config"],
    "report.html": ["balsamic-report"],
    "BALSAMIC_X.X.X_graph.pdf": ["balsamic-dag"],
    "metrics_deliverables.yaml": ["yaml", "qc-metrics-yaml"],
    "multiqc_report.html": ["html", "multiqc-html"],
    "multiqc_data.json": ["json", "multiqc-json"],
    # Alignment files (PANEL & WGS)
    "tumor.merged.cram": ["cram", "tumor-cram"],
    "tumor.merged.cram.crai": ["cram", "tumor-cram-index"],
    "normal.merged.cram": ["cram", "normal-cram"],
    "normal.merged.cram.crai": ["cram", "normal-cram-index"],
    "tumor_umi_consensusfiltered.merged.cram": ["cram", "umi-tumor-cram"],
    "tumor_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-tumor-cram-index"],
    "normal_umi_consensusfiltered.merged.cram": ["cram", "umi-normal-cram"],
    "normal_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-normal-cram-index"],
    # Merged SV (manta, delly) and CNV (cnvkit, ascat) callers (PANEL & WGS)
    "svdb.vcf.gz": ["vcf-svdb", "research-vcf-svdb"],
    "svdb.vcf.gz.tbi": ["vcf-svdb", "research-vcf-svdb-index"],
    "svdb.all.filtered.pass.vcf.gz": ["vcf-pass-svdb", "clinical-vcf-pass-svdb"],
    "svdb.all.filtered.pass.vcf.gz.tbi": ["vcf-pass-svdb", "clinical-vcf-pass-svdb-index"],
    # Germline SNVs (PANEL & WGS)
    "germline.tumor_normal.dnascope.vcf.gz": [
        "vcf-all",
        "snv",
        "dnascope",
        "annotated-germline-vcf-all",
    ],
    "germline.tumor_normal.dnascope.vcf.gz.tbi": [
        "vcf-all",
        "snv",
        "dnascope",
        "annotated-germline-vcf-all-index",
    ],
    # Germline SVs (PANEL & WGS)
    "germline.tumor_normal.manta_germline.vcf.gz": [
        "vcf-all",
        "sv",
        "manta-germline",
        "annotated-germline-vcf-all",
    ],
    "germline.tumor_normal.manta_germline.vcf.gz.tbi": [
        "vcf-all",
        "sv",
        "manta-germline",
        "annotated-germline-vcf-all-index",
    ],
    # SNVs (WGS)
    "tnscope.vcf.gz": [
        "vcf-tnscope",
        "research-vcf-tnscope",
    ],
    "tnscope.vcf.gz.tbi": [
        "vcf-tnscope",
        "research-vcf-tnscope-index",
    ],
    "tnscope.all.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope",
        "snv",
        "clinical-vcf-pass-tnscope",
    ],
    "tnscope.all.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope",
        "snv",
        "clinical-vcf-pass-tnscope-index",
    ],
    # SNVs/INDELs (PANEL)
    # vardict
    "vardict.vcf.gz": [
        "vcf-vardict",
        "research-vcf-vardict",
    ],
    "vardict.vcf.gz.tbi": [
        "vcf-vardict",
        "research-vcf-vardict-index",
    ],
    "vardict.all.filtered.pass.vcf.gz": [
        "vcf-pass-vardict",
        "snv",
        "clinical-vcf-pass-vardict",
    ],
    "vardict.all.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-vardict",
        "snv",
        "clinical-vcf-pass-vardict-index",
    ],
    # TNscope_umi
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
    # CNVs (PANEL)
    "tumor.merged.cns": ["cns", "cnv-cns"],
    "tumor.merged-scatter.pdf": ["scatter", "cnv-scatter"],
    "tumor.merged-diagram.pdf": ["diagram", "cnv-diagram"],
    "gene_metrics": ["gene-metrics", "cnv-gene-metrics"],
    "cnvkit.vcf2cytosure.cgh": ["cgh-file", "cnv-somatic-cgh-file"],
    # CNVs (WGS)
    "ascat.output.pdf": ["ascat-pdf", "clinical-ascat-pdf"],
    "ascat.copynumber.txt.gz": ["ascat-copynumber", "clinical-ascat-copynumber"],
    # CNVs (PANEL & WGS)
    "dellycnv.cov.gz": ["rd-delly", "clinical-rd-delly"],
}

BALSAMIC_COMMON_TAGS = {
    # Config, QC and reports (PANEL & WGS)
    frozenset(TAGS["config.json"]): {  # BALSAMIC config json
        "tags": ["balsamic-config"],
        "is_mandatory": True,
        "used_by": ["audit", "cg"],
    },
    frozenset(TAGS["report.html"]): {  # BALSAMIC report html
        "tags": ["balsamic-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["BALSAMIC_X.X.X_graph.pdf"]): {  # DAG
        "tags": ["balsamic-dag"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["metrics_deliverables.yaml"]): {  # QC metrics
        "tags": ["qc-metrics"],
        "is_mandatory": True,
        "used_by": ["audit", "cg", "vogue"],
    },
    frozenset(TAGS["multiqc_report.html"]): {  # MultiQC html
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": ["audit", "deliver", "scout"],
    },
    frozenset(TAGS["multiqc_data.json"]): {  # MultiQC json
        "tags": ["multiqc-json"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    # Alignment files (PANEL & WGS)
    frozenset(TAGS["tumor.merged.cram"]): {  # cram (tumor)
        "tags": ["tumor", "cram"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["tumor.merged.cram.crai"]): {
        "tags": ["tumor", "cram-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal.merged.cram"]): {  # cram (normal)
        "tags": ["normal", "cram"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal.merged.cram.crai"]): {
        "tags": ["normal", "cram-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram"]): {  # UMI cram (tumor)
        "tags": ["umi-cram", "tumor"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram.crai"]): {
        "tags": ["umi-cram-index", "tumor"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal_umi_consensusfiltered.merged.cram"]): {  # UMI cram (normal)
        "tags": ["umi-cram", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal_umi_consensusfiltered.merged.cram.crai"]): {
        "tags": ["umi-cram-index", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # Merged SV (manta, delly) and CNV (cnvkit, ascat) callers (PANEL & WGS)
    frozenset(TAGS["svdb.vcf.gz"]): {
        "tags": ["svdb", "vcf-sv-research"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["svdb.vcf.gz.tbi"]): {
        "tags": ["svdb", "vcf-sv-research-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["svdb.all.filtered.pass.vcf.gz"]): {
        "tags": ["svdb", "vcf-sv-clinical"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["svdb.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["svdb", "vcf-sv-clinical-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    # Germline SNVs (PANEL & WGS)
    frozenset(TAGS["germline.tumor_normal.dnascope.vcf.gz"]): {
        "tags": ["dnascope", "germline", "vcf"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["germline.tumor_normal.dnascope.vcf.gz.tbi"]): {
        "tags": ["dnascope", "germline", "vcf-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    # Germline SVs (PANEL & WGS)
    frozenset(TAGS["germline.tumor_normal.manta_germline.vcf.gz"]): {
        "tags": ["manta", "germline", "vcf"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["germline.tumor_normal.manta_germline.vcf.gz.tbi"]): {
        "tags": ["manta", "germline", "vcf-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    # SNVs (WGS)
    frozenset(TAGS["tnscope.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-research"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-research-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-clinical"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-clinical-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNVs (WGS)
    frozenset(TAGS["ascat.output.pdf"]): {
        "tags": ["ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["ascat.copynumber.txt.gz"]): {
        "tags": ["ascatngs", "metrics"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    # SNVs/INDELs (PANEL)
    # vardict
    frozenset(TAGS["vardict.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-research"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-research-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-clinical"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-clinical-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # TNscope_umi
    frozenset(TAGS["TNscope_umi.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-research"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["TNscope_umi.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-research-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope-umi", "vcf-umi-clinical"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope-umi", "vcf-umi-clinical-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNVs (PANEL)
    frozenset(TAGS["tumor.merged.cns"]): {
        "tags": ["cnvkit", "metrics", "segments"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {
        "tags": ["cnvkit", "visualization", "scatter"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {
        "tags": ["cnvkit", "visualization", "diagram"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["gene_metrics"]): {
        "tags": ["cnvkit", "metrics", "genes"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["cnvkit.vcf2cytosure.cgh"]): {
        "tags": ["cnvkit", "vcf2cytosure"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNVs (PANEL & WGS)
    frozenset(TAGS["dellycnv.cov.gz"]): {
        "tags": ["delly", "metrics"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
}


TUMOR_ONLY_WGS_TAGS = {
    # SNVs (WGS)
    frozenset(TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL & WGS)
    frozenset(TAGS["dellycnv.cov.gz"]): {"is_mandatory": True},
}


TUMOR_NORMAL_WGS_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
    # SNVs (WGS)
    frozenset(TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (WGS)
    frozenset(TAGS["ascat.output.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.copynumber.txt.gz"]): {"is_mandatory": True},
}


TUMOR_ONLY_PANEL_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram.crai"]): {"is_mandatory": True},
    # SNVs/INDELs (PANEL)
    # vardict
    frozenset(TAGS["vardict.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # TNscope_umi
    frozenset(TAGS["TNscope_umi.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
    # CNVs (PANEL & WGS)
    frozenset(TAGS["dellycnv.cov.gz"]): {"is_mandatory": True},
}


TUMOR_NORMAL_PANEL_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_umi_consensusfiltered.merged.cram.crai"]): {"is_mandatory": True},
    frozenset(TAGS["normal_umi_consensusfiltered.merged.cram"]): {"is_mandatory": True},
    frozenset(TAGS["normal_umi_consensusfiltered.merged.cram.crai"]): {"is_mandatory": True},
    # SNVs/INDELs (PANEL)
    # vardict
    frozenset(TAGS["vardict.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # TNscope_umi
    frozenset(TAGS["TNscope_umi.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
}
