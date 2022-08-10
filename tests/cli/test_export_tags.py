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


def test_export_mip_dna_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline mip
    result = cli_runner.invoke(app, ["--pipeline", "mip-dna"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags was exported
    assert "Mip-dna tags" in result.output


def test_export_mip_rna_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline mip
    result = cli_runner.invoke(app, ["--pipeline", "mip-rna"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags was exported
    assert "Mip-rna tags" in result.output


def test_export_balsamic_tags(cli_runner: CliRunner):
    """Tests export of all the Balsamic tags"""

    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline balsamic
    result = cli_runner.invoke(app, ["--pipeline", "balsamic"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the balsamic tags was exported
    assert "Balsamic tags" in result.output
    assert "umi" in result.output


def test_export_fluffy_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline balsamic
    result = cli_runner.invoke(app, ["--pipeline", "fluffy"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the mip_dna tags was exported
    assert "Fluffy tags" in result.output


def test_export_rnafusion_tags(cli_runner: CliRunner):
    # GIVEN a cli runner

    # WHEN running the export tags command for pipeline rnafusion
    result = cli_runner.invoke(app, ["--pipeline", "rnafusion"])

    # THEN assert that the command exits without problems
    assert result.exit_code == 0
    # THEN assert that the rnafusion tags was exported
    assert "Rnafusion tags" in result.output
