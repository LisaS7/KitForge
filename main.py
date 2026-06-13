import logging
import sys

from PySide6.QtWidgets import QApplication

from src.config import LOG_FILE, PROJECT_ROOT
from src.views.kit_list_view import KitListView

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
    ],
)


def main():
    app = QApplication(sys.argv)
    qss = (PROJECT_ROOT / "src" / "styles.qss").read_text()
    app.setStyleSheet(qss)

    view = KitListView()
    view.resize(1200, 800)
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
