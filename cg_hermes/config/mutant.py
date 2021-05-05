MUTANT_COMMON_TAGS = {

    frozenset({"sampleinfo", "runinfo"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["config"],
        "used_by": ["storage", "audit"],
    },
    frozenset({"runtime-settings", "runinfo"}): {
        "is_mandatory": True,
        "tags": ["mutant-config"],
        "used_by": ["storage", "audit"],
    },
    frozenset({"concatination", "forward-reads"}): {
        "is_mandatory": True,
        "tags": ["fastq", "forward-strand"],
        "used_by": ["storage"],
    },
    frozenset({"reverse-reads", "concatination"}): {
        "is_mandatory": True,
        "tags": ["fastq", "reverse-strand"],
        "used_by": ["storage"],
    },
    frozenset({"consensus"}): {
        "is_mandatory": True,
        "tags": ["ks", "fastq", "consensus"],
        "used_by": ["deliver", "storage"],
    },
    frozenset({"runinfo", "logfile"}): {
        "is_mandatory": True,
        "tags": ["mutant-log"],
        "used_by": ["audit"],
    },
    frozenset({"multiqc-json"}): {
        "is_mandatory": True,
        "tags": ["multiqc-json"],
        "used_by": ["vogue"],
    },
    frozenset({"multiqc-html"}): {
        "is_mandatory": True,
        "tags": ["ks", "multiqc-html"],
        "used_by": ["deliver"],
    },
    frozenset({"ks-results"}): {
        "is_mandatory": True,
        "tags": ["ks", "pangolin", "typing-report", "visualization", "csv"],
        "used_by": ["deliver"],
    },
    frozenset({"ks-aux-results"}): {
        "is_mandatory": True,
        "tags": ["ks", "pangolin", "typing-report", "visualization", "csv"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-info", "report"}): {
        "is_mandatory": False,
        "tags": ["komplettering", "fohm", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-qc", "result_aggregation"}): {
        "is_mandatory": False,
        "tags": ["fohm", "qc-report", "csv", "visualization"],
        "used_by": ["audit"],
    },
    frozenset({"pangolin-typing"}): {
        "is_mandatory": False,
        "tags": ["fohm", "typing-report", "visualization", "csv"],
        "used_by": ["audit"],
    },
    frozenset({"alignment", "reference-alignment-sorted"}): {
        "is_mandatory": False,
        "tags": ["bam"],
        "used_by": ["storage"],
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
    frozenset({"SARS-CoV-2-json", "result_aggregation"}): {
        "is_mandatory": False,
        "tags": ["typing-report"],
        "used_by": ["audit"],
    },
    frozenset({"SARS-CoV-2-sum", "report"}): {
        "is_mandatory": False,
        "tags": ["summary", "csv"],
        "used_by": ["audit"],
    },
    frozenset({"SARS-CoV-2-var", "report"}): {
        "is_mandatory": False,
        "tags": ["variants", "csv"],
        "used_by": ["audit"],
    },
 
}
