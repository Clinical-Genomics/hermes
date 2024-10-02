from cg_hermes.models.workflow_deliverables import BalsamicFile, FileBase


def test_instantiate_file_base(file_base_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a file base

    # WHEN instantiating an object
    file_base = FileBase.model_validate(file_base_raw)

    # THEN assert that it was successfully created
    assert isinstance(file_base, FileBase)


def test_instantiate_balsamic_file(balsamic_file_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a Balsamic file base

    # WHEN instantiating an object
    balsamic_file = BalsamicFile.model_validate(balsamic_file_raw)

    # THEN assert that it was successfully created
    assert isinstance(balsamic_file, BalsamicFile)


def test_balsamic_file_tag_validator(balsamic_file_raw: dict):
    """
    Tests instantiating model."""
    # GIVEN a dictionary with a Balsamic file base

    # GIVEN an incorrect tag
    balsamic_file_raw["tag"] = "an_incorrect_tag, tag_2"

    # WHEN instantiating an object
    balsamic_file = BalsamicFile.model_validate(balsamic_file_raw)

    # THEN tag should be a list
    assert isinstance(balsamic_file.tag, list)
