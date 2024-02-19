from typing import FrozenSet

from pydantic import BaseModel, validator

from .tags import CGTag

# Classes to represent file entries in the deliverables files


class FileBase(BaseModel):
    """Definition for elements in deliverables file"""

    path: str
    tag: str | None
    id: str


class MipFile(FileBase):
    """Definition for elements in MIP deliverables"""

    format: str
    path_index: str | None
    step: str


class MicrosaltFile(FileBase):
    """Definition for elements in Microsalt deliverables"""

    format: str
    step: str


class MutantFile(FileBase):
    """Definition for elements in Mutant deliverables"""

    format: str
    step: str


class RnafusionFile(FileBase):
    """Definition for elements in Rnafusion deliverables"""

    format: str
    path_index: str | None
    step: str


class BalsamicFile(FileBase):
    """Definition of elements in balsamic deliverables"""

    format: str | None
    tag: list[str]

    @validator("tag", pre=True)
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v


# Classes to represent deliverable files


class WorkflowDeliverables(BaseModel):
    """Specification for a general deliverables file"""

    files: list[FileBase]


class MipDeliverables(WorkflowDeliverables):
    """Specification for a MIP specific deliverables file"""

    files: list[MipFile]


class MicrosaltDeliverables(WorkflowDeliverables):
    """Specification for a MIP specific deliverables file"""

    files: list[MicrosaltFile]


class BalsamicDeliverables(WorkflowDeliverables):
    """Specification for a BALSAMIC specific deliverables file"""

    files: list[BalsamicFile]


class FluffyDeliverables(WorkflowDeliverables):
    """Specification for a FLUFFY specific deliverables file"""

    files: list[FileBase]


class MutantDeliverables(WorkflowDeliverables):
    """Specification for a MUTANT specific deliverables file"""

    files: list[MutantFile]


class RnafusionDeliverables(WorkflowDeliverables):
    """Specification for a RNAFUSION specific deliverables file"""

    files: list[RnafusionFile]


class CGDeliverables(WorkflowDeliverables):
    """Class that specifies the output to CG"""

    workflow: str
    bundle_id: str
    files: list[CGTag]


class TagBase(BaseModel):
    """Internal mapping of deliverable file content"""

    tags: FrozenSet[str]
    subject_id: str
    path: str
    path_index: str | None
