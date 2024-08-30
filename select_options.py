from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel

import sys
from dialog_ui import Ui_Dialog


class OptionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an Option")

        self.result = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.start_btn.clicked.connect(self.choose_option1)
        self.ui.change_btn.clicked.connect(self.choose_option2)

    def choose_option1(self):
        self.result = "start"
        print("start")
        self.accept()

    def choose_option2(self):
        self.result = "change"
        print("change")
        self.accept()


def main():
    app = QApplication(sys.argv)

    dialog = OptionDialog()
    sys.exit(dialog.exec())


if __name__ == "__main__":
    main()
