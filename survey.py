import sys
import csv
import random

import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from Uis.light_form_ui import Ui_Widget

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QButtonGroup, QMessageBox
from PySide6.QtGui import QPixmap

from utils.file_io import read_lines

from PySide6.QtCore import Qt
from Uis.export_ui import Ui_Form

from random import randint
from utils.maxdiff import *
from utils.gen_plots import *

from utils.pdf_export import *
from utils.maxdiff import set_rank_scores, set_question_ranks
from maxdiff_function import generate_maxdiff_survey


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
        self.score = 0
        self.rank = 0

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
        q = Question(f"Question {i + 1}" + "x" * 0, i + 1)
        q.most_preferred = randint(1, 10)
        q.least_preferred = randint(1, 10)
        q.total_proposed = q.most_preferred + q.least_preferred + randint(1, 10)
        questions.append(q)

    return (questions, total_pages := 30)


MAX_NUMBER_OF_APPEARANCES = 5
MAX_QUESTIONS_PER_PAGE = 4


class Widget(QWidget):
    def __init__(self, parent=None, show_export_widget=False):
        super().__init__(parent)
        self.setWindowTitle("MaxDiff Survey")
        self.resources_dir = "resources/"
        self._create_dir()
        self.show_export_widget = show_export_widget

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.question_sets = self.create_question_sets()
        self.total_pages = len(self.question_sets)
        self.current_set_index = 0

        self.update_question_reminder_label(
            self.current_set_index + 1, len(self.question_sets)
        )

        self.setup_widget(self)

        self.next_button_style = self.ui.NextButton.styleSheet()

        if not self.question_sets:
            msg = QMessageBox()
            msg.setWindowTitle("No Questions added")
            msg.setText("No questions added to the survey.")
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
            self.close()

        self.load_question_set(self.question_sets[self.current_set_index])

        if show_export_widget:
            self.close()
            self.exportWidget()
        else:
            self.show()

    def setup_widget(self, widget):
        self.ui.left_button_group = QButtonGroup(self)
        self.ui.left_button_group.setExclusive(True)

        self.ui.right_button_group = QButtonGroup(self)
        self.ui.right_button_group.setExclusive(True)

        self.ui.question_widgets = []

        for i in range(1, MAX_QUESTIONS_PER_PAGE + 1):
            # Access widgets by name
            question_label = getattr(self.ui, f"q{i}_l")
            left_radio = getattr(self.ui, f"q{i}_least")
            right_radio = getattr(self.ui, f"q{i}_most")

            # Add radios to their respective column groups
            self.ui.left_button_group.addButton(left_radio)
            self.ui.right_button_group.addButton(right_radio)

            # Store references in a list for easy access
            self.ui.question_widgets.append(
                {
                    "label": question_label,
                    "left_radio": left_radio,
                    "right_radio": right_radio,
                    "question": Question("", _id=-(i + 1)),
                }
            )

            # Connect signals for row-wise restriction
            left_radio.toggled.connect(
                lambda checked, idx=i - 1: self.handle_left_radio_toggle(checked, idx)
            )
            right_radio.toggled.connect(
                lambda checked, idx=i - 1: self.handle_right_radio_toggle(checked, idx)
            )

        self.ui.NextButton.clicked.connect(self.next_question_set)

    def handle_left_radio_toggle(self, checked, index):
        """
        When a left radio button is toggled:
        - If checked, disable the right radio button in the same row.
        - If unchecked, enable the right radio button in the same row.
        """
        right_radio = self.ui.question_widgets[index]["right_radio"]
        right_radio.setEnabled(not checked)
        self.check_enable_next_button()

    def handle_right_radio_toggle(self, checked, index):
        """
        When a right radio button is toggled:
        - If checked, disable the left radio button in the same row.
        - If unchecked, enable the left radio button in the same row.
        """
        left_radio = self.ui.question_widgets[index]["left_radio"]
        left_radio.setEnabled(not checked)
        self.check_enable_next_button()

    def check_enable_next_button(self, is_finish=False):
        # Enable the "Next" button only if each row has one selection
        any_left_selected = any(
            w["left_radio"].isChecked() for w in self.ui.question_widgets
        )
        any_right_selected = any(
            w["right_radio"].isChecked() for w in self.ui.question_widgets
        )
        button_style = "background-color: #c0392b;" if is_finish else ""

        # Enable or disable the Next button based on selections
        if any_left_selected and any_right_selected:
            self.ui.NextButton.setEnabled(True)
            self.ui.NextButton.setStyleSheet(
                self.next_button_style
            )  # Reset to default style
        else:
            self.ui.NextButton.setEnabled(False)
            self.ui.NextButton.setStyleSheet(
                "background-color: lightgray; color: gray;"
            )

    def create_question_sets(self):
        # Create question instances
        questions = read_lines("Bullets.txt")
        self.question_objs = []
        for i, q_text in enumerate(questions):
            Q = Question(q_text, _id=i + 1)
            self.question_objs.append(Q)

        result = generate_maxdiff_survey(
            self.question_objs, MAX_NUMBER_OF_APPEARANCES, MAX_QUESTIONS_PER_PAGE
        )

        # number_of_sets = len(self.question_objs) * 3
        # number_of_sets = 2

        # for i in range(0, len(self.question_objs), 4):
        #     # subset = random.sample(self.Bullet_objs, 4)
        #     # result.append(subset)
        #     result.append(self.question_objs[i:i+4])

        # Define sets of questions (can have repeated questions)
        return result

    def load_question_set(self, question_set: list[Question]):
        self.ui.left_button_group.setExclusive(False)
        self.ui.right_button_group.setExclusive(False)

        for widget in self.ui.question_widgets:
            widget["left_radio"].setChecked(False)
            widget["right_radio"].setChecked(False)
            widget["left_radio"].setEnabled(True)
            widget["right_radio"].setEnabled(True)

        self.ui.left_button_group.setExclusive(True)
        self.ui.right_button_group.setExclusive(True)

        for i, question in enumerate(question_set):
            self.ui.question_widgets[i]["label"].setText(question.question_html)
            self.ui.question_widgets[i]["question"] = question

        self.check_enable_next_button()

    def update_questions_results(self):
        questions = [w["question"] for w in self.ui.question_widgets]

        for widget in self.ui.question_widgets:
            widget["question"].increment_total_proposed()

            if widget["right_radio"].isChecked():
                widget["question"].increment_and_update_as_most_preferred(questions)
            elif widget["left_radio"].isChecked():
                widget["question"].increment_and_update_as_least_preferred(questions)

    def update_question_reminder_label(self, number: int, total: int):
        self.ui.questions_part.setText(f"Questions: {number}/{total}")

    def next_question_set(self):
        # Save or process selected answers if needed
        self.update_questions_results()
        self.current_set_index += 1
        if self.current_set_index < len(self.question_sets):
            if self.current_set_index == len(self.question_sets) - 1:
                self.ui.NextButton.setText("Finish")
                self.ui.NextButton.setStyleSheet("background-color: #c0392b;")
                self.next_button_style = self.ui.NextButton.styleSheet()

                # self.ui.NextButton.styleSheet = "background-color: red"
            self.load_question_set(self.question_sets[self.current_set_index])
            self.update_question_reminder_label(
                self.current_set_index + 1, len(self.question_sets)
            )
        else:
            # print("Bullets:")
            # for q in self.get_questions():
            #     print(q)
            # print("No more questions.")

            self.close()
            self.exportWidget()
            # Handle end of questions, e.g., show results or submit data

    def get_questions(self):
        return self.question_objs

    def exportWidget(self):
        def show_plot():
            dir = "resources/images/"
            file_path = os.path.join(dir, "maxdiff.png")
            fig = plot_best_worst_scores(self.questions, self.total_pages)
            fig.savefig(file_path, format="png")
            pixmap = QPixmap(file_path)

            # Get the original size of the image
            original_width = pixmap.width()
            original_height = pixmap.height()

            # Get the QLabel's dimensions
            label_width = self.ui.plot_pic.width()
            label_height = self.ui.plot_pic.height()

            # Get the Form dimensions (or use your monitor's resolution if needed)
            form_width = (
                self.width()
            )  # You can also use a fixed max size, e.g., 1920 for width
            form_height = self.height()  # Or a fixed max height, e.g., 1080

            # Set a reasonable maximum size, which could be the Form size or the QLabel size
            max_width = min(form_width, label_width)
            max_height = min(form_height, label_height)

            # Calculate aspect ratios
            scaled_w_ratio = max_width / original_width
            scaled_h_ratio = max_height / original_height

            # Use the smaller ratio to maintain the aspect ratio without exceeding available space
            scale_ratio = min(scaled_w_ratio, scaled_h_ratio)

            # Calculate new scaled width and height based on the chosen ratio
            scaled_width = int(original_width * scale_ratio)
            scaled_height = int(original_height * scale_ratio)

            # Ensure the scaled dimensions do not exceed the form or label size
            scaled_width = min(scaled_width, max_width)
            scaled_height = min(scaled_height, max_height)

            # if form_width < scaled_width:
            width_ratio = form_width / scaled_width
            scaled_width = scaled_width * width_ratio
            scaled_height = scaled_height * width_ratio
            self.setFixedHeight(max_height)
            self.setFixedWidth(max_width)

            # print(f"Original: {original_width}x{original_height}")
            # print(f"Scaled: {scaled_width}x{scaled_height}")
            # print(f"Form size: {form_width}x{form_height}")
            # print(f"Label size: {label_width}x{label_height}")

            # Scale the image while keeping the aspect ratio
            scaled_pixmap = pixmap.scaled(
                scaled_width,
                scaled_height + 15,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )

            # Set the scaled pixmap to the QLabel
            self.ui.plot_pic.setPixmap(scaled_pixmap)
            self.ui.formWidget_2.setFixedHeight(scaled_height)
            self.ui.formWidget_2.setFixedWidth(scaled_width)

            # Optionally adjust the QLabel size if needed:
            self.ui.plot_pic.setFixedSize(scaled_width, scaled_height)

        # get questions
        if self.show_export_widget:
            self.questions, self.total_pages = generate_random_questions(30)
        else:
            self.questions = self.get_questions()
        set_rank_scores(self.questions, self.total_pages)

        # self.questions.sort(key=lambda )
        # Create a new widget to show
        self.new_widget = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.new_widget)
        # self.new_widget.setWindowTitle("New Widget")

        # Add some content to the new widget
        # layout = QVBoxLayout()
        # layout.addWidget(QLabel("This is the new widget!"))
        # self.new_widget.setLayout(layout)

        # Show the new widget
        self.new_widget.showFullScreen()
        show_plot()
        # self.comboBox = self.ui.comboBox
        # self.comboBox.addItem("csv")
        # self.comboBox.addItem("pdf")
        # self.comboBox.addItem("png")
        self.ui.exportData.clicked.connect(self.export_data)

    def _create_dir(self):
        if not os.path.exists(self.resources_dir):
            os.makedirs(self.resources_dir)
        if not os.path.exists(os.path.join(self.resources_dir, "csv/")):
            os.makedirs(os.path.join(self.resources_dir, "csv/"))
        if not os.path.exists(os.path.join(self.resources_dir, "images/")):
            os.makedirs(os.path.join(self.resources_dir, "images/"))

    def export_data(self):
        def get_filepath(extension: str):
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(
                filter=f"{extension.upper()} files (*.{extension})",
            )
            # and extensions to csv file
            if f".{extension}" not in file_path:
                file_path = file_path + f".{extension}"
            return file_path

        def export_csv():
            file_path = get_filepath("csv")

            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        "Rank",
                        "ID",
                        "Question",
                        "Most Preferred",
                        "Least Preferred",
                        "Appearnaces",
                        "Scores",
                    ]
                )
                for q in self.questions:
                    writer.writerow(
                        [
                            q.rank,
                            q.id,
                            q.question_text,
                            q.most_preferred,
                            q.least_preferred,
                            q.total_proposed,
                            q.score,
                        ]
                    )

        def export_pdf():
            # Sample dictionary data
            dir = "resources/images/"
            image_path = os.path.join(dir, "maxdiff.png")
            export_png(show_dialog=False, save_path=image_path)
            # Export to PDF
            pdf_output_path = get_filepath("pdf")
            export_maxdiff_to_pdf(self.questions, pdf_output_path, image_path)

        def export_png(show_dialog=True, save_path=None):
            if show_dialog:
                file_path = get_filepath("png")
            else:
                file_path = save_path

            fig = plot_best_worst_scores(self.questions, self.total_pages)
            fig.savefig(file_path, format="png")

            # show success messagebox
            msg = QMessageBox()
            msg.setWindowTitle("Export Successful")
            msg.setText("PNG exported successfully.")
            msg.setIcon(QMessageBox.Information)
            msg.exec()

        print("Exporting data")

        # if self.comboBox.currentText() == "csv":
        #     print("Exporting as CSV")
        #     export_csv()
        # elif self.comboBox.currentText() == "pdf":
        #     export_pdf()
        # elif self.comboBox.currentText() == "png":
        export_png()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget(show_export_widget=True)
    # widget.exportWidget()
    # widget.show()

    sys.exit(app.exec())
