from typing import FrozenSet, List, Optional

from pydantic import BaseModel

from .tags import CGTag


class FileBase(BaseModel):
    "Definition for elements in deliverables file"
    path: str
    tag: Optional[str]
    id: str


class MipFile(FileBase):
    """Definition for elements in MIP deliverables"""

    format: str
    path_index: Optional[str]
    step: str


class BalsamicFile(FileBase):
    """Definition of elements in balsamic deliverables"""

    format: Optional[str]


class PipelineDeliverables(BaseModel):
    """Specification for a general deliverables file"""

    files: List[FileBase]


class MipDeliverables(PipelineDeliverables):
    """Specification for a MIP specific deliverables file"""

    files: List[MipFile]


class BalsamicDeliverables(PipelineDeliverables):
    """Specification for a BALSAMIC specific deliverables file"""

    files: List[BalsamicFile]


class FluffyDeliverables(PipelineDeliverables):
    """Specification for a FLUFFY specific deliverables file"""

    files: List[FileBase]


class CGDeliverables(PipelineDeliverables):
    """Class that specifies the output to CG"""

    pipeline: str
    bundle_id: str
    files: List[CGTag]


class TagBase(BaseModel):
    """Internal mapping of deliverable file content"""

    tags: FrozenSet[str]
    subject_id: str
    path: str
    path_index: Optional[str]
