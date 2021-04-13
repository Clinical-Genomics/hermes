MUTANT_COMMON_TAGS = {
    frozenset({"sampleinfo", "runinfo"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["config"],
        "used_by": ["storage", "audit"],
    },
    frozenset({"variants", "genotyping"}): {
        "is_mandatory": False,
        "tags": ["vcf", "vcf-report"],
        "used_by": ["deliver"],
    },
    frozenset({"variants", "variant-calling"}): {
        "is_mandatory": False,
        "tags": ["tsv", "vcf-report"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-qc", "result_aggregation"}): {
        "is_mandatory": False,
        "tags": ["qc-report", "csv", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-type", "typing"}): {
        "is_mandatory": False,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-json", "result_aggregation"}): {
        "is_mandatory": False,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-sum", "report"}): {
        "is_mandatory": False,
        "tags": ["summary", "csv", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-var", "report"}): {
        "is_mandatory": False,
        "tags": ["variants", "csv", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-info", "report"}): {
        "is_mandatory": False,
        "tags": ["komplettering", "fohm", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"runtime-settings", "runinfo"}): {
        "is_mandatory": False,
        "tags": ["mutant-config"],
        "used_by": ["storage", "audit"],
    },
    frozenset({"concatination", "forward-reads"}): {
        "is_mandatory": False,
        "tags": ["fastq", "forward-strand"],
        "used_by": ["storage"],
    },
    frozenset({"reverse-reads", "concatination"}): {
        "is_mandatory": False,
        "tags": ["fastq", "reverse-strand"],
        "used_by": ["storage"],
    },
    frozenset({"consensus"}): {
        "is_mandatory": False,
        "tags": ["fastq", "consensus"],
        "used_by": ["deliver", "storage"],
    },
    frozenset({"runinfo", "logfile"}): {
        "is_mandatory": False,
        "tags": ["mutant-log"],
        "used_by": ["audit"],
    },
    frozenset({"alignment", "reference-alignment-sorted"}): {
        "is_mandatory": False,
        "tags": ["bam"],
        "used_by": ["storage"],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": False,
        "tags": ["multiqc-json"],
        "used_by": ["vogue"],
    },
    frozenset({"pangolin-typing"}): {
        "is_mandatory": False,
        "tags": ["pangolin", "typing-report", "csv"],
        "used_by": ["deliver"],
    },
    frozenset({"pangolin-summary"}): {
        "is_mandatory": False,
        "tags": ["pangolin", "typing-summary", "csv"],
        "used_by": ["deliver"],
    },
}
