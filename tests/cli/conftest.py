"""Fixtures for cli tests"""

import pytest
from typer.testing import CliRunner


@pytest.fixture(name="cli_runner")
def fixture_cli_runner() -> CliRunner:
    return CliRunner()
