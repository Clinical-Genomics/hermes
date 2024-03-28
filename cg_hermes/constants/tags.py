from enum import StrEnum
from typing import Any


class AlignmentTags(StrEnum):
    BAM_INDEX: str = "bam-index"
    BAM_MT: str = "bam-mt"
    BAM: str = "bam"
    CRAM_INDEX: str = "cram-index"
    CRAM: str = "cram"

    @property
    def description(self):
        descriptions: dict[AlignmentTags, str] = {
            self.BAM_INDEX: "Index file for alignment file in BAM format",
            self.BAM_MT: "Alignment file in BAM format holding the reads from chrMT",
            self.BAM: "Alignment file in BAM format",
            self.CRAM_INDEX: "Index file for alignment file in CRAM format",
            self.CRAM: "Alignment file in CRAM format",
        }
        return descriptions.get(self, "Description not available")


class RawDataTags(StrEnum):
    FASTA: str = "fasta"
    FASTQ: str = "fastq"
    FORWARD_STRAND: str = "forward-strand"
    REVERSE_STRAND: str = "reverse-strand"
    RNA: str = "rna"
    UNPAIRED_READS: str = "unpaired-reads"

    @property
    def description(self):
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
    NORMAL: str = "normal"
    RHOCALL_VIZ: str = "rhocall-viz"
    SMN_CALLING: str = "smn-calling"
    SNV_BCF: str = "snv-bcf"
    SNV_GBCF: str = "snv-gbcf"
    SNV: str = "snv"
    SOMATIC: str = "somatic"
    SV_BCF: str = "sv-bcf"
    SV_VCF_INDEX: str = "sv-vcf-index"
    SV_VCF: str = "sv-vcf"
    SV: str = "sv"
    TELOMERE_CALLING: str = "telomere-calling"
    TMB: str = "tmb"
    TUMOR: str = "tumor"
    UPD: str = "upd"
    VARIANTS: str = "variants"
    VCF_INDEX: str = "vcf-index"
    VCF_SNV_CLINICAL_INDEX: str = "vcf-snv-clinical-index"
    VCF_SNV_CLINICAL: str = "vcf-snv-clinical"
    VCF_SNV_FILTERED_INDEX: str = "vcf-snv-filtered-index"
    VCF_SNV_FILTERED: str = "vcf-snv-filtered"
    VCF_SNV_GERMLINE_NORMAL_INDEX: str = "vcf-snv-germline-normal-index"
    VCF_SNV_GERMLINE_NORMAL: str = "vcf-snv-germline-normal"
    VCF_SNV_GERMLINE_TUMOR_INDEX: str = "vcf-snv-germline-tumor-index"
    VCF_SNV_GERMLINE_TUMOR: str = "vcf-snv-germline-tumor"
    VCF_SNV_INDEX: str = "vcf-snv-index"
    VCF_SNV_RESEARCH_INDEX: str = "vcf-snv-research-index"
    VCF_SNV_RESEARCH: str = "vcf-snv-research"
    VCF_SNV: str = "vcf-snv"
    VCF_STR_INDEX: str = "vcf-str-index"
    VCF_STR: str = "vcf-str"
    VCF_SV_CLINICAL_INDEX: str = "vcf-sv-clinical-index"
    VCF_SV_CLINICAL: str = "vcf-sv-clinical"
    VCF_SV_GERMLINE_NORMAL_INDEX: str = "vcf-sv-germline-normal-index"
    VCF_SV_GERMLINE_NORMAL: str = "vcf-sv-germline-normal"
    VCF_SV_GERMLINE_TUMOR_INDEX: str = "vcf-sv-germline-tumor-index"
    VCF_SV_GERMLINE_TUMOR: str = "vcf-sv-germline-tumor"
    VCF_SV_INDEX: str = "vcf-sv-index"
    VCF_SV_RESEARCH_INDEX: str = "vcf-sv-research-index"
    VCF_SV_RESEARCH: str = "vcf-sv-research"
    VCF_SV: str = "vcf-sv"
    VCF_UMI_SNV_CLINICAL_INDEX: str = "vcf-umi-snv-clinical-index"
    VCF_UMI_SNV_CLINICAL: str = "vcf-umi-snv-clinical"
    VCF_UMI_SNV_INDEX: str = "vcf-umi-snv-index"
    VCF_UMI_SNV_RESEARCH_INDEX: str = "vcf-umi-snv-research-index"
    VCF_UMI_SNV_RESEARCH: str = "vcf-umi-snv-research"
    VCF_UMI_SNV: str = "vcf-umi-snv"
    VCF: str = "vcf"
    VCF2CYTOSURE: str = "vcf2cytosure"

    @property
    def description(self):
        descriptions: dict[VariantTags, str] = {
            self.CNV: "Copy number variants",
            self.GERMLINE: "Associated with germline variants",
            self.MOBILE_ELEMENTS: "Mobile elements",
            self.NORMAL: "Associated with normal sample",
            self.RHOCALL_VIZ: "Runs of homozygosity index",
            self.SMN_CALLING: "Copy number calls for the SMN gene",
            self.SNV_BCF: "Gvcf including all SNV variants",
            self.SNV_GBCF: "Gvcf including all SNV variants",
            self.SNV: "Single nucleotide variants and short indels",
            self.SOMATIC: "Associated with somatic variants",
            self.SV_BCF: "Gvcf including all SV variants",
            self.SV_VCF_INDEX: "Following index",
            self.SV_VCF: "Variant call formatted file with structural variants",
            self.SV: "Structural variants",
            self.TELOMERE_CALLING: "Variants from telomere calling",
            self.TMB: "Tumor mutational burden information",
            self.TUMOR: "Associated with tumor sample",
            self.UPD: "Uniparental disomy variants",
            self.VARIANTS: "File pertaining variant information in some way",
            self.VCF_INDEX: "Following index",
            self.VCF_SNV_CLINICAL_INDEX: "Following index",
            self.VCF_SNV_CLINICAL: "SNV variants from clinical panels",
            self.VCF_SNV_FILTERED_INDEX: "Following index",
            self.VCF_SNV_FILTERED: "SNV variants filtered by BALSAMIC",
            self.VCF_SNV_GERMLINE_NORMAL_INDEX: "Following index",
            self.VCF_SNV_GERMLINE_NORMAL: "SNV germline normal variants",
            self.VCF_SNV_GERMLINE_TUMOR_INDEX: "Following index",
            self.VCF_SNV_GERMLINE_TUMOR: "SNV germline tumor variants",
            self.VCF_SNV_INDEX: "Following index",
            self.VCF_SNV_RESEARCH_INDEX: "Following index",
            self.VCF_SNV_RESEARCH: "SNV variants from whole genome",
            self.VCF_SNV: "SNV variant call formatted file",
            self.VCF_STR_INDEX: "Following index",
            self.VCF_STR: "Short tandem repeat variants",
            self.VCF_SV_CLINICAL_INDEX: "Following index",
            self.VCF_SV_CLINICAL: "SV variants from clinical panels",
            self.VCF_SV_GERMLINE_NORMAL_INDEX: "Following index",
            self.VCF_SV_GERMLINE_NORMAL: "SV germline normal variants",
            self.VCF_SV_GERMLINE_TUMOR_INDEX: "Following index",
            self.VCF_SV_GERMLINE_TUMOR: "SV germline tumor variants",
            self.VCF_SV_INDEX: "Following index",
            self.VCF_SV_RESEARCH_INDEX: "Following index",
            self.VCF_SV_RESEARCH: "SV variants from whole genome",
            self.VCF_SV: "SV variant call formatted file",
            self.VCF_UMI_SNV_CLINICAL_INDEX: "Following index",
            self.VCF_UMI_SNV_CLINICAL: "SNV UMI variants from clinical panels",
            self.VCF_UMI_SNV_INDEX: "Following index",
            self.VCF_UMI_SNV_RESEARCH_INDEX: "Following index",
            self.VCF_UMI_SNV_RESEARCH: "SNV UMI variant formatted file",
            self.VCF_UMI_SNV: "Raw SNV UMI variant formatted file",
            self.VCF: "Variant call formatted file",
            self.VCF2CYTOSURE: "Conversion from VCF format to cytosure format",
        }
        return descriptions.get(self, "Description not available")


class FamilyTags(StrEnum):
    PED: str = "ped"
    PEDIGREE: str = "pedigree"

    @property
    def description(self):
        descriptions: dict[FamilyTags, str] = {
            self.PED: "Pedigree information",
            self.PEDIGREE: "Pedigree information",
        }
        return descriptions.get(self, "Description not available")


class ReportTags(StrEnum):
    AUDIT: str = "audit"
    CNV_REPORT: str = "cnv-report"
    CSV: str = "csv"
    DELIVERABLE: str = "deliverable"
    DELIVERY_REPORT: str = "delivery-report"
    GENE_COUNTS: str = "gene-counts"
    GENERAL_STATS: str = "general-stats"
    MULTIQC_HTML: str = "multiqc-html"
    MULTIQC_JSON: str = "multiqc-json"
    MULTIQC: str = "multiqc"
    PDF: str = "pdf"
    PICARD_ALIGNMENT: str = "picard-alignment"
    PICARD_DUPLICATES: str = "picard-duplicates"
    PICARD_HS: str = "picard-hs"
    PICARD_INSERT_SIZE: str = "picard-insert-size"
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

    @property
    def description(self):
        descriptions: dict[ReportTags, str] = {
            self.AUDIT: "Audit file",
            self.CNV_REPORT: "CNV variant calling report",
            self.CSV: "Comma separated values",
            self.DELIVERABLE: "Deliverables file",
            self.DELIVERY_REPORT: "Delivery report with result for upload to Scout",
            self.GENE_COUNTS: "STAR read counts output per gene",
            self.GENERAL_STATS: "General statistics reported from MultiQC",
            self.MULTIQC_HTML: "MultiQC analysis report in HTML format",
            self.MULTIQC_JSON: "MultiQC analysis report in JSON format",
            self.MULTIQC: "MultiQC related files",
            self.PDF: "Portable document format",
            self.PICARD_ALIGNMENT: "High level metrics about the alignment of reads",
            self.PICARD_DUPLICATES: "Metrics calculated during marking duplicates",
            self.PICARD_HS: "Metrics for the analysis of target-capture sequencing",
            self.PICARD_INSERT_SIZE: "Metrics about the insert size distribution",
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

    @property
    def description(self):
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
    BED_INDEX: str = "bed-index"
    BED: str = "bed"
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
    PROFILE_PLOT: str = "profile-plot"
    QC_CRAM_INDEX: str = "qc-cram-index"
    QC_CRAM: str = "qc-cram"
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
    UMI_CRAM_INDEX: str = "umi-cram-index"
    UMI_CRAM: str = "umi-cram"
    UMI: str = "umi"
    VCF_FUSION: str = "vcf-fusion"
    VISUALIZATION: str = "visualization"

    @property
    def description(self):
        descriptions: dict[AnalysisTags, str] = {
            self.ASPCF_PLOT: "Plot of LogR and BAF values",
            self.ASSEMBLY: "Assembly",
            self.AUTOZYG: "Autozygous region",
            self.BED_INDEX: "Following index",
            self.BED: "Bed file",
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
            self.PROFILE_PLOT: "Copy number profile plot",
            self.QC_CRAM_INDEX: "QC index file for alignment file in CRAM format",
            self.QC_CRAM: "QC alignment file in CRAM format",
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
            self.UMI_CRAM_INDEX: "Index for the UMI consensus filtered cram file",
            self.UMI_CRAM: "UMI consensus filtered cram file",
            self.UMI: "Files related to UMI workflow",
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
    EXPANSIONHUNTER: str = "expansionhunter"
    FASTP: str = "fastp"
    FUSIONCATCHER_SUMMARY: str = "fusioncatcher-summary"
    FUSIONCATCHER: str = "fusioncatcher"
    FUSIONINSPECTOR: str = "fusioninspector"
    GENOTYPER: str = "genotyper"
    GENS: str = "gens"
    GFFCOMPARE: str = "gffcompare"
    HAPLOTYPE_CALLER: str = "haplotype-caller"
    MANTA: str = "manta"
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
    TNSCOPE_UMI: str = "tnscope-umi"
    TNSCOPE: str = "tnscope"
    UPD: str = "upd"
    VARDICT: str = "vardict"
    WISECONDOR: str = "wisecondor"

    @property
    def description(self):
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
            self.EXPANSIONHUNTER: "Call repeat expansions",
            self.FASTP: "Preprocessing tool for FastQ files",
            self.FUSIONCATCHER_SUMMARY: "Fusion caller summary",
            self.FUSIONCATCHER: "Fusion caller",
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
            self.TNSCOPE_UMI: "Call snv indels for umi",
            self.TNSCOPE: "Call snv indels",
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

    @property
    def description(self):
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

    @property
    def description(self):
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

    @property
    def description(self):
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
    CONSENSUS_SAMPLE: str = "consensus-sample"
    CONSENSUS: str = "consensus"
    FOHM_DELIVERY: str = "fohm-delivery"
    INSTRUMENT_PROPERTIES: str = "instrument-properties"
    KOMPLETTERING: str = "komplettering"
    KS_AUX_RESULTS: str = "ks-aux-results"
    KS_DELIVERY: str = "ks-delivery"
    KS_RESULTS: str = "ks-results"
    MUTANT_CONFIG: str = "mutant-config"
    MUTANT_LOG: str = "mutant-log"
    PANGOLIN_TYPING_FOHM: str = "pangolin-typing-fohm"
    PANGOLIN_TYPING: str = "pangolin-typing"
    PANGOLIN: str = "pangolin"
    TYPING_REPORT: str = "typing-report"
    TYPING_SUMMARY: str = "typing-summary"
    VCF_COVID: str = "vcf-covid"

    @property
    def description(self):
        descriptions: dict[MutantTags, str] = {
            self.ARTIC_JSON: "GMS-Artic json file",
            self.ARTIC_QC: "GMS-Artic QC file",
            self.ARTIC_SUM: "GMS-Artic summary file",
            self.ARTIC_TYPE: "GMS-Artic typing file",
            self.ARTIC_VAR: "GMS-Artic variant file",
            self.CONSENSUS_SAMPLE: "Separate sample consensus fasta",
            self.CONSENSUS: "Consensus sequence",
            self.FOHM_DELIVERY: "Relevant for FoHM",
            self.INSTRUMENT_PROPERTIES: "Sequencing metadata",
            self.KOMPLETTERING: "Filetype specific for national uploading of microbial data",
            self.KS_AUX_RESULTS: "KS modification of pangolin called variants",
            self.KS_DELIVERY: "Relevant for Karolinska hospital/microbial routine",
            self.KS_RESULTS: "KS modification of pangolin typing results",
            self.MUTANT_CONFIG: "Config settings for mutant analysis",
            self.MUTANT_LOG: "SLURM log for mutant analysis",
            self.PANGOLIN_TYPING_FOHM: "Pangolin typing report with only qc_pass samples included",
            self.PANGOLIN_TYPING: "Pangolin typing results",
            self.PANGOLIN: "Pangolin specific output",
            self.TYPING_REPORT: "Results from typing",
            self.TYPING_SUMMARY: "Summary of results from typing",
            self.VCF_COVID: "VCF file containing covid data. Distinction req. by production",
        }
        return descriptions.get(self, "Description not available")


class RnafusionTags(StrEnum):
    ARRIBA_VISUALISATION: str = "arriba-visualisation"
    FUSIONINSPECTOR_HTML: str = "fusioninspector-html"
    FUSIONREPORT: str = "fusionreport"

    @property
    def description(self):
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

    @property
    def description(self):
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


class NextflowTags(StrEnum):
    SAMPLESHEET_VALID: str = "samplesheet-valid"
    SOFTWARE_VERSIONS: str = "software-versions"

    @property
    def description(self):
        descriptions: dict[str, NextflowTags] = {
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


TAG_CATEGORIES: list[Any] = [
    AlignmentTags,
    AnalysisTags,
    BalsamicTags,
    BioinfoToolsTags,
    FamilyTags,
    MicrosaltTags,
    MipTags,
    MutantTags,
    NextflowTags,
    QCTags,
    RawDataTags,
    ReportTags,
    RnafusionTags,
    TaxprofilerTags,
    VariantTags,
]

ALL_TAGS: set[str] = {tag.value for category in TAG_CATEGORIES for tag in category}
