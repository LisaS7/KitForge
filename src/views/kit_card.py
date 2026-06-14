from typing import Any

from PySide6.QtCore import Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QFrame, QVBoxLayout

from src.config import PROJECT_ROOT
from src.models import Kit

UI_PATH = PROJECT_ROOT / "src" / "views" / "ui" / "kit_card.ui"


class KitCard(QFrame):
    edit_requested = Signal()
    copy_requested = Signal()
    delete_requested = Signal()

    def __init__(self, kit: Kit, parent=None):
        super().__init__(parent)
        self.ui: Any = QUiLoader().load(str(UI_PATH), self)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)

        self.ui.lbl_name.setText(kit.name)
        self.ui.lbl_score.setText("-")
        self.ui.lbl_weight.setText("-")
        self.ui.lbl_modified.setText(kit.modified_at.strftime("%-d %B %Y"))

        self.ui.btn_edit.clicked.connect(self.edit_requested)
        self.ui.btn_copy.clicked.connect(self.copy_requested)
        self.ui.btn_delete.clicked.connect(self.delete_requested)
