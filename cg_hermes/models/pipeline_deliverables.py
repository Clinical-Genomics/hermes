from typing import List, Optional

from pydantic import BaseModel

from .tags import CGTag


class FileBase(BaseModel):
    path: str
    tag: Optional[str]
    id: str


class MipFile(FileBase):
    format: str
    path_index: Optional[str]
    step: str


class BalsamicFile(FileBase):
    format: Optional[str]


class PipelineDeliverables(BaseModel):
    files: List[FileBase]


class MipDeliverables(PipelineDeliverables):
    files: List[MipFile]


class BalsamicDeliverables(PipelineDeliverables):
    files: List[BalsamicFile]


class CGDeliverables(PipelineDeliverables):
    pipeline: str
    files: List[CGTag]


class TagBase(BaseModel):
    tags: List[str]
    subject_id: str
    path: str
