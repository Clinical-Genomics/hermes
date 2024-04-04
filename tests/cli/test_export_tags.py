"""Tests for the export command."""

import pytest
from _pytest.fixtures import FixtureRequest
from typer.testing import CliRunner

from cg_hermes.cli.export import app
from cg_hermes.constants.workflow import Workflow


def test_export_common_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export common tags command
    result = cli_runner.invoke(app, [])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0

    # THEN assert that the common tags were exported
    for table_name in [
        "Alignment Tags",
        "Analysis Tags",
        "Bioinfo Tools Tags",
        "Family Tags",
        "QC Tags",
        "Raw Data Tags",
        "Report Tags",
        "Variant Tags",
    ]:
        assert table_name in result.output


def test_export_mip_dna_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for workflow mip
    result = cli_runner.invoke(app, ["--workflow", "mip-dna"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags were exported
    assert "Mip-dna tags" in result.output


def test_export_mip_rna_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for workflow mip
    result = cli_runner.invoke(app, ["--workflow", "mip-rna"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags was exported
    assert "Mip-rna tags" in result.output


def test_export_balsamic_tags(cli_runner: CliRunner):
    """Tests export of all the Balsamic tags"""

    # GIVEN a cli runner

    # WHEN running the export tags command for workflow balsamic
    result = cli_runner.invoke(app, ["--workflow", "balsamic"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the balsamic tags was exported
    assert "Balsamic tags" in result.output
    assert "umi" in result.output


def test_export_fluffy_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for workflow balsamic
    result = cli_runner.invoke(app, ["--workflow", "fluffy"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags was exported
    assert "Fluffy tags" in result.output


def test_export_microsalt_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for MicroSALT
    result = cli_runner.invoke(app, ["--workflow", "microsalt"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the MicroSALT tags were exported
    assert "Microsalt tags" in result.output


def test_export_mutant_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for Mutant
    result = cli_runner.invoke(app, ["--workflow", "mutant"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the MicroSALT tags were exported
    assert "Mutant tags" in result.output


@pytest.mark.parametrize(
    "workflow",
    Workflow.get_nf_workflows(),
)
def test_export_nf_workflow_tags(
    cli_runner: CliRunner,
    workflow: Workflow,
    request: FixtureRequest,
):
    """Test that tags are exported for nextflow workflows."""
    # WHEN invoking the export tags command
    result = cli_runner.invoke(app, ["--workflow", workflow])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0

    # THEN assert that tags were exported
    assert f"{workflow.capitalize()} tags" in result.output
