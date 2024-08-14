import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from maxdiff_function import generate_maxdiff_survey
import pandas as pd

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MaxDiff Survey Tool")

        # Entry to add questions manually
        self.question_entry = tk.Entry(self, width=50)
        self.question_entry.grid(row=0, column=0, padx=10, pady=10)

        # Button to add questions manually
        self.add_question_button = tk.Button(self, text="Add Question", command=self.add_question)
        self.add_question_button.grid(row=0, column=1, padx=10, pady=10)

        # Button to select a file with questions
        self.load_file_button = tk.Button(self, text="Load Questions from File", command=self.load_questions_from_file)
        self.load_file_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Button to generate the survey
        self.generate_survey_button = tk.Button(self, text="Generate Survey", command=self.generate_survey)
        self.generate_survey_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.questions = []
        self.responses = []

    def add_question(self):
        question = self.question_entry.get().strip()
        if question:
            self.questions.append(question)
            self.question_entry.delete(0, tk.END)

    def load_questions_from_file(self):
        file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.questions = [line.strip() for line in file if line.strip()]
                messagebox.showinfo("Success", f"Loaded {len(self.questions)} questions from the file.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load questions from file: {e}")

    def generate_survey(self):
        if not self.questions:
            messagebox.showwarning("No Questions", "Please enter or load at least one question.")
            return

        survey_data = generate_maxdiff_survey(self.questions,5,3)
        survey_list = survey_data['OtherItems'].tolist()
        self.display_next_survey(survey_list, 0)

    def display_next_survey(self, survey_list, index):
        if index < len(survey_list):
            survey_window = SurveyWindow(self, survey_list[index], lambda most, least: self.collect_response(most, least, survey_list, index + 1))
            survey_window.grab_set()
        else:
            self.show_results()

    def collect_response(self, most, least, survey_list, next_index):
        self.responses.append((most, least))
        self.display_next_survey(survey_list, next_index)

    def show_results(self):
        counts = {question: {'most': 0, 'least': 0} for question in self.questions}
        
        for most, least in self.responses:
            counts[most]['most'] += 1
            counts[least]['least'] += 1

        result_window = tk.Toplevel(self)
        result_window.title("Survey Results")

        tree = ttk.Treeview(result_window, columns=("Feature", "Most Preferred", "Least Preferred", "Score"), show="headings")
        tree.heading("Feature", text="Feature")
        tree.heading("Most Preferred", text="Times Most Preferred")
        tree.heading("Least Preferred", text="Times Least Preferred")
        tree.heading("Score", text="Score")

        for feature, count in counts.items():
            most_preferred = count['most']
            least_preferred = count['least']
            score = most_preferred - least_preferred
            tree.insert("", "end", values=(feature, most_preferred, least_preferred, score))

        tree.pack(fill="both", expand=True)

class SurveyWindow(tk.Toplevel):
    def __init__(self, parent, survey_set, on_complete):
        super().__init__(parent)
        self.survey_set = survey_set
        self.on_complete = on_complete

        self.title("Survey Set")

        self.question_label = tk.Label(self, text="Select the most and least important:")
        self.question_label.grid(row=0, column=1, padx=10, pady=10)

        self.var_most = tk.StringVar()
        self.var_least = tk.StringVar()

        self.most_frame = ttk.Labelframe(self, text="Most Important")
        self.most_frame.grid(row=1, column=0, padx=5, pady=5)
        self.question_frame = ttk.Labelframe(self, text="Question")
        self.question_frame.grid(row=1, column=1, padx=5, pady=5)
        self.least_frame = ttk.Labelframe(self, text="Least Important")
        self.least_frame.grid(row=1, column=2, padx=5, pady=5)

        for question in self.survey_set:
            question_label = tk.Label(self.question_frame, text=question)
            question_label.pack(anchor="w")

            most_rb = ttk.Radiobutton(self.most_frame, text="", variable=self.var_most, value=question)
            least_rb = ttk.Radiobutton(self.least_frame, text="", variable=self.var_least, value=question)
            most_rb.pack(anchor="w")
            least_rb.pack(anchor="w")

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=1, padx=10, pady=10)

    def submit(self):
        most = self.var_most.get()
        least = self.var_least.get()
        if not most or not least:
            messagebox.showwarning("Incomplete", "Please select both the most and least important options.")
            return

        self.on_complete(most, least)
        self.destroy()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
