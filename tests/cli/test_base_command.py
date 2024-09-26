"""Tests for the Hermes base CLI."""

from typer.testing import CliRunner

from cg_hermes.cli.base import app

version = "4.4.13"


def test_run_base(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the base command
    result = cli_runner.invoke(app, [])

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_run_version_command(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the base command with version flag
    result = cli_runner.invoke(app, ["--version"])

    # THEN assert the correct version is displayed
    assert f"hermes version: {version}" in result.output
