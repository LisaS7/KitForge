from typing import Any

from PySide6.QtCore import Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QGridLayout, QLabel, QWidget

from src.config import PROJECT_ROOT
from src.models import Kit

UI_PATH = PROJECT_ROOT / "src" / "views" / "ui" / "kit_list.ui"


class KitListView(QWidget):
    new_kit_requested = Signal()

    def __init__(self, parent=None, kits: list[Kit] | None = None):
        super().__init__(parent)
        self.ui: Any = QUiLoader().load(str(UI_PATH), self)

        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)

        self.ui.btn_new_kit.clicked.connect(self.new_kit_requested)

        self._cards_layout = QGridLayout(self.ui.cards_container)
        self._populate(kits)

    def _populate(self, kits):
        if not kits:
            self._cards_layout.addWidget(
                QLabel("No kits yet. Create one to get started."), 0, 0
            )
            return
        for i, kit in enumerate(kits):
            self._cards_layout.addWidget(QLabel(kit.name), i // 3, i % 3)
