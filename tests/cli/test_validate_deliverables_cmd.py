"""Tests for the validate deliverables cli command"""

from pathlib import Path

from typer.testing import CliRunner

from cg_hermes.cli.validate import app


def test_validate_mip_deliverables_file(cli_runner: CliRunner, mip_dna_deliverables: Path):
    # GIVEN a existing mip deliverables file and a CLI runner
    assert mip_dna_deliverables.exists()

    # WHEN running the validate deliverables command
    result = cli_runner.invoke(
        app, ["deliverables", str(mip_dna_deliverables), "--pipeline", "mip"]
    )

    # THEN assert it exits without problem
    assert result.exit_code == 0
