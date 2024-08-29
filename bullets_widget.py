import sys

# import csv
# import random

# import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog


from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QListWidget,
    QListWidgetItem,
    QButtonGroup,
)

# from utils.file_reader import read_questions
from select_bullets import Ui_Form


class Question:
    def __init__(self, question_text, _id):
        self.id = _id
        self.question_text = question_text
        self.question_html = (
            '<html><head/><body><p align="center">{}</p></body></html>'.format(
                self.question_text
            )
        )
        self.label = QLabel(self.question_text)
        self.most_preferred = 0
        self.least_preferred = 0
        self.total_proposed = 0
        self.more_preferred_than_listed = []
        self.less_preferred_than_listed = []

    def increment_and_update_as_most_preferred(self, compared_questions: list = []):
        self.most_preferred += 1

        for q in compared_questions:
            if q.id != self.id:
                self.more_preferred_than_listed.append(q)

    def increment_and_update_as_least_preferred(self, compared_questions: list = []):
        self.least_preferred += 1

        for q in compared_questions:
            if q.id != self.id:
                self.less_preferred_than_listed.append(q)

    def increment_total_proposed(self):
        self.total_proposed += 1

    def __str__(self) -> str:
        return f"{self.question_text}: Most: {self.most_preferred}, Least: {self.least_preferred}, Total: {self.total_proposed}"

    def __repr__(self) -> str:
        return self.__str__()


def generate_random_questions(number_of_questions: int):
    """this function is for testing purposes"""
    questions = []
    for i in range(number_of_questions):
        q = Question(f"Question {i + 1}" * 1, i)
        q.most_preferred = randint(1, 10)
        q.least_preferred = randint(1, 10)
        q.total_proposed = q.most_preferred + q.least_preferred + randint(1, 10)
        questions.append(q)

    return questions


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Main Window")
        # self.show_new_widget()
        self.resources_dir = "resources/"

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.question_sets = self.create_question_sets()
        self.current_set_index = 0

        self.setup_widget(self)

    def listWigetSetItem(
        self,
        list_widget,
        value=None,
        default_values=True,
    ):
        if default_values and value is None:
            value = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        else:
            value = value
        list_widget.addItems(value)

    def setup_widget(self, widget):
        list_widget = self.ui.q1_bullets

        # set default values
        self.listWigetSetItem(list_widget, value=["test"])

        list_widget.setEditTriggers(QListWidget.DoubleClicked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    # widget.exportWidget.show()
    widget.show()

    sys.exit(app.exec())
