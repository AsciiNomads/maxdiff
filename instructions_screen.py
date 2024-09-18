from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Signal

class InstructionsScreen(QWidget):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("MaxDiff Survey Instructions")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("MaxDiff Survey Instructions")
        layout.addWidget(title)

        instructions = QLabel(
            "1. You will be presented with sets of items.\n"
            "2. For each set, choose the MOST important and LEAST important item.\n"
            "3. Click on the radio buttons to make your selections.\n"
            "4. Use the 'Next' button to move to the next set of items.\n"
            "5. Complete all sets to finish the survey.\n"
            "\nRemember, there are no right or wrong answers. We're interested in your preferences!"
        )
        layout.addWidget(instructions)

        start_button = QPushButton("Start Survey")
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
