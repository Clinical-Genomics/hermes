MICROSALT_COMMON_TAGS = {
    frozenset({"sampleinfo", "analysis"}): {
        "is_mandatory": True,
        "bundle_id": True,
        "tags": ["summary"],
        "used_by": ["storage"],
    },
    frozenset({"microsalt-qc", "result_aggregation"}): {
        "is_mandatory": True,
        "tags": ["summary"],
        "used_by": ["storage"],
    },
    frozenset({"microsalt-type", "result_aggregation"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"microsalt-json", "result_aggregation"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"runtime-settings", "analysis"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"assembly"}): {"is_mandatory": True, "tags": [], "used_by": ["storage"]},
    frozenset({"concatination", "trimmed-forward-reads"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"trimmed-reverse-reads", "concatination"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"trimmed-unpaired-reads", "concatination"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"analysis", "logfile"}): {"is_mandatory": True, "tags": [], "used_by": ["storage"]},
    frozenset({"quast-results", "assembly"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"alignment", "reference-alignment-sorted"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"alignment", "reference-alignment-deduplicated"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
    frozenset({"picard-insertsize", "insertsize_calc"}): {
        "is_mandatory": True,
        "tags": [],
        "used_by": ["storage"],
    },
}
