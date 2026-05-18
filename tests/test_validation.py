from app.catalogue import check_unique_ids, validate_catalogue
from app.models import CatalogueItem, Category


def make_item(id: str, **overrides) -> CatalogueItem:
    defaults = dict(
        id=id,
        name=id,
        category=Category.TOOLS,
        weight_g=100,
        calories=0,
        water_ml=0,
        water_purification_ml=0,
        default_qty=1,
    )
    return CatalogueItem(**{**defaults, **overrides})


# --- check_unique_ids ---

def test_unique_ids_no_errors():
    items = [make_item("a"), make_item("b")]
    assert check_unique_ids(items) == []


def test_unique_ids_detects_duplicate():
    items = [make_item("a"), make_item("b"), make_item("a")]
    errors = check_unique_ids(items)
    assert len(errors) == 1
    assert "a" in errors[0]


def test_unique_ids_multiple_duplicates():
    items = [make_item("a"), make_item("a"), make_item("b"), make_item("b")]
    errors = check_unique_ids(items)
    assert len(errors) == 2


def test_unique_ids_empty():
    assert check_unique_ids([]) == []


# --- validate_catalogue ---

def test_validate_catalogue_valid():
    items = [make_item("a"), make_item("b")]
    assert validate_catalogue(items) == []


def test_validate_catalogue_includes_duplicate_id_errors():
    items = [make_item("x"), make_item("x")]
    errors = validate_catalogue(items)
    assert any("x" in e for e in errors)


def test_validate_catalogue_real_catalogue():
    from app.catalogue import load_catalogue
    items = load_catalogue()
    assert validate_catalogue(items) == []
