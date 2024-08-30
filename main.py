# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication

from widget import Widget
from utils.gen_plots import plot_best_worst_scores, plot_best_worst_percentages

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.showFullScreen()
    exit_code = app.exec()

    # An example of how to use the functions to plot the results 
    
    # questions = widget.get_questions()
    
    # plot_best_worst_scores(questions)
    # plot_best_worst_percentages(questions)
    
    sys.exit(exit_code)
