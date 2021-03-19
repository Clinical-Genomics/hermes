"""Common fixtures for hermes"""

from pathlib import Path

import pytest

# Folder fixtures


@pytest.fixture(name="fixtures_dir")
def fixture_fixtures_dir() -> Path:
    return Path("tests/fixtures")


@pytest.fixture(name="mip_files")
def fixture_mip_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "mip"


@pytest.fixture(name="balsamic_files")
def fixture_balsamic_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "balsamic"


@pytest.fixture(name="fluffy_files")
def fixture_fluffy_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "fluffy"


@pytest.fixture(name="microsalt_files")
def fixture_microsalt_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "microsalt"


@pytest.fixture(name="mutant_files")
def fixture_mutant_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "mutant"


# File fixtures


@pytest.fixture(name="mip_dna_deliverables")
def fixture_mip_dna_deliverables(mip_files: Path) -> Path:
    return mip_files / "case_id_deliverables.yaml"


@pytest.fixture(name="fluffy_deliverables")
def fixture_fluffy_deliverables(fluffy_files: Path) -> Path:
    return fluffy_files / "deliverables.yaml"


@pytest.fixture(name="microsalt_deliverables")
def fixture_microsalt_deliverables(microsalt_files: Path) -> Path:
    return microsalt_files / "deliverables.yaml"


@pytest.fixture(name="mutant_deliverables")
def fixture_mutant_deliverables(mutant_files: Path) -> Path:
    return mutant_files / "deliverables.yaml"


@pytest.fixture(name="balsamic_t_wgs_deliverables")
def fixture_balsamic_t_wgs_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "oneel.hk"


@pytest.fixture(name="balsamic_tn_panel_deliverables")
def fixture_balsamic_tn_panel_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "TN_panel.hk"


@pytest.fixture(name="balsamic_t_only_panel_deliverables")
def fixture_balsamic_t_only_panel_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "T_panel.hk"
