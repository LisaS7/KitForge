import datetime as dt

import pytest

from src.models import Category, CatalogueItem, Kit, KitConfig, KitItem


@pytest.fixture
def config():
    return KitConfig(
        weight_limit_g=10000,
        num_adults=1,
        num_children=0,
        num_young_children=0,
        num_infants=0,
        duration_days=3,
    )


@pytest.fixture
def kit(config):
    return Kit.create("Test Kit", config)


@pytest.fixture
def catalogue_item():
    return CatalogueItem(
        id="water_bottle",
        name="Water Bottle",
        category=Category.WATER,
        weight_g=200,
        calories=0,
        water_ml=1000,
        water_purification_ml=0,
        default_qty=1,
    )
