"""Tests for the validate deliverables cli command"""

from pathlib import Path

from typer.testing import CliRunner

from cg_hermes.cli.validate import app


def test_validate_mip_deliverables_file(cli_runner: CliRunner, mip_dna_deliverables: Path):
    # GIVEN a existing mip_dna deliverables file and a CLI runner
    assert mip_dna_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app, ["deliverables", str(mip_dna_deliverables), "--pipeline", "mip-dna"]
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_mip_rna_deliverables_file(cli_runner: CliRunner, mip_rna_deliverables: Path):
    # GIVEN a existing mip_dna deliverables file and a CLI runner
    assert mip_rna_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app, ["deliverables", str(mip_rna_deliverables), "--pipeline", "mip-rna"]
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0


def test_validate_balsamic_deliverables_file(
    cli_runner: CliRunner, balsamic_t_wgs_deliverables: Path
):
    # GIVEN a existing balsamic deliverables file and a CLI runner
    assert balsamic_t_wgs_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app,
        [
            "deliverables",
            str(balsamic_t_wgs_deliverables),
            "--pipeline",
            "balsamic",
            "--analysis-type",
            "tumor_wgs",
        ],
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0
