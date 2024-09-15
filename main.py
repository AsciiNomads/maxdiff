import sys, os

from PySide6.QtWidgets import QApplication
from app_controller import AppController

os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=0"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.start()
    sys.exit(app.exec())
    sys.exit(exit_code)
