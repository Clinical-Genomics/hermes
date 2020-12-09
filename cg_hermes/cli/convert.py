"""CLI for converting between formats"""

import json
import logging
from pathlib import Path
from typing import Optional

import typer
from pydantic import ValidationError

from cg_hermes import validate
from cg_hermes.cli.common import get_deliverables
from cg_hermes.config.pipelines import Pipeline
from cg_hermes.exceptions import MissingFileError
from cg_hermes.parse import convert_to_cg_deliverables

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command(name="deliverables")
def convert_cmd(infile: Path, pipeline: Pipeline, outfile: Optional[Path] = None):
    LOG.info("Convert deliverable file %s to CG format", infile)
    deliverables_raw: dict = get_deliverables(infile)
    if pipeline == Pipeline.mip:
        validation_function = validate.validate_mip_deliverables
    if pipeline == Pipeline.fluffy:
        validation_function = validate.validate_fluffy_deliverables
    try:
        deliverables = validation_function(deliverables_raw)
    except (ValidationError, MissingFileError) as err:
        LOG.error(err)
        LOG.warning("File %s does not follow the spec", infile)
        raise typer.Abort()
    raise typer.Exit()
    cg_deliverables = convert_to_cg_deliverables(deliverables, pipeline=pipeline)
    if outfile:
        with open(outfile, "w") as handle:
            json.dump(cg_deliverables.dict(), handle)
            raise typer.Exit()
    typer.echo(json.dumps(cg_deliverables.dict(), indent=2))
