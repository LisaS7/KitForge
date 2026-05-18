import json
import logging
from collections import defaultdict

from .config import CATALOGUE_PATH
from .models import CatalogueItem, Category

logger = logging.getLogger(__name__)

# ------------- LOADING -------------


def load_catalogue() -> list[CatalogueItem]:
    with open(CATALOGUE_PATH) as f:
        data = json.load(f)["items"]

    logger.info(f"Loaded {len(data)} items")
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


def validate_catalogue(data: list[CatalogueItem]) -> list[str]:
    errors = []
    errors.extend(check_unique_ids(data))
    return errors
