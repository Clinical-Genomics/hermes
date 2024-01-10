"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

RAW_TAGS = {
    # Config, QC and reports (PANEL & WGS)
    "config.json": ["balsamic-config"],
    "report.html": ["balsamic-report"],
    "BALSAMIC_X.X.X_graph.pdf": ["balsamic-dag"],
    "multiqc_report.html": ["html", "multiqc-html"],
    "multiqc_data.json": ["json", "multiqc-json"],
    # Custom QC
    "metrics_deliverables.yaml": ["yaml", "qc-metrics-yaml"],
    # Alignment files (PANEL & WGS)
    "tumor.merged.cram": ["cram", "tumor-cram"],
    "tumor.merged.cram.crai": ["cram", "tumor-cram-index"],
    "normal.merged.cram": ["cram", "normal-cram"],
    "normal.merged.cram.crai": ["cram", "normal-cram-index"],
    # UMI alignment files (PANEL)
    "tumor_umi_consensusfiltered.merged.cram": ["cram", "umi-tumor-cram"],
    "tumor_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-tumor-cram-index"],
    "normal_umi_consensusfiltered.merged.cram": ["cram", "umi-normal-cram"],
    "normal_umi_consensusfiltered.merged.cram.crai": ["cram", "umi-normal-cram-index"],
    # Germline SNVs (PANEL & WGS)
    "germline.tumor.dnascope.vcf.gz": [
        "vcf-tumor",
        "snv",
        "dnascope",
        "germline-vcf-tumor",
    ],
    "germline.tumor.dnascope.vcf.gz.tbi": [
        "vcf-tumor",
        "snv",
        "dnascope",
        "germline-vcf-tumor-index",
    ],
    "germline.normal.dnascope.vcf.gz": [
        "vcf-normal",
        "snv",
        "dnascope",
        "germline-vcf-normal",
    ],
    "germline.normal.dnascope.vcf.gz.tbi": [
        "vcf-normal",
        "snv",
        "dnascope",
        "germline-vcf-normal-index",
    ],
    "genotype.normal.dnascope.vcf.gz": [
        "vcf-dnascope",
        "genotype-vcf-dnascope",
    ],
    "genotype.normal.dnascope.vcf.gz.tbi": [
        "vcf-dnascope",
        "genotype-vcf-dnascope-index",
    ],
    # Germline SVs (PANEL & WGS)
    "germline.tumor.manta_germline.vcf.gz": [
        "vcf-tumor",
        "sv",
        "manta-germline",
        "germline-vcf-tumor",
    ],
    "germline.tumor.manta_germline.vcf.gz.tbi": [
        "vcf-tumor",
        "sv",
        "manta-germline",
        "germline-vcf-tumor-index",
    ],
    "germline.normal.manta_germline.vcf.gz": [
        "vcf-normal",
        "sv",
        "manta-germline",
        "germline-vcf-normal",
    ],
    "germline.normal.manta_germline.vcf.gz.tbi": [
        "vcf-normal",
        "sv",
        "manta-germline",
        "germline-vcf-normal-index",
    ],
    # Merged SV (manta, delly) and CNV (cnvkit, ascat) callers (PANEL & WGS)
    "svdb.vcf.gz": ["vcf-svdb", "research-vcf-svdb"],
    "svdb.vcf.gz.tbi": ["vcf-svdb", "research-vcf-svdb-index"],
    "svdb.research.filtered.pass.vcf.gz": ["vcf-pass-svdb", "research-vcf-pass-svdb"],
    "svdb.research.filtered.pass.vcf.gz.tbi": ["vcf-pass-svdb", "research-vcf-pass-svdb-index"],
    "svdb.clinical.filtered.pass.vcf.gz": ["vcf-pass-svdb", "clinical-vcf-pass-svdb"],
    "svdb.clinical.filtered.pass.vcf.gz.tbi": ["vcf-pass-svdb", "clinical-vcf-pass-svdb-index"],
    # SNVs (WGS)
    "tnscope.vcf.gz": [
        "vcf-tnscope",
        "research-vcf-tnscope",
    ],
    "tnscope.vcf.gz.tbi": [
        "vcf-tnscope",
        "research-vcf-tnscope-index",
    ],
    "tnscope.research.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope",
        "snv",
        "research-vcf-pass-tnscope",
    ],
    "tnscope.research.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope",
        "snv",
        "research-vcf-pass-tnscope-index",
    ],
    "tnscope.clinical.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope",
        "snv",
        "clinical-vcf-pass-tnscope",
    ],
    "tnscope.clinical.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope",
        "snv",
        "clinical-vcf-pass-tnscope-index",
    ],
    # SNVs/INDELs (PANEL)
    "vardict.vcf.gz": [
        "vcf-vardict",
        "research-vcf-vardict",
    ],
    "vardict.vcf.gz.tbi": [
        "vcf-vardict",
        "research-vcf-vardict-index",
    ],
    "vardict.research.filtered.pass.vcf.gz": [
        "vcf-pass-vardict",
        "snv",
        "research-vcf-pass-vardict",
    ],
    "vardict.research.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-vardict",
        "snv",
        "research-vcf-pass-vardict-index",
    ],
    "vardict.clinical.filtered.pass.vcf.gz": [
        "vcf-pass-vardict",
        "snv",
        "clinical-vcf-pass-vardict",
    ],
    "vardict.clinical.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-vardict",
        "snv",
        "clinical-vcf-pass-vardict-index",
    ],
    # UMI SNVs/INDELs (PANEL)
    "tnscope_umi.vcf.gz": [
        "vcf-tnscope-umi",
        "research-vcf-tnscope-umi",
    ],
    "tnscope_umi.vcf.gz.tbi": [
        "vcf-tnscope-umi",
        "research-vcf-tnscope-umi-index",
    ],
    "tnscope_umi.research.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope-umi",
        "snv",
        "research-vcf-pass-tnscope-umi",
    ],
    "tnscope_umi.research.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope-umi",
        "snv",
        "research-vcf-pass-tnscope-umi-index",
    ],
    "tnscope_umi.clinical.filtered.pass.vcf.gz": [
        "vcf-pass-tnscope-umi",
        "snv",
        "clinical-vcf-pass-tnscope-umi",
    ],
    "tnscope_umi.clinical.filtered.pass.vcf.gz.tbi": [
        "vcf-pass-tnscope-umi",
        "snv",
        "clinical-vcf-pass-tnscope-umi-index",
    ],
    # CNVs (PANEL)
    "tumor.merged.cns": ["cns", "cnv-cns"],
    "tumor.merged.cnr": ["cnr", "cnv-cnr"],
    "gene_metrics": ["gene-metrics", "cnv-gene-metrics"],
    "cnvkit.vcf2cytosure.cgh": ["cgh-tumor", "cnv-somatic-cgh-tumor"],
    # CNVs (WGS)
    "ascat.copynumber.txt.gz": ["ascat-copynumber", "clinical-ascat-copynumber"],
    "dellycnv.cov.gz": ["rd-delly", "clinical-rd-delly"],
    "tumor.vcf2cytosure.cgh": ["cgh-tumor", "cnv-somatic-cgh-tumor"],
    "normal.vcf2cytosure.cgh": ["cgh-normal", "cnv-somatic-cgh-normal"],
    "cov.bed.gz": ["cov", "gens-bed", "cnv-gens-bed"],
    "cov.bed.gz.tbi": ["cov", "gens-bed", "cnv-gens-bed-index"],
    "baf.bed.gz": ["baf", "gens-bed", "cnv-gens-bed"],
    "baf.bed.gz.tbi": ["baf", "gens-bed", "cnv-gens-bed-index"],
    # CNV report
    "report.pdf": ["cnv-report-pdf", "clinical-cnv-report-pdf"],
    "cnvpytor.circular.png": ["circular-cnvpytor", "clinical-circular-cnvpytor"],
    "cnvpytor.scatter.png": ["scatter-cnvpytor", "clinical-scatter-cnvpytor"],
    "ascat.ascatprofile.png": ["plot-ascat-profile", "clinical-plot-ascat-profile"],
    "ascat.rawprofile.png": ["plot-raw-profile", "clinical-plot-raw-profile"],
    "ascat.ASPCF.png": ["plot-aspcf", "clinical-plot-aspcf"],
    "ascat.tumor.png": ["plot-tumor", "clinical-plot-tumor"],
    "ascat.germline.png": ["plot-germline", "clinical-plot-germline"],
    "ascat.sunrise.png": ["plot-sunrise", "clinical-plot-sunrise"],
    # SVs (WGS)
    "tumor.tiddit_cov.bed": ["cov-tumor-tiddit", "clinical-cov-tumor-tiddit"],
    "normal.tiddit_cov.bed": ["cov-normal-tiddit", "clinical-cov-normal-tiddit"],
    # TMB (PANEL)
    "vardict.balsamic_stat": ["snv", "vardict", "tmb", "research-tmb"],
    "tnscope_umi.balsamic_stat": ["snv", "tnscope-umi", "tmb", "research-tmb"],
    # TMB (WGS)
    "tnscope.balsamic_stat": ["snv", "tnscope", "tmb", "research-tmb"],
}

QC_TAGS = {
    # Config, QC and reports (PANEL & WGS)
    frozenset(RAW_TAGS["config.json"]): {  # BALSAMIC config json
        "tags": ["balsamic-config"],
        "is_mandatory": True,
        "used_by": ["audit", "cg"],
    },
    frozenset(RAW_TAGS["report.html"]): {  # BALSAMIC report html
        "tags": ["balsamic-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(RAW_TAGS["BALSAMIC_X.X.X_graph.pdf"]): {  # DAG
        "tags": ["balsamic-dag"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(RAW_TAGS["multiqc_report.html"]): {  # MultiQC html
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": ["audit", "deliver", "scout"],
    },
    frozenset(RAW_TAGS["multiqc_data.json"]): {  # MultiQC json
        "tags": ["multiqc-json"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    # Custom QC
    frozenset(RAW_TAGS["metrics_deliverables.yaml"]): {  # QC metrics
        "tags": ["qc-metrics"],
        "is_mandatory": True,
        "used_by": ["audit", "cg", "vogue"],
    },
}

ALIGNMENT_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["tumor.merged.cram"]): {  # cram (tumor)
        "tags": ["tumor", "cram"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["tumor.merged.cram.crai"]): {
        "tags": ["tumor", "cram-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["normal.merged.cram"]): {  # cram (normal)
        "tags": ["normal", "cram"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {
        "tags": ["normal", "cram-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
}

GERMLINE_TAGS = {
    # Germline SNVs (PANEL & WGS)
    frozenset(RAW_TAGS["germline.tumor.dnascope.vcf.gz"]): {
        "tags": ["germline", "vcf-snv-germline-tumor"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.tumor.dnascope.vcf.gz.tbi"]): {
        "tags": ["germline", "vcf-snv-germline-tumor-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz"]): {
        "tags": ["germline", "vcf-snv-germline-normal"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz.tbi"]): {
        "tags": ["germline", "vcf-snv-germline-normal-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz"]): {
        "tags": ["dnascope", "normal", "vcf"],
        "is_mandatory": False,
        "used_by": ["cg", "genotype"],
    },
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz.tbi"]): {
        "tags": ["dnascope", "normal", "vcf-index"],
        "is_mandatory": False,
        "used_by": ["cg", "genotype"],
    },
    # Germline SVs (PANEL & WGS)
    frozenset(RAW_TAGS["germline.tumor.manta_germline.vcf.gz"]): {
        "tags": ["germline", "vcf-sv-germline-tumor"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.tumor.manta_germline.vcf.gz.tbi"]): {
        "tags": ["germline", "vcf-sv-germline-tumor-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz"]): {
        "tags": ["germline", "vcf-sv-germline-normal"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz.tbi"]): {
        "tags": ["germline", "vcf-sv-germline-normal-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
}

CALLERS_TAGS = {
    # Merged SV (manta, delly) and CNV (cnvkit, ascat) callers (PANEL & WGS)
    frozenset(RAW_TAGS["svdb.vcf.gz"]): {
        "tags": ["svdb", "vcf-sv"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["svdb.vcf.gz.tbi"]): {
        "tags": ["svdb", "vcf-sv-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["svdb.research.filtered.pass.vcf.gz"]): {
        "tags": ["svdb", "vcf-sv-research"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["svdb.research.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["svdb", "vcf-sv-research-index"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["svdb.clinical.filtered.pass.vcf.gz"]): {
        "tags": ["svdb", "vcf-sv-clinical"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["svdb.clinical.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["svdb", "vcf-sv-clinical-index"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    # SNVs (WGS)
    frozenset(RAW_TAGS["tnscope.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-research"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-research-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-clinical"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-clinical-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNVs (WGS)
    frozenset(RAW_TAGS["ascat.copynumber.txt.gz"]): {
        "tags": ["ascatngs", "metrics"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["dellycnv.cov.gz"]): {
        "tags": ["delly", "coverage"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tumor.vcf2cytosure.cgh"]): {
        "tags": ["tiddit", "tumor", "vcf2cytosure"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["normal.vcf2cytosure.cgh"]): {
        "tags": ["tiddit", "normal", "vcf2cytosure"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["cov.bed.gz"]): {
        "tags": ["gens", "coverage", "bed"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(RAW_TAGS["cov.bed.gz.tbi"]): {
        "tags": ["gens", "coverage", "bed-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(RAW_TAGS["baf.bed.gz"]): {
        "tags": ["gens", "fracsnp", "bed"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(RAW_TAGS["baf.bed.gz.tbi"]): {
        "tags": ["gens", "fracsnp", "bed-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    # SNVs/INDELs (PANEL)
    frozenset(RAW_TAGS["vardict.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["vardict.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-research"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-research-index"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-clinical"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-clinical-index"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNVs (PANEL)
    frozenset(RAW_TAGS["tumor.merged.cns"]): {
        "tags": ["cnvkit", "metrics", "segments"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["tumor.merged.cnr"]): {
        "tags": ["cnvkit", "regions"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["gene_metrics"]): {
        "tags": ["cnvkit", "metrics", "genes"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["cnvkit.vcf2cytosure.cgh"]): {
        "tags": ["cnvkit", "tumor", "vcf2cytosure"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # CNV report
    frozenset(RAW_TAGS["report.pdf"]): {
        "tags": ["cnv-report"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(RAW_TAGS["cnvpytor.circular.png"]): {
        "tags": ["circular-plot", "cnvpytor", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["cnvpytor.scatter.png"]): {
        "tags": ["scatter-plot", "cnvpytor", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.ascatprofile.png"]): {
        "tags": ["profile-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.rawprofile.png"]): {
        "tags": ["raw-profile-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.ASPCF.png"]): {
        "tags": ["aspcf-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.tumor.png"]): {
        "tags": ["tumor-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.germline.png"]): {
        "tags": ["germline-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(RAW_TAGS["ascat.sunrise.png"]): {
        "tags": ["sunrise-plot", "ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    # SVs (WGS)
    frozenset(RAW_TAGS["tumor.tiddit_cov.bed"]): {
        "tags": ["tiddit", "tumor", "coverage"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(RAW_TAGS["normal.tiddit_cov.bed"]): {
        "tags": ["tiddit", "normal", "coverage"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    # TMB (PANEL)
    frozenset(RAW_TAGS["vardict.balsamic_stat"]): {
        "tags": ["research", "vardict", "tmb"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    # TMB (WGS)
    frozenset(RAW_TAGS["tnscope.balsamic_stat"]): {
        "tags": ["research", "tnscope", "tmb"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
}

BALSAMIC_TAGS = {
    **QC_TAGS,
    **ALIGNMENT_TAGS,
    **GERMLINE_TAGS,
    **CALLERS_TAGS,
}

TUMOR_ONLY_WGS_TAGS = {
    # SNVs (WGS)
    frozenset(RAW_TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (WGS)
    frozenset(RAW_TAGS["tumor.vcf2cytosure.cgh"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cov.bed.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cov.bed.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["baf.bed.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["baf.bed.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvpytor.circular.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvpytor.scatter.png"]): {"is_mandatory": True},
    # SVs (WGS)
    frozenset(RAW_TAGS["tumor.tiddit_cov.bed"]): {"is_mandatory": True},
    # TMB (WGS)
    frozenset(RAW_TAGS["tnscope.balsamic_stat"]): {"is_mandatory": True},
}

TUMOR_NORMAL_WGS_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
    # Germline SNVs (PANEL & WGS)
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.dnascope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["germline.normal.manta_germline.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["genotype.normal.dnascope.vcf.gz.tbi"]): {"is_mandatory": True},
    # SNVs (WGS)
    frozenset(RAW_TAGS["tnscope.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.research.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tnscope.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (WGS)
    frozenset(RAW_TAGS["ascat.copynumber.txt.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tumor.vcf2cytosure.cgh"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.vcf2cytosure.cgh"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cov.bed.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cov.bed.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["baf.bed.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["baf.bed.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.ascatprofile.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.rawprofile.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.ASPCF.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.tumor.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.germline.png"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["ascat.sunrise.png"]): {"is_mandatory": True},
    # SVs (WGS)
    frozenset(RAW_TAGS["tumor.tiddit_cov.bed"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.tiddit_cov.bed"]): {"is_mandatory": True},
    # TMB (WGS)
    frozenset(RAW_TAGS["tnscope.balsamic_stat"]): {"is_mandatory": True},
}

TUMOR_ONLY_PANEL_TAGS = {
    # SNVs/INDELs (PANEL)
    frozenset(RAW_TAGS["vardict.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(RAW_TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
    # TMB (PANEL)
    frozenset(RAW_TAGS["vardict.balsamic_stat"]): {"is_mandatory": True},
}

TUMOR_NORMAL_PANEL_TAGS = {
    # Alignment files (PANEL & WGS)
    frozenset(RAW_TAGS["normal.merged.cram"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
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
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.research.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["vardict.clinical.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # CNVs (PANEL)
    frozenset(RAW_TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["gene_metrics"]): {"is_mandatory": True},
    frozenset(RAW_TAGS["cnvkit.vcf2cytosure.cgh"]): {"is_mandatory": True},
    # TMB (PANEL)
    frozenset(RAW_TAGS["vardict.balsamic_stat"]): {"is_mandatory": True},
}
