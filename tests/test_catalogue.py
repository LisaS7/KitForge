import pytest

from src.catalogue import (
    check_category_requirements,
    check_item_requirements,
    check_resource_requirements,
    check_unique_ids,
    validate_catalogue,
)
from src.models import (
    CatalogueItem,
    Category,
    Requirement,
    RequirementType,
    ResourceType,
)


def make_item(id, requires=None):
    return CatalogueItem(
        id=id,
        name=id,
        category=Category.TOOLS,
        weight_g=100,
        calories=0,
        water_ml=0,
        water_purification_ml=0,
        default_qty=1,
        requires=requires or [],
    )


def test_check_unique_ids_no_errors():
    items = [make_item("a"), make_item("b")]
    assert check_unique_ids(items) == []


def test_check_unique_ids_duplicate():
    items = [make_item("a"), make_item("a")]
    errors = check_unique_ids(items)
    assert len(errors) == 1
    assert "a" in errors[0]


def test_check_item_requirements_valid():
    req = Requirement(type=RequirementType.ITEM, target_id="b")
    items = [make_item("a", requires=[req]), make_item("b")]
    assert check_item_requirements(items) == []


def test_check_item_requirements_unknown_target():
    req = Requirement(type=RequirementType.ITEM, target_id="missing")
    items = [make_item("a", requires=[req])]
    errors = check_item_requirements(items)
    assert len(errors) == 1
    assert "missing" in errors[0]


def test_check_item_requirements_self_reference():
    req = Requirement(type=RequirementType.ITEM, target_id="a")
    items = [make_item("a", requires=[req])]
    errors = check_item_requirements(items)
    assert any("itself" in e for e in errors)


def test_check_category_requirements_valid():
    req = Requirement(type=RequirementType.CATEGORY, target_category=Category.WATER)
    items = [make_item("a", requires=[req])]
    assert check_category_requirements(items) == []


def test_check_category_requirements_missing_category():
    req = Requirement(type=RequirementType.CATEGORY, target_category=None)
    items = [make_item("a", requires=[req])]
    errors = check_category_requirements(items)
    assert len(errors) == 1


def test_check_resource_requirements_water_ml_valid():
    req = Requirement(type=RequirementType.RESOURCE, resource=ResourceType.WATER_ML, amount=500)
    items = [make_item("a", requires=[req])]
    assert check_resource_requirements(items) == []


def test_check_resource_requirements_water_ml_no_amount():
    req = Requirement(type=RequirementType.RESOURCE, resource=ResourceType.WATER_ML, amount=None)
    items = [make_item("a", requires=[req])]
    errors = check_resource_requirements(items)
    assert len(errors) == 1


def test_check_resource_requirements_no_resource():
    req = Requirement(type=RequirementType.RESOURCE, resource=None)
    items = [make_item("a", requires=[req])]
    errors = check_resource_requirements(items)
    assert len(errors) == 1


def test_validate_catalogue_clean():
    items = [make_item("a"), make_item("b")]
    assert validate_catalogue(items) == []


def test_validate_catalogue_collects_all_errors():
    req = Requirement(type=RequirementType.ITEM, target_id="missing")
    items = [make_item("a", requires=[req]), make_item("a")]  # duplicate + unknown ref
    errors = validate_catalogue(items)
    assert len(errors) >= 2
