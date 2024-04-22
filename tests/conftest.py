"""Common fixtures for Hermes."""

from pathlib import Path

import pytest

# Folder fixtures


@pytest.fixture(name="fixtures_dir")
def fixture_fixtures_dir() -> Path:
    return Path("tests/fixtures")


@pytest.fixture(name="mip_dna_files")
def fixture_mip_dna_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "mip_dna"


@pytest.fixture(name="mip_rna_files")
def fixture_mip_rna_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "mip_rna"


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


@pytest.fixture(name="rarediease_files")
def fixture_raredisease_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "raredisease"


@pytest.fixture(name="rnafusion_files")
def fixture_rnafusion_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "rnafusion"


@pytest.fixture(name="taxprofiler_files")
def fixture_taxprofiler_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "taxprofiler"


@pytest.fixture(name="tomte_files")
def fixture_tomte_files(fixtures_dir: Path) -> Path:
    return fixtures_dir / "tomte"


# File fixtures


@pytest.fixture(name="mip_dna_deliverables")
def fixture_mip_dna_deliverables(mip_dna_files: Path) -> Path:
    return mip_dna_files / "case_id_deliverables.yaml"


@pytest.fixture(name="mip_rna_deliverables")
def fixture_mip_rna_deliverables(mip_rna_files: Path) -> Path:
    return mip_rna_files / "case_id_deliverables.yaml"


@pytest.fixture(name="fluffy_deliverables")
def fixture_fluffy_deliverables(fluffy_files: Path) -> Path:
    return fluffy_files / "deliverables.yaml"


@pytest.fixture(name="microsalt_deliverables")
def fixture_microsalt_deliverables(microsalt_files: Path) -> Path:
    return microsalt_files / "deliverables.yaml"


@pytest.fixture(name="mutant_deliverables")
def fixture_mutant_deliverables(mutant_files: Path) -> Path:
    return mutant_files / "deliverables.yaml"


@pytest.fixture(name="balsamic_tn_wgs_deliverables")
def fixture_balsamic_tn_wgs_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "TN_wgs.hk"


@pytest.fixture(name="balsamic_t_only_wgs_deliverables")
def fixture_balsamic_t_only_wgs_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "T_wgs.hk"


@pytest.fixture(name="balsamic_tn_panel_deliverables")
def fixture_balsamic_tn_panel_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "TN_panel.hk"


@pytest.fixture(name="balsamic_t_only_panel_deliverables")
def fixture_balsamic_t_only_panel_deliverables(balsamic_files: Path) -> Path:
    return balsamic_files / "T_panel.hk"


@pytest.fixture(name="raredisease_deliverables")
def fixture_raredisease_deliverables(raredisease_files: Path) -> Path:
    return raredisease_files / "case_id_deliverables.yaml"


@pytest.fixture(name="rnafusion_deliverables")
def fixture_rnafusion_deliverables(rnafusion_files: Path) -> Path:
    return rnafusion_files / "case_id_deliverables.yaml"


@pytest.fixture(name="taxprofiler_deliverables")
def fixture_taxprofiler_deliverables(taxprofiler_files: Path) -> Path:
    return taxprofiler_files / "case_id_deliverables.yaml"


@pytest.fixture(name="tomte_deliverables")
def fixture_tomte_deliverables(tomte_files: Path) -> Path:
    return tomte_files / "case_id_deliverables.yaml"
