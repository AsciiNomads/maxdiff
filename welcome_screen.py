from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal

class WelcomeScreen(QWidget):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to MaxDiff Survey")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        welcome_label = QLabel("Welcome to the MaxDiff Survey App!")
        layout.addWidget(welcome_label)

        instructions = QLabel(
            "This app will guide you through creating and taking a MaxDiff survey.\n"
            "1. First, you'll add questions to your survey.\n"
            "2. Then, you'll be able to start the survey or modify questions.\n"
            "3. During the survey, you'll choose the most and least important items.\n"
            "\nLet's start by adding questions to your survey!"
        )
        layout.addWidget(instructions)

        start_button = QPushButton("Start Adding Questions")
        start_button.clicked.connect(self.on_start_clicked)
        start_button.setStyleSheet("""
            /* Button Style */
            QPushButton {
                background-color: #3B82F6; /* Blue background for the button */
                color: white; /* White text for visibility */
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                margin: 4px 0;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #2563EB; /* Darker blue on hover */
            }

            QPushButton:pressed {
                background-color: #1D4ED8; /* Even darker blue on press */
            }
        """)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def on_start_clicked(self):
        self.finished.emit()
        self.close()
