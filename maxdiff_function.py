import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from collections import defaultdict

def generate_maxdiff_survey(questions, n_appearances, items_per_set):
    number_of_surveys = (len(questions) * n_appearances) // items_per_set
    survey_list = [[] for _ in range(number_of_surveys)]
    
    # Dictionary to track the number of appearances of each question
    question_count = defaultdict(int)

    # Shuffle the questions to ensure random distribution
    random.shuffle(questions)
    
    for _ in range(n_appearances):
        # Shuffle surveys to ensure random distribution of questions
        random.shuffle(survey_list)
        
        for question in questions:
            # Sort survey lists based on the number of items and current question appearance count
            survey_list.sort(key=lambda x: (len(x), question_count[question]))
            
            # Find the first survey that does not already contain the question and has space
            for survey in survey_list:
                if question not in survey and len(survey) < items_per_set:
                    survey.append(question)
                    question_count[question] += 1
                    break

    return survey_list


def generate_maxdiff_survey_nopair(questions, n_appearances, items_per_set):
    number_of_surveys = (len(questions) * n_appearances) // items_per_set
    survey_list = [[] for _ in range(number_of_surveys)]
    
    # Dictionary to track the number of appearances of each question
    question_count = defaultdict(int)

    # Set to track pairs that have already appeared together
    used_pairs = set()

    # Shuffle the questions to ensure random distribution
    random.shuffle(questions)
    
    for _ in range(n_appearances):
        # Shuffle surveys to ensure random distribution of questions
        random.shuffle(survey_list)
        
        for question in questions:
            # Sort survey lists based on the number of items and current question appearance count
            survey_list.sort(key=lambda x: (len(x), question_count[question]))

            # Find the first survey that does not already contain the question, has space,
            # and does not form a pair with any existing question in the survey that violates the pair constraint
            for survey in survey_list:
                if question not in survey and len(survey) < items_per_set:
                    # Check if adding this question would violate the pair constraint
                    valid = True
                    for existing_question in survey:
                        if (existing_question, question) in used_pairs or (question, existing_question) in used_pairs:
                            valid = False
                            break

                    if valid:
                        # Add the question to the survey and record the pairs
                        survey.append(question)
                        question_count[question] += 1
                        for existing_question in survey:
                            if existing_question != question:
                                used_pairs.add((existing_question, question))
                        break

    return survey_list


# def generate_maxdiff_survey(questions, total_sets, items_per_set):
#     surveys = []
#     while len(surveys) < total_sets:
#         random.shuffle(questions)
#         for i in range(0, len(questions), items_per_set):
#             if len(surveys) >= total_sets:
#                 break
#             set_items = questions[i:i + items_per_set]
#             if len(set_items) == items_per_set:  # Ensure the set has the required number of items
#                 survey = {"MostPreferred": None, "LeastPreferred": None, "OtherItems": set_items}
#                 surveys.append(survey)
#     return pd.DataFrame(surveys)

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
