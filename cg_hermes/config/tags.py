ALIGNMENT_COMMON = {
    "cram": {
        "description": "Alignment file in CRAM format",
    },
    "cram-index": {
        "description": "Index file for alignment file in CRAM format",
    },
    "bam": {
        "description": "Alignment file in BAM format",
    },
    "bam-index": {
        "description": "Index file for alignment file in BAM format",
    },
    "bam-mt": {
        "description": "Alignment file in BAM format holding the reaads from chrMT",
    },
}

RAW_DATA = {"fastq": {"description": "Files with raw data in fastq format"}}


VARIANT_COMMON = {
    "snv-gbcf": {"description": "Gvcf including all SNV variants"},
    "snv-bcf": {"description": "Gvcf including all SNV variants"},
    "sv-bcf": {"description": "Gvcf including all SV variants"},
    "upd": {"description": "Uniparental disomy variants"},
    "vcf-snv-clinical": {"description": "SNV variants from clinical panels"},
    "vcf-snv-clinical-index": {"description": "Following index"},
    "vcf-sv-clinical": {"description": "SV variants from clinical panels"},
    "vcf-sv-clinical-index": {"description": "Following index"},
    "vcf-snv-research": {"description": "SNV variants from whole genome"},
    "vcf-snv-research-index": {"description": "Following index"},
    "vcf-sv-research": {"description": "SV variants from whole genome"},
    "vcf-sv-research-index": {"description": "Following index"},
    "vcf-str": {"description": "Short tandem repeat variants"},
    "vcf-str-index": {"description": "Following index"},
    "rhocall-viz": {"description": "Runs of homozygosity index"},
    "smn-calling": {"description": "Copy number calls for the SMN gene"},
    "telomere-calling": {"description": "Variants from telomere calling"},
    "vcf2cytosure": {"description": "Conversion from vcf format to cytosure format"},
    "tumor": {"description": "Associated with tumor sample"},
    "normal": {"description": "Associated with normal sample"},
    "vcf": {"description": "Variant call formated file"},
    "vcf-index": {"description": "Following index"},
    "sv-vcf": {"description": "Variant call formated file with structural variants"},
    "sv-vcf-index": {"description": "Following index"},
    "tmb": {"Tumor mutational burden information"},
}

FAMILY_COMMON = {
    "pedigree": {"description": "Pedigree information"},
    "ped": {"description": "Pedigree information"},
}

REPORTING_COMMON = {
    "multiqc-html": {"description": "Multiqc report for the run in html format"},
    "multiqc-json": {"description": "Multiqc report for the run in json format"},
    "sambamba-depth": {"description": "Coverage information from sambamba"},
    "vcf-report": {"Results and QC from variant calling"},
}

VALIDATIONS_COMMON = {
    "sex-check": {"description": "Results from sex validation"},
    "qc-metrics": {"description": "QC metrics from analysis"},
    "ped-check": {"description": "Results from pedigree validation"},
}

ANALYSIS_COMMON = {
    "config": {"description": "Config file"},
    "reference-info": {"description": "Information about references used in analysis"},
    "sites": {"description": "Output for sites"},
    "genes": {"description": "Related to genes"},
    "regions": {"description": "Output for regions"},
    "segments": {"description": "Output for segments"},
    "tcov": {"description": "Coverage output"},
    "autozyg": {"description": "Autozygous region"},
    "fracsnp": {"description": "Fraction of reads with snp"},
    "tiddit-coverage": {"description": "Coverage output from tiddit"},
    "bigwig": {"description": "Bigwig formated file"},
    "coverage": {"description": "Output with coverage information"},
    "visualization": {"description": "Visualizes data"},
    "diagram": {"description": "Data diagram"},
    "metrics": {"description": "Data metrics"},
    "filtered": {"description": "Filtered data"},
}

TOOLS = {
    "chanjo": {"description": "Tool to keep track of coverage over specific regions"},
    "peddy": {"description": "Tool to check pedigree and ancestral relations"},
    "chromograph": {"description": "Tool to create PNG images from BED and WIG files from mikaell"},
    "cyrius": {"description": "Tool to call the problematic CYP2D6 gene"},
    "upd": {"description": "Uniparent disomy caller from bjhall"},
    "cnvkit": {"description": "Tool to call copy number variations"},
    "manta": {"description": "Tool to call structural variants"},
    "sention": {"description": "Sention algorithm"},
    "haplotype-caller": {"description": "Call snv and indels"},
    "scope": {"description": "Call snv indels"},
    "genotyper": {"description": "SNV indel caller from sention"},
    "vardict": {"description": "Cancer variant caller"},
    "strelka": {"description": "Cancer variant caller"},
    "mutect": {"description": "Cancer variant caller"},
    "wisecondor": {"description": "NIPT caller"},
}

MIP_SPECIFIC = {
    "mip-config": {"description": "MIP configs for analysis"},
    "mip-analyse": {"description": "MIP information about analysis"},
    "mip-log": {"description": "Logs for MIP analysis"},
    "sample-info": {"description": "MIP info file about samples"},
    "pedigree-yaml": {"description": "YAML file with pedigree information"},
    "exe-ver": {"description": "Executable versions"},
}

BALSAMIC_SPECIFIC = {
    "balsamic-config": {"description": "Balsamic configs for analysis"},
    "balsamic-report": {"description": "Report from analysis"},
    "balsamic-dag": {"description": "Balsamic run schema"},
}

AVAILABLE_USAGES = {
    "scout",
    "cg",
    "vogue",
    "chanjo",
    "storage",
    "genotype",
    "audit",
    "deliver",
    "nipt",
}

COMMON_TAG_CATEGORIES = {
    "alignment_tags": ALIGNMENT_COMMON,
    "raw_data": RAW_DATA,
    "variant_tags": VARIANT_COMMON,
    "family_tags": FAMILY_COMMON,
    "reporting_tags": REPORTING_COMMON,
    "validation_tags": VALIDATIONS_COMMON,
    "analysis_tags": ANALYSIS_COMMON,
    "tool_tags": TOOLS,
}

ALL_TAG_CATEGORIES = [
    ALIGNMENT_COMMON,
    RAW_DATA,
    VARIANT_COMMON,
    FAMILY_COMMON,
    REPORTING_COMMON,
    VALIDATIONS_COMMON,
    ANALYSIS_COMMON,
    TOOLS,
    MIP_SPECIFIC,
    BALSAMIC_SPECIFIC,
]

ALL_TAGS = set(tag for category in ALL_TAG_CATEGORIES for tag in category.keys())


if __name__ == "__main__":
    print(ALL_TAGS)
