# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGroupBox,
    QLabel,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(1078, 552)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(280, 10, 521, 101))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(70, 0, 391, 61))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 50, 481, 41))
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setGeometry(QRect(240, 200, 601, 271))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 60, 561, 41))
        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setGeometry(QRect(20, 10, 21, 24))
        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setGeometry(QRect(530, 10, 21, 24))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(30, 10, 501, 21))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(220, 20, 151, 18))
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 110, 561, 41))
        self.radioButton_3 = QRadioButton(self.groupBox_4)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 10, 21, 24))
        self.radioButton_4 = QRadioButton(self.groupBox_4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setGeometry(QRect(530, 10, 21, 24))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(30, 10, 501, 21))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setGeometry(QRect(20, 160, 561, 41))
        self.radioButton_5 = QRadioButton(self.groupBox_5)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setGeometry(QRect(20, 10, 21, 24))
        self.radioButton_6 = QRadioButton(self.groupBox_5)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setGeometry(QRect(530, 10, 21, 24))
        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(30, 10, 501, 21))
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 210, 561, 41))
        self.radioButton_7 = QRadioButton(self.groupBox_6)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_7.setGeometry(QRect(20, 10, 21, 24))
        self.radioButton_8 = QRadioButton(self.groupBox_6)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_8.setGeometry(QRect(530, 10, 21, 24))
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(30, 10, 501, 21))
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(0, 10, 81, 41))
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(520, 10, 81, 41))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(490, 480, 91, 26))
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(400, 510, 271, 23))
        self.progressBar.setValue(24)
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName("label_10")
        self.label_10.setGeometry(QRect(240, 130, 601, 51))
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName("label_11")
        self.label_11.setGeometry(QRect(240, 180, 58, 18))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Widget", None))
        self.groupBox.setTitle("")
        self.label_7.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center"><span style="font-size:20px;font-weight:700;">Sawtooth Software - Demo Version</span></p></body></html>',
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center">NOTE: The demo version is limited to 10 respondent data records</p></body></html>',
                None,
            )
        )
        self.groupBox_2.setTitle("")
        self.groupBox_3.setTitle("")
        self.radioButton.setText("")
        self.radioButton_2.setText("")
        self.label_3.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center">Taking over for an existing/retiring CEO and allow for smooth transition</p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center"><span style=" font-weight:700;">Requirements</span></p></body></html>',
                None,
            )
        )
        self.groupBox_4.setTitle("")
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.label_4.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center">Creating great followers through collaboration</p></body></html>',
                None,
            )
        )
        self.groupBox_5.setTitle("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.label_5.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center">Streamlining internal processes where productivity suffers</p></body></html>',
                None,
            )
        )
        self.groupBox_6.setTitle("")
        self.radioButton_7.setText("")
        self.radioButton_8.setText("")
        self.label_6.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center">Selling a non-commoditized product unless it holds a significant market share</p></body></html>',
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center" style="line-height: 0.25;">Most</p><p align="center">important</p></body></html>',
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p align="center" style="line-height: 0.25;">Least</p><p align="center">important</p></body></html>',
                None,
            )
        )
        self.pushButton.setText(QCoreApplication.translate("Widget", "Next", None))
        self.label_10.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p style="line-height: 0.35;">Choose one item from the &quot;Most important&quot; column on the left and one item from the &quot;least</p><p>important&quot; column on the right. You are only allowed one response per column.</p></body></html>',
                None,
            )
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "Widget",
                '<html><head/><body><p><span style=" font-weight:700;">1 / 30</span></p></body></html>',
                None,
            )
        )

    # retranslateUi
