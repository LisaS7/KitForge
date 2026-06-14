import json
from pathlib import Path

from src.store import load_all


def test_load_all_returns_kits(tmp_path, kit):
    (tmp_path / f"{kit.id}.json").write_text(kit.model_dump_json(), encoding="utf-8")
    kits = load_all(tmp_path)
    assert len(kits) == 1
    assert kits[0].id == kit.id


def test_load_all_empty_dir(tmp_path):
    assert load_all(tmp_path) == []


def test_load_all_missing_dir(tmp_path):
    assert load_all(tmp_path / "nonexistent") == []


def test_load_all_skips_invalid(tmp_path, kit):
    (tmp_path / "bad.json").write_text("not valid json", encoding="utf-8")
    (tmp_path / f"{kit.id}.json").write_text(kit.model_dump_json(), encoding="utf-8")
    kits = load_all(tmp_path)
    assert len(kits) == 1
