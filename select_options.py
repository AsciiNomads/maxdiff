from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel

import sys
from Uis.dialog_ui import Ui_Dialog

from bullets_widget import Widget as wg
from Uis.select_bullets_ui import Ui_Form


class OptionDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an Option")

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.start_btn.clicked.connect(self.choose_option1)
        self.ui.change_btn.clicked.connect(self.choose_option2)

    def goto_bullet_option_select(self, default):
        self.new_widget = wg(default=default)
        self.ui = Ui_Form()
        self.ui.setupUi(self.new_widget)

        self.new_widget.showFullScreen()
        # self.close()
        self.accept()

    def choose_option1(self):
        print("start")
        # start survey
        self.goto_bullet_option_select(default=True)
        # self.accept()

    def choose_option2(self):
        print("change")
        # change survey options
        self.goto_bullet_option_select(default=False)
        # self.accept()


def main():
    app = QApplication(sys.argv)

    dialog = OptionDialog()
    sys.exit(dialog.exec())


if __name__ == "__main__":
    main()
