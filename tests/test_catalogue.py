from app.catalogue import group_by_category, load_catalogue
from app.models import CatalogueItem, Category


def test_load_catalogue_returns_items():
    items = load_catalogue()
    assert len(items) > 0
    assert all(isinstance(i, CatalogueItem) for i in items)


def test_load_catalogue_covers_all_categories():
    items = load_catalogue()
    found = {i.category for i in items}
    assert found == set(Category)


def test_group_by_category_keys():
    items = load_catalogue()
    grouped = group_by_category(items)
    assert set(grouped.keys()) == {i.category for i in items}


def test_group_by_category_items_in_correct_bucket():
    items = load_catalogue()
    grouped = group_by_category(items)
    for category, bucket in grouped.items():
        assert all(i.category == category for i in bucket)


def test_group_by_category_no_items_lost():
    items = load_catalogue()
    grouped = group_by_category(items)
    assert sum(len(v) for v in grouped.values()) == len(items)


def test_group_by_category_empty_input():
    assert group_by_category([]) == {}
