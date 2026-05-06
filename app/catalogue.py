import json
from pathlib import Path

catalogue_path = Path("data/catalogue.json")


def load_json():
    with open(catalogue_path) as f:
        data = json.load(f)["items"]

    print(f"Loaded {len(data)} items")
    return data


def group_by_category(data):
    categories = {}

    for item in data:
        category = item["category"]

        if category not in categories:
            categories[category] = []

        categories[category].append(item)

    return categories
