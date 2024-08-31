import sys

import csv
import pandas as pd

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
from Uis.select_bullets_ui import Ui_Form
from survey import Widget as wg
import Uis.light_form_ui as light_survey_form

from QuestionBullets import QuestionBullets


class Widget(QWidget):
    def __init__(self, parent=None, default=False):
        super().__init__(parent)
        self.setWindowTitle("Main Window")
        # self.show_new_widget()
        self.resources_dir = "resources/"

        self.number_of_questions = 6
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_widget(self)
        self.fill_list_widget_with_csv_file("bullets.xlsx")
        # self.fill_list_widget_with_csv_file("bullets.csv")

        self.bullets = []
        self.all_bullets = []
        self.ui.confirm_btn.clicked.connect(
            lambda: self.get_all_list_widgets_items(in_one_list=True)
        )

        if default:
            self.get_all_list_widgets_items(in_one_list=True)

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
        for i in range(1, self.number_of_questions + 1):
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
        if file.endswith(".csv"):
            with open(file, "r") as f:
                reader = csv.reader(f, delimiter="|")
                for row in reader:
                    questions.append(row[0])
                    bullets.append(row[1:])
        elif file.endswith(".xlsx"):
            try:
                df = pd.read_excel(file)
                print(df)
                for i in range(len(df)):
                    questions.append(df.iloc[i, 0])
                    bullets.append(
                        [item.strip() for item in df.iloc[i, 1:] if pd.notna(item)]
                    )
            except Exception as e:
                print("Error reading xlsx file")
                print(e)
        else:
            print("Invalid file format. Only CSV and XLSX files are supported.")

        question_bullet_dict = {}
        list_widgets = []
        tittles = []
        for i in range(1, self.number_of_questions + 1):
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

    def save_content_of_listWidgets(self, file):
        if file.endswith(".csv"):
            with open(file, "w") as f:
                writer = csv.writer(f, delimiter="|")
                for i in range(1, self.number_of_questions + 1):
                    list_widget = getattr(self.ui, f"q_bullets_{i}")
                    title = getattr(self.ui, f"q_title_{i}")

                    items = [
                        list_widget.item(j).text() for j in range(list_widget.count())
                    ]
                    writer.writerow([title.text()] + items)
        elif file.endswith(".xlsx"):
            try:
                # df = pd.DataFrame(columns=["Question"])
                list_of_items = []
                list_of_titles = []
                for i in range(1, self.number_of_questions + 1):
                    list_widget = getattr(self.ui, f"q_bullets_{i}")
                    title = getattr(self.ui, f"q_title_{i}")
                    list_of_titles.append(title.text())
                    # print("title", title.text())

                    items = [
                        list_widget.item(j).text() for j in range(list_widget.count())
                    ]
                    # print("items", items)
                    row = [title.text()] + items
                    print("row ", row)
                    list_of_items.append(row)

                print(list_of_items)

                df_header = pd.DataFrame(["Question"])
                df_data = pd.DataFrame(list_of_items)
                df = pd.concat([df_header, df_data], ignore_index=True)
                df.to_excel(file, header=False, index=False)

            except Exception as e:
                print("Error writing xlsx file")
                print(e)
        else:
            print("Invalid file format. Only CSV and XLSX files are supported.")

    def get_all_list_widgets_items(self, in_one_list=False):
        all_bullets = []
        self.questions = []
        for i in range(1, self.number_of_questions + 1):
            items = []
            question_widget = getattr(self.ui, f"q_title_{i}")
            list_widget = getattr(self.ui, f"q_bullets_{i}")
            for j in range(list_widget.count()):
                items.append(list_widget.item(j).text())
            self.questions.append(QuestionBullets(i, question_widget.text(), items))
            all_bullets.append(items)

        if in_one_list:
            self.all_bullets = [item for sublist in all_bullets for item in sublist]
            # return self.all_bullets

        write_lines("Bullets.txt", self.all_bullets)
        self.save_content_of_listWidgets("bullets.xlsx")
        self.goto_maxdiff_widget()

        self.all_bullets = all_bullets

        return all_bullets

    def goto_maxdiff_widget(self):
        self.close()
        self.new_widget = wg()
        self.ui = light_survey_form.Ui_Widget()
        self.ui.setupUi(self.new_widget)

        self.new_widget.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.showFullScreen()

    # get all items for each list_widget
    # print(widget.get_all_list_widgets_items(in_one_list=True))

    sys.exit(app.exec())
