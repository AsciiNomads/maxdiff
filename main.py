import sys, os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from app_controller import AppController

# set to light mode
if sys.platform == "win32":
    os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=0"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--remove-first-time":
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
            sys.exit(0)
    app = QApplication(sys.argv)
    controller = AppController()
    controller.start()
    sys.exit(app.exec())
    sys.exit(exit_code)
