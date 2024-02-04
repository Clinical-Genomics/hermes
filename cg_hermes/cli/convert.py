"""CLI for converting between formats."""

import json
import logging
from pathlib import Path

import typer
from pydantic import ValidationError

from cg_hermes.cli.common import get_deliverables
from cg_hermes.config.pipelines import AnalysisType
from cg_hermes.constants.workflow import Workflow
from cg_hermes.deliverables import Deliverables
from cg_hermes.exceptions import MissingFileError
from cg_hermes.models.pipeline_deliverables import CGDeliverables
from cg_hermes.validate import get_deliverables_obj

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command(name="deliverables")
def convert_cmd(
    infile: Path,
    pipeline: Workflow = typer.Option(..., help="Specify the analysis type"),
    analysis_type: AnalysisType = typer.Option(None, help="Specify the analysis type"),
):
    LOG.info(f"Convert deliverable file: {infile} from workflow {pipeline} to CG format")

    raw_deliverables: dict[str, list[dict[str, str]]] = get_deliverables(infile)
    try:
        deliverables: Deliverables = get_deliverables_obj(
            deliverables=raw_deliverables, pipeline=pipeline, analysis_type=analysis_type
        )
        deliverables.validate_mandatory_files()
    except SyntaxError:
        raise typer.Abort()
    except (ValidationError, MissingFileError) as err:
        LOG.error(err)
        LOG.warning(f"File: {infile} does not follow the specification")
        raise typer.Abort()

    cg_deliverables: CGDeliverables = deliverables.convert_to_cg_deliverables()

    typer.echo(json.dumps(cg_deliverables.dict(), indent=2))
