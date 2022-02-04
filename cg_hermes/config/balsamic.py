"""Tags that are defined in Balsamic deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However the tags that are available to a particular analysis is mandatory for that analysis.
"""

TAGS = {
    # QC & reports
    "multiqc_report.html": ["html", "multiqc-html"],
    "multiqc_data.json": ["json", "multiqc-json"],
    "report.html": ["balsamic-report"],
    "config.json": ["balsamic-config"],
    "BALSAMIC_X.X.X_graph.pdf": ["balsamic-dag"],
    "metrics_deliverables.yaml": ["yaml", "qc-metrics-yaml"],
    "concatenated_*_R_fastp.html": ["html", "quality-trimmed-fastq-html"],
    "concatenated_*_R_fastp.json": ["json", "quality-trimmed-fastq-json"],
    # Raw data & alignment files
    "concatenated_*_R_1.fp.fastq.gz": ["read1", "quality-trimmed-fastq-read1"],
    "concatenated_*_R_2.fp.fastq.gz": ["read2", "quality-trimmed-fastq-read2"],
    "tumor.merged.cram": ["cram", "tumor-cram"],
    "tumor.merged.cram.crai": ["cram", "tumor-cram-index"],
    "normal.merged.cram": ["cram", "normal-cram"],
    "normal.merged.cram.crai": ["cram", "normal-cram-index"],
    # tnscope (WGS)
    "tnscope.all.vcf.gz": ["tnscope", "snv", "vcf-all", "annotated-somatic-vcf-all"],
    "tnscope.all.vcf.gz.tbi": ["tnscope", "snv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "tnscope.all.vcf.gz_summary.html": [
        "tnscope",
        "snv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "tnscope.balsamic_stat": ["tnscope", "snv", "tmb", "stat-somatic-tmb"],
    "tnscope.all.filtered.vcf.gz": ["snv", "vcf-filtered-tnscope", "clinical-vcf-filtered-tnscope"],
    "tnscope.all.filtered.vcf.gz.tbi": [
        "snv",
        "vcf-filtered-tnscope",
        "clinical-vcf-filtered-tnscope-index",
    ],
    "tnscope.all.filtered.pass.vcf.gz": ["snv", "vcf-pass-tnscope", "clinical-vcf-pass-tnscope"],
    "tnscope.all.filtered.pass.vcf.gz.tbi": [
        "snv",
        "vcf-pass-tnscope",
        "clinical-vcf-pass-tnscope-index",
    ],
    # vardict (PANEL)
    "vardict.all.vcf.gz": ["vardict", "snv", "vcf-all", "annotated-somatic-vcf-all"],
    "vardict.all.vcf.gz.tbi": ["vardict", "snv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "vardict.all.vcf.gz_summary.html": [
        "vardict",
        "snv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "vardict.balsamic_stat": ["vardict", "snv", "tmb", "stat-somatic-tmb"],
    "vardict.all.filtered.vcf.gz": ["snv", "vcf-filtered-vardict", "clinical-vcf-filtered-vardict"],
    "vardict.all.filtered.vcf.gz.tbi": [
        "snv",
        "vcf-filtered-vardict",
        "clinical-vcf-filtered-vardict-index",
    ],
    "vardict.all.filtered.pass.vcf.gz": ["snv", "vcf-pass-vardict", "clinical-vcf-pass-vardict"],
    "vardict.all.filtered.pass.vcf.gz.tbi": [
        "snv",
        "vcf-pass-vardict",
        "clinical-vcf-pass-vardict-index",
    ],
    # tnhaplotyper
    "tnhaplotyper.all.vcf.gz": ["tnhaplotyper", "snv", "vcf-all", "annotated-somatic-vcf-all"],
    "tnhaplotyper.all.vcf.gz.tbi": [
        "tnhaplotyper",
        "snv",
        "vcf-all",
        "annotated-somatic-vcf-all-index",
    ],
    "tnhaplotyper.all.vcf.gz_summary.html": [
        "tnhaplotyper",
        "snv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "tnhaplotyper.balsamic_stat": ["tnhaplotyper", "snv", "tmb", "stat-somatic-tmb"],
    "tnhaplotyper.all.filtered.vcf.gz": [
        "snv",
        "vcf-filtered-tnhaplotyper",
        "research-vcf-filtered-tnhaplotyper",
    ],
    "tnhaplotyper.all.filtered.vcf.gz.tbi": [
        "snv",
        "vcf-filtered-tnhaplotyper",
        "research-vcf-filtered-tnhaplotyper-index",
    ],
    "tnhaplotyper.all.filtered.pass.vcf.gz": [
        "snv",
        "vcf-pass-tnhaplotyper",
        "research-vcf-pass-tnhaplotyper",
    ],
    "tnhaplotyper.all.filtered.pass.vcf.gz.tbi": [
        "snv",
        "vcf-pass-tnhaplotyper",
        "research-vcf-pass-tnhaplotyper-index",
    ],
    # dnascope – germline
    "tumor_normal.dnascope.vcf.gz": ["dnascope", "snv", "vcf-all", "annotated-germline-vcf-all"],
    "tumor_normal.dnascope.vcf.gz.tbi": [
        "dnascope",
        "snv",
        "vcf-all",
        "annotated-germline-vcf-all-index",
    ],
    "tumor_normal.dnascope.vcf.gz_summary.html": [
        "dnascope",
        "snv",
        "vcf-summary",
        "annotated-germline-vcf-summary",
    ],
    # haplotypecaller – germline (PANEL)
    "tumor_normal.haplotypecaller.vcf.gz": [
        "haplotypecaller",
        "snv",
        "vcf-all",
        "annotated-germline-vcf-all",
    ],
    "tumor_normal.haplotypecaller.vcf.gz.tbi": [
        "haplotypecaller",
        "snv",
        "vcf-all",
        "annotated-germline-vcf-all-index",
    ],
    "tumor_normal.haplotypecaller.vcf.gz_summary.html": [
        "haplotypecaller",
        "snv",
        "vcf-summary",
        "annotated-germline-vcf-summary",
    ],
    # manta
    "manta.all.vcf.gz": ["manta", "sv", "vcf-all", "annotated-somatic-vcf-all"],
    "manta.all.vcf.gz.tbi": ["manta", "sv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "manta.all.vcf.gz_summary.html": [
        "manta",
        "sv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "manta.all.filtered.pass.vcf.gz": ["vcf-sv-pass", "clinical-vcf-sv-pass"],
    "manta.all.filtered.pass.vcf.gz.tbi": ["vcf-sv-pass", "clinical-vcf-sv-pass-index"],
    "tumor_normal.manta_germline.vcf.gz": [
        "manta-germline",
        "sv",
        "vcf-all",
        "annotated-germline-vcf-all",
    ],
    "tumor_normal.manta_germline.vcf.gz.tbi": [
        "manta-germline",
        "sv",
        "vcf-all",
        "annotated-germline-vcf-all-index",
    ],
    "tumor_normal.manta_germline.vcf.gz_summary.html": [
        "manta-germline",
        "sv",
        "vcf-summary",
        "annotated-germline-vcf-summary",
    ],
    # delly
    "delly.all.vcf.gz": ["delly", "sv", "vcf-all", "annotated-somatic-vcf-all"],
    "delly.all.vcf.gz.tbi": ["delly", "sv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "delly.all.vcf.gz_summary.html": [
        "delly",
        "sv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "delly.all.filtered.pass.vcf.gz": ["vcf-sv-pass-delly", "research-vcf-sv-pass-delly"],
    "delly.all.filtered.pass.vcf.gz.tbi": ["vcf-sv-pass-delly", "research-vcf-sv-pass-delly-index"],
    # cnvkit (PANEL)
    "cnvkit.all.vcf.gz": ["cnvkit", "cnv", "vcf-all", "annotated-somatic-vcf-all"],
    "cnvkit.all.vcf.gz.tbi": ["cnvkit", "cnv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "cnvkit.all.vcf.gz_summary.html": [
        "cnvkit",
        "cnv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "cnvkit.all.filtered.pass.vcf.gz": ["cnv", "vcf-cnv-pass", "research-vcf-cnv-pass"],
    "cnvkit.all.filtered.pass.vcf.gz.tbi": ["cnv", "vcf-cnv-pass", "research-vcf-cnv-pass-index"],
    "tumor.merged.cnr": ["cnr", "cnv-cnr"],
    "tumor.merged.cns": ["cns", "cnv-cns"],
    "tumor.merged-scatter.pdf": ["scatter", "cnv-scatter"],
    "tumor.merged-diagram.pdf": ["diagram", "cnv-diagram"],
    ".gene_metrics": ["gene-metrics", "cnv-gene-metrics"],
    ".gene_breaks": ["gene-breaks", "cnv-gene-breaks"],
    # TNscope_umi (PANEL)
    "TNscope_umi.all.vcf.gz": ["tnscope-umi", "snv", "vcf-all", "annotated-somatic-vcf-all"],
    "TNscope_umi.all.vcf.gz.tbi": [
        "tnscope-umi",
        "snv",
        "vcf-all",
        "annotated-somatic-vcf-all-index",
    ],
    "TNscope_umi.all.vcf.gz_summary.html": [
        "tnscope-umi",
        "snv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "TNscope_umi.balsamic_stat": ["tnscope-umi", "snv", "tmb", "stat-somatic-tmb"],
    "TNscope_umi.all.filtered.vcf.gz": [
        "snv",
        "vcf-filtered-tnscope-umi",
        "research-vcf-filtered-tnscope-umi",
    ],
    "TNscope_umi.all.filtered.vcf.gz.tbi": [
        "snv",
        "vcf-filtered-tnscope-umi",
        "research-vcf-filtered-tnscope-umi-index",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz": [
        "snv",
        "vcf-pass-tnscope-umi",
        "research-vcf-pass-tnscope-umi",
    ],
    "TNscope_umi.all.filtered.pass.vcf.gz.tbi": [
        "snv",
        "vcf-pass-tnscope-umi",
        "research-vcf-pass-tnscope-umi-index",
    ],
    # ascat (TN_WGS)
    "ascat.all.vcf.gz": ["ascat", "cnv", "vcf-all", "annotated-somatic-vcf-all"],
    "ascat.all.vcf.gz.tbi": ["ascat", "cnv", "vcf-all", "annotated-somatic-vcf-all-index"],
    "ascat.all.vcf.gz_summary.html": [
        "ascat",
        "cnv",
        "vcf-summary",
        "annotated-somatic-vcf-summary",
    ],
    "ascat.all.filtered.pass.vcf.gz": ["vcf-cnv-pass-ascat", "research-vcf-cnv-pass-ascat"],
    "ascat.all.filtered.pass.vcf.gz.tbi": [
        "vcf-cnv-pass-ascat",
        "research-vcf-cnv-pass-ascat-index",
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
