from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton
from select_options import OptionDialog
from bullets_widget import Widget as BulletsWidget
from survey import Widget as survey_widget
from Uis.light_form_ui import Ui_Widget as survey_form

import csv
import pandas as pd
import os
import sys

SHOW_AT_LAUNCH_MESSAGE = (
            "Career Guidance helps you make crucial career decisions by using a survey-based research technique used to measure preferences. Using data and analytics, Career Guidance helps you:\n\n"
            "• Identify what's important to you in your next job\n"
            "• Decide what roles to pursue\n"
            "• Evaluate each new opportunity\n\n"
            "There are 3 steps to the Career Guidance process:\n\n"
            "• Answer 7 questions\n"
            "• Complete a short survey\n"
            "• Review the results\n\n"
            "Using Career Guidance leads to smarter decisions and ultimately greater job satisfaction and success."
        )

SHOW_BEFORE_SURVEY_MESSAGE = (
    "<b>Instructions for the completing the survey</b><br><br>"
    "The survey will take 15 to 20 minutes to complete so allow enough time to finish in one setting." 
    "When taking the survey, you will choose one item from the “most important” column on the left and one item from the “least important “column on the right. You are only allowed one response per column."
    "You will see that the items repeat so while it may feel repetitive, this is how the survey determines priorities from multiple items."
)

SHOW_AT_FIRST_RUN_OR_ANSWER_CHANGE = (
    "<b>Instructions for the completing the questionnaire</b><br><br>"
    "<b>Career Guidance renders better on a larger screen like a tablet, laptop, or desktop. It does work on your phone but requires typing and you will need to scroll back and forth which may become annoying.</b><br><br>"
    "Please read and follow the instructions closely before completing the questionnaire.<br><br>" 
    "<b>You are limited to</b> a total of 30 answers for all 7 questions<br>"
    "<b>One item per bullet</b> – Avoid words such as “and” or “as well as” or “in addition” or “also” in the same bullet<br>"
    "Don't use words like <b>required, preferred or desirable</b><br>"
    "<b>Be clear and concise</b> with your answers<br>"
    "<b>Please remove all duplicates</b> or items that say the same thing but differently<br>"
    "<b>Don’t use the word “I” when answering.</b>  For example – “Work in an energized culture” versus I want to work in an energized culture.<br>"
    "<b>Read all 7 questions</b> first before starting<br>"
)

class AppController:
    def __init__(self):
        self.option_dialog = None
        self.bullets_widget = None
        self.all_bullets = []
        self.second_run_bullets = False

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Create a custom button with the specified styles
        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #3B82F6;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                margin: 4px 0;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563EB;
            }
            QPushButton:pressed {
                background-color: #1D4ED8;
            }
        """)

        # Add the custom button to the message box
        msg_box.addButton(ok_button, QMessageBox.AcceptRole)

        msg_box.exec()

    def show_duplicate_check_prompt(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Review Your Answers")
        msg_box.setText("Before proceeding to the survey, please review your answers carefully:\n\n"
                        "1. Look for any duplicate items.\n"
                        "2. Check for items that express the same idea in different words.\n"
                        "3. Remove or consolidate any redundant entries.\n\n"
                        "This step is crucial for ensuring the quality of your survey data.")
        
        review_button = QPushButton("Continue to Survey")
        review_button.setStyleSheet("""
            QPushButton {
                background-color: #3B82F6;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                margin: 4px 0;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563EB;
            }
            QPushButton:pressed {
                background-color: #1D4ED8;
            }
        """)
        stay_button = QPushButton("Review Answers")
        stay_button.setStyleSheet("""
            QPushButton {
                background-color: #F87171;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                margin: 4px 0;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #EF4444;
            }
            QPushButton:pressed {
                background-color: #DC2626;
            }
        """)
        if self.second_run_bullets:
            msg_box.addButton(review_button, QMessageBox.AcceptRole)
        msg_box.addButton(stay_button, QMessageBox.RejectRole)
        
        return msg_box.exec()


    def show_survey_widget(self):
        self.save_bullets_into_txt("bullets.xlsx", "Bullets.txt")
        self.new_widget = survey_widget()
        self.ui = survey_form()
        self.ui.setupUi(self.new_widget)
        # Show the pre-survey message
        self.new_widget.show()

    def show_pre_survey_message(self):
        # Show the pre-survey message
        self.show_message("Survey Instructions", SHOW_BEFORE_SURVEY_MESSAGE)

    def show_option_dialog(self):
        if self.option_dialog is None:
            self.option_dialog = OptionDialog()
        self.option_dialog.show()
        self.option_dialog.survey_button_clicked.connect(self.show_pre_survey_message)
        self.option_dialog.change_clicked.connect(self.click_on_show_bullets)
    
    def click_on_show_bullets(self):
        self.show_message("Questionnaire Instructions", SHOW_AT_FIRST_RUN_OR_ANSWER_CHANGE)
        self.show_bullets_widget()

    def show_bullets_widget(self):
        if self.bullets_widget is None:
            self.bullets_widget = BulletsWidget()
        self.bullets_widget.showMaximized()
        self.bullets_widget.confirm_clicked.connect(self.on_bullets_confirm)
        if self.option_dialog:
            self.option_dialog.close()

    def set_to_not_first_time(self):
        # exit the program and remove the first time file
        config_file = "not_first_time"
        if sys.platform == "win32":
            config_path = os.path.join(os.getenv("APPDATA"), "maxdiff")
        elif sys.platform == "darwin":
            config_path = os.path.expanduser("~/Library/Application Support/maxdiff")
        else:
            config_path = os.path.expanduser("~/.config/maxdiff")
        if not os.path.exists(config_path):
            os.makedirs(config_path)
        config_file = os.path.join(config_path, config_file)
        if os.path.exists(config_file):
            os.remove(config_file)
        print("First time file removed.")
        # exit the program
        sys.exit(0)
    
    def check_if_first_time(self) -> bool:
        config_file = "not_first_time"
        if sys.platform == "win32":
            config_path = os.path.join(os.getenv("APPDATA"), "maxdiff")
        elif sys.platform == "darwin":
            config_path = os.path.expanduser("~/Library/Application Support/maxdiff")
        else:
            config_path = os.path.expanduser("~/.config/maxdiff")
        if not os.path.exists(config_path):
            os.makedirs(config_path)
        config_file = os.path.join(config_path, config_file)
        if not os.path.exists(config_file):
            with open(config_file, "w") as f:
                f.write("This is just a file to check if the app has been run before.")
            return True
        else:
            return False
    
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
    
    def on_bullets_confirm(self):
        response = self.show_duplicate_check_prompt()
        if not self.second_run_bullets:
            response = 3
        if response == 2: # 2 is for AcceptRole
            print("Start survey")
            self.bullets_widget.close()
            self.show_pre_survey_message()
            self.show_survey_widget()
        elif response == 3: # 3 is for RejectRole
            print("Review answers")
            self.second_run_bullets = True

    def check_questions_bullets(self, file) -> bool:
        if file.endswith(".csv"):
            with open(file, "r") as f:
                reader = csv.reader(f, delimiter="|")
                for row in reader:
                    try:
                        if len(row[1:]) > 0:
                            return True
                    except Exception as e:
                        pass
        elif file.endswith(".xlsx"):
            try:
                df = pd.read_excel(file)
                for i in range(len(df)):
                    try:
                        for item in df.iloc[i, 1:]:
                            if pd.notna(item):
                                return True
                    except Exception as e:
                        pass
            except Exception as e:
                print("Error reading xlsx file")
                print(e)
        else:
            print("Invalid file format. Only CSV and XLSX files are supported.")

        return False

    def start(self):
        self.show_message("Welcome to Career Guidance", SHOW_AT_LAUNCH_MESSAGE)
        if self.check_if_first_time():
            # Show the first run or answer change message
            self.show_message("Questionnaire Instructions", SHOW_AT_FIRST_RUN_OR_ANSWER_CHANGE)
            self.show_bullets_widget()
        else:
            self.show_option_dialog()


        # elif not self.check_questions_bullets("bullets.xlsx"):
        #     self.show_bullets_widget()
        # else:
        #     self.show_option_dialog()