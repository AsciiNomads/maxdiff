# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_bullets.ui'
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
        Form.resize(1017, 1084)
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
"\n"
"QLabel#title {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #1C2833; /* Darker, bold title */\n"
"    padding: 12px 0;\n"
"    background-color: #F7F9F9; /* S"
                        "lightly off-white background for the title */\n"
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
"    color: #E9ECEF; /* Light gray text */\n"
"    border: 1px solid #C3E6CB; /* Light green border when disabled */\n"
"}\n"
"\n"
""
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
"QPushButton#add_btn:hover {\n"
"    background-color: #218838; /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton#add_btn:pressed {\n"
"    background-color: #1E7E34; /* Even darker green when pressed */\n"
"    padding-top: 10px; /* Simulates button press effect */\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton#add_btn:disabled {\n"
"    background-color: #A9DFBF; /* Light green when disabled */\n"
"    color: #E9ECEF; /* Light gray text */\n"
"    border: 1px solid #C3E6CB; /* Light green border when disabled */\n"
"}\n"
"\n"
"/* Remove Button */\n"
"QPushButton#remove_btn {\n"
"    background-color: #DC3545; /* Modern red color for remove *"
                        "/\n"
"    color: #FFFFFF; /* White text */\n"
"    font-size: 16px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"    border-radius: 6px; /* Rounded corners */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#remove_btn:hover {\n"
"    background-color: #C82333; /* Darker red on hover */\n"
"}\n"
"\n"
"QPushButton#remove_btn:pressed {\n"
"    background-color: #A71D2A; /* Even darker red when pressed */\n"
"    padding-top: 10px; /* Simulates button press effect */\n"
"    padding-bottom: 6px;\n"
"}\n"
"\n"
"QPushButton#remove_btn:disabled {\n"
"    background-color: #F5B7B1; /* Light red when disabled */\n"
"    color: #F8F9FA; /* Light gray text */\n"
"    border: 1px solid #E6B0AA; /* Light red border when disabled */\n"
"}\n"
"")
        self.verticalLayout_38 = QVBoxLayout(Form)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.instruciton = QLabel(self.frame)
        self.instruciton.setObjectName(u"instruciton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.instruciton.sizePolicy().hasHeightForWidth())
        self.instruciton.setSizePolicy(sizePolicy)
        self.instruciton.setMinimumSize(QSize(0, 50))
        self.instruciton.setBaseSize(QSize(0, 100))

        self.verticalLayout_33.addWidget(self.instruciton)

        self.question_frame_1 = QFrame(self.frame)
        self.question_frame_1.setObjectName(u"question_frame_1")
        self.question_frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.question_frame_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.q1_title = QLabel(self.question_frame_1)
        self.q1_title.setObjectName(u"q1_title")

        self.verticalLayout_8.addWidget(self.q1_title)

        self.frame_2 = QFrame(self.question_frame_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.q1_bullets = QListWidget(self.frame_2)
        QListWidgetItem(self.q1_bullets)
        self.q1_bullets.setObjectName(u"q1_bullets")

        self.horizontalLayout.addWidget(self.q1_bullets)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_btn = QPushButton(self.frame_4)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)

        self.remove_btn = QPushButton(self.frame_4)
        self.remove_btn.setObjectName(u"remove_btn")

        self.verticalLayout.addWidget(self.remove_btn)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.frame_2)


        self.verticalLayout_33.addWidget(self.question_frame_1)

        self.question_frame_2 = QFrame(self.frame)
        self.question_frame_2.setObjectName(u"question_frame_2")
        self.question_frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.question_frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_6 = QLabel(self.question_frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.frame_5 = QFrame(self.question_frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget_2 = QListWidget(self.frame_5)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.horizontalLayout_4.addWidget(self.listWidget_2)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)


        self.horizontalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_9.addWidget(self.frame_5)


        self.verticalLayout_33.addWidget(self.question_frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)

        self.question_frame_15 = QFrame(self.frame)
        self.question_frame_15.setObjectName(u"question_frame_15")
        self.question_frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.question_frame_15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_23 = QLabel(self.question_frame_15)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_25.addWidget(self.label_23)

        self.frame_7 = QFrame(self.question_frame_15)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.listWidget_15 = QListWidget(self.frame_7)
        QListWidgetItem(self.listWidget_15)
        self.listWidget_15.setObjectName(u"listWidget_15")

        self.horizontalLayout_23.addWidget(self.listWidget_15)

        self.frame_33 = QFrame(self.frame_7)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_33)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.add_2 = QPushButton(self.frame_33)
        self.add_2.setObjectName(u"add_2")

        self.verticalLayout_30.addWidget(self.add_2)

        self.pushButton_36 = QPushButton(self.frame_33)
        self.pushButton_36.setObjectName(u"pushButton_36")

        self.verticalLayout_30.addWidget(self.pushButton_36)


        self.horizontalLayout_23.addWidget(self.frame_33)


        self.verticalLayout_25.addWidget(self.frame_7)


        self.verticalLayout_33.addWidget(self.question_frame_15)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_33.addWidget(self.frame_3)

        self.question_frame_16 = QFrame(self.frame)
        self.question_frame_16.setObjectName(u"question_frame_16")
        self.question_frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.question_frame_16)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_24 = QLabel(self.question_frame_16)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_31.addWidget(self.label_24)

        self.frame_39 = QFrame(self.question_frame_16)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.listWidget_16 = QListWidget(self.frame_39)
        QListWidgetItem(self.listWidget_16)
        self.listWidget_16.setObjectName(u"listWidget_16")

        self.horizontalLayout_24.addWidget(self.listWidget_16)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_40)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.pushButton_37 = QPushButton(self.frame_40)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.verticalLayout_32.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.frame_40)
        self.pushButton_38.setObjectName(u"pushButton_38")

        self.verticalLayout_32.addWidget(self.pushButton_38)


        self.horizontalLayout_24.addWidget(self.frame_40)


        self.verticalLayout_31.addWidget(self.frame_39)


        self.verticalLayout_33.addWidget(self.question_frame_16)

        self.question_frame_17 = QFrame(self.frame)
        self.question_frame_17.setObjectName(u"question_frame_17")
        self.question_frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.question_frame_17)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_25 = QLabel(self.question_frame_17)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_34.addWidget(self.label_25)

        self.frame_41 = QFrame(self.question_frame_17)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.listWidget_17 = QListWidget(self.frame_41)
        QListWidgetItem(self.listWidget_17)
        self.listWidget_17.setObjectName(u"listWidget_17")

        self.horizontalLayout_25.addWidget(self.listWidget_17)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_42)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.pushButton_39 = QPushButton(self.frame_42)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.verticalLayout_35.addWidget(self.pushButton_39)

        self.pushButton_40 = QPushButton(self.frame_42)
        self.pushButton_40.setObjectName(u"pushButton_40")

        self.verticalLayout_35.addWidget(self.pushButton_40)


        self.horizontalLayout_25.addWidget(self.frame_42)


        self.verticalLayout_34.addWidget(self.frame_41)


        self.verticalLayout_33.addWidget(self.question_frame_17)

        self.question_frame_18 = QFrame(self.frame)
        self.question_frame_18.setObjectName(u"question_frame_18")
        self.question_frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.question_frame_18)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_26 = QLabel(self.question_frame_18)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_36.addWidget(self.label_26)

        self.frame_43 = QFrame(self.question_frame_18)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.listWidget_18 = QListWidget(self.frame_43)
        QListWidgetItem(self.listWidget_18)
        self.listWidget_18.setObjectName(u"listWidget_18")

        self.horizontalLayout_26.addWidget(self.listWidget_18)

        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_44)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.pushButton_41 = QPushButton(self.frame_44)
        self.pushButton_41.setObjectName(u"pushButton_41")

        self.verticalLayout_37.addWidget(self.pushButton_41)

        self.pushButton_42 = QPushButton(self.frame_44)
        self.pushButton_42.setObjectName(u"pushButton_42")

        self.verticalLayout_37.addWidget(self.pushButton_42)


        self.horizontalLayout_26.addWidget(self.frame_44)


        self.verticalLayout_36.addWidget(self.frame_43)


        self.verticalLayout_33.addWidget(self.question_frame_18)

        self.confirm_btn = QPushButton(self.frame)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.verticalLayout_33.addWidget(self.confirm_btn)


        self.verticalLayout_38.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.instruciton.setText(QCoreApplication.translate("Form", u"select bullet", None))
        self.q1_title.setText(QCoreApplication.translate("Form", u"questions 1 ", None))

        __sortingEnabled = self.q1_bullets.isSortingEnabled()
        self.q1_bullets.setSortingEnabled(False)
        ___qlistwidgetitem = self.q1_bullets.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.q1_bullets.setSortingEnabled(__sortingEnabled)

        self.add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.remove_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"questions 2", None))

        __sortingEnabled1 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_2.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled1)

        self.pushButton_4.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"questions 3", None))

        __sortingEnabled2 = self.listWidget_15.isSortingEnabled()
        self.listWidget_15.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_15.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.listWidget_15.setSortingEnabled(__sortingEnabled2)

        self.add_2.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_36.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"questions 4", None))

        __sortingEnabled3 = self.listWidget_16.isSortingEnabled()
        self.listWidget_16.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_16.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.listWidget_16.setSortingEnabled(__sortingEnabled3)

        self.pushButton_37.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_38.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"questions 5", None))

        __sortingEnabled4 = self.listWidget_17.isSortingEnabled()
        self.listWidget_17.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.listWidget_17.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.listWidget_17.setSortingEnabled(__sortingEnabled4)

        self.pushButton_39.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_40.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"questions 6", None))

        __sortingEnabled5 = self.listWidget_18.isSortingEnabled()
        self.listWidget_18.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.listWidget_18.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"bullet 1 ", None));
        self.listWidget_18.setSortingEnabled(__sortingEnabled5)

        self.pushButton_41.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_42.setText(QCoreApplication.translate("Form", u"-", None))
        self.confirm_btn.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

