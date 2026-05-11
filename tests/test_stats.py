from app.models import CatalogueItem, Category, Kit, KitConfig
from app.stats import KitStats


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


def make_item(id: str, weight_g=100, calories=50, water_ml=0, water_purification_ml=0) -> CatalogueItem:
    return CatalogueItem(
        id=id,
        name=id,
        category=Category.FOOD,
        weight_g=weight_g,
        calories=calories,
        water_ml=water_ml,
        water_purification_ml=water_purification_ml,
        default_qty=1,
    )


def test_empty_kit():
    kit = Kit.create("test", make_config())
    stats = KitStats.calculate_stats(kit, {})
    assert stats.total_weight_g == 0
    assert stats.total_calories == 0
    assert stats.stored_water_ml == 0
    assert stats.purifiable_water_ml == 0
    assert stats.weight_limit_g == 10000


def test_single_item():
    kit = Kit.create("test", make_config())
    item = make_item("a", weight_g=200, calories=300, water_ml=500, water_purification_ml=1000)
    kit.add_item("a")
    stats = KitStats.calculate_stats(kit, {"a": item})
    assert stats.total_weight_g == 200
    assert stats.total_calories == 300
    assert stats.stored_water_ml == 500
    assert stats.purifiable_water_ml == 1000


def test_qty_multiplied():
    kit = Kit.create("test", make_config())
    item = make_item("a", weight_g=100, calories=50)
    kit.add_item("a")
    kit.add_item("a")  # qty becomes 2
    stats = KitStats.calculate_stats(kit, {"a": item})
    assert stats.total_weight_g == 200
    assert stats.total_calories == 100


def test_multiple_items_summed():
    kit = Kit.create("test", make_config())
    items = {
        "a": make_item("a", weight_g=100, calories=200),
        "b": make_item("b", weight_g=300, calories=400),
    }
    kit.add_item("a")
    kit.add_item("b")
    stats = KitStats.calculate_stats(kit, items)
    assert stats.total_weight_g == 400
    assert stats.total_calories == 600


def test_weight_limit_from_config():
    kit = Kit.create("test", make_config(weight_limit_g=5000))
    stats = KitStats.calculate_stats(kit, {})
    assert stats.weight_limit_g == 5000


def test_defaults_for_unset_fields():
    kit = Kit.create("test", make_config())
    stats = KitStats.calculate_stats(kit, {})
    assert stats.calorie_requirement == 0
    assert stats.water_requirement_ml == 0
    assert stats.readiness_score == 0
