import logging
from pathlib import Path

import typer
from pydantic import ValidationError

from cg_hermes.cli.common import get_deliverables
from cg_hermes.config.balsamic import BALSAMIC_COMMON_TAGS
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.pipelines import Pipeline
from cg_hermes.exceptions import MissingFileError
from cg_hermes.validate import (
    validate_balsamic_deliverables,
    validate_mip_deliverables,
    validate_tag_map,
)

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command("deliverables")
def validate_deliverables(
    infile: Path,
    pipeline: Pipeline = typer.Option(Pipeline.mip, help="Specify what pipeline"),
):
    """Validate a deliverables file"""
    LOG.info("Validating file '%s' from pipeline %s", infile, pipeline.value)

    # Read raw file into dict
    deliverables = get_deliverables(infile)
    # Initiate the correct validation method
    validation_method = validate_mip_deliverables
    if pipeline == "balsamic":
        validation_method = validate_balsamic_deliverables

    try:
        validation_method(deliverables)
    except (ValidationError, MissingFileError) as err:
        LOG.error(err)
        LOG.warning("File %s does not follow the spec", infile)
        raise typer.Abort()
    LOG.info("Deliverables file seems to be on correct format")


@app.command("tags")
def validate_tags_cmd(pipeline: Pipeline):
    """Validate the tag maps for one of the definitions"""
    if pipeline == Pipeline.mip:
        tag_map = MIP_DNA_TAGS
        LOG.info("Validating MIP dna tags")
    elif pipeline == Pipeline.balsamic:
        tag_map = BALSAMIC_COMMON_TAGS
        LOG.info("Validating balsamic common tags")
    elif pipeline == Pipeline.fluffy:
        tag_map = FLUFFY_COMMON_TAGS
        LOG.info("Validating Fluffy common tags")
    else:
        LOG.info("Could not find pipeline tags for %s", pipeline.value)
        raise typer.Exit()

    try:
        validate_tag_map(tags=tag_map)
        LOG.info("Tag map looks fine")
    except ValidationError as err:
        LOG.warning(err)
        raise typer.Abort()
