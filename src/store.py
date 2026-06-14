import logging
from pathlib import Path

from src.models import Kit

logger = logging.getLogger(__name__)


def load_all(kits_dir: Path) -> list[Kit]:
    if not kits_dir.exists():
        return []

    kits = []
    for path in kits_dir.glob("*.json"):
        try:
            kits.append(Kit.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception as e:
            logger.warning("Skipping invalid kit file %s: %s", path.name, e)
    return kits


def save(kit: Kit):
    pass


def delete(kit_id: str):
    pass
