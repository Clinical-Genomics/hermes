import copy
import logging
from enum import StrEnum

import typer
from tabulate import tabulate

from cg_hermes.config.balsamic_umi import BALSAMIC_UMI_TAGS
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.microsalt import MICROSALT_COMMON_TAGS
from cg_hermes.config.mip_dna import MIP_DNA_TAGS
from cg_hermes.config.mip_rna import MIP_RNA_TAGS
from cg_hermes.config.mutant import MUTANT_COMMON_TAGS
from cg_hermes.config.rnafusion import NXF_RNAFUSION_COMMON_TAGS
from cg_hermes.config.tags import COMMON_TAG_CATEGORIES
from cg_hermes.constants.workflow import Workflow

app = typer.Typer()

LOG = logging.getLogger(__name__)


def get_table(tags: dict):
    table = []
    for pipeline_tags, tag_info in tags.items():
        row = [
            ", ".join(pipeline_tags),
            str(tag_info["is_mandatory"]),
            ", ".join(tag_info["tags"]),
            ", ".join(tag_info["used_by"]),
        ]
        table.append(row)
    return table


class OutputFormat(StrEnum):
    github = "github"
    plain = "plain"


BALSAMIC_COMMON_TAGS = copy.deepcopy(BALSAMIC_UMI_TAGS)

PIPELINE_MAP = {
    Workflow.MIP_DNA: {
        "header": ["Mip-dna tags", "Mandatory", "HK tags", "Used by"],
        "tags": MIP_DNA_TAGS,
    },
    Workflow.MIP_RNA: {
        "header": ["Mip-rna tags", "Mandatory", "HK tags", "Used by"],
        "tags": MIP_RNA_TAGS,
    },
    Workflow.FLUFFY: {
        "header": ["Fluffy tags", "Mandatory", "HK tags", "Used by"],
        "tags": FLUFFY_COMMON_TAGS,
    },
    Workflow.MICROSALT: {
        "header": ["Microsalt tags", "Mandatory", "HK tags", "Used by"],
        "tags": MICROSALT_COMMON_TAGS,
    },
    Workflow.BALSAMIC: {
        "header": ["Balsamic tags", "Mandatory", "HK tags", "Used by"],
        "tags": BALSAMIC_COMMON_TAGS,
    },
    Workflow.MUTANT: {
        "header": ["Mutant tags", "Mandatory", "HK tags", "Used by"],
        "tags": MUTANT_COMMON_TAGS,
    },
    Workflow.RNAFUSION: {
        "header": ["Rnafusion tags", "Mandatory", "HK tags", "Used by"],
        "tags": NXF_RNAFUSION_COMMON_TAGS,
    },
}


@app.command(name="tags")
def export_tags_cmd(
    output: OutputFormat = typer.Option(OutputFormat.github),
    pipeline: Workflow = None,
):
    """Export tag definitions from Hermes."""
    LOG.info(f"Running export tags for workflow: {pipeline}")

    if not pipeline:
        header = ["Tag name", "Description"]
        for category in COMMON_TAG_CATEGORIES:
            table_name = category.upper().replace("_", " ")
            if output == "github":
                typer.echo(f"## {table_name}")
            else:
                typer.echo(table_name)
            typer.echo()
            table = [
                [
                    tag_name,
                    COMMON_TAG_CATEGORIES[category][tag_name]["description"],
                ]
                for tag_name in COMMON_TAG_CATEGORIES[category]
            ]

            typer.echo(tabulate(table, headers=header, tablefmt=output))
            typer.echo()
        raise typer.Exit()
    if pipeline not in PIPELINE_MAP:
        LOG.info("Could not recognize workflow")
        raise typer.Exit(code=1)

    header = PIPELINE_MAP[pipeline]["header"]
    table = get_table(PIPELINE_MAP[pipeline]["tags"])

    typer.echo(tabulate(table, headers=header, tablefmt=output))
