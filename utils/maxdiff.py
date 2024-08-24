import numpy as np

# from widget import Question


def get_scores(questions: list) -> tuple[np.ndarray, np.ndarray]:
    indices = []
    scores = []
    for item in questions:
        indices.append(item.id)
        try:
            scores.append(
                (item.most_preferred - item.least_preferred) / item.total_proposed
            )
        except ZeroDivisionError:
            scores.append(0)

    scores = np.array(scores)
    positions = np.argsort(-scores)
    indices = np.array(indices)[positions]
    scores = scores[positions]

    return indices, scores


def get_percentages(
    questions: list,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    indices = []
    scores = []
    most_preferred_scores = []
    least_preferred_scores = []
    for item in questions:
        indices.append(item.id)
        try:
            scores.append(
                (item.most_preferred - item.least_preferred) / item.total_proposed
            )
            most_preferred_scores.append(item.most_preferred / item.total_proposed)
            least_preferred_scores.append(item.least_preferred / item.total_proposed)
        except ZeroDivisionError:
            scores.append(0)
            most_preferred_scores.append(0)
            least_preferred_scores.append(0)

    scores = np.array(scores)
    positions = np.argsort(-scores)
    indices = np.array(indices)[positions]
    scores = scores[positions]
    most_preferred_scores = np.array(most_preferred_scores)[positions]
    least_preferred_scores = np.array(least_preferred_scores)[positions]

    return indices, scores, most_preferred_scores, least_preferred_scores
