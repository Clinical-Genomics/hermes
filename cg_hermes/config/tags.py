ALIGNMENT_COMMON = {
    "bam": {
        "description": "Alignment file in BAM format",
    },
    "bam-index": {
        "description": "Index file for alignment file in BAM format",
    },
    "bam-mt": {
        "description": "Alignment file in BAM format holding the reaads from chrMT",
    },
    "cram": {
        "description": "Alignment file in CRAM format",
    },
    "cram-index": {
        "description": "Index file for alignment file in CRAM format",
    },
}

RAW_DATA = {
    "fastq": {"description": "Files with raw data in fastq format"},
    "forward-strand": {"description": "Reads from forward strand"},
    "reverse-strand": {"description": "Reads from reverse strand"},
    "unpaired-reads": {"description": "Reads that could not be paired"},
}


VARIANT_COMMON = {
    "cnv": {"description": "Copy number variants"},
    "normal": {"description": "Associated with normal sample"},
    "rhocall-viz": {"description": "Runs of homozygosity index"},
    "smn-calling": {"description": "Copy number calls for the SMN gene"},
    "snv-bcf": {"description": "Gvcf including all SNV variants"},
    "snv-gbcf": {"description": "Gvcf including all SNV variants"},
    "sv-bcf": {"description": "Gvcf including all SV variants"},
    "sv-vcf": {"description": "Variant call formated file with structural variants"},
    "sv-vcf-index": {"description": "Following index"},
    "telomere-calling": {"description": "Variants from telomere calling"},
    "tmb": {"description": "Tumor mutational burden information"},
    "tumor": {"description": "Associated with tumor sample"},
    "upd": {"description": "Uniparental disomy variants"},
    "vcf": {"description": "Variant call formated file"},
    "vcf-index": {"description": "Following index"},
    "vcf-snv-clinical": {"description": "SNV variants from clinical panels"},
    "vcf-snv-clinical-index": {"description": "Following index"},
    "vcf-snv-research": {"description": "SNV variants from whole genome"},
    "vcf-snv-research-index": {"description": "Following index"},
    "vcf-str": {"description": "Short tandem repeat variants"},
    "vcf-str-index": {"description": "Following index"},
    "vcf-sv-clinical": {"description": "SV variants from clinical panels"},
    "vcf-sv-clinical-index": {"description": "Following index"},
    "vcf-sv-research": {"description": "SV variants from whole genome"},
    "vcf-sv-research-index": {"description": "Following index"},
    "vcf2cytosure": {"description": "Conversion from vcf format to cytosure format"},
}

FAMILY_COMMON = {
    "pedigree": {"description": "Pedigree information"},
    "ped": {"description": "Pedigree information"},
}

REPORTING_COMMON = {
    "multiqc-html": {"description": "Multiqc report for the run in html format"},
    "multiqc-json": {"description": "Multiqc report for the run in json format"},
    "sambamba-depth": {"description": "Coverage information from sambamba"},
    "vcf-report": {"description": "Results and QC from variant calling"},
    "qc-report": {"description": "Results and QC"},
}

VALIDATIONS_COMMON = {
    "ped-check": {"description": "Results from pedigree validation"},
    "qc-metrics": {"description": "QC metrics from analysis"},
    "sex-check": {"description": "Results from sex validation"},
}

ANALYSIS_COMMON = {
    "autozyg": {"description": "Autozygous region"},
    "bigwig": {"description": "Bigwig formated file"},
    "config": {"description": "Config file"},
    "coverage": {"description": "Output with coverage information"},
    "diagram": {"description": "Data diagram"},
    "filtered": {"description": "Filtered data"},
    "fracsnp": {"description": "Fraction of reads with snp"},
    "genes": {"description": "Related to genes"},
    "metrics": {"description": "Data metrics"},
    "reference-info": {"description": "Information about references used in analysis"},
    "regions": {"description": "Output for regions"},
    "segments": {"description": "Output for segments"},
    "sites": {"description": "Output for sites"},
    "tcov": {"description": "Coverage output"},
    "tiddit-coverage": {"description": "Coverage output from tiddit"},
    "visualization": {"description": "Visualizes data"},
    "assembly": {"description": "Assembled genome"},
}

TOOLS = {
    "chanjo": {"description": "Tool to keep track of coverage over specific regions"},
    "chromograph": {"description": "Tool to create PNG images from BED and WIG files from mikaell"},
    "cnvkit": {"description": "Tool to call copy number variations"},
    "cyrius": {"description": "Tool to call the problematic CYP2D6 gene"},
    "genotyper": {"description": "SNV indel caller from sention"},
    "haplotype-caller": {"description": "Call snv and indels"},
    "manta": {"description": "Tool to call structural variants"},
    "mutect": {"description": "Cancer variant caller"},
    "peddy": {"description": "Tool to check pedigree and ancestral relations"},
    "picard": {"description": "Picard set of bioinformatic tools"},
    "scope": {"description": "Call snv indels"},
    "sention": {"description": "Sention algorithm"},
    "strelka": {"description": "Cancer variant caller"},
    "upd": {"description": "Uniparent disomy caller from bjhall"},
    "vardict": {"description": "Cancer variant caller"},
    "wisecondor": {"description": "NIPT caller"},
}

MIP_SPECIFIC = {
    "exe-ver": {"description": "Executable versions"},
    "mip-analyse": {"description": "MIP information about analysis"},
    "mip-config": {"description": "MIP configs for analysis"},
    "mip-log": {"description": "Logs for MIP analysis"},
    "pedigree-yaml": {"description": "YAML file with pedigree information"},
    "sample-info": {"description": "MIP info file about samples"},
}

BALSAMIC_SPECIFIC = {
    "balsamic-config": {"description": "Balsamic configs for analysis"},
    "balsamic-dag": {"description": "Balsamic run schema"},
    "balsamic-report": {"description": "Report from analysis"},
}

MICROSALT_SPECIFIC = {
    "microsalt-config": {"description": "Config settings for microsalt analysis"},
    "microsalt-log": {"description": "SLURM log for microsalt analysis"},
    "typing-report": {"description": "Results from bacterial typing"},
}

AVAILABLE_USAGES = {
    "audit",
    "cg",
    "chanjo",
    "deliver",
    "genotype",
    "nipt",
    "scout",
    "storage",
    "vogue",
}

COMMON_TAG_CATEGORIES = {
    "alignment_tags": ALIGNMENT_COMMON,
    "analysis_tags": ANALYSIS_COMMON,
    "family_tags": FAMILY_COMMON,
    "raw_data": RAW_DATA,
    "reporting_tags": REPORTING_COMMON,
    "tool_tags": TOOLS,
    "validation_tags": VALIDATIONS_COMMON,
    "variant_tags": VARIANT_COMMON,
}

ALL_TAG_CATEGORIES = [
    ALIGNMENT_COMMON,
    ANALYSIS_COMMON,
    BALSAMIC_SPECIFIC,
    FAMILY_COMMON,
    MIP_SPECIFIC,
    MICROSALT_SPECIFIC,
    RAW_DATA,
    REPORTING_COMMON,
    TOOLS,
    VALIDATIONS_COMMON,
    VARIANT_COMMON,
]

ALL_TAGS = set(tag for category in ALL_TAG_CATEGORIES for tag in category.keys())


if __name__ == "__main__":
    print(ALL_TAGS)
