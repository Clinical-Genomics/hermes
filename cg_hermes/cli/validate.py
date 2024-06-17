import logging
from pathlib import Path

import typer
from pydantic import ValidationError

from cg_hermes.cli.common import get_deliverables
from cg_hermes.config.balsamic import BALSAMIC_TAGS
from cg_hermes.config.balsamic_qc import BALSAMIC_QC_TAGS
from cg_hermes.config.balsamic_umi import BALSAMIC_UMI_TAGS
from cg_hermes.config.fluffy import FLUFFY_COMMON_TAGS
from cg_hermes.config.mip_dna import MIP_DNA_TAGS
from cg_hermes.config.mip_rna import MIP_RNA_TAGS
from cg_hermes.config.mutant import MUTANT_COMMON_TAGS
from cg_hermes.config.raredisease import RAREDISEASE_TAGS
from cg_hermes.config.rnafusion import RNAFUSION_TAGS
from cg_hermes.config.taxprofiler import TAXPROFILER_TAGS
from cg_hermes.config.tomte import TOMTE_TAGS
from cg_hermes.constants.workflow import CancerAnalysisType, Workflow
from cg_hermes.deliverables import Deliverables
from cg_hermes.exceptions import MissingFileError
from cg_hermes.validate import get_deliverables_obj, validate_tag_map

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command("deliverables")
def validate_deliverables(
    deliverables_file: Path,
    workflow: Workflow = typer.Option(Workflow.FLUFFY, help="Specify workflow"),
    analysis_type: CancerAnalysisType = typer.Option(None, help="Specify the analysis type"),
    force: bool = typer.Option(False, "--force", "-f", help="Bypass deliverables file validation"),
) -> None:
    """
    Validate a deliverables file.

    Raises:
        typer.Abort: If there is an error in parsing or validating the deliverables file.
    """
    LOG.info(f"Validating file: {deliverables_file} from workflow: {workflow}")
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
    LOG.info("Deliverables file has the correct format")


@app.command("tags")
def validate_tags_cmd(workflow: Workflow) -> None:
    """Validate the tag maps for one of the definitions."""
    LOG.info(f"Validating {workflow} common tags")
    exit_code = 0

    if workflow == Workflow.MIP_DNA:
        tag_map = MIP_DNA_TAGS
    elif workflow == Workflow.MIP_RNA:
        tag_map = MIP_RNA_TAGS
    elif workflow == Workflow.BALSAMIC:
        tag_map = BALSAMIC_TAGS
    elif workflow == Workflow.BALSAMIC_UMI:
        tag_map = BALSAMIC_UMI_TAGS
    elif workflow == Workflow.BALSAMIC_QC:
        tag_map = BALSAMIC_QC_TAGS
    elif workflow == Workflow.FLUFFY:
        tag_map = FLUFFY_COMMON_TAGS
    elif workflow == Workflow.MUTANT:
        tag_map = MUTANT_COMMON_TAGS
    elif workflow == Workflow.RAREDISEASE:
        tag_map = RAREDISEASE_TAGS
    elif workflow == Workflow.RNAFUSION:
        tag_map = RNAFUSION_TAGS
    elif workflow == Workflow.TAXPROFILER:
        tag_map = TAXPROFILER_TAGS
    elif workflow == Workflow.TOMTE:
        tag_map = TOMTE_TAGS
    else:
        LOG.info(f"Could not find workflow tags for {workflow}")
        raise typer.Exit(code=exit_code)

    try:
        validate_tag_map(tag_map=tag_map)
        LOG.info("Tag map looks fine")
    except ValidationError as error:
        LOG.warning(error)
        exit_code = 1
    raise typer.Exit(code=exit_code)
