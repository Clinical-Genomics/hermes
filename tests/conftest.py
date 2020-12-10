"""Common fixtures for hermes"""

from pathlib import Path

import pytest

# File fixtures


@pytest.fixture(name="fixtures_dir")
def fixture_fixtures_dir() -> Path:
    return Path("tests/fixtures")


@pytest.fixture(name="mip_files")
def fixture_mip_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "mip"


@pytest.fixture(name="balsamic_files")
def fixture_balsamic_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "balsamic"


@pytest.fixture(name="mip_dna_deliverables")
def fixture_mip_dna_deliverables(mip_files: Path) -> Path:
    return mip_files / "case_id_deliverables.yaml"


@pytest.fixture(name="balsamic_t_wgs_deliverables")
def fixture_balsamic_t_wgs_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "oneel.hk"
