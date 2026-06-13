from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# LOGGING
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "kitforge.log"

# CATALOGUE
CATALOGUE_PATH = PROJECT_ROOT / "data" / "catalogue.json"

# SAVED KITS
KITS_DIR = PROJECT_ROOT / "data" / "kits"
KITS_DIR.mkdir(exist_ok=True)
