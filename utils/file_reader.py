def read_questions(file_path: str) -> list:
    questions = list()
    with open(file_path) as file:
        for line in file:
            questions.append(line.strip())
    return questions
