# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1101, 716)
        Widget.setStyleSheet(u"/* Global Styles */\n"
"QWidget {\n"
"    background-color: #1E1E2F; /* Dark modern background */\n"
"    font-family: \"Arial\", sans-serif; /* Use a modern, clean font */\n"
"    color: #E5E7EB; /* Light gray text for better visibility */\n"
"}\n"
"\n"
"/* Box Style */\n"
"QFrame#box {\n"
"    background-color: #2D2D44; /* Darker box color */\n"
"    border: 1px solid #3E3E5C; /* Slightly lighter border */\n"
"    border-radius: 8px; /* Rounded corners */\n"
"    padding: 16px;\n"
"    margin: 8px;\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Stronger shadow */\n"
"    color: #E5E7EB; /* Light gray text inside the box */\n"
"}\n"
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
""
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
"    color: #FFFFFF; /* White color for the title to stand out on the dark background */\n"
"    margin-bottom: 16px;\n"
"}\n"
"\n"
"/* Radio Button Style */\n"
"QRadioButton {\n"
"    font-size: 16px;\n"
"    color: #E5E7EB; /* Light gray text for better visibility */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #3B82F6; /* Blue border */\n"
"    background-color: #2D2D44; /* Darker background */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #3B82F6; /* Blue dot when checked */\n"
"    border: 2px solid #2563EB; /* Darker blue border when checked */\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_10)


        self.verticalLayout.addWidget(self.frame_3)

        self.Questions_g = QGroupBox(self.frame)
        self.Questions_g.setObjectName(u"Questions_g")
        self.Questions_g.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.Questions_g)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.Questions_g)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LeastImportant_L = QLabel(self.frame_2)
        self.LeastImportant_L.setObjectName(u"LeastImportant_L")

        self.horizontalLayout_6.addWidget(self.LeastImportant_L)

        self.Requirements_L = QLabel(self.frame_2)
        self.Requirements_L.setObjectName(u"Requirements_L")

        self.horizontalLayout_6.addWidget(self.Requirements_L)

        self.MostImportant_L = QLabel(self.frame_2)
        self.MostImportant_L.setObjectName(u"MostImportant_L")

        self.horizontalLayout_6.addWidget(self.MostImportant_L)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.q1_g = QGroupBox(self.Questions_g)
        self.q1_g.setObjectName(u"q1_g")
        self.horizontalLayout = QHBoxLayout(self.q1_g)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.q1_most = QRadioButton(self.q1_g)
        self.q1_most.setObjectName(u"q1_most")

        self.horizontalLayout.addWidget(self.q1_most)

        self.q1_l = QLabel(self.q1_g)
        self.q1_l.setObjectName(u"q1_l")

        self.horizontalLayout.addWidget(self.q1_l)

        self.q1_least = QRadioButton(self.q1_g)
        self.q1_least.setObjectName(u"q1_least")

        self.horizontalLayout.addWidget(self.q1_least, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.q1_g)

        self.q2_g = QGroupBox(self.Questions_g)
        self.q2_g.setObjectName(u"q2_g")
        self.horizontalLayout_3 = QHBoxLayout(self.q2_g)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.q2_most = QRadioButton(self.q2_g)
        self.q2_most.setObjectName(u"q2_most")

        self.horizontalLayout_3.addWidget(self.q2_most)

        self.q2_l = QLabel(self.q2_g)
        self.q2_l.setObjectName(u"q2_l")

        self.horizontalLayout_3.addWidget(self.q2_l)

        self.q2_least = QRadioButton(self.q2_g)
        self.q2_least.setObjectName(u"q2_least")

        self.horizontalLayout_3.addWidget(self.q2_least, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.q2_g)

        self.q3_g = QGroupBox(self.Questions_g)
        self.q3_g.setObjectName(u"q3_g")
        self.horizontalLayout_4 = QHBoxLayout(self.q3_g)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.q3_most = QRadioButton(self.q3_g)
        self.q3_most.setObjectName(u"q3_most")

        self.horizontalLayout_4.addWidget(self.q3_most)

        self.q3_l = QLabel(self.q3_g)
        self.q3_l.setObjectName(u"q3_l")

        self.horizontalLayout_4.addWidget(self.q3_l)

        self.q3_least = QRadioButton(self.q3_g)
        self.q3_least.setObjectName(u"q3_least")

        self.horizontalLayout_4.addWidget(self.q3_least, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.q3_g)

        self.q4_g = QGroupBox(self.Questions_g)
        self.q4_g.setObjectName(u"q4_g")
        self.horizontalLayout_5 = QHBoxLayout(self.q4_g)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.q4_most = QRadioButton(self.q4_g)
        self.q4_most.setObjectName(u"q4_most")

        self.horizontalLayout_5.addWidget(self.q4_most)

        self.q4_l = QLabel(self.q4_g)
        self.q4_l.setObjectName(u"q4_l")

        self.horizontalLayout_5.addWidget(self.q4_l)

        self.q4_least = QRadioButton(self.q4_g)
        self.q4_least.setObjectName(u"q4_least")

        self.horizontalLayout_5.addWidget(self.q4_least, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.q4_g)


        self.verticalLayout.addWidget(self.Questions_g)

        self.NextButton = QPushButton(self.frame)
        self.NextButton.setObjectName(u"NextButton")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(11)
        font.setBold(True)
        self.NextButton.setFont(font)

        self.verticalLayout.addWidget(self.NextButton)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:20px; font-weight:700;\">Survey App  - Demo Version</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p style=\"line-height: 0.35;\">Choose one item from the &quot;Most important&quot; column on the left and one item from the &quot;least</p><p>important&quot; column on the right. You are only allowed one response per column.</p></body></html>", None))
        self.Questions_g.setTitle("")
        self.LeastImportant_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\" style=\"line-height: 0.25;\">Least</p><p align=\"center\">important</p></body></html>", None))
        self.Requirements_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Requirements</span></p></body></html>", None))
        self.MostImportant_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\" style=\"line-height: 0.25;\">Most</p><p align=\"center\">important</p></body></html>", None))
        self.q1_g.setTitle("")
        self.q1_most.setText("")
        self.q1_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Taking over for an existing/retiring CEO and allow for smooth transition</p></body></html>", None))
        self.q1_least.setText("")
        self.q2_g.setTitle("")
        self.q2_most.setText("")
        self.q2_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Creating great followers through collaboration</p></body></html>", None))
        self.q2_least.setText("")
        self.q3_g.setTitle("")
        self.q3_most.setText("")
        self.q3_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Streamlining internal processes where productivity suffers</p></body></html>", None))
        self.q3_least.setText("")
        self.q4_g.setTitle("")
        self.q4_most.setText("")
        self.q4_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Selling a non-commoditized product unless it holds a significant market share</p></body></html>", None))
        self.q4_least.setText("")
        self.NextButton.setText(QCoreApplication.translate("Widget", u"Next", None))
    # retranslateUi

