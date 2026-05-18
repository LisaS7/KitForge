from app.catalogue import (
    check_category_requirements,
    check_item_requirements,
    check_resource_requirements,
    check_unique_ids,
    validate_catalogue,
)
from app.models import CatalogueItem, Category, Requirement, RequirementType, ResourceType


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


# --- check_item_requirements ---

def make_item_req(target_id: str) -> Requirement:
    return Requirement(type=RequirementType.ITEM, target_id=target_id)


def make_category_req(category: Category) -> Requirement:
    return Requirement(type=RequirementType.CATEGORY, target_category=category)


def test_item_requirements_no_errors():
    a = make_item("a")
    b = make_item("b", requires=[make_item_req("a")])
    assert check_item_requirements([a, b]) == []


def test_item_requirements_unknown_target():
    a = make_item("a", requires=[make_item_req("missing")])
    errors = check_item_requirements([a])
    assert len(errors) == 1
    assert "missing" in errors[0]


def test_item_requirements_self_reference():
    a = make_item("a", requires=[make_item_req("a")])
    errors = check_item_requirements([a])
    assert any("itself" in e for e in errors)


def test_item_requirements_ignores_non_item_types():
    a = make_item("a", requires=[make_category_req(Category.WATER)])
    assert check_item_requirements([a]) == []


def test_item_requirements_empty():
    assert check_item_requirements([]) == []


def test_item_requirements_none_target_id():
    req = Requirement(type=RequirementType.ITEM, target_id=None)
    a = make_item("a", requires=[req])
    errors = check_item_requirements([a])
    assert len(errors) == 1
    assert "no target" in errors[0].lower()


# --- check_category_requirements ---

def test_category_requirements_no_errors():
    a = make_item("a", requires=[make_category_req(Category.WATER)])
    assert check_category_requirements([a]) == []


def test_category_requirements_ignores_non_category_types():
    a = make_item("a", requires=[make_item_req("b")])
    assert check_category_requirements([a]) == []


def test_category_requirements_empty():
    assert check_category_requirements([]) == []


def test_category_requirements_none_target_category():
    req = Requirement(type=RequirementType.CATEGORY, target_category=None)
    a = make_item("a", requires=[req])
    errors = check_category_requirements([a])
    assert len(errors) == 1
    assert "no target" in errors[0].lower()


# --- check_resource_requirements ---

def make_resource_req(resource: ResourceType, amount: int | None = None) -> Requirement:
    return Requirement(type=RequirementType.RESOURCE, resource=resource, amount=amount)


def test_resource_requirements_water_source_no_errors():
    a = make_item("a", requires=[make_resource_req(ResourceType.WATER_SOURCE)])
    assert check_resource_requirements([a]) == []


def test_resource_requirements_water_ml_valid():
    a = make_item("a", requires=[make_resource_req(ResourceType.WATER_ML, amount=500)])
    assert check_resource_requirements([a]) == []


def test_resource_requirements_water_ml_no_amount():
    a = make_item("a", requires=[make_resource_req(ResourceType.WATER_ML, amount=None)])
    errors = check_resource_requirements([a])
    assert len(errors) == 1
    assert "amount" in errors[0].lower()


def test_resource_requirements_water_ml_zero_amount():
    a = make_item("a", requires=[make_resource_req(ResourceType.WATER_ML, amount=0)])
    errors = check_resource_requirements([a])
    assert len(errors) == 1
    assert "not positive" in errors[0].lower()


def test_resource_requirements_water_ml_negative_amount():
    a = make_item("a", requires=[make_resource_req(ResourceType.WATER_ML, amount=-100)])
    errors = check_resource_requirements([a])
    assert len(errors) == 1


def test_resource_requirements_none_resource():
    req = Requirement(type=RequirementType.RESOURCE, resource=None)
    a = make_item("a", requires=[req])
    errors = check_resource_requirements([a])
    assert len(errors) == 1
    assert "no resource" in errors[0].lower()


def test_resource_requirements_ignores_non_resource_types():
    a = make_item("a", requires=[make_item_req("b")])
    assert check_resource_requirements([a]) == []


def test_resource_requirements_empty():
    assert check_resource_requirements([]) == []
