import logging
from enum import Enum

import typer
from tabulate import tabulate

from cg_hermes.config.balsamic import BALSAMIC_COMMON_TAGS
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.microsalt import MICROSALT_COMMON_TAGS
from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.pipelines import Pipeline
from cg_hermes.config.tags import COMMON_TAG_CATEGORIES

app = typer.Typer()

LOG = logging.getLogger(__name__)


def get_table(tags: dict):
    table = []
    for pipeline_tags in tags:
        tag_info = tags[pipeline_tags]
        row = [
            ", ".join(pipeline_tags),
            str(tag_info["is_mandatory"]),
            ", ".join(tag_info["tags"]),
            ", ".join(tag_info["used_by"]),
        ]
        table.append(row)
    return table


class OutputFormat(str, Enum):
    github = "github"
    plain = "plain"


PIPELINE_MAP = {
    Pipeline.mip.value: {
        "header": ["Mip tags", "Mandatory", "HK tags", "Used by"],
        "tags": MIP_DNA_TAGS,
    },
    Pipeline.fluffy.value: {
        "header": ["Fluffy tags", "Mandatory", "HK tags", "Used by"],
        "tags": FLUFFY_COMMON_TAGS,
    },
    Pipeline.fluffy.microsalt: {
        "header": ["Microsalt tags", "Mandatory", "HK tags", "Used by"],
        "tags": MICROSALT_COMMON_TAGS,
    },
    Pipeline.fluffy.balsamic: {
        "header": ["Balsamic tags", "Mandatory", "HK tags", "Used by"],
        "tags": BALSAMIC_COMMON_TAGS,
    },
}


@app.command(name="tags")
def export_tags_cmd(
    pipeline: Pipeline = typer.Option(Pipeline.cg),
    output: OutputFormat = typer.Option(OutputFormat.github),
):
    """Export tag definitions from hermes"""
    LOG.info("Running export tags for pipeline %s", pipeline.value)

    if pipeline == Pipeline.cg:
        header = ["Tag name", "Description"]
        for category in COMMON_TAG_CATEGORIES:
            table_name = category.upper().replace("_", " ")
            if output.value == "github":
                typer.echo(f"## {table_name}")
            else:
                typer.echo(table_name)
            typer.echo()
            table = []
            for tag_name in COMMON_TAG_CATEGORIES[category]:
                table.append([tag_name, COMMON_TAG_CATEGORIES[category][tag_name]["description"]])
            typer.echo(tabulate(table, headers=header, tablefmt=output.value))
            typer.echo()
        raise typer.Exit()
    if pipeline.value not in PIPELINE_MAP:
        LOG.info("Could not recognize pipeline")
        raise typer.Exit(code=1)

    header = PIPELINE_MAP[pipeline.value]["header"]
    table = get_table(PIPELINE_MAP[pipeline.value]["tags"])

    typer.echo(tabulate(table, headers=header, tablefmt=output.value))
