import sys

import csv

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

from utils.file_io import write_lines
from select_bullets import Ui_Form
from widget import Widget as wg
import ui_form
from QuestionBullets import QuestionBullets

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Main Window")
        # self.show_new_widget()
        self.resources_dir = "resources/"

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_widget(self)
        self.bullets = []
        self.all_bullets = []
        self.ui.confirm_btn.clicked.connect(
            lambda: self.get_all_list_widgets_items(in_one_list=True)
        )

    def set_editable_items(self, list_widget):
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            item.setFlags(item.flags() | Qt.ItemIsEditable)

    def listWidgetSetItem(
        self,
        l_w,
        value=None,
        default_values=True,
    ):
        if default_values and value is None:
            value = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        else:
            value = value

        list_widget = l_w
        list_widget.addItems(value)
        self.set_editable_items(list_widget)

    # def delete_item(self, btn, list_widget):
    def removeItem(self, l_w):
        list_widget = l_w

        if list_widget:
            for item in list_widget.selectedItems():
                list_widget.takeItem(list_widget.row(item))
        else:
            print("QListWidget not found")

    def setup_widget(self, widget):
        # set default for listwidget
        self.question_bullet_dict = {}
        for i in range(1, 7):
            tmp = {}
            list_widget = getattr(self.ui, f"q_bullets_{i}")

            self.set_editable_items(list_widget)

            add_btn = getattr(self.ui, f"add_btn_{i}")
            remove_btn = getattr(self.ui, f"remove_btn_{i}")

            tmp["add_btn"] = add_btn
            tmp["remove_btn"] = remove_btn
            tmp["list_widget"] = list_widget
            self.question_bullet_dict[i] = tmp

            # Use a helper function to capture the current list_widget correctly
            add_btn.clicked.connect(self._make_add_item_lambda(list_widget))
            remove_btn.clicked.connect(self._make_remove_item_lambda(list_widget))

    def _make_add_item_lambda(self, list_widget):
        """Returns a lambda that correctly captures the list_widget."""
        return lambda: self.listWidgetSetItem(list_widget, value=["new item"])

    def _make_remove_item_lambda(self, list_widget):
        """Returns a lambda that correctly captures the list_widget."""
        return lambda: self.removeItem(list_widget)

    def fill_list_widget_with_csv_file(self, file):
        bullets = []
        questions = []
        with open(file, "r") as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                questions.append(row[0])
                bullets.append(row[1:])

        question_bullet_dict = {}
        list_widgets = []
        tittles = []
        for i in range(1, 7):
            tmp = {}
            list_widget = getattr(self.ui, f"q_bullets_{i}")
            title = getattr(self.ui, f"q_title_{i}")

            tittles.append(title)
            list_widgets.append(list_widget)

            tmp["list_widget"] = list_widget
            question_bullet_dict[i] = tmp

            tittles[i - 1].setText(questions[i - 1])
            list_widgets[i - 1].addItems(bullets[i - 1])
            self.set_editable_items(list_widgets[i - 1])

    def get_all_list_widgets_items(self, in_one_list=False):
        all_bullets = []
        self.questions = []
        for i in range(1, 7):
            items = []
            question_widget = getattr(widget.ui, f"q_title_{i}")
            list_widget = getattr(widget.ui, f"q_bullets_{i}")
            for j in range(list_widget.count()):
                items.append(list_widget.item(j).text())
            self.questions.append(QuestionBullets(i, question_widget.text(), items))
            all_bullets.append(items)
            
        if in_one_list:
            self.all_bullets = [item for sublist in all_bullets for item in sublist]
            # return self.all_bullets
        
        write_lines("Bullets.txt", self.all_bullets)        
        self.goto_maxdiff_widget()

        self.all_bullets = all_bullets
        
        return all_bullets

    def goto_maxdiff_widget(self):
        self.new_widget = wg()
        self.ui = ui_form.Ui_Widget()
        self.ui.setupUi(self.new_widget)
        
        self.new_widget.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    widget.fill_list_widget_with_csv_file("bullets.csv")

    # get all items for each list_widget
    # print(widget.get_all_list_widgets_items(in_one_list=True))

    sys.exit(app.exec())
