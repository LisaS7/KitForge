import json
from pathlib import Path

from models import CatalogueItem, Category

catalogue_path = Path("data/catalogue.json")


def load_catalogue() -> list[CatalogueItem]:
    with open(catalogue_path) as f:
        data = json.load(f)["items"]

    print(f"Loaded {len(data)} items")
    return [CatalogueItem.model_validate(item) for item in data]


def group_by_category(data: list[CatalogueItem]) -> dict[Category, list[CatalogueItem]]:
    categories = {}

    for item in data:
        category = item.category

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    return categories
