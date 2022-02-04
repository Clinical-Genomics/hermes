"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

TAGS = {
    # QC & reports
    "multiqc_report.html": ["multiqc-html", "html"],
    "multiqc_data.json": ["json", "multiqc-json"],
    "report.html": ["balsamic-report"],
    "config.json": ["balsamic-config"],
    "BALSAMIC_X.X.X_graph.pdf": ["balsamic-dag"],
    "metrics_deliverables.yaml": ["qc-metrics-yaml", "yaml"],
    "concatenated_*_R_fastp.html": [
        "quality-trimmed-fastq-html",
        "html",
    ],
    "concatenated_*_R_fastp.json": [
        "json",
        "quality-trimmed-fastq-json",
    ],
    # Raw data & alignment files
    "concatenated_*_R_1.fp.fastq.gz": [
        "quality-trimmed-fastq-read1",
        "read1",
    ],
    "concatenated_*_R_2.fp.fastq.gz": [
        "quality-trimmed-fastq-read2",
        "read2",
    ],
    "tumor.merged.cram": ["tumor-cram", "cram"],
    "tumor.merged.cram.crai": ["tumor-cram-index", "cram"],
    "normal.merged.cram": ["normal-cram", "cram"],
    "normal.merged.cram.crai": ["normal-cram-index", "cram"],
    # tnscope (WGS)
    "tnscope.all.vcf.gz": ["tnscope", "vcf-all", "snv", "annotated-somatic-vcf-all"],
    "tnscope.all.vcf.gz.tbi": ["tnscope", "annotated-somatic-vcf-all-index", "vcf-all", "snv"],
    "tnscope.all.vcf.gz_summary.html": [
        "tnscope",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
        "snv",
    ],
    "tnscope.balsamic_stat": ["stat-somatic-tmb", "snv", "tmb", "tnscope"],
    "tnscope.all.filtered.vcf.gz": ["vcf-filtered-tnscope", "clinical-vcf-filtered-tnscope", "snv"],
    "tnscope.all.filtered.vcf.gz.tbi": [
        "vcf-filtered-tnscope",
        "clinical-vcf-filtered-tnscope-index",
        "snv",
    ],
    "tnscope.all.filtered.pass.vcf.gz": ["clinical-vcf-pass-tnscope", "vcf-pass-tnscope", "snv"],
    "tnscope.all.filtered.pass.vcf.gz.tbi": [
        "clinical-vcf-pass-tnscope-index",
        "vcf-pass-tnscope",
        "snv",
    ],
    # vardict (PANEL)
    "vardict.all.vcf.gz": ["annotated-somatic-vcf-all", "snv", "vardict", "vcf-all"],
    "vardict.all.vcf.gz.tbi": ["snv", "vardict", "vcf-all", "annotated-somatic-vcf-all-index"],
    "vardict.all.vcf.gz_summary.html": [
        "snv",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
        "vardict",
    ],
    "vardict.balsamic_stat": ["tmb", "snv", "stat-somatic-tmb", "vardict"],
    "vardict.all.filtered.vcf.gz": ["vcf-filtered-vardict", "clinical-vcf-filtered-vardict", "snv"],
    "vardict.all.filtered.vcf.gz.tbi": [
        "vcf-filtered-vardict",
        "clinical-vcf-filtered-vardict-index",
        "snv",
    ],
    "vardict.all.filtered.pass.vcf.gz": ["clinical-vcf-pass-vardict", "vcf-pass-vardict", "snv"],
    "vardict.all.filtered.pass.vcf.gz.tbi": [
        "clinical-vcf-pass-vardict-index",
        "vcf-pass-vardict",
        "snv",
    ],
    # tnhaplotyper
    "tnhaplotyper.all.vcf.gz": ["tnhaplotyper", "vcf-all", "snv", "annotated-somatic-vcf-all"],
    "tnhaplotyper.all.vcf.gz.tbi": [
        "tnhaplotyper",
        "annotated-somatic-vcf-all-index",
        "vcf-all",
        "snv",
    ],
    "tnhaplotyper.all.vcf.gz_summary.html": [
        "tnhaplotyper",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
        "snv",
    ],
    "tnhaplotyper.balsamic_stat": ["tmb", "snv", "stat-somatic-tmb", "tnhaplotyper"],
    "tnhaplotyper.all.filtered.vcf.gz": [
        "research-vcf-filtered-tnhaplotyper",
        "vcf-filtered-tnhaplotyper",
        "snv",
    ],
    "tnhaplotyper.all.filtered.vcf.gz.tbi": [
        "vcf-filtered-tnhaplotyper",
        "snv",
        "research-vcf-filtered-tnhaplotyper-index",
    ],
    "tnhaplotyper.all.filtered.pass.vcf.gz": [
        "research-vcf-pass-tnhaplotyper",
        "vcf-pass-tnhaplotyper",
        "snv",
    ],
    "tnhaplotyper.all.filtered.pass.vcf.gz.tbi": [
        "research-vcf-pass-tnhaplotyper-index",
        "vcf-pass-tnhaplotyper",
        "snv",
    ],
    # dnascope – germline
    "tumor_normal.dnascope.vcf.gz": ["annotated-germline-vcf-all", "dnascope", "snv", "vcf-all"],
    "tumor_normal.dnascope.vcf.gz.tbi": [
        "dnascope",
        "snv",
        "annotated-germline-vcf-all-index",
        "vcf-all",
    ],
    "tumor_normal.dnascope.vcf.gz_summary.html": [
        "annotated-germline-vcf-summary",
        "dnascope",
        "vcf-summary",
        "snv",
    ],
    # haplotypecaller – germline (PANEL)
    "tumor_normal.haplotypecaller.vcf.gz": [
        "snv",
        "annotated-germline-vcf-all",
        "vcf-all",
        "haplotypecaller",
    ],
    "tumor_normal.haplotypecaller.vcf.gz.tbi": [
        "annotated-germline-vcf-all-index",
        "snv",
        "vcf-all",
        "haplotypecaller",
    ],
    "tumor_normal.haplotypecaller.vcf.gz_summary.html": [
        "vcf-summary",
        "snv",
        "haplotypecaller",
        "annotated-germline-vcf-summary",
    ],
    # manta
    "manta.all.vcf.gz": ["manta", "sv", "vcf-all", "annotated-somatic-vcf-all"],
    "manta.all.vcf.gz.tbi": ["manta", "annotated-somatic-vcf-all-index", "sv", "vcf-all"],
    "manta.all.vcf.gz_summary.html": [
        "manta",
        "sv",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
    ],
    "manta.all.filtered.pass.vcf.gz": ["clinical-vcf-sv-pass", "vcf-sv-pass"],
    "manta.all.filtered.pass.vcf.gz.tbi": ["clinical-vcf-sv-pass-index", "vcf-sv-pass"],
    "tumor_normal.manta_germline.vcf.gz": [
        "annotated-germline-vcf-all",
        "sv",
        "manta-germline",
        "vcf-all",
    ],
    "tumor_normal.manta_germline.vcf.gz.tbi": [
        "sv",
        "annotated-germline-vcf-all-index",
        "manta-germline",
        "vcf-all",
    ],
    "tumor_normal.manta_germline.vcf.gz_summary.html": [
        "annotated-germline-vcf-summary",
        "sv",
        "manta-germline",
        "vcf-summary",
    ],
    # delly
    "delly.all.vcf.gz": ["sv", "vcf-all", "delly", "annotated-somatic-vcf-all"],
    "delly.all.vcf.gz.tbi": ["annotated-somatic-vcf-all-index", "sv", "vcf-all", "delly"],
    "delly.all.vcf.gz_summary.html": [
        "sv",
        "annotated-somatic-vcf-summary",
        "delly",
        "vcf-summary",
    ],
    "delly.all.filtered.pass.vcf.gz": ["vcf-sv-pass-delly", "research-vcf-sv-pass-delly"],
    "delly.all.filtered.pass.vcf.gz.tbi": ["vcf-sv-pass-delly", "research-vcf-sv-pass-delly-index"],
    # cnvkit (PANEL)
    "cnvkit.all.vcf.gz": ["cnv", "annotated-somatic-vcf-all", "cnvkit", "vcf-all"],
    "cnvkit.all.vcf.gz.tbi": ["cnv", "cnvkit", "vcf-all", "annotated-somatic-vcf-all-index"],
    "cnvkit.all.vcf.gz_summary.html": [
        "cnv",
        "cnvkit",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
    ],
    "cnvkit.all.filtered.pass.vcf.gz": ["cnv", "research-vcf-cnv-pass", "vcf-cnv-pass"],
    "cnvkit.all.filtered.pass.vcf.gz.tbi": ["cnv", "research-vcf-cnv-pass-index", "vcf-cnv-pass"],
    "tumor.merged.cnr": ["cnv-cnr", "cnr"],
    "tumor.merged.cns": ["cns", "cnv-cns"],
    "tumor.merged-scatter.pdf": ["scatter", "cnv-scatter"],
    "tumor.merged-diagram.pdf": ["cnv-diagram", "diagram"],
    ".gene_metrics": ["gene-metrics", "cnv-gene-metrics"],
    ".gene_breaks": ["cnv-gene-breaks", "gene-breaks"],
    # TNscope_umi (PANEL)
    "TNscope_umi.all.vcf.gz": ["tnscope-umi", "annotated-somatic-vcf-all", "snv", "vcf-all"],
    "TNscope_umi.all.vcf.gz.tbi": [
        "tnscope-umi",
        "snv",
        "vcf-all",
        "annotated-somatic-vcf-all-index",
    ],
    "TNscope_umi.all.vcf.gz_summary.html": [
        "tnscope-umi",
        "snv",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
    ],
    "TNscope_umi.balsamic_stat": ["tmb", "tnscope-umi", "snv", "stat-somatic-tmb"],
    "TNscope_umi.all.filtered.vcf.gz": [
        "research-vcf-filtered-tnscope-umi",
        "vcf-filtered-tnscope-umi",
        "snv",
    ],
    "TNscope_umi.all.filtered.vcf.gz.tbi": [
        "vcf-filtered-tnscope-umi",
        "snv",
        "research-vcf-filtered-tnscope-umi-index",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz": [
        "research-vcf-pass-tnscope-umi",
        "vcf-pass-tnscope-umi",
        "snv",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz.tbi": [
        "research-vcf-pass-tnscope-umi-index",
        "vcf-pass-tnscope-umi",
        "snv",
    ],
    # ascat (TN_WGS)
    "ascat.all.vcf.gz": ["vcf-all", "annotated-somatic-vcf-all", "ascat", "cnv"],
    "ascat.all.vcf.gz.tbi": ["vcf-all", "ascat", "cnv", "annotated-somatic-vcf-all-index"],
    "ascat.all.vcf.gz_summary.html": [
        "cnv",
        "ascat",
        "annotated-somatic-vcf-summary",
        "vcf-summary",
    ],
    "ascat.all.filtered.pass.vcf.gz": ["research-vcf-cnv-pass-ascat", "vcf-cnv-pass-ascat"],
    "ascat.all.filtered.pass.vcf.gz.tbi": [
        "research-vcf-cnv-pass-ascat-index",
        "vcf-cnv-pass-ascat",
    ],
    "ascat.output.pdf": ["ascat-output-pdf", "research-ascat-output-pdf"],
}

BALSAMIC_COMMON_TAGS = {
    # QC & reports
    frozenset(TAGS["multiqc_report.html"]): {  # MultiQC html
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": ["deliver", "scout", "audit"],
    },
    frozenset(TAGS["multiqc_data.json"]): {  # MultiQC json
        "tags": ["multiqc-json"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["report.html"]): {  # BALSAMIC report html
        "tags": ["balsamic-report"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["config.json"]): {  # BALSAMIC config json
        "tags": ["balsamic-config"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["BALSAMIC_X.X.X_graph.pdf"]): {  # DAG
        "tags": ["balsamic-dag"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["concatenated_*_R_fastp.html"]): {  # fastq html
        "tags": ["fastq", "visualization"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["concatenated_*_R_fastp.json"]): {  # fastq json
        "tags": ["fastq", "visualization"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["metrics_deliverables.yaml"]): {  # QC metrics
        "tags": ["qc-metrics", "deliverable"],
        "is_mandatory": True,
        "used_by": ["vogue"],
    },
    # Raw data & alignment files
    frozenset(TAGS["concatenated_*_R_1.fp.fastq.gz"]): {  # fastq (read1)
        "tags": ["fastq"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["concatenated_*_R_2.fp.fastq.gz"]): {  # fastq (read2)
        "tags": ["fastq"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged.cram"]): {  # cram (tumor)
        "tags": ["cram", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["tumor.merged.cram.crai"]): {
        "tags": ["cram-index", "tumor"],
        "is_mandatory": True,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal.merged.cram"]): {  # cram (normal)
        "tags": ["cram", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    frozenset(TAGS["normal.merged.cram.crai"]): {
        "tags": ["cram-index", "normal"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
    # tnscope (WGS)
    frozenset(TAGS["tnscope.all.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-research", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.all.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-research-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.balsamic_stat"]): {
        "tags": ["tmb", "tnscope", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.all.vcf.gz_summary.html"]): {
        "tags": ["tnscope", "vcf-report", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset(TAGS["tnscope.all.filtered.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-filtered", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tnscope.all.filtered.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-filtered-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {
        "tags": ["tnscope", "vcf-snv-clinical", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["tnscope", "vcf-snv-clinical-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    # vardict (PANEL)
    frozenset(TAGS["vardict.all.vcf.gz"]): {
        "tags": ["vardict", "vcf", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.all.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.balsamic_stat"]): {
        "tags": ["vardict", "tmb", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.all.vcf.gz_summary.html"]): {
        "tags": ["vardict", "vcf-report", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset(TAGS["vardict.all.filtered.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-filtered", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["vardict.all.filtered.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-filtered-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {
        "tags": ["vardict", "vcf-snv-clinical", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vardict", "vcf-snv-clinical-index", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    # tnhaplotyper
    frozenset(TAGS["tnhaplotyper.all.vcf.gz"]): {  # tnhaplotyper
        "tags": ["vcf", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tnhaplotyper.all.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tnhaplotyper.balsamic_stat"]): {
        "tags": ["tmb", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tnhaplotyper.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "haplotype-caller", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["tnhaplotyper.all.filtered.vcf.gz"]): {
        "tags": ["vcf-snv-research", "haplotype-caller", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnhaplotyper.all.filtered.vcf.gz.tbi"]): {
        "tags": ["vcf-snv-research-index", "haplotype-caller", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnhaplotyper.all.filtered.pass.vcf.gz"]): {
        "tags": ["vcf", "haplotype-caller", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tnhaplotyper.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "haplotype-caller", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    # dnascope – germline
    frozenset(TAGS["tumor_normal.dnascope.vcf.gz"]): {
        "tags": ["vcf", "dnascope", "germline"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.dnascope.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "dnascope", "germline"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.dnascope.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "dnascope", "germline"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    # haplotypecaller – germline (PANEL)
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz"]): {
        "tags": ["vcf", "haplotype-caller", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "haplotype-caller", "germline"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "haplotype-caller", "germline"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    # manta
    frozenset(TAGS["manta.all.vcf.gz"]): {
        "tags": ["vcf-sv-research", "manta", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["manta.all.vcf.gz.tbi"]): {
        "tags": ["vcf-sv-research-index", "manta", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["manta.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "manta", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["manta.all.filtered.pass.vcf.gz"]): {
        "tags": ["vcf-sv-clinical", "manta", "filtered"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["manta.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vcf-sv-clinical-index", "manta", "filtered"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor_normal.manta_germline.vcf.gz"]): {  # manta germline
        "tags": ["sv-vcf", "manta", "germline"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.manta_germline.vcf.gz.tbi"]): {
        "tags": ["sv-vcf-index", "manta", "germline"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(TAGS["tumor_normal.manta_germline.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "manta", "germline"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    # delly
    frozenset(TAGS["delly.all.vcf.gz"]): {
        "tags": ["vcf", "delly", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["delly.all.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "delly", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["delly.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "delly", "somatic"],
        "is_mandatory": True,
        "used_by": ["audit"],
    },
    frozenset(TAGS["delly.all.filtered.pass.vcf.gz"]): {
        "tags": ["delly", "vcf", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["delly.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["delly", "vcf-index", "filtered", "somatic"],
        "is_mandatory": True,
        "used_by": ["deliver"],
    },
    # cnvkit (PANEL)
    frozenset(TAGS["cnvkit.all.vcf.gz"]): {
        "tags": ["sv-vcf", "cnvkit", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["cnvkit.all.vcf.gz.tbi"]): {
        "tags": ["sv-vcf-index", "cnvkit", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["cnvkit.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "cnvkit", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz"]): {
        "tags": ["cnvkit", "vcf-sv-research", "filtered"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["cnvkit", "vcf-sv-research-index", "filtered"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged.cns"]): {
        "tags": ["cnvkit", "segments"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged.cnr"]): {
        "tags": ["cnvkit", "regions"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {
        "tags": ["cnvkit", "visualization"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {
        "tags": ["cnvkit", "visualization", "diagram"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS[".gene_breaks"]): {
        "tags": ["cnvkit", "genes"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS[".gene_metrics"]): {
        "tags": ["cnvkit", "genes", "metrics"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    # TNscope_umi (PANEL)
    frozenset(TAGS["TNscope_umi.all.vcf.gz"]): {
        "tags": ["vcf", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset(TAGS["TNscope_umi.balsamic_stat"]): {
        "tags": ["tmb", "tnscope-umi", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz"]): {
        "tags": ["vcf-snv-research", "filtered", "somatic", "tnscope-umi"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz.tbi"]): {
        "tags": ["vcf-snv-research-index", "filtered", "somatic", "tnscope-umi"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {
        "tags": ["vcf", "tnscope-umi", "filtered", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "tnscope-umi", "filtered", "somatic"],
        "is_mandatory": False,
        "used_by": ["storage"],
    },
    # ascat (TN_WGS)
    frozenset(TAGS["ascat.all.vcf.gz"]): {
        "tags": ["vcf", "ascatngs", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["ascat.all.vcf.gz.tbi"]): {
        "tags": ["vcf-index", "ascatngs", "somatic"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["ascat.all.vcf.gz_summary.html"]): {
        "tags": ["vcf-report", "ascatngs", "somatic"],
        "is_mandatory": False,
        "used_by": ["audit"],
    },
    frozenset(TAGS["ascat.all.filtered.pass.vcf.gz"]): {
        "tags": ["ascatngs", "vcf", "filtered"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["ascat.all.filtered.pass.vcf.gz.tbi"]): {
        "tags": ["ascatngs", "vcf-index", "filtered"],
        "is_mandatory": False,
        "used_by": ["deliver"],
    },
    frozenset(TAGS["ascat.output.pdf"]): {
        "tags": ["ascatngs", "visualization"],
        "is_mandatory": False,
        "used_by": ["deliver", "scout"],
    },
}

TUMOR_ONLY_WGS_TAGS = {
    # tnscope
    frozenset(TAGS["tnscope.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
}

TUMOR_NORMAL_WGS_TAGS = {
    # Raw data & alignment files
    frozenset(TAGS["normal.merged.cram"]): {"is_mandatory": True},  # cram (normal)
    frozenset(TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
    # tnscope
    frozenset(TAGS["tnscope.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tnscope.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # ascat
    frozenset(TAGS["ascat.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["ascat.output.pdf"]): {"is_mandatory": True},
}

TUMOR_ONLY_PANEL_TAGS = {
    # vardict
    frozenset(TAGS["vardict.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # haplotypecaller – germline
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz_summary.html"]): {"is_mandatory": True},
    # cnvkit
    frozenset(TAGS["cnvkit.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {"is_mandatory": True},
    frozenset(TAGS[".gene_metrics"]): {"is_mandatory": True},
    frozenset(TAGS[".gene_breaks"]): {"is_mandatory": True},
    # TNscope_umi
    frozenset(TAGS["TNscope_umi.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
}

TUMOR_NORMAL_PANEL_TAGS = {
    # Raw data & alignment files
    frozenset(TAGS["normal.merged.cram"]): {"is_mandatory": True},  # cram (normal)
    frozenset(TAGS["normal.merged.cram.crai"]): {"is_mandatory": True},
    # vardict
    frozenset(TAGS["vardict.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["vardict.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    # haplotypecaller – germline
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tumor_normal.haplotypecaller.vcf.gz_summary.html"]): {"is_mandatory": True},
    # cnvkit
    frozenset(TAGS["cnvkit.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["cnvkit.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged.cns"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged.cnr"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-scatter.pdf"]): {"is_mandatory": True},
    frozenset(TAGS["tumor.merged-diagram.pdf"]): {"is_mandatory": True},
    frozenset(TAGS[".gene_metrics"]): {"is_mandatory": True},
    frozenset(TAGS[".gene_breaks"]): {"is_mandatory": True},
    # TNscope_umi
    frozenset(TAGS["TNscope_umi.all.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.vcf.gz_summary.html"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.balsamic_stat"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.vcf.gz.tbi"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz"]): {"is_mandatory": True},
    frozenset(TAGS["TNscope_umi.all.filtered.pass.vcf.gz.tbi"]): {"is_mandatory": True},
}
