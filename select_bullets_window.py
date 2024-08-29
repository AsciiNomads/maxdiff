# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_bullets_window.ui'
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
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 763)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
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
        QListWidgetItem(self.q_bullets_1)
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
        QListWidgetItem(self.q_bullets_2)
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
        QListWidgetItem(self.q_bullets_3)
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
        QListWidgetItem(self.q_bullets_4)
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
        QListWidgetItem(self.q_bullets_5)
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
        QListWidgetItem(self.q_bullets_6)
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


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.instruciton.setText(QCoreApplication.translate("MainWindow", u"select bullet", None))
        self.q_title_1.setText(QCoreApplication.translate("MainWindow", u"questions 1 ", None))

        __sortingEnabled = self.q_bullets_1.isSortingEnabled()
        self.q_bullets_1.setSortingEnabled(False)
        ___qlistwidgetitem = self.q_bullets_1.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_1.setSortingEnabled(__sortingEnabled)

        self.add_btn_1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.q_title_2.setText(QCoreApplication.translate("MainWindow", u"questions 2", None))

        __sortingEnabled1 = self.q_bullets_2.isSortingEnabled()
        self.q_bullets_2.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.q_bullets_2.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_2.setSortingEnabled(__sortingEnabled1)

        self.add_btn_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.q_title_3.setText(QCoreApplication.translate("MainWindow", u"questions 3", None))

        __sortingEnabled2 = self.q_bullets_3.isSortingEnabled()
        self.q_bullets_3.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.q_bullets_3.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_3.setSortingEnabled(__sortingEnabled2)

        self.add_btn_3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.q_title_4.setText(QCoreApplication.translate("MainWindow", u"questions 4", None))

        __sortingEnabled3 = self.q_bullets_4.isSortingEnabled()
        self.q_bullets_4.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.q_bullets_4.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_4.setSortingEnabled(__sortingEnabled3)

        self.add_btn_4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.q_title_5.setText(QCoreApplication.translate("MainWindow", u"questions 5", None))

        __sortingEnabled4 = self.q_bullets_5.isSortingEnabled()
        self.q_bullets_5.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.q_bullets_5.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_5.setSortingEnabled(__sortingEnabled4)

        self.add_btn_5.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.q_title_6.setText(QCoreApplication.translate("MainWindow", u"questions 6", None))

        __sortingEnabled5 = self.q_bullets_6.isSortingEnabled()
        self.q_bullets_6.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.q_bullets_6.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"bullet 1 ", None));
        self.q_bullets_6.setSortingEnabled(__sortingEnabled5)

        self.add_btn_6.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.remove_btn_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.confirm_btn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
    # retranslateUi

