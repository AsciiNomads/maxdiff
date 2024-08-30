import matplotlib.pyplot as plt
import numpy as np

from utils.maxdiff import get_scores, get_percentages

# Assuming the following:
# - questions is a list of Question objects
# - get_scores() and get_percentages() are defined as provided


# Function to plot Best-Worst Scores
def plot_best_worst_scores(questions):
    indices, scores = get_scores(questions)

    max_label_length = max(len(question.question_text) for question in questions)
    
    # Calculate the figure width and height based on the number of questions
    fig_width = max(6.5, 0.25 * max_label_length)
    fig_height = max(4, 0.5 * len(questions))

    titles = [
        q.question_text[:50] + "..." if len(q.question_text) > 50 else q.question_text
        for q in questions
    ]

    # Creating horizontal bars
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    plt.subplots_adjust(left=0.4, bottom=0.3)  # Adjust margins for labels

    sorted_titles = [titles[i] for i in indices]

    # Determine colors based on scores
    colors = ["green" if score >= 0 else "blue" for score in scores]

    ax.barh(sorted_titles, scores, color=colors)

    ax.set_xlabel("Scores")
    ax.set_ylabel("Question Title")
    ax.set_title("Best-Worst Scores")

    ax.invert_yaxis()  # Highest score on top

    return fig


# Function to plot Best-Worst Percentages
def plot_best_worst_percentages(questions):
    indices, scores, most_preferred_scores, least_preferred_scores = get_percentages(
        questions
    )

    # Convert indices to strings for better readability (optional)
    indices = [str(i) for i in indices]

    n = len(indices)
    bar_height = 0.4

    # Creating the plot
    fig, ax = plt.subplots(figsize=(10, n * 0.5))

    # Plot the most preferred (blue)
    ax.barh(
        indices,
        most_preferred_scores,
        height=bar_height,
        color="blue",
        label="Most Preferred",
    )

    # Plot the least preferred (red)
    ax.barh(
        indices,
        least_preferred_scores,
        height=bar_height,
        color="red",
        label="Least Preferred",
        left=most_preferred_scores,
    )

    # Calculate the remaining percentage for gray
    remaining_scores = 1 - (most_preferred_scores + least_preferred_scores)
    ax.barh(
        indices,
        remaining_scores,
        height=bar_height,
        color="gray",
        label="Remaining",
        left=most_preferred_scores + least_preferred_scores,
    )

    plt.xlabel("Percentage")
    plt.ylabel("Question ID")
    plt.title("Best-Worst Percentages")
    plt.legend(loc="best")

    plt.gca().invert_yaxis()  # Invert y-axis to have the highest score on top
    plt.show()
