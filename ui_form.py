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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Question:
    def __init__(self, question_text, option1_text, option2_text):
        self.question_text = question_text
        self.option1_text = option1_text
        self.option2_text = option2_text

        self.radio_button_1 = QRadioButton(self.option1_text)
        self.radio_button_2 = QRadioButton(self.option2_text)

        self.label = QLabel(self.question_text)

class Ui_Widget(object):
    def __init__(self) -> None:
        self.current_set_index = 0
        self.question_sets = self.create_question_sets()
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1078, 552)
        
        self.question_widgets = []
        
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(280, 10, 521, 101))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 0, 391, 61))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 481, 41))
        self.Questions_g = QGroupBox(Widget)
        self.Questions_g.setObjectName(u"Questions_g")
        self.Questions_g.setGeometry(QRect(240, 200, 601, 271))
        
        self.q1_g = QGroupBox(self.Questions_g)
        self.q1_g.setObjectName(u"q1_g")
        self.q1_g.setGeometry(QRect(20, 60, 561, 41))
        self.q1_most = QRadioButton(self.q1_g)
        self.q1_most.setObjectName(u"q1_most")
        self.q1_most.setGeometry(QRect(20, 10, 21, 24))
        self.q1_least = QRadioButton(self.q1_g)
        self.q1_least.setObjectName(u"q1_least")
        self.q1_least.setGeometry(QRect(530, 10, 21, 24))
        self.q1_l = QLabel(self.q1_g)
        self.q1_l.setObjectName(u"q1_l")
        self.q1_l.setGeometry(QRect(30, 10, 501, 21))
        
        self.question_widgets.append({
            "radio1": self.q1_most,
            "radio2": self.q1_least,
            "label": self.q1_l
        })
        
        self.Requirements_L = QLabel(self.Questions_g)
        self.Requirements_L.setObjectName(u"Requirements_L")
        self.Requirements_L.setGeometry(QRect(220, 20, 151, 18))
        
        self.q2_g = QGroupBox(self.Questions_g)
        self.q2_g.setObjectName(u"q2_g")
        self.q2_g.setGeometry(QRect(20, 110, 561, 41))
        self.q2_most = QRadioButton(self.q2_g)
        self.q2_most.setObjectName(u"q2_most")
        self.q2_most.setGeometry(QRect(20, 10, 21, 24))
        self.q2_least = QRadioButton(self.q2_g)
        self.q2_least.setObjectName(u"q2_least")
        self.q2_least.setGeometry(QRect(530, 10, 21, 24))
        self.q2_l = QLabel(self.q2_g)
        self.q2_l.setObjectName(u"q2_l")
        self.q2_l.setGeometry(QRect(30, 10, 501, 21))
        
        self.question_widgets.append({
            "radio1": self.q2_most,
            "radio2": self.q2_least,
            "label": self.q2_l
        })
        
        self.q3_g = QGroupBox(self.Questions_g)
        self.q3_g.setObjectName(u"q3_g")
        self.q3_g.setGeometry(QRect(20, 160, 561, 41))
        self.q3_most = QRadioButton(self.q3_g)
        self.q3_most.setObjectName(u"q3_most")
        self.q3_most.setGeometry(QRect(20, 10, 21, 24))
        self.q3_least = QRadioButton(self.q3_g)
        self.q3_least.setObjectName(u"q3_least")
        self.q3_least.setGeometry(QRect(530, 10, 21, 24))
        self.q3_l = QLabel(self.q3_g)
        self.q3_l.setObjectName(u"q3_l")
        self.q3_l.setGeometry(QRect(30, 10, 501, 21))
        
        self.question_widgets.append({
            "radio1": self.q3_most,
            "radio2": self.q3_least,
            "label": self.q3_l
        })
        
        self.q4_g = QGroupBox(self.Questions_g)
        self.q4_g.setObjectName(u"q4_g")
        self.q4_g.setGeometry(QRect(20, 210, 561, 41))
        self.q4_most = QRadioButton(self.q4_g)
        self.q4_most.setObjectName(u"q4_most")
        self.q4_most.setGeometry(QRect(20, 10, 21, 24))
        self.q4_least = QRadioButton(self.q4_g)
        self.q4_least.setObjectName(u"q4_least")
        self.q4_least.setGeometry(QRect(530, 10, 21, 24))
        self.q4_l = QLabel(self.q4_g)
        self.q4_l.setObjectName(u"q4_l")
        self.q4_l.setGeometry(QRect(30, 10, 501, 21))
        
        self.question_widgets.append({
            "radio1": self.q4_most,
            "radio2": self.q4_least,
            "label": self.q4_l
        })
        
        self.MostImportant_L = QLabel(self.Questions_g)
        self.MostImportant_L.setObjectName(u"MostImportant_L")
        self.MostImportant_L.setGeometry(QRect(0, 10, 81, 41))
        self.LeastImportant_L = QLabel(self.Questions_g)
        self.LeastImportant_L.setObjectName(u"LeastImportant_L")
        self.LeastImportant_L.setGeometry(QRect(520, 10, 81, 41))
        
        self.NextButton = QPushButton(Widget)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setGeometry(QRect(490, 480, 91, 26))
        self.NextButton.clicked.connect(self.next_question_set)
        
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(400, 510, 271, 23))
        self.progressBar.setValue(24)
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(240, 130, 601, 51))
        self.progressNumber = QLabel(Widget)
        self.progressNumber.setObjectName(u"progressNumber")
        self.progressNumber.setGeometry(QRect(240, 180, 58, 18))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\"font-size:20px;font-weight:700;\">Sawtooth Software - Demo Version</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">NOTE: The demo version is limited to 10 respondent data records</p></body></html>", None))
        self.Questions_g.setTitle("")
        self.q1_g.setTitle("")
        self.q1_most.setText("")
        self.q1_least.setText("")
        self.q1_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Taking over for an existing/retiring CEO and allow for smooth transition</p></body></html>", None))
        self.Requirements_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Requirements</span></p></body></html>", None))
        self.q2_g.setTitle("")
        self.q2_most.setText("")
        self.q2_least.setText("")
        self.q2_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Creating great followers through collaboration</p></body></html>", None))
        self.q3_g.setTitle("")
        self.q3_most.setText("")
        self.q3_least.setText("")
        self.q3_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Streamlining internal processes where productivity suffers</p></body></html>", None))
        self.q4_g.setTitle("")
        self.q4_most.setText("")
        self.q4_least.setText("")
        self.q4_l.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Selling a non-commoditized product unless it holds a significant market share</p></body></html>", None))
        self.MostImportant_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\" style=\"line-height: 0.25;\">Most</p><p align=\"center\">important</p></body></html>", None))
        self.LeastImportant_L.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\" style=\"line-height: 0.25;\">Least</p><p align=\"center\">important</p></body></html>", None))
        self.NextButton.setText(QCoreApplication.translate("Widget", u"Next", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p style=\"line-height: 0.35;\">Choose one item from the &quot;Most important&quot; column on the left and one item from the &quot;least</p><p>important&quot; column on the right. You are only allowed one response per column.</p></body></html>", None))
        self.progressNumber.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-weight:700;\">1 / 30</span></p></body></html>", None))
    # retranslateUi

    def create_question_sets(self):
        # Create question instances
        q1 = Question("Question 1", "Yes", "No")
        q2 = Question("Question 2", "True", "False")
        q3 = Question("Question 3", "Agree", "Disagree")
        q4 = Question("Question 4", "Option A", "Option B")
        q5 = Question("Question 5", "Option C", "Option D")
        q6 = Question("Question 6", "Option E", "Option F")

        # Define sets of questions (can have repeated questions)
        return [
            [q1, q2, q3, q4],
            [q1, q5, q6, q4],
            [q3, q5, q4, q2],
            [q1, q5, q3, q2],
            # Add more sets as needed
        ]

    def load_question_set(self, question_set):
        for i, question in enumerate(question_set):
            self.question_widgets[i]["label"].setText(question.question_text)
            # self.question_widgets[i]["radio1"].setText(question.option1_text)
            # self.question_widgets[i]["radio2"].setText(question.option2_text)

            # Clear previous selections
            self.question_widgets[i]["radio1"].setChecked(False)
            self.question_widgets[i]["radio2"].setChecked(False)

    def next_question_set(self):
        # Save or process selected answers if needed

        self.current_set_index += 1
        if self.current_set_index < len(self.question_sets):
            self.load_question_set(self.question_sets[self.current_set_index])
        else:
            print("No more questions.")
            # Handle end of questions, e.g., show results or submit data