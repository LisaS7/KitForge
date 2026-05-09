import pytest
from pydantic import ValidationError

from app.models import CatalogueItem, Category, Kit, KitConfig, KitItem


def make_config(**overrides) -> KitConfig:
    defaults = dict(
        weight_limit_g=10000,
        num_adults=1,
        num_children=0,
        num_young_children=0,
        num_infants=0,
        duration_days=3,
    )
    return KitConfig(**{**defaults, **overrides})


# --- KitConfig ---

def test_kitconfig_valid():
    cfg = make_config()
    assert cfg.weight_limit_g == 10000
    assert cfg.num_adults == 1


def test_kitconfig_zero_weight_limit_rejected():
    with pytest.raises(ValidationError):
        make_config(weight_limit_g=0)


def test_kitconfig_zero_duration_rejected():
    with pytest.raises(ValidationError):
        make_config(duration_days=0)


def test_kitconfig_no_people_rejected():
    with pytest.raises(ValidationError):
        make_config(num_adults=0)


def test_kitconfig_multiple_person_types():
    cfg = make_config(num_adults=0, num_children=1, num_young_children=1, num_infants=1)
    assert cfg.num_children == 1


# --- Kit ---

def test_kit_create():
    cfg = make_config()
    kit = Kit.create("Go Bag", cfg)
    assert kit.name == "Go Bag"
    assert kit.id
    assert kit.created_at == kit.modified_at
    assert kit.items == []


def test_kit_create_unique_ids():
    cfg = make_config()
    assert Kit.create("A", cfg).id != Kit.create("B", cfg).id


# --- CatalogueItem ---

def test_catalogue_item_valid():
    item = CatalogueItem(
        id="test_item",
        name="Test Item",
        category=Category.WATER,
        weight_g=100,
        calories=0,
        water_ml=500,
        water_purification_ml=0,
        default_qty=1,
    )
    assert item.category == Category.WATER


def test_catalogue_item_negative_weight_rejected():
    with pytest.raises(ValidationError):
        CatalogueItem(
            id="x",
            name="X",
            category=Category.FOOD,
            weight_g=-1,
            calories=0,
            water_ml=0,
            water_purification_ml=0,
            default_qty=1,
        )


def test_catalogue_item_zero_qty_rejected():
    with pytest.raises(ValidationError):
        CatalogueItem(
            id="x",
            name="X",
            category=Category.FOOD,
            weight_g=0,
            calories=0,
            water_ml=0,
            water_purification_ml=0,
            default_qty=0,
        )


def test_kit_item_zero_qty_rejected():
    with pytest.raises(ValidationError):
        KitItem(item_id="x", qty=0)


# --- Kit.add_item ---

def test_add_item_new():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    assert len(kit.items) == 1
    assert kit.items[0].item_id == "item_1"
    assert kit.items[0].qty == 1


def test_add_item_increments_existing():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.add_item("item_1")
    assert len(kit.items) == 1
    assert kit.items[0].qty == 2


def test_add_item_distinct_items():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.add_item("item_2")
    assert len(kit.items) == 2


def test_add_item_updates_modified_at():
    kit = Kit.create("Bag", make_config())
    before = kit.modified_at
    kit.add_item("item_1")
    assert kit.modified_at >= before


# --- Kit.remove_item ---

def test_remove_item():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.remove_item("item_1")
    assert kit.items == []


def test_remove_item_leaves_others():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.add_item("item_2")
    kit.remove_item("item_1")
    assert len(kit.items) == 1
    assert kit.items[0].item_id == "item_2"


def test_remove_item_missing_is_noop():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.remove_item("item_99")
    assert len(kit.items) == 1


def test_remove_item_updates_modified_at():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    before = kit.modified_at
    kit.remove_item("item_1")
    assert kit.modified_at >= before


# --- Kit.increment_item ---

def test_increment_item():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.increment_item("item_1")
    assert kit.items[0].qty == 2


def test_increment_item_missing_is_noop():
    kit = Kit.create("Bag", make_config())
    kit.increment_item("item_99")
    assert kit.items == []


def test_increment_item_updates_modified_at():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    before = kit.modified_at
    kit.increment_item("item_1")
    assert kit.modified_at >= before


# --- Kit.decrement_item ---

def test_decrement_item_reduces_qty():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.add_item("item_1")
    kit.decrement_item("item_1")
    assert kit.items[0].qty == 1


def test_decrement_item_removes_at_one():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    kit.decrement_item("item_1")
    assert kit.items == []


def test_decrement_item_missing_is_noop():
    kit = Kit.create("Bag", make_config())
    kit.decrement_item("item_99")
    assert kit.items == []


def test_decrement_item_updates_modified_at():
    kit = Kit.create("Bag", make_config())
    kit.add_item("item_1")
    before = kit.modified_at
    kit.decrement_item("item_1")
    assert kit.modified_at >= before
