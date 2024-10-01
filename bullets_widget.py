import sys
import csv
import pandas as pd

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

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
    confirm_clicked = Signal()

    def __init__(self, parent=None, default=False):
        super().__init__(parent)
        self.setWindowTitle("Change the answers")
        self.resources_dir = "resources/"

        self.number_of_questions = 6
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_widget(self)
        self.fill_list_widget_with_csv_file("bullets.xlsx")

        self.bullets = []
        self.all_bullets = []
        self.ui.stackedWidget.setCurrentIndex(0)  # Index 0 corresponds to the first page
        self.update_bullets_page()

        self.ui.confirm_btn.clicked.connect(self.on_confirm)
        self.ui.next_btn.clicked.connect(
            lambda: self.show_next_page(self.ui.stackedWidget)
        )
        self.ui.pre_btn.clicked.connect(
            lambda: self.show_pre_page(self.ui.stackedWidget)
        )


        if default:
            self.save_all_bullets_from_listWidgets(in_one_list=True)

    def on_confirm(self):
        self.save_content_of_listWidgets("bullets.xlsx")
        self.confirm_clicked.emit()
        # self.close()

    def on_confirm(self):
        self.save_content_of_listWidgets("bullets.xlsx")
        self.confirm_clicked.emit()
        # self.close()

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
        self.update_bullets_num_label()

    def removeItem(self, l_w):
        list_widget = l_w

        if list_widget:
            for item in list_widget.selectedItems():
                list_widget.takeItem(list_widget.row(item))
        else:
            print("QListWidget not found")
        self.update_bullets_num_label()

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
        def change_font_size(list_widget, font_size=12):
            font = QFont()
            font.setPointSize(font_size)
            list_widget.setFont(font)

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
                # print(df)
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
            change_font_size(list_widget, 15)
            self.set_editable_items(list_widgets[i - 1])
        self.update_bullets_num_label()

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
                list_of_items = []
                list_of_titles = []
                for i in range(1, self.number_of_questions + 1):
                    list_widget = getattr(self.ui, f"q_bullets_{i}")
                    title = getattr(self.ui, f"q_title_{i}")
                    list_of_titles.append(title.text())

                    items = [
                        list_widget.item(j).text() for j in range(list_widget.count())
                    ]
                    row = [title.text()] + items
                    # print("row ", row)
                    list_of_items.append(row)

                # print(list_of_items)

                df_header = pd.DataFrame(["Question"])
                df_data = pd.DataFrame(list_of_items)
                df = pd.concat([df_header, df_data], ignore_index=True)
                df.to_excel(file, header=False, index=False)

            except Exception as e:
                print("Error writing xlsx file")
                print(e)
        else:
            print("Invalid file format. Only CSV and XLSX files are supported.")

    def read_bullets_from_widget(self, in_one_list=True) -> int:
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
        else:
            self.all_bullets = all_bullets

        return len(self.all_bullets)

    def save_all_bullets_from_listWidgets(self, in_one_list=False) -> None:

        self.read_bullets_from_widget(in_one_list)

        write_lines("Bullets.txt", self.all_bullets)
        self.save_content_of_listWidgets("bullets.xlsx")
        self.goto_maxdiff_widget()

        return self.all_bullets

    def update_bullets_num_label(self):
        bullets_num = self.read_bullets_from_widget(in_one_list=True)
        label_text = f"Number of bullets: {bullets_num}"
        self.ui.bullet_num.setText(label_text)

        if bullets_num > 30:
            self.ui.confirm_btn.setEnabled(False)
            self.ui.bullet_num.setStyleSheet("color: red")
            self.ui.confirm_btn.setToolTip("The number of bullets should not exceed 30")
            self.ui.confirm_btn.setStyleSheet("background-color: red")
        else:
            self.ui.confirm_btn.setEnabled(True)
            self.ui.bullet_num.setStyleSheet("color: black")
            self.ui.confirm_btn.setToolTip("")
            self.ui.confirm_btn.setStyleSheet("background-color: #4CAF50")

    def goto_maxdiff_widget(self):
        self.close()
        self.new_widget = wg()
        self.ui = light_survey_form.Ui_Widget()
        self.ui.setupUi(self.new_widget)

        self.new_widget.show()

    def show_next_page(self, stacked_widget):
        current_index = stacked_widget.currentIndex()
        next_index = (current_index + 1) % stacked_widget.count()  # Cycle through pages
        stacked_widget.setCurrentIndex(next_index)
        self.update_bullets_page()

    def show_pre_page(self, stacked_widget):
        current_index = stacked_widget.currentIndex()
        next_index = (current_index - 1) % stacked_widget.count()  # Cycle through pages
        stacked_widget.setCurrentIndex(next_index)
        self.update_bullets_page()

    def update_page_num_label(self):
        current_index = self.ui.stackedWidget.currentIndex()
        total_pages = self.ui.stackedWidget.count()
        self.ui.page_num.setText(f"Page {current_index + 1} of {total_pages}")

    def check_if_next_is_valid(self):
        current_index = self.ui.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.ui.stackedWidget.count()
        if next_index == 0:
            self.ui.next_btn.setEnabled(False)
        else:
            self.ui.next_btn.setEnabled(True)
        if current_index == 0:
            self.ui.pre_btn.setEnabled(False)
        else:
            self.ui.pre_btn.setEnabled(True)
    
    def update_bullets_page(self):
        self.update_page_num_label()
        self.check_if_next_is_valid()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
