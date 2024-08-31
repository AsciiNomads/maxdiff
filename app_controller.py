from PySide6.QtWidgets import QApplication
from select_options import OptionDialog
from bullets_widget import Widget as BulletsWidget

class AppController:
    def __init__(self):
        self.option_dialog = None
        self.bullets_widget = None

    def show_option_dialog(self):
        if self.option_dialog is None:
            self.option_dialog = OptionDialog()
        self.option_dialog.show()
        self.option_dialog.change_clicked.connect(self.show_bullets_widget)

    def show_bullets_widget(self):
        if self.bullets_widget is None:
            self.bullets_widget = BulletsWidget()
        self.bullets_widget.show()
        self.bullets_widget.confirm_clicked.connect(self.on_bullets_confirm)
        if self.option_dialog:
            self.option_dialog.close()

    def on_bullets_confirm(self):
        self.bullets_widget.close()
        self.show_option_dialog()

    def start(self):
        self.show_option_dialog()
