"""Tags that are defined in Tomte deliverables mapped to tags used in CG

The tag sets that exists in all files are set to mandatory. Tag sets that exists in < 4 deliverables are not
mandatory by default. However, the tags that are available to a particular analysis is mandatory for that analysis.
"""

from cg_hermes.config.nextflow import NEXTFLOW_TAGS


RAREDISEASE_COMMON_TAGS = {
    frozenset(["chromograph_upd", "sites"]): {
        "tags": ["chromograph", "upd", "sites"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["chromograph_upd", "regions"]): {
        "tags": ["chromograph", "upd", "regions"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["chromograph_cov", "tcov"]): {
        "tags": ["chromograph", "tcov"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["chromograph_rhoviz", "autozyg"]): {
        "tags": ["chromograph", "autozyg"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["rank_and_filter", "clinical"]): {
        "tags": ["vcf-snv-clinical"],
        "index_tags": ["vcf-snv-clinical-index"],
        "is_mandatory": True,
        "bundle_id": True,
        "used_by": ["scout"],
    },
    frozenset(["rank_and_filter", "research"]): {
        "tags": ["vcf-snv-research"],
        "index_tags": ["vcf-snv-research-index"],
        "is_mandatory": True,
        "used_by": ["scout"],
    },
    frozenset(["expansionhunter", "sv_str"]): {
        "tags": ["vcf-str"],
        "index_tags": ["vcf-str-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["expansionhunter", "str_variants"]): {
        "tags": ["expansionhunter", "vcf-str"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["expansionhunter", "str_alignment"]): {
        "tags": ["expansionhunter", "bam"],
        "index_tags": ["expansionhunter", "bam-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["expansionhunter", "variant_catalog"]): {
        "tags": ["expansionhunter", "variant-catalog"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["alignment", "alignment"]): {
        "tags": ["cram"],
        "index_tags": ["cram-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["gens_generatedata", "baf"]): {
        "tags": ["gens", "fracsnp", "bed"],
        "index_tags": ["gens", "fracsnp", "bed-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["gens_generatedata", "cov"]): {
        "tags": ["gens", "coverage", "bed"],
        "index_tags": ["gens", "coverage", "bed-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["pedigree", "pedigree_fam"]): {
        "tags": ["pedigree"],
        "is_mandatory": True,
        "used_by": ["scout"],
    },
    frozenset(["multiqc", "html"]): {
        "tags": ["multiqc-html"],
        "is_mandatory": True,
        "used_by": ["scout"],
    },
    frozenset(["multiqc", "json"]): {
        "tags": ["multiqc-json"],
        "is_mandatory": True,
        "used_by": ["storage"],
    },
    frozenset(["call_sv_mt", "mitodel"]): {
        "tags": ["mitodel"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["peddy", "ped_check"]): {
        "tags": ["peddy", "ped-check"],
        "is_mandatory": True,
        "used_by": ["audit", "scout"],
    },
    frozenset(["peddy", "peddy"]): {
        "tags": ["peddy", "ped"],
        "is_mandatory": True,
        "used_by": ["audit", "scout"],
    },
    frozenset(["peddy", "sex_check"]): {
        "tags": ["peddy", "sex-check"],
        "is_mandatory": True,
        "used_by": ["audit", "scout"],
    },
    frozenset(["annotate_snv", "rhocall_viz"]): {
        "tags": ["rhocall-viz"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["alignment", "subsample_mt"]): {
        "tags": ["bam-mt"],
        "index_tags": ["bam-mt-index"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["smncopynumbercaller", "tsv"]): {
        "tags": ["smn-calling"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["tiddit_coverage", "tiddit_coverage"]): {
        "tags": ["tiddit-coverage", "bigwig"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
    frozenset(["vcf2cytosure", "vcf2cytosure"]): {
        "tags": ["vcf2cytosure"],
        "is_mandatory": False,
        "used_by": ["scout"],
    },
}

RAREDISEASE_TAGS = {**RAREDISEASE_COMMON_TAGS, **NEXTFLOW_TAGS}
