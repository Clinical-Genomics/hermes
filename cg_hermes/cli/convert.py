"""CLI for converting between formats."""

import json
import logging
from pathlib import Path

import typer
from pydantic import ValidationError

from cg_hermes.cli.common import get_deliverables
from cg_hermes.constants.workflow import CancerAnalysisType, Workflow
from cg_hermes.deliverables import Deliverables
from cg_hermes.exceptions import MissingFileError
from cg_hermes.models.workflow_deliverables import CGDeliverables
from cg_hermes.validate import get_deliverables_obj

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command(name="deliverables")
def convert_cmd(
    deliverables_file: Path,
    workflow: Workflow = typer.Option(..., help="Specify the workflow"),
    analysis_type: CancerAnalysisType = typer.Option(None, help="Specify the analysis type"),
    force: bool = typer.Option(False, "--force", "-f", help="Bypass deliverables file validation"),
) -> None:
    """
    Convert deliverable file to CG format.

    Raises:
        typer.Abort: If an error occurs during conversion or validation.
    """
    LOG.info(f"Convert deliverable file: {deliverables_file} from workflow {workflow} to CG format")
    raw_deliverables: dict[str, list[dict[str, str]]] = get_deliverables(deliverables_file)
    try:
        deliverables: Deliverables = get_deliverables_obj(
            deliverables=raw_deliverables, workflow=workflow, analysis_type=analysis_type
        )
        deliverables.validate_mandatory_files(force)
    except SyntaxError as error:
        LOG.error(error)
        raise typer.Abort()
    except (ValidationError, MissingFileError) as error:
        LOG.error(error)
        LOG.error(f"File: {deliverables_file} does not follow the specification")
        raise typer.Abort()
    cg_deliverables: CGDeliverables = deliverables.convert_to_cg_deliverables()
    typer.echo(json.dumps(cg_deliverables.dict(), indent=2))
