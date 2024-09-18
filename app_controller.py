from PySide6.QtWidgets import QApplication
from select_options import OptionDialog
from bullets_widget import Widget as BulletsWidget
import csv
import pandas as pd
import os
import sys

class AppController:
    def __init__(self):
        self.option_dialog = None
        self.bullets_widget = None
        self.welcome_screen = None

    def show_option_dialog(self):
        if self.option_dialog is None:
            self.option_dialog = OptionDialog()
        self.option_dialog.show()
        self.option_dialog.change_clicked.connect(self.show_bullets_widget)

    def show_bullets_widget(self):
        if self.bullets_widget is None:
            self.bullets_widget = BulletsWidget()
        self.bullets_widget.showMaximized()
        self.bullets_widget.confirm_clicked.connect(self.on_bullets_confirm)
        if self.option_dialog:
            self.option_dialog.close()

    def on_welcome_screen_closed(self):
        # exit the program and remove the first time file
        config_file = "not_first_time"
        if os.name == "posix":
            config_path = os.path.expanduser("~/.config/maxdiff")
        else:
            config_path = os.path.join(os.getenv("APPDATA"), "maxdiff")
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
        if os.name == "posix":
            config_path = os.path.expanduser("~/.config/maxdiff")
        else:
            config_path = os.path.join(os.getenv("APPDATA"), "maxdiff")
        if not os.path.exists(config_path):
            os.makedirs(config_path)
        config_file = os.path.join(config_path, config_file)
        if not os.path.exists(config_file):
            with open(config_file, "w") as f:
                f.write("This is just a file to check if the app has been run before.")
            return True
        else:
            return False
    
    def on_bullets_confirm(self):
        self.bullets_widget.close()
        self.show_option_dialog()

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
        if not self.check_questions_bullets("bullets.xlsx"):
            self.show_bullets_widget()
        else:
            self.show_option_dialog()
