import pytest

from app.models import Kit, KitConfig
from app.storage import load_all_kits, save_kit


def make_kit(name="Test Kit") -> Kit:
    cfg = KitConfig(
        weight_limit_g=10000,
        num_adults=1,
        num_children=0,
        num_young_children=0,
        num_infants=0,
        duration_days=3,
    )
    return Kit.create(name, cfg)


def test_save_kit_creates_file(tmp_path):
    kit = make_kit()
    save_kit(kit, tmp_path)
    assert (tmp_path / f"{kit.id}.json").exists()


def test_save_kit_creates_dir_if_missing(tmp_path):
    kit = make_kit()
    kits_dir = tmp_path / "nested" / "kits"
    save_kit(kit, kits_dir)
    assert (kits_dir / f"{kit.id}.json").exists()


def test_save_kit_updates_modified_at(tmp_path):
    kit = make_kit()
    before = kit.modified_at
    save_kit(kit, tmp_path)
    assert kit.modified_at >= before


def test_load_all_kits_returns_saved_kit(tmp_path):
    kit = make_kit("My Kit")
    save_kit(kit, tmp_path)
    loaded = load_all_kits(tmp_path)
    assert len(loaded) == 1
    assert loaded[0].id == kit.id
    assert loaded[0].name == "My Kit"


def test_load_all_kits_multiple(tmp_path):
    kits = [make_kit(f"Kit {i}") for i in range(3)]
    for k in kits:
        save_kit(k, tmp_path)
    loaded = load_all_kits(tmp_path)
    assert len(loaded) == 3
    assert {k.id for k in loaded} == {k.id for k in kits}


def test_load_all_kits_missing_dir(tmp_path):
    assert load_all_kits(tmp_path / "nonexistent") == []


def test_load_all_kits_skips_invalid_files(tmp_path):
    (tmp_path / "bad.json").write_text("not valid json", encoding="utf-8")
    kit = make_kit()
    save_kit(kit, tmp_path)
    loaded = load_all_kits(tmp_path)
    assert len(loaded) == 1
    assert loaded[0].id == kit.id
