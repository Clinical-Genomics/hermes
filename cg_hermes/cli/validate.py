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
from cg_hermes.config.pipelines import AnalysisType
from cg_hermes.config.rnafusion import NXF_RNAFUSION_COMMON_TAGS
from cg_hermes.constants.workflow import Workflow
from cg_hermes.deliverables import Deliverables
from cg_hermes.exceptions import MissingFileError
from cg_hermes.validate import get_deliverables_obj, validate_tag_map

LOG = logging.getLogger(__name__)

app = typer.Typer()


@app.command("deliverables")
def validate_deliverables(
    infile: Path,
    pipeline: Workflow = typer.Option(Workflow.FLUFFY, help="Specify workflow"),
    analysis_type: AnalysisType = typer.Option(None, help="Specify the analysis type"),
):
    """Validate a deliverables file."""
    LOG.info(f"Validating file: {infile} from workflow: {pipeline}")

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
        LOG.warning(f"File {infile} does not follow the spec")
        raise typer.Abort()
    LOG.info("Deliverables file has the correct format")


@app.command("tags")
def validate_tags_cmd(pipeline: Workflow):
    """Validate the tag maps for one of the definitions."""
    LOG.info(f"Validating {pipeline} common tags")
    exit_code = 0

    if pipeline == Workflow.MIP_DNA:
        tag_map = MIP_DNA_TAGS
    elif pipeline == Workflow.MIP_RNA:
        tag_map = MIP_RNA_TAGS
    elif pipeline == Workflow.BALSAMIC:
        tag_map = BALSAMIC_TAGS
    elif pipeline == Workflow.BALSAMIC_UMI:
        tag_map = BALSAMIC_UMI_TAGS
    elif pipeline == Workflow.BALSAMIC_QC:
        tag_map = BALSAMIC_QC_TAGS
    elif pipeline == Workflow.FLUFFY:
        tag_map = FLUFFY_COMMON_TAGS
    elif pipeline == Workflow.MUTANT:
        tag_map = MUTANT_COMMON_TAGS
    elif pipeline == Workflow.RNAFUSION:
        tag_map = NXF_RNAFUSION_COMMON_TAGS
    else:
        LOG.info(f"Could not find workflow tags for {pipeline}")
        raise typer.Exit(code=exit_code)

    try:
        validate_tag_map(tag_map=tag_map)
        LOG.info("Tag map looks fine")
    except ValidationError as error:
        LOG.warning(error)
        exit_code = 1
    raise typer.Exit(code=exit_code)
