# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kit_list.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_bar = QWidget(Form)
        self.header_bar.setObjectName(u"header_bar")
        self.header_bar.setMinimumSize(QSize(0, 60))
        self.header_bar.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout = QHBoxLayout(self.header_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.header_title_container = QWidget(self.header_bar)
        self.header_title_container.setObjectName(u"header_title_container")
        self.verticalLayout_header = QVBoxLayout(self.header_title_container)
        self.verticalLayout_header.setObjectName(u"verticalLayout_header")
        self.verticalLayout_header.setContentsMargins(-1, 0, -1, 0)
        self.lbl_title = QLabel(self.header_title_container)
        self.lbl_title.setObjectName(u"lbl_title")

        self.verticalLayout_header.addWidget(self.lbl_title)

        self.lbl_subtitle = QLabel(self.header_title_container)
        self.lbl_subtitle.setObjectName(u"lbl_subtitle")

        self.verticalLayout_header.addWidget(self.lbl_subtitle)


        self.horizontalLayout.addWidget(self.header_title_container)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_new_kit = QPushButton(self.header_bar)
        self.btn_new_kit.setObjectName(u"btn_new_kit")

        self.horizontalLayout.addWidget(self.btn_new_kit)


        self.verticalLayout.addWidget(self.header_bar)

        self.content = QWidget(Form)
        self.content.setObjectName(u"content")
        self.contentLayout = QVBoxLayout(self.content)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(48, 32, 48, 32)
        self.lbl_section_title = QLabel(self.content)
        self.lbl_section_title.setObjectName(u"lbl_section_title")

        self.contentLayout.addWidget(self.lbl_section_title)

        self.scroll_area = QScrollArea(self.content)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.cards_container = QWidget()
        self.cards_container.setObjectName(u"cards_container")
        self.cards_container.setGeometry(QRect(0, 0, 380, 214))
        self.gridLayout = QGridLayout(self.cards_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(16)
        self.scroll_area.setWidget(self.cards_container)

        self.contentLayout.addWidget(self.scroll_area)


        self.verticalLayout.addWidget(self.content)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_title.setText(QCoreApplication.translate("Form", u"KitForge", None))
        self.lbl_subtitle.setText(QCoreApplication.translate("Form", u"Emergency Kit Planner", None))
        self.btn_new_kit.setText(QCoreApplication.translate("Form", u"+ New Kit", None))
        self.lbl_section_title.setText(QCoreApplication.translate("Form", u"YOUR KITS", None))
    # retranslateUi

