# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kit_card.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 220)
        self.kit_card = QFrame(Form)
        self.kit_card.setObjectName(u"kit_card")
        self.kit_card.setGeometry(QRect(0, 0, 300, 220))
        self.kit_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.kit_card.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.kit_card)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 0)
        self.lbl_name = QLabel(self.kit_card)
        self.lbl_name.setObjectName(u"lbl_name")

        self.verticalLayout.addWidget(self.lbl_name)

        self.lbl_score = QLabel(self.kit_card)
        self.lbl_score.setObjectName(u"lbl_score")

        self.verticalLayout.addWidget(self.lbl_score)

        self.lbl_readiness_caption = QLabel(self.kit_card)
        self.lbl_readiness_caption.setObjectName(u"lbl_readiness_caption")

        self.verticalLayout.addWidget(self.lbl_readiness_caption)

        self.widget_meta = QWidget(self.kit_card)
        self.widget_meta.setObjectName(u"widget_meta")
        self.formLayout = QFormLayout(self.widget_meta)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_weight_label = QLabel(self.widget_meta)
        self.lbl_weight_label.setObjectName(u"lbl_weight_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_weight_label)

        self.lbl_weight = QLabel(self.widget_meta)
        self.lbl_weight.setObjectName(u"lbl_weight")
        self.lbl_weight.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lbl_weight)

        self.lbl_modified_label = QLabel(self.widget_meta)
        self.lbl_modified_label.setObjectName(u"lbl_modified_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_modified_label)

        self.lbl_modified = QLabel(self.widget_meta)
        self.lbl_modified.setObjectName(u"lbl_modified")
        self.lbl_modified.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lbl_modified)


        self.verticalLayout.addWidget(self.widget_meta)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.footer = QFrame(self.kit_card)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_edit = QPushButton(self.footer)
        self.btn_edit.setObjectName(u"btn_edit")

        self.horizontalLayout.addWidget(self.btn_edit)

        self.btn_copy = QPushButton(self.footer)
        self.btn_copy.setObjectName(u"btn_copy")

        self.horizontalLayout.addWidget(self.btn_copy)

        self.btn_delete = QPushButton(self.footer)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout.addWidget(self.btn_delete)


        self.verticalLayout.addWidget(self.footer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"Kit Name", None))
        self.lbl_score.setText(QCoreApplication.translate("Form", u"31%", None))
        self.lbl_readiness_caption.setText(QCoreApplication.translate("Form", u"READINESS", None))
        self.lbl_weight_label.setText(QCoreApplication.translate("Form", u"Weight", None))
        self.lbl_weight.setText(QCoreApplication.translate("Form", u"1.2 kg / 5 kg", None))
        self.lbl_modified_label.setText(QCoreApplication.translate("Form", u"Last modified", None))
        self.lbl_modified.setText(QCoreApplication.translate("Form", u"15 April 2026", None))
        self.btn_edit.setText(QCoreApplication.translate("Form", u"\u270e Edit", None))
        self.btn_copy.setText(QCoreApplication.translate("Form", u"\u29c9 Copy", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"\U0001f5d1 Delete", None))
    # retranslateUi

