# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(844, 670)
        Form.setStyleSheet(u"/* ComboBox Style */\n"
"QComboBox {\n"
"    background-color: #FFFFFF; /* White background for the dropdown */\n"
"    border: 1px solid #D1D5DB; /* Light border to match other elements */\n"
"    border-radius: 6px; /* Slightly rounded corners for a modern look */\n"
"    padding: 8px 12px; /* Padding for inner content */\n"
"    color: #333333; /* Dark gray text for readability */\n"
"    font-size: 16px; /* Consistent font size */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #D1D5DB; /* Separate drop-down button with a light border */\n"
"    background-color: #F4F4F9; /* Light modern background for the drop-down button */\n"
"    width: 30px; /* Width of the drop-down button */\n"
"    padding: 5px; /* Padding inside the drop-down button */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down-arrow.png); /* Custom down arrow icon */\n"
"    width: 12px; /* Size of the arrow */\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FF"
                        "FFFF; /* White background for the dropdown list */\n"
"    border: 1px solid #D1D5DB; /* Light border for the list */\n"
"    padding: 8px; /* Padding around the items */\n"
"    selection-background-color: #3B82F6; /* Blue highlight for selected item */\n"
"    selection-color: white; /* White text on selected item */\n"
"    color: #333333; /* Dark gray text for list items */\n"
"}\n"
"\n"
"/* Global Styles */\n"
"QWidget {\n"
"    background-color: #F4F4F9; /* Light modern background */\n"
"    font-family: \"Arial\", sans-serif; /* Use a modern, clean font */\n"
"    color: #333333; /* Dark gray text for better visibility */\n"
"}\n"
"\n"
"/* Box Style */\n"
"QFrame#box {\n"
"    background-color: #FFFFFF; /* White box color */\n"
"    border: 1px solid #D1D5DB; /* Light border */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"    padding: 16px;\n"
"    margin: 8px;\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */\n"
"    color: #333333; /* Dark gray text inside the box */\n"
"}"
                        "\n"
"\n"
"/* Button Style */\n"
"QPushButton {\n"
"    background-color: #3B82F6; /* Blue background for the button */\n"
"    color: white; /* White text for visibility */\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    margin: 4px 0;\n"
"    font-weight: bold;\n"
"    transition: background-color 0.3s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563EB; /* Darker blue on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1D4ED8; /* Even darker blue on press */\n"
"}\n"
"\n"
"/* Title Style */\n"
"QLabel#title {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #111827; /* Darker color for the title to stand out on the light background */\n"
"    margin-bottom: 16px;\n"
"}\n"
"\n"
"/* Radio Button Style */\n"
"QRadioButton {\n"
"    font-size: 16px;\n"
"    color: #333333; /* Dark gray text for better visibility */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-rad"
                        "ius: 10px;\n"
"    border: 2px solid #3B82F6; /* Blue border */\n"
"    background-color: #FFFFFF; /* White background */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6; /* Blue dot when checked */\n"
"    border: 2px solid #2563EB; /* Darker blue border when checked */\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.export_frame = QHBoxLayout()
        self.export_frame.setSpacing(6)
        self.export_frame.setObjectName(u"export_frame")
        self.export_frame.setContentsMargins(-1, 0, -1, -1)
        self.exportData = QPushButton(Form)
        self.exportData.setObjectName(u"exportData")

        self.export_frame.addWidget(self.exportData)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.export_frame.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.export_frame)

        self.formWidget_2 = QWidget(Form)
        self.formWidget_2.setObjectName(u"formWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.formWidget_2.sizePolicy().hasHeightForWidth())
        self.formWidget_2.setSizePolicy(sizePolicy)
        self.formWidget_2.setMinimumSize(QSize(600, 600))
        self.formWidget_2.setMaximumSize(QSize(16777215, 600))
        self.formWidget_2.setBaseSize(QSize(400, 400))
        self.horizontalLayout = QHBoxLayout(self.formWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 35, -1, -1)
        self.plot_pic = QLabel(self.formWidget_2)
        self.plot_pic.setObjectName(u"plot_pic")
        self.plot_pic.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plot_pic.sizePolicy().hasHeightForWidth())
        self.plot_pic.setSizePolicy(sizePolicy1)
        self.plot_pic.setMinimumSize(QSize(400, 400))
        self.plot_pic.setBaseSize(QSize(600, 600))
        self.plot_pic.setAutoFillBackground(True)
        self.plot_pic.setPixmap(QPixmap(u":/newPrefix/images/wallhaven-01wzrv.jpg"))
        self.plot_pic.setScaledContents(True)

        self.horizontalLayout.addWidget(self.plot_pic)


        self.verticalLayout_2.addWidget(self.formWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.exportData.setText(QCoreApplication.translate("Form", u"export", None))
        self.plot_pic.setText("")
    # retranslateUi

