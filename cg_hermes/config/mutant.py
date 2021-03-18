MUTANT_COMMON_TAGS = {
    frozenset({"sampleinfo", "runinfo"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["config"],
        "used_by": ["storage", "audit"],
    },
    frozenset({"variants","genotyping"}): {
        "is_mandatory": True,
        "tags": ["qc-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"variants","variant-calling"}): {
        "is_mandatory": True,
        "tags": ["qc-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-qc", "result_aggregation"}): {
        "is_mandatory": True,
        "tags": ["qc-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-type", "typing"}): {
        "is_mandatory": True,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-json", "result_aggregation"}): {
        "is_mandatory": True,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-sum", "report"}): {
        "is_mandatory": True,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-var", "report"}): {
        "is_mandatory": True,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"SARS-CoV-2-info", "report"}): {
        "is_mandatory": True,
        "tags": ["typing-report", "visualization"],
        "used_by": ["deliver"],
    },
    frozenset({"runtime-settings", "runinfo"}): {
        "is_mandatory": True,
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
        "tags": ["fastq", "unpaired-reads"],
        "used_by": ["storage"],
    },
    frozenset({"runinfo", "logfile"}): {
        "is_mandatory": True,
        "tags": ["mutant-log"],
        "used_by": ["audit"],
    },
    frozenset({"alignment", "reference-alignment-sorted"}): {
        "is_mandatory": True,
        "tags": ["bam"],
        "used_by": ["storage"],
    },
}
