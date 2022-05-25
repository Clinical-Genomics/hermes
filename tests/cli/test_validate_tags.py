"""Tests for the validate tags cli"""

from typer.testing import CliRunner

from cg_hermes.cli.validate import app


def test_cli_validate_mip_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "mip-dna"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0


def test_cli_validate_balsamic_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "balsamic"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0


def test_cli_validate_balsamic_umi_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "balsamic-umi"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0


def test_cli_validate_balsamic_qc_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "balsamic-qc"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0


def test_cli_validate_fluffy_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "fluffy"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0


def test_cli_validate_mutant_tags(cli_runner: CliRunner):
    # GIVEN a CLI runner

    # WHEN testing to validate the common tags from the CLI
    result = cli_runner.invoke(app, ["tags", "sars-cov-2"])

    # THEN assert that the validation was successful
    assert result.exit_code == 0
