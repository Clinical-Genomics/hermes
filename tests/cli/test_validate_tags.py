"""Tests for the validate tags cli"""

from typer.testing import CliRunner

from cg_hermes.cli.validate import app


def test_cli_validate_cg_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "cg"])

    # THEN assert that the validation was succesfull
    assert result.exit_code == 0


def test_cli_validate_mip_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "mip"])

    # THEN assert that the validation was succesfull
    assert result.exit_code == 0


def test_cli_validate_balsamic_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "balsamic"])

    # THEN assert that the validation was succesfull
    assert result.exit_code == 0


def test_cli_validate_fluffy_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "fluffy"])

    # THEN assert that the validation was succesfull
    assert result.exit_code == 0
