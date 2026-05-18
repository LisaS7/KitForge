import logging
from datetime import UTC, datetime
from pathlib import Path

from app.models import Kit

logger = logging.getLogger(__name__)


def save_kit(kit: Kit, kits_dir: Path) -> None:
    kits_dir.mkdir(parents=True, exist_ok=True)
    kit.modified_at = datetime.now(UTC)

    path = kits_dir / f"{kit.id}.json"
    path.write_text(kit.model_dump_json(indent=2), encoding="utf-8")

    logger.debug("Saved kit %s to %s", kit.id, path)


def load_all_kits(kits_dir: Path) -> list[Kit]:
    if not kits_dir.exists():
        return []
    kits = []
    for path in kits_dir.glob("*.json"):
        try:
            kits.append(Kit.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception as e:
            logger.warning("Skipping invalid kit file %s: %s", path.name, e)
    return kits
