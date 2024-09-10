# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_bullets_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1017, 962)
        Form.setStyleSheet(u"/* Modern Light Theme */\n"
"\n"
"/* Style for QCheckBox */\n"
"QCheckBox {\n"
"    font-size: 14px;\n"
"    color: #2C3E50; /* Slightly darker text for better readability */\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 1px solid #BDC3C7; /* Light gray border */\n"
"    background-color: #ECF0F1; /* Light background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #D5DBDB; /* Slightly darker on hover */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #3498DB; /* Blue color when checked */\n"
"    border: none;\n"
"}\n"
"\n"
"/* Style for QTabWidget */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #D6DBDF; /* Light border around the tab content */\n"
"    background-color: #FAFAFA; /* Light background */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #F2F3F4; /* Light gray background for tabs */\n"
"    border: 1px solid #D6DBDF;\n"
"    padd"
                        "ing: 8px 20px;\n"
"    margin-right: 3px;\n"
"    font-size: 14px;\n"
"    color: #2C3E50; /* Darker text color for better contrast */\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #FFFFFF; /* White background for the selected tab */\n"
"    color: #1A5276; /* Darker blue for selected tab text */\n"
"    border-bottom-color: transparent; /* Removes the bottom border of the selected tab */\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #E5E8E8; /* Light gray on hover */\n"
"}\n"
"\n"
"/* Style for QLabel */\n"
"QLabel {\n"
"    font-size: 14px;\n"
"\n"
"    color: #34495E; /* Darker text color */\n"
"    padding: 6px;\n"
"    /* background-color: #FFFFFF; /* White background for a clean look */\n"
"	background-color: None; \n"
"}\n"
"QLabel#bullet_num {\n"
"    font-size: 13px;\n"
"	color: #777;\n"
"}\n"
"QLabel#instruciton {\n"
"    font-size: 22px;\n"
"}\n"
"\n"
"QLabel#title {\n"
"    font-size: 18px;\n"
"    fon"
                        "t-weight: bold;\n"
"    color: #1C2833; /* Darker, bold title */\n"
"    padding: 12px 0;\n"
"    background-color: #F7F9F9; /* Slightly off-white background for the title */\n"
"}\n"
"/* Modern Green Confirm Button */\n"
"\n"
"QPushButton#confirm_btn {\n"
"    background-color: #28A745; /* Modern green color */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-size: 16px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#confirm_btn:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton#confirm_btn:pressed {\n"
"    background-color: #1E7E34; /* Even darker green when pressed */\n"
"    padding-top: 10px; /* Slightly shifts down when pressed for a tactile effect */\n"
"    padding-bottom: 6px; /* Compensates for the shift */\n"
"}\n"
"\n"
"QPushButton#confirm_btn:disabled {\n"
"    background-color: #A9DFBF; /* Light green when disabled */\n"
""
                        "    color: #E9ECEF; /* Light gray text */\n"
"    border: 1px solid #C3E6CB; /* Light green border when disabled */\n"
"}\n"
"\n"
"/* -------------------------------- */\n"
"/* Add Button */\n"
"QPushButton#add_btn {\n"
"    background-color: #28A745; /* Modern green color for add */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-size: 16px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 6px; /* Rounded corners */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* ----------------------------------------*/\n"
"/* Add Button */\n"
"QPushButton#add_btn_1,\n"
"QPushButton#add_btn_2,\n"
"QPushButton#add_btn_3,\n"
"QPushButton#add_btn_4,\n"
"QPushButton#add_btn_5,\n"
"QPushButton#add_btn_6,\n"
"QPushButton#add_btn_7 {\n"
"    background-color: #28A745; /* Modern green color for add */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-size: 16px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 6px; /* Rounded corners */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"Q"
                        "PushButton#add_btn_1:hover,\n"
"QPushButton#add_btn_2:hover,\n"
"QPushButton#add_btn_3:hover,\n"
"QPushButton#add_btn_4:hover,\n"
"QPushButton#add_btn_5:hover,\n"
"QPushButton#add_btn_6:hover,\n"
"QPushButton#add_btn_7:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton#add_btn_1:pressed,\n"
"QPushButton#add_btn_2:pressed,\n"
"QPushButton#add_btn_3:pressed,\n"
"QPushButton#add_btn_4:pressed,\n"
"QPushButton#add_btn_5:pressed,\n"
"QPushButton#add_btn_6:pressed,\n"
"QPushButton#add_btn_7:pressed {\n"
"    background-color: #1E7E34; /* Even darker green when pressed */\n"
"    padding-top: 10px; /* Simulates button press effect */\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"\n"
"/* Remove Button */\n"
"QPushButton#remove_btn_1,\n"
"QPushButton#remove_btn_2,\n"
"QPushButton#remove_btn_3,\n"
"QPushButton#remove_btn_4,\n"
"QPushButton#remove_btn_5,\n"
"QPushButton#remove_btn_6,\n"
"QPushButton#remove_btn_7 {\n"
"    background-color: #DC3545; /* Modern red color for remo"
                        "ve */\n"
"    color: #FFFFFF; /* White text */\n"
"    font-size: 16px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 6px; /* Rounded corners */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#remove_btn_1:hover,\n"
"QPushButton#remove_btn_2:hover,\n"
"QPushButton#remove_btn_3:hover,\n"
"QPushButton#remove_btn_4:hover,\n"
"QPushButton#remove_btn_5:hover,\n"
"QPushButton#remove_btn_6:hover,\n"
"QPushButton#remove_btn_7:hover {\n"
"    background-color: #C82333; /* Darker red on hover */\n"
"}\n"
"\n"
"QPushButton#remove_btn_1:pressed,\n"
"QPushButton#remove_btn_2:pressed,\n"
"QPushButton#remove_btn_3:pressed,\n"
"QPushButton#remove_btn_4:pressed,\n"
"QPushButton#remove_btn_5:pressed,\n"
"QPushButton#remove_btn_6:pressed,\n"
"QPushButton#remove_btn_7:pressed {\n"
"    background-color: #BD2130; /* Even darker red when pressed */\n"
"    padding-top: 10px; /* Simulates button press effect */\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"    backgrou"
                        "nd-color: transparent; /* Optional: If you want a transparent background */\n"
"}\n"
"\n"
"QFrame#question_frame_1,\n"
"QFrame#question_frame_2,\n"
"QFrame#question_frame_3,\n"
"QFrame#question_frame_4,\n"
"QFrame#question_frame_5,\n"
"QFrame#question_frame_6 {\n"
"    border: none; /* Removes all borders */\n"
"    border-bottom: 2px solid #000000; /* Adds a 2px solid blue bottom border */\n"
"    background-color: transparent; /* Optional: Set the background color to transparent */\n"
"    border-radius: 0px; /* Ensures no rounded corners at the bottom */\n"
"}\n"
"QListWidget::item:selected:active {\n"
"    background-color: white; /* Set highlight color to white during editing */\n"
"    color: black; /* Change text color to black for visibility */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #3B82F6; /* Keep the normal selected item highlight color */\n"
"    color: white; /* Normal selected text color */\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(Form)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.instruciton = QLabel(self.frame_2)
        self.instruciton.setObjectName(u"instruciton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instruciton.sizePolicy().hasHeightForWidth())
        self.instruciton.setSizePolicy(sizePolicy)
        self.instruciton.setMinimumSize(QSize(0, 50))
        self.instruciton.setBaseSize(QSize(0, 100))
        font = QFont()
        font.setBold(True)
        self.instruciton.setFont(font)

        self.verticalLayout_3.addWidget(self.instruciton)

        self.bullet_num = QLabel(self.frame_2)
        self.bullet_num.setObjectName(u"bullet_num")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.bullet_num.setFont(font1)

        self.verticalLayout_3.addWidget(self.bullet_num)


        self.verticalLayout_33.addWidget(self.frame_2)

        self.question_frame_1 = QFrame(self.frame)
        self.question_frame_1.setObjectName(u"question_frame_1")
        self.question_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.question_frame_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.q_title_1 = QLabel(self.question_frame_1)
        self.q_title_1.setObjectName(u"q_title_1")

        self.verticalLayout_8.addWidget(self.q_title_1)

        self.frame_1_1 = QFrame(self.question_frame_1)
        self.frame_1_1.setObjectName(u"frame_1_1")
        self.frame_1_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_1_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_1 = QListWidget(self.frame_1_1)
        self.q_bullets_1.setObjectName(u"q_bullets_1")

        self.horizontalLayout.addWidget(self.q_bullets_1)

        self.frame_1_2 = QFrame(self.frame_1_1)
        self.frame_1_2.setObjectName(u"frame_1_2")
        self.frame_1_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_1_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_btn_1 = QPushButton(self.frame_1_2)
        self.add_btn_1.setObjectName(u"add_btn_1")
        self.add_btn_1.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.add_btn_1)

        self.remove_btn_1 = QPushButton(self.frame_1_2)
        self.remove_btn_1.setObjectName(u"remove_btn_1")

        self.verticalLayout.addWidget(self.remove_btn_1)


        self.horizontalLayout.addWidget(self.frame_1_2)


        self.verticalLayout_8.addWidget(self.frame_1_1)


        self.verticalLayout_33.addWidget(self.question_frame_1)

        self.question_frame_2 = QFrame(self.frame)
        self.question_frame_2.setObjectName(u"question_frame_2")
        self.question_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.question_frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.q_title_2 = QLabel(self.question_frame_2)
        self.q_title_2.setObjectName(u"q_title_2")

        self.verticalLayout_9.addWidget(self.q_title_2)

        self.frame_2_1 = QFrame(self.question_frame_2)
        self.frame_2_1.setObjectName(u"frame_2_1")
        self.frame_2_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2_1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_2 = QListWidget(self.frame_2_1)
        self.q_bullets_2.setObjectName(u"q_bullets_2")

        self.horizontalLayout_4.addWidget(self.q_bullets_2)

        self.frame_2_2 = QFrame(self.frame_2_1)
        self.frame_2_2.setObjectName(u"frame_2_2")
        self.frame_2_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_btn_2 = QPushButton(self.frame_2_2)
        self.add_btn_2.setObjectName(u"add_btn_2")

        self.verticalLayout_2.addWidget(self.add_btn_2)

        self.remove_btn_2 = QPushButton(self.frame_2_2)
        self.remove_btn_2.setObjectName(u"remove_btn_2")

        self.verticalLayout_2.addWidget(self.remove_btn_2)


        self.horizontalLayout_4.addWidget(self.frame_2_2)


        self.verticalLayout_9.addWidget(self.frame_2_1)


        self.verticalLayout_33.addWidget(self.question_frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)

        self.question_frame_3 = QFrame(self.frame)
        self.question_frame_3.setObjectName(u"question_frame_3")
        self.question_frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.question_frame_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.q_title_3 = QLabel(self.question_frame_3)
        self.q_title_3.setObjectName(u"q_title_3")

        self.verticalLayout_25.addWidget(self.q_title_3)

        self.frame_3_1 = QFrame(self.question_frame_3)
        self.frame_3_1.setObjectName(u"frame_3_1")
        self.frame_3_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_3_1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_3 = QListWidget(self.frame_3_1)
        self.q_bullets_3.setObjectName(u"q_bullets_3")

        self.horizontalLayout_23.addWidget(self.q_bullets_3)

        self.frame_3_2 = QFrame(self.frame_3_1)
        self.frame_3_2.setObjectName(u"frame_3_2")
        self.frame_3_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_3_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.add_btn_3 = QPushButton(self.frame_3_2)
        self.add_btn_3.setObjectName(u"add_btn_3")

        self.verticalLayout_30.addWidget(self.add_btn_3)

        self.remove_btn_3 = QPushButton(self.frame_3_2)
        self.remove_btn_3.setObjectName(u"remove_btn_3")

        self.verticalLayout_30.addWidget(self.remove_btn_3)


        self.horizontalLayout_23.addWidget(self.frame_3_2)


        self.verticalLayout_25.addWidget(self.frame_3_1)


        self.verticalLayout_33.addWidget(self.question_frame_3)

        self.question_frame_4 = QFrame(self.frame)
        self.question_frame_4.setObjectName(u"question_frame_4")
        self.question_frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.question_frame_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, 0, -1, 0)
        self.q_title_4 = QLabel(self.question_frame_4)
        self.q_title_4.setObjectName(u"q_title_4")

        self.verticalLayout_31.addWidget(self.q_title_4)

        self.frame_4_1 = QFrame(self.question_frame_4)
        self.frame_4_1.setObjectName(u"frame_4_1")
        self.frame_4_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_4_1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_4 = QListWidget(self.frame_4_1)
        self.q_bullets_4.setObjectName(u"q_bullets_4")

        self.horizontalLayout_24.addWidget(self.q_bullets_4)

        self.frame_4_2 = QFrame(self.frame_4_1)
        self.frame_4_2.setObjectName(u"frame_4_2")
        self.frame_4_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_4_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.add_btn_4 = QPushButton(self.frame_4_2)
        self.add_btn_4.setObjectName(u"add_btn_4")

        self.verticalLayout_32.addWidget(self.add_btn_4)

        self.remove_btn_4 = QPushButton(self.frame_4_2)
        self.remove_btn_4.setObjectName(u"remove_btn_4")

        self.verticalLayout_32.addWidget(self.remove_btn_4)


        self.horizontalLayout_24.addWidget(self.frame_4_2)


        self.verticalLayout_31.addWidget(self.frame_4_1)


        self.verticalLayout_33.addWidget(self.question_frame_4)

        self.question_frame_5 = QFrame(self.frame)
        self.question_frame_5.setObjectName(u"question_frame_5")
        self.question_frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.question_frame_5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 0, -1, 0)
        self.q_title_5 = QLabel(self.question_frame_5)
        self.q_title_5.setObjectName(u"q_title_5")

        self.verticalLayout_34.addWidget(self.q_title_5)

        self.frame_5_1 = QFrame(self.question_frame_5)
        self.frame_5_1.setObjectName(u"frame_5_1")
        self.frame_5_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_5_1)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_5 = QListWidget(self.frame_5_1)
        self.q_bullets_5.setObjectName(u"q_bullets_5")

        self.horizontalLayout_25.addWidget(self.q_bullets_5)

        self.frame_5_2 = QFrame(self.frame_5_1)
        self.frame_5_2.setObjectName(u"frame_5_2")
        self.frame_5_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_5_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.add_btn_5 = QPushButton(self.frame_5_2)
        self.add_btn_5.setObjectName(u"add_btn_5")

        self.verticalLayout_35.addWidget(self.add_btn_5)

        self.remove_btn_5 = QPushButton(self.frame_5_2)
        self.remove_btn_5.setObjectName(u"remove_btn_5")

        self.verticalLayout_35.addWidget(self.remove_btn_5)


        self.horizontalLayout_25.addWidget(self.frame_5_2)


        self.verticalLayout_34.addWidget(self.frame_5_1)


        self.verticalLayout_33.addWidget(self.question_frame_5)

        self.question_frame_6 = QFrame(self.frame)
        self.question_frame_6.setObjectName(u"question_frame_6")
        self.question_frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.question_frame_6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 0, -1, 0)
        self.q_title_6 = QLabel(self.question_frame_6)
        self.q_title_6.setObjectName(u"q_title_6")

        self.verticalLayout_36.addWidget(self.q_title_6)

        self.frame_6_1 = QFrame(self.question_frame_6)
        self.frame_6_1.setObjectName(u"frame_6_1")
        self.frame_6_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_6_1)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.q_bullets_6 = QListWidget(self.frame_6_1)
        self.q_bullets_6.setObjectName(u"q_bullets_6")

        self.horizontalLayout_26.addWidget(self.q_bullets_6)

        self.frame_6_2 = QFrame(self.frame_6_1)
        self.frame_6_2.setObjectName(u"frame_6_2")
        self.frame_6_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_6_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.add_btn_6 = QPushButton(self.frame_6_2)
        self.add_btn_6.setObjectName(u"add_btn_6")

        self.verticalLayout_37.addWidget(self.add_btn_6)

        self.remove_btn_6 = QPushButton(self.frame_6_2)
        self.remove_btn_6.setObjectName(u"remove_btn_6")

        self.verticalLayout_37.addWidget(self.remove_btn_6)


        self.horizontalLayout_26.addWidget(self.frame_6_2)


        self.verticalLayout_36.addWidget(self.frame_6_1)


        self.verticalLayout_33.addWidget(self.question_frame_6)

        self.confirm_btn = QPushButton(self.frame)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.verticalLayout_33.addWidget(self.confirm_btn)


        self.verticalLayout_38.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Change the questions", None))
        self.instruciton.setText(QCoreApplication.translate("Form", u"Select bullet", None))
        self.bullet_num.setText(QCoreApplication.translate("Form", u"Number of bullets: ", None))
        self.q_title_1.setText(QCoreApplication.translate("Form", u"questions 1 ", None))
        self.add_btn_1.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_1.setText(QCoreApplication.translate("Form", u"-", None))
        self.q_title_2.setText(QCoreApplication.translate("Form", u"questions 2", None))
        self.add_btn_2.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.q_title_3.setText(QCoreApplication.translate("Form", u"questions 3", None))
        self.add_btn_3.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_3.setText(QCoreApplication.translate("Form", u"-", None))
        self.q_title_4.setText(QCoreApplication.translate("Form", u"questions 4", None))
        self.add_btn_4.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_4.setText(QCoreApplication.translate("Form", u"-", None))
        self.q_title_5.setText(QCoreApplication.translate("Form", u"questions 5", None))
        self.add_btn_5.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_5.setText(QCoreApplication.translate("Form", u"-", None))
        self.q_title_6.setText(QCoreApplication.translate("Form", u"questions 6", None))
        self.add_btn_6.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn_6.setText(QCoreApplication.translate("Form", u"-", None))
        self.confirm_btn.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

