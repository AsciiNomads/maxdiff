import sys

# import csv
# import random

# import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
from PySide6.QtCore import Qt


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

    def set_editable_items(self, list_widget):
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def listWigetSetItem(
        self,
        l_w,
        value=None,
        default_values=True,
    ):
        if default_values and value is None:
            value = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        else:
            value = value

        # list_widget = btn.parent().parent().findChild(QListWidget)
        list_widget = l_w
        list_widget.addItems(value)
        self.set_editable_items(list_widget)

    # def delete_item(self, btn, list_widget):
    def removeItem(self, l_w):
        list_widget = l_w
        # list_widget = btn.parent().parent().findChild(QListWidget)

        if list_widget:
            for item in list_widget.selectedItems():
                list_widget.takeItem(list_widget.row(item))
        else:
            print("QListWidget not found")

    def connet_buttons(self):
        # Find all QPushButton widgets
        buttons = self.findChildren(QPushButton)
        list_widgets = self.findChildren(QListWidget)
        # print(list_widgets[0])
        list_widgets_counter = 0
        for button in buttons:
            # print(button.text())
            if list_widgets_counter >= 2:
                try:
                    list_widgets.pop(0)
                except:
                    pass
            if button.text() == "+":
                button.clicked.connect(
                    lambda: self.listWigetSetItem(list_widgets[1], value=["new item"])
                )
                list_widgets_counter += 1
            elif button.text() == "-":
                button.clicked.connect(lambda: self.removeItem(list_widgets[1]))
                list_widgets_counter += 1

    def setup_widget(self, widget):
        # list_widget = self.ui.q1_bullets

        self.connet_buttons()

        # set default values
        # self.listWigetSetItem(list_widget)
        # self.ui.add_btn.clicked.connect(
        #     lambda: self.listWigetSetItem(list_widget, value=["new item"])
        # )
        # self.ui.remove_btn.clicked.connect(lambda: self.removeItem(list_widget))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    # widget.exportWidget.show()
    widget.show()

    sys.exit(app.exec())
