from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

class WelcomeScreen(QWidget):
    close_signal = Signal()
    def __init__(self, is_first_time=True):
        super().__init__()
        self.is_first_time = is_first_time
        self.init_ui()
        self.apply_stylesheets()

    def closeEvent(self, event):
        self.close_signal.emit()
        super().closeEvent(event)
    
    def init_ui(self):
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to MaxDiff Survey App!")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(QFont("Arial", 16, QFont.Bold))

        instructions = self.get_instructions()
        instruction_label = QLabel(instructions)
        instruction_label.setWordWrap(True)
        instruction_label.setAlignment(Qt.AlignCenter)

        start_button = QPushButton("Start Survey")
        start_button.clicked.connect(self.close)
        

        layout.addWidget(welcome_label)
        layout.addWidget(instruction_label)
        layout.addWidget(start_button)

        self.setLayout(layout)
        self.setWindowTitle("Welcome to MaxDiff Survey")
        self.resize(400, 300)

    def apply_stylesheets(self):
        button_style = """
        QPushButton {
            background-color: #3B82F6;
            color: white;
            font-size: 12px;
            padding: 10px 20px;
            border: 1px solid #D0D0D0;
            border-radius: 8px;
            font-weight: 500;
        }

        QPushButton:hover {
            background-color: #2563EB;
            border-color: #C0C0C0;
        }

        QPushButton:pressed {
            background-color: #1D4ED8;
            border-color: #A0A0A0;
            padding-top: 12px;
            padding-bottom: 8px;
        }

        QPushButton:disabled {
            background-color: #F5F5F5;
            color: #B0B0B0;
            border-color: #E0E0E0;
        }
        """
        self.setStyleSheet(button_style)

    def get_instructions(self):
        if self.is_first_time:
            return ("Welcome to your first MaxDiff survey!\n\n"
                    "1. You'll see sets of items on each screen.\n"
                    "2. For each set, select the item you most prefer and the item you least prefer.\n"
                    "3. Click 'Next' to move to the next set of items.\n"
                    "4. Continue until you've completed all sets.\n"
                    "5. At the end, you'll see your results and have the option to export them.\n\n"
                    "Take your time and choose based on your honest preferences. Let's begin!")
        else:
            return ("Welcome back to the MaxDiff Survey App!\n\n"
                    "If you want to change your previous answers or redo the survey:\n"
                    "1. Click on 'Change Questions' on the main screen.\n"
                    "2. You can modify the question set or start a new survey.\n"
                    "3. Your new results will replace the previous ones.\n\n"
                    "Ready to continue or make changes? Let's go!")

def show_welcome_screen(is_first_time=True):
    welcome = WelcomeScreen(is_first_time)
    welcome.show()
    return welcome
