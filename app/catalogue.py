import json
import logging

from .config import CATALOGUE_PATH
from .models import CatalogueItem, Category

logger = logging.getLogger(__name__)


def load_catalogue() -> list[CatalogueItem]:
    with open(CATALOGUE_PATH) as f:
        data = json.load(f)["items"]

    logger.info(f"Loaded {len(data)} items")
    return [CatalogueItem.model_validate(item) for item in data]


def group_by_category(data: list[CatalogueItem]) -> dict[Category, list[CatalogueItem]]:
    categories = {}

    for item in data:
        category = item.category

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    return categories
