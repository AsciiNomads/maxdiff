from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal

import sys
from Uis.dialog_ui import Ui_Dialog
import csv
import pandas as pd

from bullets_widget import Widget as wg
from Uis.select_bullets_ui import Ui_Form
from Uis.light_form_ui import Ui_Widget as survey_form
from survey import Widget as survey_widget


class OptionDialog(QDialog):
    change_clicked = Signal()
    survey_button_clicked = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an Option")

        self.all_bullets = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.start_btn.clicked.connect(self.choose_option1)
        self.ui.change_btn.clicked.connect(self.on_change)

    def on_change(self):
        self.change_clicked.emit()
        self.close()

    def goto_bullet_option_select(self, choice="start"):
        if choice == "start":
            self.survey_button_clicked.emit()
            self.save_bullets_into_txt("bullets.xlsx", "Bullets.txt")
            self.new_widget = survey_widget()
            self.ui = survey_form()
            self.ui.setupUi(self.new_widget)

            self.new_widget.show()
            self.accept()

        elif choice == "change":
            self.new_widget = wg()
            self.ui = Ui_Form()
            self.ui.setupUi(self.new_widget)

            self.new_widget.showMaximized()
            self.accept()

    def save_bullets_into_txt(self, read_file, write_file):
        if read_file.endswith(".xlsx"):
            df = pd.read_excel(read_file)
            for _, row in df.iterrows():
                for value in row[1:]:
                    if pd.notna(value):  # Check if the cell is not NaN
                        self.all_bullets.append(value.strip())

            with open(write_file, "w") as file:
                for bullet in self.all_bullets:
                    print(bullet)
                    file.write(f"{bullet}\n")
        else:
            with open(read_file, "r") as file:
                reader = csv.reader(file, delimiter="|")
                for row in reader:
                    self.all_bullets.append(row[1:])

    def choose_option1(self):
        print("start")
        self.goto_bullet_option_select(choice="start")

    def choose_option2(self):
        print("change")
        self.goto_bullet_option_select(choice="change")


def main():
    app = QApplication(sys.argv)

    dialog = OptionDialog()
    sys.exit(dialog.exec())


if __name__ == "__main__":
    main()
