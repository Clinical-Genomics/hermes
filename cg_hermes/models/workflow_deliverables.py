from typing import FrozenSet

from pydantic import BaseModel, field_validator

from cg_hermes.models.tags import CGTag

# Classes to represent file entries in the deliverables files


class FileBase(BaseModel):
    """Definition for elements in deliverables file"""

    path: str
    tag: str | None = None
    id: str


class MipFile(FileBase):
    """Definition for elements in MIP deliverables"""

    format: str
    path_index: str | None = None
    step: str


class MicrosaltFile(FileBase):
    """Definition for elements in Microsalt deliverables"""

    format: str
    step: str


class MutantFile(FileBase):
    """Definition for elements in Mutant deliverables"""

    format: str
    step: str


class NfAnalysisFile(FileBase):
    """Definition for elements in deliverables for nextflow workflows."""

    format: str
    path_index: str | None = None
    step: str


class BalsamicFile(FileBase):
    """Definition of elements in Balsamic deliverables."""

    format: str | None = None
    tag: list[str]

    @field_validator("tag", mode="before")
    @classmethod
    def split_str(cls, tag: list[str]):
        return tag.split(",") if isinstance(tag, str) else tag


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


class NfAnalysisDeliverables(WorkflowDeliverables):
    """Specification for a deliverable file for a nextflow workflow."""

    files: list[NfAnalysisFile]


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
    path_index: str | None = None
