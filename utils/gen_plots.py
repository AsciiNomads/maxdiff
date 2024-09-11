import matplotlib.pyplot as plt
import numpy as np

from utils.maxdiff import set_rank_scores, get_percentages

# Assuming the following:
# - questions is a list of Question objects
# - set_rank_scores() and get_percentages() are defined as provided


# Function to plot Best-Worst Scores
def plot_best_worst_scores(questions, n_total_pages):
    if any([q.rank == 0 for q in questions]):
        set_rank_scores(questions, n_total_pages)

    max_label_length = max(len(question.question_text) for question in questions)
    sorted_questions = sorted(questions, key=lambda q: q.rank)
    scores = [q.score for q in sorted_questions]

    
    # Calculate the figure width and height based on the number of questions
    fig_width = max(6.5, 0.25 * max_label_length)
    fig_width = 1500 / 96
    fig_height = max(4, 0.5 * len(questions))

    titles = [
        q.question_text[:37] + "..." if len(q.question_text) > 40 else q.question_text
        for q in sorted_questions
    ]

    # Creating horizontal bars
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=150)
    plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.2)  # Adjust margins for labels

    # Determine colors based on scores
    colors = ["green" if score >= 0 else "blue" for score in scores]

    # Plot horizontal bars
    bars = ax.barh(titles, scores, color=colors)

    # Add horizontal lines for each row (black lines)
    for i in range(len(titles)):
        ax.hlines(i, -120, 120, colors="lightgray", linestyles="--", linewidth=0.5)

    # Add vertical line at x=0
    ax.axvline(x=0, color="red", linestyle="--", linewidth=1)

    # Set x-axis limits to [-100, 100]
    ax.set_xlim(-120, 120)

    # Add the scores as text on the bars
    for bar, score in zip(bars, scores):
        x_position = bar.get_width()  # Get the bar length for the x-position
        y_position = bar.get_y() + bar.get_height() / 2  # Center the text vertically

        # Display the score text either inside or outside the bar depending on the score
        if x_position < 0:
            ax.text(x_position - 5, y_position, f'{score:.2f}', va='center', ha='right', color='black')  # inside left
        else:
            ax.text(x_position + 5, y_position, f'{score:.2f}', va='center', ha='left', color='black')  # outside right

    ax.set_xlabel("Scores", fontsize=14)
    ax.set_ylabel("Question Title", fontsize=14)
    ax.set_title("Best-Worst Scores", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=12)
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
