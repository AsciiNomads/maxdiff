# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(400, 200))
        Dialog.setMaximumSize(QSize(400, 200))
        Dialog.setBaseSize(QSize(200, 200))
        Dialog.setStyleSheet(u"QPushButton {\n"
"    background-color:  #3B82F6; /* Light grey background */\n"
"    color: white; /* Dark grey text */\n"
"    font-size: 12px;\n"
"    padding: 10px 20px;\n"
"    border: 1px solid #D0D0D0; /* Light border */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"    font-weight: 500; /* Medium font weight */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563EB; /* Slightly darker grey on hover */\n"
"    border-color: #C0C0C0; /* Darker border on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1D4ED8; /* Darker grey when pressed */\n"
"    border-color: #A0A0A0; /* Even darker border when pressed */\n"
"    padding-top: 12px; /* Simulates button press effect */\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F5F5F5; /* Very light grey when disabled */\n"
"    color: #B0B0B0; /* Light grey text for disabled state */\n"
"    border-color: #E0E0E0; /* Light grey border for disabled state */\n"
"}\n"
"QFrame {"
                        "\n"
"    border: none;\n"
"    background-color: transparent; /* Optional: If you want a transparent background */\n"
"}\n"
"")
        Dialog.setSizeGripEnabled(False)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(400, 100))
        self.label.setBaseSize(QSize(0, 100))
        self.label.setStyleSheet(u"font: 14pt \"Sans Serif\";")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.start_btn = QPushButton(self.frame_2)
        self.start_btn.setObjectName(u"start_btn")

        self.horizontalLayout.addWidget(self.start_btn)

        self.change_btn = QPushButton(self.frame_2)
        self.change_btn.setObjectName(u"change_btn")

        self.horizontalLayout.addWidget(self.change_btn)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Choose an Option", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select Survey", None))
        self.start_btn.setText(QCoreApplication.translate("Dialog", u"Start Survey", None))
        self.change_btn.setText(QCoreApplication.translate("Dialog", u"Change Questions", None))
    # retranslateUi

