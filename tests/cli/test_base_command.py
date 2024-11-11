"""Tests for the Hermes base CLI."""

from typer.testing import CliRunner

from cg_hermes.cli.base import app
from cg_hermes.constants.hermes import HERMES_VERSION


def test_run_base(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the base command
    result = cli_runner.invoke(app, [])

    # THEN assert it exits without a problem
    assert result.exit_code == 0


def test_run_version_command(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the base command with the version flag
    result = cli_runner.invoke(app, ["--version"])

    # THEN assert the correct version is displayed
    assert f"hermes version: {HERMES_VERSION}" in result.output
