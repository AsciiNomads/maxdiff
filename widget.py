import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from ui_form import Ui_Widget
import random

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QButtonGroup
from PySide6.QtGui import QPixmap

from utils.file_reader import read_questions

from export_ui import Ui_Form

from random import randint
from utils.maxdiff import *
from utils.gen_plots import *

from utils.pdf_export import *


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
        q = Question(f"Question {i + 1}", i)
        q.most_preferred = randint(1, 10)
        q.least_preferred = randint(1, 10)
        q.total_proposed = q.most_preferred + q.least_preferred + randint(1, 10)
        questions.append(q)

    return questions


MAX_QUESTIONS_PER_PAGE = 4


# TODO :
# 1. if a radio button is going to be checked that both in its row and column are checked, it will not work properly. and next button will not be enabled.
# 2. if have not most and least selected, next button will not be enabled.
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Main Window")
        # self.show_new_widget()
        self.resources_dir = "resources/"
        self._create_dir()

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.question_sets = self.create_question_sets()
        self.current_set_index = 0
        self.change_remind_question_lable(
            self.current_set_index + 1, len(self.question_sets)
        )

        self.setup_widget(self)

        self.load_question_set(self.question_sets[self.current_set_index])

    def setup_widget(self, widget):
        self.ui.left_button_group = QButtonGroup(widget)
        self.ui.right_button_group = QButtonGroup(widget)
        self.ui.question_widgets = []

        for i in range(1, MAX_QUESTIONS_PER_PAGE + 1):
            qi_l = getattr(self.ui, f"q{i}_l")
            qi_most = getattr(self.ui, f"q{i}_most")
            qi_least = getattr(self.ui, f"q{i}_least")

            question_button_group = QButtonGroup(self)
            question_button_group.addButton(qi_least)
            question_button_group.addButton(qi_most)
            self.ui.left_button_group.addButton(qi_least)
            self.ui.right_button_group.addButton(qi_most)

            self.ui.question_widgets.append(
                {
                    "radio1": qi_most,
                    "radio2": qi_least,
                    "label": qi_l,
                    "button_group": question_button_group,
                    "question": Question("", _id=-(i + 1)),
                }
            )

        self.ui.NextButton.clicked.connect(self.next_question_set)

    def create_question_sets(self):
        # Create question instances
        questions = read_questions("questions.txt")
        self.question_objs = []
        for i, q_text in enumerate(questions):
            Q = Question(q_text, _id=i)
            self.question_objs.append(Q)

        result = []

        number_of_sets = len(self.question_objs) * MAX_QUESTIONS_PER_PAGE
        for i in range(number_of_sets):
            subset = random.sample(self.question_objs, 4)
            result.append(subset)

        # Define sets of questions (can have repeated questions)
        return result

    def load_question_set(self, question_set: list[Question]):
        # TODO: If a radio button is going to be checked that both in its row and column are checked, it will not work properly. and next button will not be enabled.
        self.ui.left_button_group.setExclusive(False)
        self.ui.right_button_group.setExclusive(False)
        for btn in self.ui.right_button_group.buttons():
            btn.setChecked(False)
        for btn in self.ui.left_button_group.buttons():
            btn.setChecked(False)
        self.ui.left_button_group.setExclusive(True)
        self.ui.right_button_group.setExclusive(True)

        for i, question in enumerate(question_set):
            self.ui.question_widgets[i]["label"].setText(question.question_html)
            self.ui.question_widgets[i]["question"] = question

    def update_questions_results(self):
        questions = [w["question"] for w in self.ui.question_widgets]

        for widget in self.ui.question_widgets:
            widget["question"].increment_total_proposed()

            if widget["radio1"].isChecked():
                widget["question"].increment_and_update_as_most_preferred(questions)
            elif widget["radio2"].isChecked():
                widget["question"].increment_and_update_as_least_preferred(questions)

    def change_remind_question_lable(self, number: int, total: int):
        self.ui.questions_part.setText(f"Questions: {number}/{total}")

    def next_question_set(self):
        # Save or process selected answers if needed
        self.update_questions_results()
        self.current_set_index += 1
        if self.current_set_index < len(self.question_sets):
            if self.current_set_index == len(self.question_sets) - 1:
                self.ui.NextButton.setText("Finish")
                self.ui.NextButton.setStyleSheet("background-color: #c0392b;")

                # self.ui.NextButton.styleSheet = "background-color: red"
            self.load_question_set(self.question_sets[self.current_set_index])
            self.change_remind_question_lable(
                self.current_set_index + 1, len(self.question_sets)
            )
        else:
            for q in self.get_questions():
                print(q)
            print("No more questions.")

            self.close()
            self.exportWidget()
            # Handle end of questions, e.g., show results or submit data

    def get_questions(self):
        return self.question_objs

    def exportWidget(self):
        def show_plot():
            dir = "resources/images/"
            file_path = os.path.join(dir, "maxdiff.png")
            fig = plot_best_worst_scores(self.questions)
            fig.savefig(file_path, format="png")
            self.ui.plot_pic.setPixmap(QPixmap(file_path))

        # get questions
        self.questions = self.get_questions()
        # self.questions = generate_random_questions(15)
        print(self.questions)
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
        self.new_widget.show()
        show_plot()
        self.comboBox = self.ui.comboBox
        self.comboBox.addItem("csv")
        self.comboBox.addItem("pdf")
        self.comboBox.addItem("png")
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
                # filter=f"{extension.upper()} files (*.{extension})",
            )
            # and extensions to csv file
            if f".{extension}" not in file_path:
                file_path = file_path + f".{extension}"
            return file_path

        def export_csv():
            # dir = os.path.join(self.resources_dir, "csv/")
            # file_path = os.path.join(dir, "maxdiff.csv")
            file_path = get_filepath("csv")

            with open(file_path, "w") as f:
                f.write("Question,Most Preferred,Least Preferred,Total Proposed\n")
                for q in self.questions:
                    f.write(
                        f"{q.id},{q.question_text},{q.most_preferred},{q.least_preferred},{q.total_proposed}\n"
                    )

        def export_pdf():
            # Sample dictionary data
            data = self.questions
            dir = "resources/images/"
            image_path = os.path.join(dir, "maxdiff.png")
            export_png(show_dialog=False, save_path=image_path)
            # Export to PDF
            pdf_output_path = get_filepath("pdf")
            export_maxdiff_to_pdf(data, pdf_output_path, image_path)

        def export_png(show_dialog=True, save_path=None):
            if show_dialog:
                file_path = get_filepath("png")
            else:
                file_path = save_path

            fig = plot_best_worst_scores(self.questions)
            fig.savefig(file_path, format="png")

        print("Exporting data")
        print(self.comboBox.currentText())

        if self.comboBox.currentText() == "csv":
            print("Exporting as CSV")
            export_csv()
        elif self.comboBox.currentText() == "pdf":
            export_pdf()
        elif self.comboBox.currentText() == "png":
            export_png()
        elif self.comboBox.currentText() == "show plot":
            show_plot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    # widget.exportWidget.show()
    widget.show()

    sys.exit(app.exec())
