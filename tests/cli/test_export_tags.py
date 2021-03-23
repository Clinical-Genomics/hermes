"""Tests for the export cli command"""

from typer.testing import CliRunner

from cg_hermes.cli.export import app


def test_export_common_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export common tags command
    result = cli_runner.invoke(app, [])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the common cg tags was exported
    assert "VARIANT TAGS" in result.output


def test_export_mip_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline mip
    result = cli_runner.invoke(app, ["--pipeline", "mip-dna"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip tags was exported
    assert "Mip tags" in result.output


def test_export_balsamic_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline balsamic
    result = cli_runner.invoke(app, ["--pipeline", "balsamic"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip tags was exported
    assert "Balsamic tags" in result.output


def test_export_fluffy_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline balsamic
    result = cli_runner.invoke(app, ["--pipeline", "fluffy"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip tags was exported
    assert "Fluffy tags" in result.output
