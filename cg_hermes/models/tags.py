from pydantic import BaseModel, field_validator

from cg_hermes.constants.tags import ALL_TAGS, USAGE_TAGS


class TagMap(BaseModel):
    tags: list[str]
    is_mandatory: bool
    used_by: list[str]
    bundle_id: bool | None = False

    @field_validator("tags")
    @classmethod
    def check_tags(cls, tags: list[str]):
        for tag in tags:
            if tag not in ALL_TAGS:
                raise ValueError(tags, f"{tag} not a valid tag")
        return tags

    @field_validator("used_by")
    @classmethod
    def check_usage(cls, used_by: list[str]):
        for user in used_by:
            if user not in USAGE_TAGS:
                raise ValueError(used_by, f"{user} not a valid user")
        return used_by


class CGTag(BaseModel):
    path: str
    tags: list[str]
    mandatory: bool
