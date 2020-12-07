import logging
from enum import Enum

import typer
from tabulate import tabulate

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


@app.command(name="tags")
def export_tags_cmd(
    pipeline: Pipeline = typer.Option(Pipeline.cg),
    output: OutputFormat = typer.Option(OutputFormat.github),
):
    """Export tag definitions from hermes"""
    LOG.info("Running export tags for pipeline %s", pipeline.value)
    if pipeline.value == "mip":
        header = ["Mip tags", "Mandatory", "HK tags", "Used by"]
        table = get_table(MIP_DNA_TAGS)
        typer.echo(tabulate(table, headers=header, tablefmt=format))
    if pipeline.value == "cg":
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
