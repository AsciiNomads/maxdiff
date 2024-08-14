import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from maxdiff_function import analyze_maxdiff_results, plot_results

class SurveyWindow(tk.Toplevel):
    def __init__(self, parent, survey_data):
        super().__init__(parent)
        self.title("MaxDiff Survey")
        self.survey_data = survey_data
        self.current_index = 0

        self.label = tk.Label(self, text="Choose the most preferred and least preferred item from each set:")
        self.label.pack(padx=10, pady=10)

        self.setup_survey()

    def setup_survey(self):
        for i, row in self.survey_data.iterrows():
            label_text = ", ".join(row["OtherItems"])
            label = tk.Label(self, text=label_text)
            label.pack(padx=10, pady=5)

            most_button = tk.Button(self, text="Most Preferred", command=lambda i=i: self.save_response(i, "MostPreferred"))
            most_button.pack(side=tk.LEFT, padx=5, pady=5)

            least_button = tk.Button(self, text="Least Preferred", command=lambda i=i: self.save_response(i, "LeastPreferred"))
            least_button.pack(side=tk.LEFT, padx=5, pady=5)

    def save_response(self, index, preference):
        self.survey_data.at[index, preference] = True
        self.current_index += 1
        if self.current_index >= len(self.survey_data):
            self.finish_survey()

    def finish_survey(self):
        labels, counts = analyze_maxdiff_results(self.survey_data)
        plot_results(labels, counts)
        self.destroy()
