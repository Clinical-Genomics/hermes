import logging
from pathlib import Path

import typer
from pydantic import ValidationError

from cg_hermes.cli.common import get_deliverables
from cg_hermes.config.balsamic import BALSAMIC_COMMON_TAGS
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.mip import MIP_DNA_TAGS
from cg_hermes.config.pipelines import AnalysisType, Pipeline
from cg_hermes.exceptions import MissingFileError
from cg_hermes.validate import DeliverablesValidator, validate_common_tags, validate_tag_map

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command("deliverables")
def validate_deliverables(
    infile: Path,
    pipeline: Pipeline = typer.Option(Pipeline.mip, help="Specify what pipeline"),
    analysis_type: AnalysisType = typer.Option(None, help="Specify the analysis type"),
):
    """Validate a deliverables file"""
    LOG.info("Validating file '%s' from pipeline %s", infile, pipeline.value)
    if pipeline == Pipeline.balsamic:
        if not analysis_type:
            LOG.info("Please specify analysis type for balsamic")
            raise typer.Exit(code=1)

    # Read raw file into dict
    deliverables = get_deliverables(infile)

    try:
        validator = DeliverablesValidator(
            deliverables=deliverables, pipeline=pipeline, analysis_type=analysis_type
        )
        validator.validate_mandatory_files()
    except (ValidationError, MissingFileError) as err:
        LOG.error(err)
        LOG.warning("File %s does not follow the spec", infile)
        raise typer.Abort()
    LOG.info("Deliverables file seems to be on correct format")


@app.command("tags")
def validate_tags_cmd(pipeline: Pipeline):
    """Validate the tag maps for one of the definitions"""
    LOG.info("Validating %s common tags", pipeline.value)
    exit_code = 0
    if pipeline == Pipeline.mip:
        tag_map = MIP_DNA_TAGS
    elif pipeline == Pipeline.balsamic:
        tag_map = BALSAMIC_COMMON_TAGS
    elif pipeline == Pipeline.fluffy:
        tag_map = FLUFFY_COMMON_TAGS
    elif pipeline == Pipeline.cg:
        try:
            validate_common_tags()
            LOG.info("Tag map looks fine")
        except AssertionError:
            exit_code = 1
        raise typer.Exit(code=exit_code)
    else:
        LOG.info("Could not find pipeline tags for %s", pipeline.value)
        raise typer.Exit(code=exit_code)

    try:
        validate_tag_map(tag_map=tag_map)
        LOG.info("Tag map looks fine")
    except ValidationError as err:
        LOG.warning(err)
        exit_code = 1
    raise typer.Exit(code=exit_code)
