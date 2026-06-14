from src.models import KitItem


def test_add_item_new(kit):
    kit.add_item("water_bottle", default_qty=2)
    assert len(kit.items) == 1
    assert kit.items[0].item_id == "water_bottle"
    assert kit.items[0].qty == 2


def test_add_item_existing_increments(kit):
    kit.add_item("water_bottle")
    kit.add_item("water_bottle")
    assert len(kit.items) == 1
    assert kit.items[0].qty == 2


def test_remove_item(kit):
    kit.add_item("water_bottle")
    kit.remove_item("water_bottle")
    assert kit.items == []


def test_remove_item_not_in_kit(kit):
    kit.remove_item("nonexistent")  # should not raise
    assert kit.items == []


def test_increment_item(kit):
    kit.add_item("water_bottle", default_qty=1)
    kit.increment_item("water_bottle")
    assert kit.items[0].qty == 2


def test_increment_item_not_in_kit(kit):
    kit.increment_item("nonexistent")  # should not raise
    assert kit.items == []


def test_decrement_item(kit):
    kit.add_item("water_bottle", default_qty=2)
    kit.decrement_item("water_bottle")
    assert kit.items[0].qty == 1


def test_decrement_item_removes_at_one(kit):
    kit.add_item("water_bottle", default_qty=1)
    kit.decrement_item("water_bottle")
    assert kit.items == []


def test_decrement_item_not_in_kit(kit):
    kit.decrement_item("nonexistent")  # should not raise
    assert kit.items == []


def test_add_item_updates_modified_at(kit):
    before = kit.modified_at
    kit.add_item("water_bottle")
    assert kit.modified_at >= before
