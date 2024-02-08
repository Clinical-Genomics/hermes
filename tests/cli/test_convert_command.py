"""Tests for the convert command"""

from pathlib import Path

from typer.testing import CliRunner

from cg_hermes.cli.convert import app
from cg_hermes.constants.workflow import Workflow


def test_convert_mip_dna_deliverables(cli_runner: CliRunner, mip_dna_deliverables: Path):
    # GIVEN the path to a mip_dna dna deliverables file
    assert mip_dna_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(mip_dna_deliverables), "--workflow", "mip-dna"])

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_mip_rna_deliverables(cli_runner: CliRunner, mip_rna_deliverables: Path):
    # GIVEN the path to a mip_dna dna deliverables file
    assert mip_rna_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(mip_rna_deliverables), "--workflow", "mip-rna"])

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_mip_deliverables_microsalt_file(
    cli_runner: CliRunner, microsalt_deliverables: Path
):
    # GIVEN the path to a microsalt deliverables file
    assert microsalt_deliverables.exists()

    # WHEN converting the deliverables to CG format using mip as workflow
    result = cli_runner.invoke(app, [str(microsalt_deliverables), "--workflow", "mip-dna"])

    # THEN assert that the program exits without success
    assert result.exit_code == 1


def test_convert_microsalt_deliverables(cli_runner: CliRunner, microsalt_deliverables: Path):
    # GIVEN the path to a microsalt dna deliverables file
    assert microsalt_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(microsalt_deliverables), "--workflow", "microsalt"])

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_mutant_deliverables(cli_runner: CliRunner, mutant_deliverables: Path):
    # GIVEN the path to a mutant deliverables file
    assert mutant_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(mutant_deliverables), "--workflow", Workflow.MUTANT])

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_fluffy_deliverables(cli_runner: CliRunner, fluffy_deliverables: Path):
    # GIVEN the path to a fluffy deliverables file
    assert fluffy_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(fluffy_deliverables), "--workflow", "fluffy"])

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_tn_panel_deliverables(
    cli_runner: CliRunner, balsamic_tn_panel_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file with TN data
    assert balsamic_tn_panel_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_tn_panel_deliverables),
            "--workflow",
            "balsamic",
            "--analysis-type",
            "tumor_normal_panel",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_t_only_panel_deliverables(
    cli_runner: CliRunner, balsamic_t_only_panel_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file with Tumor only data
    assert balsamic_t_only_panel_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_t_only_panel_deliverables),
            "--workflow",
            "balsamic",
            "--analysis-type",
            "tumor_panel",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_tn_wgs_deliverables(
    cli_runner: CliRunner, balsamic_tn_wgs_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file
    assert balsamic_tn_wgs_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_tn_wgs_deliverables),
            "--workflow",
            "balsamic",
            "--analysis-type",
            "tumor_normal_wgs",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_t_only_wgs_deliverables(
    cli_runner: CliRunner, balsamic_t_only_wgs_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file
    assert balsamic_t_only_wgs_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_t_only_wgs_deliverables),
            "--workflow",
            "balsamic",
            "--analysis-type",
            "tumor_wgs",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_umi_tn_deliverables(
    cli_runner: CliRunner, balsamic_tn_panel_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file with TN data
    assert balsamic_tn_panel_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_tn_panel_deliverables),
            "--workflow",
            "balsamic-umi",
            "--analysis-type",
            "tumor_normal_panel",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_umi_t_only_deliverables(
    cli_runner: CliRunner, balsamic_t_only_panel_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file
    assert balsamic_t_only_panel_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_t_only_panel_deliverables),
            "--workflow",
            "balsamic-umi",
            "--analysis-type",
            "tumor_panel",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_qc_tn_panel_deliverables(
    cli_runner: CliRunner, balsamic_tn_panel_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file with TN data
    assert balsamic_tn_panel_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_tn_panel_deliverables),
            "--workflow",
            "balsamic-qc",
            "--analysis-type",
            "tumor_normal_panel",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_balsamic_qc_tn_wgs_deliverables(
    cli_runner: CliRunner, balsamic_tn_wgs_deliverables: Path
):
    # GIVEN the path to a balsamic deliverables file
    assert balsamic_tn_wgs_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(
        app,
        [
            str(balsamic_tn_wgs_deliverables),
            "--workflow",
            "balsamic-qc",
            "--analysis-type",
            "tumor_normal_wgs",
        ],
    )

    # THEN assert that the program exits with success
    assert result.exit_code == 0


def test_convert_rnafusion_deliverables(cli_runner: CliRunner, rnafusion_deliverables: Path):
    # GIVEN the path to a rnafusion deliverables file
    assert rnafusion_deliverables.exists()

    # WHEN converting the deliverables to CG format
    result = cli_runner.invoke(app, [str(rnafusion_deliverables), "--workflow", "rnafusion"])

    # THEN assert that the program exits with success
    assert result.exit_code == 0
