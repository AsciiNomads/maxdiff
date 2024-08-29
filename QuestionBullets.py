class QuestionBullets:
    def __init__(self, _id, question_text, bullets=[]):
        self.id = _id
        self.question_text = question_text

    def __str__(self) -> str:
        return f"{self.question_text}"

    def __repr__(self) -> str:
        return self.__str__()