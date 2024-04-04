"""Tests for the validate deliverables cli command"""

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest
from _pytest.logging import LogCaptureFixture
from typer.testing import CliRunner

from cg_hermes.cli.validate import app
from cg_hermes.constants.workflow import Workflow


def test_validate_mip_deliverables_file(cli_runner: CliRunner, mip_dna_deliverables: Path):
    # GIVEN a existing mip_dna deliverables file and a CLI runner
    assert mip_dna_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app, ["deliverables", str(mip_dna_deliverables), "--workflow", "mip-dna"]
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_mip_rna_deliverables_file(cli_runner: CliRunner, mip_rna_deliverables: Path):
    # GIVEN a existing mip_dna deliverables file and a CLI runner
    assert mip_rna_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app, ["deliverables", str(mip_rna_deliverables), "--workflow", "mip-rna"]
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_balsamic_deliverables_file(
    cli_runner: CliRunner, balsamic_tn_wgs_deliverables: Path
):
    # GIVEN a existing balsamic deliverables file and a CLI runner
    assert balsamic_tn_wgs_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app,
        [
            "deliverables",
            str(balsamic_tn_wgs_deliverables),
            "--workflow",
            "balsamic",
            "--analysis-type",
            "tumor_normal_wgs",
        ],
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_balsamic_umi_deliverables_file(
    cli_runner: CliRunner, balsamic_tn_panel_deliverables: Path
):
    # GIVEN a existing balsamic deliverables file and a CLI runner
    assert balsamic_tn_panel_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app,
        [
            "deliverables",
            str(balsamic_tn_panel_deliverables),
            "--workflow",
            "balsamic-umi",
            "--analysis-type",
            "tumor_normal_panel",
        ],
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_balsamic_qc_deliverables_file(
    cli_runner: CliRunner, balsamic_tn_panel_deliverables: Path
):
    # GIVEN a existing balsamic deliverables file and a CLI runner
    assert balsamic_tn_panel_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app,
        [
            "deliverables",
            str(balsamic_tn_panel_deliverables),
            "--workflow",
            "balsamic-qc",
            "--analysis-type",
            "tumor_normal_panel",
        ],
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "workflow",
    Workflow.get_nf_workflows(),
)
def test_validate_nf_workflow_deliverables_file(
    cli_runner: CliRunner,
    workflow: Workflow,
    request: FixtureRequest,
    caplog: LogCaptureFixture,
):
    """Test validate deliverables file command for workflow."""
    # GIVEN the path to an existing deliverables file
    deliverables: Path = request.getfixturevalue(f"{workflow}_deliverables")
    assert deliverables.exists()

    # WHEN invoking the validate deliverables command
    result = cli_runner.invoke(app, ["deliverables", str(deliverables), "--workflow", workflow])

    # THEN assert it exits without problem
    assert result.exit_code == 0
