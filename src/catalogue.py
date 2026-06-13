import json
import logging
from collections import defaultdict

from src.config import CATALOGUE_PATH
from src.models import CatalogueItem, Category, RequirementType, ResourceType

logger = logging.getLogger(__name__)

# ------------- LOADING -------------


def load_catalogue() -> list[CatalogueItem]:
    with open(CATALOGUE_PATH) as f:
        data = json.load(f)["items"]

    logger.info("Loaded %d items", len(data))
    return [CatalogueItem.model_validate(item) for item in data]


def group_by_category(data: list[CatalogueItem]) -> dict[Category, list[CatalogueItem]]:
    categories = defaultdict(list)
    for item in data:
        categories[item.category].append(item)
    return dict(categories)


# ------------- VALIDATION -------------


def check_unique_ids(data: list[CatalogueItem]) -> list[str]:
    errors = []
    existing_ids = set()

    for item in data:
        if item.id in existing_ids:
            errors.append(f"Duplicate item ID: {item.id}")
        existing_ids.add(item.id)
    return errors


def check_item_requirements(data: list[CatalogueItem]) -> list[str]:
    errors = []
    item_ids = {item.id for item in data}

    for item in data:
        for requirement in item.requires:
            if requirement.type != RequirementType.ITEM:
                continue

            if requirement.target_id is None:
                errors.append(f"{item.id} has item requirement with no target ID")
                continue

            if requirement.target_id not in item_ids:
                errors.append(
                    f"{item.id} requires unknown item: {requirement.target_id}"
                )

            if requirement.target_id == item.id:
                errors.append(f"{item.id} requires itself")

    return errors


def check_category_requirements(data: list[CatalogueItem]) -> list[str]:
    errors = []

    for item in data:
        for requirement in item.requires:
            if requirement.type != RequirementType.CATEGORY:
                continue

            if requirement.target_category is None:
                errors.append(
                    f"{item.id} has category requirement with no target category"
                )

    return errors


def check_resource_requirements(data: list[CatalogueItem]) -> list[str]:
    errors = []

    for item in data:
        for requirement in item.requires:
            if requirement.type != RequirementType.RESOURCE:
                continue

            if requirement.resource is None:
                errors.append(f"{item.id} has resource requirement with no resource")
                continue

            if requirement.resource == ResourceType.WATER_ML:
                if requirement.amount is None:
                    errors.append(f"{item.id} requires water_ml but has no amount")
                elif requirement.amount <= 0:
                    errors.append(
                        f"{item.id} requires water_ml but amount is not positive: {requirement.amount}"
                    )

    return errors


def validate_catalogue(data: list[CatalogueItem]) -> list[str]:
    errors = []
    errors.extend(check_unique_ids(data))
    errors.extend(check_item_requirements(data))
    errors.extend(check_category_requirements(data))
    errors.extend(check_resource_requirements(data))
    return errors
