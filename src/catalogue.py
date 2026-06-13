import json
import logging

from models import CatalogueItem

from .config import CATALOGUE_PATH

logger = logging.getLogger(__name__)

# ------------- LOADING -------------


def load_catalogue() -> list[CatalogueItem]:
    with open(CATALOGUE_PATH) as f:
        data = json.load(f)["items"]

    logger.info(f"Loaded {len(data)} items")
    return [CatalogueItem.model_validate(item) for item in data]


# TODO: group by category

# ------------- VALIDATION -------------

# check for unique ids
# check item requirements
# check category requirements
# check resource requirements

# structure this as a data pipeline
