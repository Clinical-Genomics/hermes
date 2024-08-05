"""Code for validating files from different sources."""

import logging
from typing import FrozenSet

from cg_hermes.constants.workflow import CancerAnalysisType, Workflow
from cg_hermes.deliverables import Deliverables
from cg_hermes.models.tags import TagMap

LOG = logging.getLogger(__name__)


def get_deliverables_obj(
    deliverables: dict[str, list[dict[str, str]]],
    workflow: Workflow,
    analysis_type: CancerAnalysisType | None = None,
) -> Deliverables:
    if Workflow.BALSAMIC in workflow and not analysis_type:
        LOG.error(f"Please specify analysis type for {workflow}")
        raise SyntaxError
    return Deliverables(deliverables=deliverables, workflow=workflow, analysis_type=analysis_type)


def validate_tag_map(tag_map: dict[FrozenSet[str], dict]) -> bool:
    """Validate if a tag map is on the correct format."""
    for workflow_tags, value in tag_map.items():
        assert isinstance(workflow_tags, frozenset)
        TagMap.validate(value)
    return True
