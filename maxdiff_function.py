import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_maxdiff_survey(questions, total_sets, items_per_set):
    surveys = []
    while len(surveys) < total_sets:
        random.shuffle(questions)
        for i in range(0, len(questions), items_per_set):
            if len(surveys) >= total_sets:
                break
            set_items = questions[i:i + items_per_set]
            if len(set_items) == items_per_set:  # Ensure the set has the required number of items
                survey = {"MostPreferred": None, "LeastPreferred": None, "OtherItems": set_items}
                surveys.append(survey)
    return pd.DataFrame(surveys)

def analyze_maxdiff_results(survey_data):
    most_preferred_counts = survey_data["MostPreferred"].sum()
    least_preferred_counts = survey_data["LeastPreferred"].sum()
    other_items_counts = survey_data["OtherItems"].apply(lambda x: len(x)).sum() - most_preferred_counts - least_preferred_counts

    labels = ["Most Preferred", "Least Preferred", "Other Items"]
    counts = [most_preferred_counts, least_preferred_counts, other_items_counts]

    return labels, counts

def plot_results(labels, counts):
    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color=['blue', 'red', 'green'])
    plt.xlabel('Items')
    plt.ylabel('Counts')
    plt.title('MaxDiff Survey Results')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



# You can expand this file with more functions as needed for MaxDiff parameters and analysis
