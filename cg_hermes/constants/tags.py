from enum import StrEnum
from typing import Any


class AlignmentTags(StrEnum):
    BAM: str = "bam"
    BAM_INDEX: str = "bam-index"
    BAM_MT: str = "bam-mt"
    BAM_MT_INDEX: str = "bam-mt-index"
    CRAM: str = "cram"
    CRAM_INDEX: str = "cram-index"

    @classmethod
    def name(cls) -> str:
        return "Alignment Tags"

    @property
    def description(self) -> str:
        descriptions: dict[AlignmentTags, str] = {
            self.BAM: "Alignment file in BAM format",
            self.BAM_INDEX: "Index file for alignment file in BAM format",
            self.BAM_MT: "Alignment file in BAM format holding the reads from chrMT",
            self.CRAM: "Alignment file in CRAM format",
            self.CRAM_INDEX: "Index file for alignment file in CRAM format",
        }
        return descriptions.get(self, "Description not available")


class RawDataTags(StrEnum):
    FASTA: str = "fasta"
    FASTQ: str = "fastq"
    FORWARD_STRAND: str = "forward-strand"
    REVERSE_STRAND: str = "reverse-strand"
    RNA: str = "rna"
    UNPAIRED_READS: str = "unpaired-reads"

    @classmethod
    def name(cls) -> str:
        return "Raw Data Tags"

    @property
    def description(self) -> str:
        descriptions: dict[RawDataTags, str] = {
            self.FASTA: "Files with raw data in fasta format",
            self.FASTQ: "Files with raw data in fastq format",
            self.FORWARD_STRAND: "Reads from forward strand",
            self.REVERSE_STRAND: "Reads from reverse strand",
            self.RNA: "Data generated from RNA samples",
            self.UNPAIRED_READS: "Reads that could not be paired",
        }
        return descriptions.get(self, "Description not available")


class VariantTags(StrEnum):
    CNV: str = "cnv"
    GERMLINE: str = "germline"
    MOBILE_ELEMENTS: str = "mobile-elements"
    MSI: str = "msi"
    NORMAL: str = "normal"
    RHOCALL_VIZ: str = "rhocall-viz"
    SMN_CALLING: str = "smn-calling"
    SNV: str = "snv"
    SNV_BCF: str = "snv-bcf"
    SNV_GBCF: str = "snv-gbcf"
    SOMATIC: str = "somatic"
    SV: str = "sv"
    SV_BCF: str = "sv-bcf"
    SV_VCF: str = "sv-vcf"
    SV_VCF_INDEX: str = "sv-vcf-index"
    TELOMERE_CALLING: str = "telomere-calling"
    TMB: str = "tmb"
    TUMOR: str = "tumor"
    UPD: str = "upd"
    VARIANTS: str = "variants"
    VCF2CYTOSURE: str = "vcf2cytosure"
    VCF: str = "vcf"
    VCF_INDEX: str = "vcf-index"
    VCF_SNV: str = "vcf-snv"
    VCF_SNV_CLINICAL: str = "vcf-snv-clinical"
    VCF_SNV_CLINICAL_INDEX: str = "vcf-snv-clinical-index"
    VCF_SNV_CLINICAL_SCORED: str = "vcf-snv-clinical-scored"
    VCF_SNV_CLINICAL_SCORED_INDEX: str = "vcf-snv-clinical-scored-index"
    VCF_SNV_FILTERED: str = "vcf-snv-filtered"
    VCF_SNV_FILTERED_INDEX: str = "vcf-snv-filtered-index"
    VCF_SNV_GERMLINE_NORMAL: str = "vcf-snv-germline-normal"
    VCF_SNV_GERMLINE_NORMAL_INDEX: str = "vcf-snv-germline-normal-index"
    VCF_SNV_GERMLINE_TUMOR: str = "vcf-snv-germline-tumor"
    VCF_SNV_GERMLINE_TUMOR_INDEX: str = "vcf-snv-germline-tumor-index"
    VCF_SNV_INDEX: str = "vcf-snv-index"
    VCF_SNV_RESEARCH: str = "vcf-snv-research"
    VCF_SNV_RESEARCH_INDEX: str = "vcf-snv-research-index"
    VCF_SNV_RESEARCH_UNFILTERED: str = "vcf-snv-research-unfiltered"
    VCF_SNV_RESEARCH_UNFILTERED_INDEX: str = "vcf-snv-research-unfiltered-index"
    VCF_STR: str = "vcf-str"
    VCF_STR_INDEX: str = "vcf-str-index"
    VCF_SV: str = "vcf-sv"
    VCF_SV_CLINICAL: str = "vcf-sv-clinical"
    VCF_SV_CLINICAL_INDEX: str = "vcf-sv-clinical-index"
    VCF_SV_GERMLINE_NORMAL: str = "vcf-sv-germline-normal"
    VCF_SV_GERMLINE_NORMAL_INDEX: str = "vcf-sv-germline-normal-index"
    VCF_SV_GERMLINE_TUMOR: str = "vcf-sv-germline-tumor"
    VCF_SV_GERMLINE_TUMOR_INDEX: str = "vcf-sv-germline-tumor-index"
    VCF_SV_INDEX: str = "vcf-sv-index"
    VCF_SV_RESEARCH: str = "vcf-sv-research"
    VCF_SV_RESEARCH_INDEX: str = "vcf-sv-research-index"
    VCF_UMI_SNV: str = "vcf-umi-snv"
    VCF_UMI_SNV_CLINICAL: str = "vcf-umi-snv-clinical"
    VCF_UMI_SNV_CLINICAL_INDEX: str = "vcf-umi-snv-clinical-index"
    VCF_UMI_SNV_INDEX: str = "vcf-umi-snv-index"
    VCF_UMI_SNV_RESEARCH: str = "vcf-umi-snv-research"
    VCF_UMI_SNV_RESEARCH_INDEX: str = "vcf-umi-snv-research-index"
    VCF_UMI_SNV_RESEARCH_UNFILTERED: str = "vcf-umi-snv-research-unfiltered"
    VCF_UMI_SNV_RESEARCH_UNFILTERED_INDEX: str = "vcf-umi-snv-research-unfiltered-index"
    VCF_UMI_SNV_CLINICAL_RANKED: str = "vcf-umi-snv-clinical-scored"
    VCF_UMI_SNV_CLINICAL_RANKED_INDEX: str = "vcf-umi-snv-clinical-scored-index"

    @classmethod
    def name(cls) -> str:
        return "Variant Tags"

    @property
    def description(self) -> str:
        descriptions: dict[VariantTags, str] = {
            self.CNV: "Copy number variants",
            self.GERMLINE: "Associated with germline variants",
            self.MOBILE_ELEMENTS: "Mobile elements",
            self.NORMAL: "Associated with normal sample",
            self.RHOCALL_VIZ: "Runs of homozygosity index",
            self.SMN_CALLING: "Copy number calls for the SMN gene",
            self.SNV: "Single nucleotide variants and short indels",
            self.SNV_BCF: "Gvcf including all SNV variants",
            self.SNV_GBCF: "Gvcf including all SNV variants",
            self.SOMATIC: "Associated with somatic variants",
            self.SV: "Structural variants",
            self.SV_BCF: "Gvcf including all SV variants",
            self.SV_VCF: "Variant call formatted file with structural variants",
            self.SV_VCF_INDEX: "Following index",
            self.TELOMERE_CALLING: "Variants from telomere calling",
            self.TMB: "Tumor mutational burden information",
            self.TUMOR: "Associated with tumor sample",
            self.UPD: "Uniparental disomy variants",
            self.VARIANTS: "File pertaining variant information in some way",
            self.VCF2CYTOSURE: "Conversion from VCF format to cytosure format",
            self.VCF: "Variant call formatted file",
            self.VCF_INDEX: "Following index",
            self.VCF_SNV: "SNV variant call formatted file",
            self.VCF_SNV_CLINICAL: "SNV variants from clinical panels",
            self.VCF_SNV_CLINICAL_INDEX: "Following index",
            self.VCF_SNV_CLINICAL_SCORED: "Scored clinically annotated VCF with SNVs",
            self.VCF_SNV_CLINICAL_SCORED_INDEX: "Following index",
            self.VCF_SNV_FILTERED: "SNV variants filtered by BALSAMIC",
            self.VCF_SNV_FILTERED_INDEX: "Following index",
            self.VCF_SNV_GERMLINE_NORMAL: "SNV germline normal variants",
            self.VCF_SNV_GERMLINE_NORMAL_INDEX: "Following index",
            self.VCF_SNV_GERMLINE_TUMOR: "SNV germline tumor variants",
            self.VCF_SNV_GERMLINE_TUMOR_INDEX: "Following index",
            self.VCF_SNV_INDEX: "Following index",
            self.VCF_SNV_RESEARCH: "SNV variants from whole genome",
            self.VCF_SNV_RESEARCH_INDEX: "Following index",
            self.VCF_STR: "Short tandem repeat variants",
            self.VCF_STR_INDEX: "Following index",
            self.VCF_SV: "SV variant call formatted file",
            self.VCF_SV_CLINICAL: "SV variants from clinical panels",
            self.VCF_SV_CLINICAL_INDEX: "Following index",
            self.VCF_SV_GERMLINE_NORMAL: "SV germline normal variants",
            self.VCF_SV_GERMLINE_NORMAL_INDEX: "Following index",
            self.VCF_SV_GERMLINE_TUMOR: "SV germline tumor variants",
            self.VCF_SV_GERMLINE_TUMOR_INDEX: "Following index",
            self.VCF_SV_INDEX: "Following index",
            self.VCF_SV_RESEARCH: "SV variants from whole genome",
            self.VCF_SV_RESEARCH_INDEX: "Following index",
            self.VCF_UMI_SNV: "Raw SNV UMI variant formatted file",
            self.VCF_UMI_SNV_CLINICAL: "SNV UMI variants from clinical panels",
            self.VCF_UMI_SNV_CLINICAL_INDEX: "Following index",
            self.VCF_UMI_SNV_INDEX: "Following index",
            self.VCF_UMI_SNV_RESEARCH: "SNV UMI variant formatted file",
            self.VCF_UMI_SNV_RESEARCH_INDEX: "Following index",
            self.VCF_UMI_SNV_CLINICAL_RANKED: "Scored clinically annotated VCF with SNVs from UMI analysis",
            self.VCF_UMI_SNV_CLINICAL_RANKED_INDEX: "Following index",
        }
        return descriptions.get(self, "Description not available")


class FamilyTags(StrEnum):
    PED: str = "ped"
    PEDIGREE: str = "pedigree"

    @classmethod
    def name(cls) -> str:
        return "Family Tags"

    @property
    def description(self) -> str:
        descriptions: dict[FamilyTags, str] = {
            self.PED: "Pedigree information",
            self.PEDIGREE: "Pedigree information",
        }
        return descriptions.get(self, "Description not available")


class ReportTags(StrEnum):
    AUDIT: str = "audit"
    BCFTOOLS_STATS: str = "bcftools-stats"
    CNV_REPORT: str = "cnv-report"
    CSV: str = "csv"
    D4: str = "d4"
    DELIVERABLE: str = "deliverable"
    DELIVERY_REPORT: str = "delivery-report"
    GENE_COUNTS: str = "gene-counts"
    GENERAL_STATS: str = "general-stats"
    MOSDEPTH_COVDIST: str = "mosdepth-covdist"
    MOSDEPTH_CUMCOV: str = "mosdepth-cumcov"
    MOSDEPTH_PERCHROM: str = "mosdepth-perchrom"
    MULTIQC: str = "multiqc"
    MULTIQC_HTML: str = "multiqc-html"
    MULTIQC_JSON: str = "multiqc-json"
    PDF: str = "pdf"
    PICARD_ALIGNMENT: str = "picard-alignment"
    PICARD_BAMQC: str = "picard-bamqc"
    PICARD_DUPLICATES: str = "picard-duplicates"
    PICARD_HISTOGRAM: str = "picard-histogram"
    PICARD_HS: str = "picard-hs"
    PICARD_INSERT_SIZE: str = "picard-insert-size"
    PICARD_QUALITYCYCLE: str = "picard-qualitycycle"
    PICARD_QUALITYDISTR: str = "picard-qualitydistr"
    PICARD_RNASEQ: str = "picard-rnaseq"
    PICARD_WGS: str = "picard-wgs"
    QC_REPORT: str = "qc-report"
    SAMBAMBA_DEPTH: str = "sambamba-depth"
    SAMTOOLS_STATS: str = "samtools-stats"
    SOFTWARE_VERSIONS: str = "software-versions"
    STAR: str = "star"
    SUMMARY: str = "summary"
    TSV: str = "tsv"
    VCF_REPORT: str = "vcf-report"

    @classmethod
    def name(cls) -> str:
        return "Report Tags"

    @property
    def description(self) -> str:
        descriptions: dict[ReportTags, str] = {
            self.AUDIT: "Audit file",
            self.BCFTOOLS_STATS: "BCFtools variant calling metrics",
            self.CNV_REPORT: "CNV variant calling report",
            self.CSV: "Comma separated values",
            self.D4: "D4 file format coverage file",
            self.DELIVERABLE: "Deliverables file",
            self.DELIVERY_REPORT: "Delivery report with result for upload to Scout",
            self.GENE_COUNTS: "STAR read counts output per gene",
            self.GENERAL_STATS: "General statistics reported from MultiQC",
            self.MOSDEPTH_COVDIST: "Coverage distribution profile from mosdepth",
            self.MOSDEPTH_CUMCOV: "Cumulative coverage distribution profile from mosdepth",
            self.MOSDEPTH_PERCHROM: "Depth per chromosome from mosdepth",
            self.MULTIQC: "MultiQC related files",
            self.MULTIQC_HTML: "MultiQC analysis report in HTML format",
            self.MULTIQC_JSON: "MultiQC analysis report in JSON format",
            self.PDF: "Portable document format",
            self.PICARD_ALIGNMENT: "High level metrics about the alignment of reads",
            self.PICARD_BAMQC: "Qualimap BAMQC metrics",
            self.PICARD_DUPLICATES: "Metrics calculated during marking duplicates",
            self.PICARD_HISTOGRAM: "Picard histograms in JSON format",
            self.PICARD_HS: "Metrics for the analysis of target-capture sequencing",
            self.PICARD_INSERT_SIZE: "Metrics about the insert size distribution",
            self.PICARD_QUALITYCYCLE: "Picard MeanQualityByCycle Metrics",
            self.PICARD_RNASEQ: "Metrics about the alignment of RNA-seq reads",
            self.PICARD_WGS: "Metrics for evaluating the performance of WGS analysis",
            self.QC_REPORT: "Results and QC",
            self.SAMBAMBA_DEPTH: "Coverage information from sambamba",
            self.SAMTOOLS_STATS: "Comprehensive statistics from alignment file",
            self.SOFTWARE_VERSIONS: "Versions of software used in analysis",
            self.STAR: "Files related to Star aligner",
            self.SUMMARY: "Overview file without detailed information",
            self.TSV: "Tab separated values",
            self.VCF_REPORT: "Results and QC from variant calling",
        }
        return descriptions.get(self, "Description not available")


class QCTags(StrEnum):
    PED_CHECK: str = "ped-check"
    QC_METRICS: str = "qc-metrics"
    SEX_CHECK: str = "sex-check"

    @classmethod
    def name(cls) -> str:
        return "QC Tags"

    @property
    def description(self) -> str:
        descriptions: dict[QCTags, str] = {
            self.PED_CHECK: "Results from pedigree validation",
            self.QC_METRICS: "QC metrics from analysis",
            self.SEX_CHECK: "Results from sex validation",
        }
        return descriptions.get(self, "Description not available")


class AnalysisTags(StrEnum):
    ASPCF_PLOT: str = "aspcf-plot"
    ASSEMBLY: str = "assembly"
    AUTOZYG: str = "autozyg"
    BED: str = "bed"
    BED_INDEX: str = "bed-index"
    BIGWIG: str = "bigwig"
    CIRCULAR_PLOT: str = "circular-plot"
    CLINICAL: str = "clinical"
    CONFIG: str = "config"
    COVERAGE: str = "coverage"
    FILTERED: str = "filtered"
    FIRST_PASS: str = "first-pass"
    FRACSNP: str = "fracsnp"
    FUSION: str = "fusion"
    GENES: str = "genes"
    GERMLINE_PLOT: str = "germline-plot"
    JUNCTION: str = "junction"
    METRICS: str = "metrics"
    MITOCHONDRIA: str = "mitochondria"
    PROFILE_PLOT: str = "profile-plot"
    QC_CRAM: str = "qc-cram"
    QC_CRAM_INDEX: str = "qc-cram-index"
    RAW_PROFILE_PLOT: str = "raw-profile-plot"
    REFERENCE_INFO: str = "reference-info"
    REGIONS: str = "regions"
    RESEARCH: str = "research"
    SCATTER_PLOT: str = "scatter-plot"
    SECOND_PASS: str = "second-pass"
    SEGMENTS: str = "segments"
    SITES: str = "sites"
    SUNRISE_PLOT: str = "sunrise-plot"
    TCOV: str = "tcov"
    TIDDIT_COVERAGE: str = "tiddit-coverage"
    TUMOR_PLOT: str = "tumor-plot"
    UMI: str = "umi"
    UMI_CRAM: str = "umi-cram"
    UMI_CRAM_INDEX: str = "umi-cram-index"
    VCF_FUSION: str = "vcf-fusion"
    VISUALIZATION: str = "visualization"

    @classmethod
    def name(cls) -> str:
        return "Analysis Tags"

    @property
    def description(self) -> str:
        descriptions: dict[AnalysisTags, str] = {
            self.ASPCF_PLOT: "Plot of LogR and BAF values",
            self.ASSEMBLY: "Assembly",
            self.AUTOZYG: "Autozygous region",
            self.BED: "Bed file",
            self.BED_INDEX: "Following index",
            self.BIGWIG: "Bigwig formatted file",
            self.CIRCULAR_PLOT: "Circular plot",
            self.CLINICAL: "Clinical subset",
            self.CONFIG: "Config file",
            self.COVERAGE: "Output with coverage information",
            self.FILTERED: "Filtered data",
            self.FIRST_PASS: "Data metrics first pass",
            self.FRACSNP: "Fraction of reads with SNP",
            self.FUSION: "Fusion transcripts",
            self.GENES: "Related to genes",
            self.GERMLINE_PLOT: "Plot of LogR and BAF values for normal sample",
            self.JUNCTION: "Junction data",
            self.METRICS: "Data metrics",
            self.MITOCHONDRIA: "Mitochondria related",
            self.PROFILE_PLOT: "Copy number profile plot",
            self.QC_CRAM: "QC alignment file in CRAM format",
            self.QC_CRAM_INDEX: "QC index file for alignment file in CRAM format",
            self.RAW_PROFILE_PLOT: "Copy number profile without rounding to whole numbers",
            self.REFERENCE_INFO: "Information about references used in analysis",
            self.REGIONS: "Output for regions",
            self.RESEARCH: "Research set",
            self.SCATTER_PLOT: "Scatter plot",
            self.SECOND_PASS: "Data metrics second pass",
            self.SEGMENTS: "Output for segments",
            self.SITES: "Output for sites",
            self.SUNRISE_PLOT: "Sunrise plot",
            self.TCOV: "Coverage output",
            self.TIDDIT_COVERAGE: "Coverage output from tiddit",
            self.TUMOR_PLOT: "Plot of LogR and BAF values for tumor sample",
            self.UMI: "Files related to UMI workflow",
            self.UMI_CRAM: "UMI consensus filtered cram file",
            self.UMI_CRAM_INDEX: "Index for the UMI consensus filtered cram file",
            self.VCF_FUSION: "Converted RNA fusion file to SV VCF",
            self.VISUALIZATION: "Visualizes data",
        }
        return descriptions.get(self, "Description not available")


class BioinfoToolsTags(StrEnum):
    ARRIBA: str = "arriba"
    ASCATNGS: str = "ascatngs"
    ASEREADCOUNTER: str = "asereadcounter"
    CHANJO: str = "chanjo"
    CHROMOGRAPH: str = "chromograph"
    CNVKIT: str = "cnvkit"
    CNVPYTOR: str = "cnvpytor"
    CYRIUS: str = "cyrius"
    DEEPVARIANT: str = "deepvariant"
    DELLY: str = "delly"
    DESEQ2: str = "deseq2"
    DNASCOP: str = "dnascope"
    EKLIPSE: str = "eklipse"
    EXPANSIONHUNTER: str = "expansionhunter"
    FASTP: str = "fastp"
    FASTQC: str = "fastqc"
    FUSIONCATCHER: str = "fusioncatcher"
    FUSIONCATCHER_SUMMARY: str = "fusioncatcher-summary"
    FUSIONINSPECTOR: str = "fusioninspector"
    GENOTYPER: str = "genotyper"
    GENS: str = "gens"
    GFFCOMPARE: str = "gffcompare"
    HAPLOTYPE_CALLER: str = "haplotype-caller"
    MANTA: str = "manta"
    MERGED: str = "merged"
    MITODEL: str = "mitodel"
    NEXTCLADE: str = "nextclade"
    PEDDY: str = "peddy"
    PICARD: str = "picard"
    PIZZLY: str = "pizzly"
    RETROSEQ: str = "retroseq"
    SALMON_QUANT: str = "salmon-quant"
    SENTION: str = "sention"
    SOMALIER: str = "somalier"
    SQUID: str = "squid"
    STAR_FUSION: str = "star-fusion"
    STRINGTIE: str = "stringtie"
    SVDB: str = "svdb"
    TIDDIT: str = "tiddit"
    TNSCOPE: str = "tnscope"
    TNSCOPE_UMI: str = "tnscope-umi"
    UPD: str = "upd"
    VARDICT: str = "vardict"
    WISECONDOR: str = "wisecondor"

    @classmethod
    def name(cls) -> str:
        return "Bioinfo Tools Tags"

    @property
    def description(self) -> str:
        descriptions: dict[BioinfoToolsTags, str] = {
            self.ARRIBA: "Fusion caller",
            self.ASCATNGS: "Tool to identify somatically acquired copy-number alterations",
            self.ASEREADCOUNTER: "Count reads mapping to heterozygous sites",
            self.CHANJO: "Tool to keep track of coverage over specific regions",
            self.CHROMOGRAPH: "Tool to create PNG images from BED and WIG files from mikaell",
            self.CNVKIT: "Tool to call copy number variations",
            self.CNVPYTOR: "Tool for CNV/CNA analysis from depth-of-coverage by mapped reads",
            self.CYRIUS: "Tool to call the problematic CYP2D6 gene",
            self.DEEPVARIANT: "Variantcaller",
            self.DELLY: "Cancer structural variant prediction tool",
            self.DESEQ2: "Differential expression analysis with DESeq2",
            self.DNASCOP: "Call snv indels",
            self.EKLIPSE: "Detection and quantification of mitochondrial DNA deletions",
            self.EXPANSIONHUNTER: "Call repeat expansions",
            self.FASTP: "Preprocessing tool for FastQ files",
            self.FASTQC: "Quality control tool for high throughput sequence data",
            self.FUSIONCATCHER: "Fusion caller",
            self.FUSIONCATCHER_SUMMARY: "Fusion caller summary",
            self.FUSIONINSPECTOR: "Fusion inspection",
            self.GENOTYPER: "SNV indel caller from sention",
            self.GENS: "CNV visualization tool",
            self.GFFCOMPARE: "Compare gff files",
            self.HAPLOTYPE_CALLER: "Call snv and indels",
            self.MANTA: "Tool to call structural variants",
            self.MITODEL: "Tool to identify mitochondrial deletion signatures",
            self.NEXTCLADE: "Viral genome clade assignment",
            self.PEDDY: "Tool to check pedigree and ancestral relations",
            self.PICARD: "Picard set of bioinformatic tools",
            self.PIZZLY: "Fusion caller",
            self.RETROSEQ: "Mobile element caller",
            self.SALMON_QUANT: "Transcript quantification",
            self.SENTION: "Sention algorithm",
            self.SOMALIER: "Tool for sample-swap and relatedness checks",
            self.SQUID: "Fusion caller",
            self.STAR_FUSION: "Fusion caller",
            self.STRINGTIE: "Transcript assembler",
            self.SVDB: "Tool to merge SV vcf files from multiple variant callers",
            self.TIDDIT: "Tool to identify chromosomal rearrangements",
            self.TNSCOPE: "Call snv indels",
            self.TNSCOPE_UMI: "Call snv indels for umi",
            self.UPD: "Uniparent disomy caller from bjhall",
            self.VARDICT: "Cancer variant caller",
            self.WISECONDOR: "NIPT caller",
        }
        return descriptions.get(self, "Description not available")


class MipTags(StrEnum):
    EXE_VER: str = "exe-ver"
    MIP_ANALYSE: str = "mip-analyse"
    MIP_CONFIG: str = "mip-config"
    MIP_LOG: str = "mip-log"
    PEDIGREE_YAML: str = "pedigree-yaml"
    SAMPLE_INFO: str = "sample-info"
    VARIANT_CATALOG: str = "variant-catalog"

    @classmethod
    def name(cls) -> str:
        return "MIP Tags"

    @property
    def description(self) -> str:
        descriptions: dict[MipTags, str] = {
            self.EXE_VER: "Executable versions",
            self.MIP_ANALYSE: "MIP information about analysis",
            self.MIP_CONFIG: "MIP configs for analysis",
            self.MIP_LOG: "Logs for MIP analysis",
            self.PEDIGREE_YAML: "YAML file with pedigree information",
            self.SAMPLE_INFO: "MIP info file about samples",
            self.VARIANT_CATALOG: "Variant catalog used with expansionhunter",
        }
        return descriptions.get(self, "Description not available")


class BalsamicTags(StrEnum):
    BALSAMIC_CONFIG: str = "balsamic-config"
    BALSAMIC_DAG: str = "balsamic-dag"
    BALSAMIC_REPORT: str = "balsamic-report"

    @classmethod
    def name(cls) -> str:
        return "BALSAMIC Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, BalsamicTags] = {
            self.BALSAMIC_CONFIG: "Balsamic configs for analysis",
            self.BALSAMIC_DAG: "Balsamic run schema",
            self.BALSAMIC_REPORT: "Report from analysis",
        }
        return descriptions.get(self, "Description not available")


class MicrosaltTags(StrEnum):
    MICROSLAT_CONFIG: str = "microsalt-config"
    MICROSLAT_LOG: str = "microsalt-log"
    TYPING_REPORT: str = "typing-report"

    @classmethod
    def name(cls) -> str:
        return "MicroSalt Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, MicrosaltTags] = {
            self.MICROSLAT_CONFIG: "Config settings for microsalt analysis",
            self.MICROSLAT_LOG: "SLURM log for microsalt analysis",
            self.TYPING_REPORT: "Results from bacterial typing",
        }
        return descriptions.get(self, "Description not available")


class MutantTags(StrEnum):
    ARTIC_JSON: str = "artic-json"
    ARTIC_QC: str = "artic-qc"
    ARTIC_SUM: str = "artic-sum"
    ARTIC_TYPE: str = "artic-type"
    ARTIC_VAR: str = "artic-var"
    CONSENSUS: str = "consensus"
    CONSENSUS_SAMPLE: str = "consensus-sample"
    FOHM_DELIVERY: str = "fohm-delivery"
    INSTRUMENT_PROPERTIES: str = "instrument-properties"
    KOMPLETTERING: str = "komplettering"
    KS_AUX_RESULTS: str = "ks-aux-results"
    KS_DELIVERY: str = "ks-delivery"
    KS_RESULTS: str = "ks-results"
    MUTANT_CONFIG: str = "mutant-config"
    MUTANT_LOG: str = "mutant-log"
    PANGOLIN: str = "pangolin"
    PANGOLIN_TYPING: str = "pangolin-typing"
    PANGOLIN_TYPING_FOHM: str = "pangolin-typing-fohm"
    TYPING_REPORT: str = "typing-report"
    TYPING_SUMMARY: str = "typing-summary"
    VCF_COVID: str = "vcf-covid"

    @classmethod
    def name(cls) -> str:
        return "Mutant Tags"

    @property
    def description(self) -> str:
        descriptions: dict[MutantTags, str] = {
            self.ARTIC_JSON: "GMS-Artic json file",
            self.ARTIC_QC: "GMS-Artic QC file",
            self.ARTIC_SUM: "GMS-Artic summary file",
            self.ARTIC_TYPE: "GMS-Artic typing file",
            self.ARTIC_VAR: "GMS-Artic variant file",
            self.CONSENSUS: "Consensus sequence",
            self.CONSENSUS_SAMPLE: "Separate sample consensus fasta",
            self.FOHM_DELIVERY: "Relevant for FoHM",
            self.INSTRUMENT_PROPERTIES: "Sequencing metadata",
            self.KOMPLETTERING: "Filetype specific for national uploading of microbial data",
            self.KS_AUX_RESULTS: "KS modification of pangolin called variants",
            self.KS_DELIVERY: "Relevant for Karolinska hospital/microbial routine",
            self.KS_RESULTS: "KS modification of pangolin typing results",
            self.MUTANT_CONFIG: "Config settings for mutant analysis",
            self.MUTANT_LOG: "SLURM log for mutant analysis",
            self.PANGOLIN: "Pangolin specific output",
            self.PANGOLIN_TYPING: "Pangolin typing results",
            self.PANGOLIN_TYPING_FOHM: "Pangolin typing report with only qc_pass samples included",
            self.TYPING_REPORT: "Results from typing",
            self.TYPING_SUMMARY: "Summary of results from typing",
            self.VCF_COVID: "VCF file containing covid data. Distinction req. by production",
        }
        return descriptions.get(self, "Description not available")


class RarediseaseTags(StrEnum):
    ANNOTATION: str = "annotation"
    EKLIPSE_DEL: str = "eklipse-del"
    EKLIPSE_GENES: str = "eklipse-gene"
    EKLIPSE_PNG: str = "eklipse-png"
    HAPLOGREP: str = "haplogrep"
    NGSBITS: str = "ngsbits-samplegender"
    SVDBQUERY: str = "svdbquery"
    SVDBQUERY_INDEX: str = "svdbquery-index"

    @classmethod
    def name(cls) -> str:
        return "Raredisease Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, RarediseaseTags] = {
            self.ANNOTATION: "Annotation tag",
            self.EKLIPSE_DEL: "Mitochondrial eKLIPse deletions",
            self.EKLIPSE_GENES: "Mitochondrial eKLIPse genes",
            self.EKLIPSE_PNG: "Mitochondrial eKLIPse png",
            self.HAPLOGREP: "Haplogrep",
            self.NGSBITS: "Result from SampleGender tool to determine sample sex",
            self.SVDBQUERY: "Query of SVDB results",
            self.SVDBQUERY_INDEX: "Query of SVDB results, index",
        }
        return descriptions.get(self, "Description not available")


class RnafusionTags(StrEnum):
    ARRIBA_VISUALISATION: str = "arriba-visualisation"
    FUSIONINSPECTOR_HTML: str = "fusioninspector-html"
    FUSIONREPORT: str = "fusionreport"

    @classmethod
    def name(cls) -> str:
        return "Rnafusion Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, RnafusionTags] = {
            self.ARRIBA_VISUALISATION: "Arriba visualization",
            self.FUSIONINSPECTOR_HTML: "Fusioninspector report",
            self.FUSIONREPORT: "Fusion-report analysis",
        }
        return descriptions.get(self, "Description not available")


class TaxprofilerTags(StrEnum):
    BRACKEN: str = "bracken"
    CENTRIFUGE: str = "centrifuge"
    COMBINED_REPORT: str = "combined-report"
    KRAKEN2: str = "kraken2"
    KRONA: str = "krona"
    METAGENOMICS_REPORT: str = "metagenomics-report"

    @classmethod
    def name(cls) -> str:
        return "Taxprofiler Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, TaxprofilerTags] = {
            self.BRACKEN: "Tool to compute the abundance of species and is companion program to "
            "kraken2",
            self.CENTRIFUGE: "Taxonomic sequence classifier for metagenomic sequences",
            self.COMBINED_REPORT: "A combined report of taxonomic classification from all samples",
            self.KRAKEN2: "Taxonomic sequence classifier that assigns taxonomic labels to "
            "metagenomic DNA sequences",
            self.KRONA: "Visualisation tool that allows to explore relative abundances and "
            "confidences within metagenomic classifications",
            self.METAGENOMICS_REPORT: "Report describing taxonomic classification results",
        }
        return descriptions.get(self, "Description not available")


class TomteTags(StrEnum):
    FRASER: str = "fraser"
    OUTRIDER: str = "outrider"

    @classmethod
    def name(cls) -> str:
        return "Tomte Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, TomteTags] = {
            self.FRASER: "Aberrant splicing calculated with DROP",
            self.OUTRIDER: "Aberrant expression calculated with DROP",
        }
        return descriptions.get(self, "Description not available")


class NextflowTags(StrEnum):
    NEXTFLOW_CONFIG: str = "nextflow-config"
    NEXTFLOW_PARAMS: str = "nextflow-params"
    SAMPLESHEET: str = "nextflow-samplesheet"
    SAMPLESHEET_VALID: str = "samplesheet-valid"
    SOFTWARE_VERSIONS: str = "software-versions"
    MANIFEST: str = "manifest"

    @classmethod
    def name(cls) -> str:
        return "Nextflow Tags"

    @property
    def description(self) -> str:
        descriptions: dict[str, NextflowTags] = {
            self.NEXTFLOW_CONFIG: "Nextflow config for analysis",
            self.NEXTFLOW_PARAMS: "Nextflow parameters file for analysis",
            self.SAMPLESHEET: "Samplesheet for analysis",
            self.SAMPLESHEET_VALID: "Validated samplesheet",
            self.SOFTWARE_VERSIONS: "List of all software used and their versions",
        }
        return descriptions.get(self, "Description not available")


class UsageTags(StrEnum):
    AUDIT: str = "audit"
    CG: str = "cg"
    CHANJO: str = "chanjo"
    CLINICAL_DELIVERY: str = "clinical-delivery"
    DELIVER: str = "deliver"  # Deprecated
    GENOTYPE: str = "genotype"
    JANUS: str = "janus"
    LONG_TERM_STORAGE: str = "long-term-storage"
    NIPT: str = "nipt"
    SCOUT: str = "scout"
    STORAGE: str = "storage"  # Deprecated


USAGE_TAGS: set[str] = {tag.value for tag in UsageTags}

COMMON_TAG_CATEGORIES: list[Any] = [
    AlignmentTags,
    AnalysisTags,
    BioinfoToolsTags,
    FamilyTags,
    QCTags,
    RawDataTags,
    ReportTags,
    VariantTags,
]


TAG_CATEGORIES: list[Any] = COMMON_TAG_CATEGORIES + [
    BalsamicTags,
    MicrosaltTags,
    MipTags,
    MutantTags,
    NextflowTags,
    RarediseaseTags,
    RnafusionTags,
    TaxprofilerTags,
    TomteTags,
]

ALL_TAGS: set[str] = {tag.value for category in TAG_CATEGORIES for tag in category}
