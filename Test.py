class Question:

    def __init__(self, question_text, answer, points=None):
        self.question_text = question_text
        self.answer = answer
        self.points = points

    def evaluate(self, user_answer):
        raise NotImplementedError("This method should be implemented in subclasses")


class SingleChoiceQuestion(Question):

    def __init__(self, question_text, options, correct_answer, points=None):
        super().__init__(question_text, correct_answer, points)
        self.options = options

    def evaluate(self, user_answer):
        return 1 if user_answer == self.answer else 0


class MultipleChoiceQuestion(Question):

    def __init__(self, question_text, options, correct_answers, points=None):
        super().__init__(question_text, correct_answers, points)
        self.options = options

    def evaluate(self, user_answer):
        correct_answers_set = set(self.answer)
        user_answers_set = set(user_answer)
        correct_count = len(correct_answers_set & user_answers_set)
        total_correct = len(correct_answers_set)

        return (correct_count / total_correct) if total_correct > 0 else 0


class OpenQuestion(Question):

    def __init__(self, question_text, correct_answer, points=None):
        super().__init__(question_text, correct_answer, points)

    def evaluate(self, user_answer):
        return 1 if user_answer.strip().lower() == self.answer.strip().lower() else 0


class Test:

    def __init__(self, title, topic, questions, total_points):
        self.title = title
        self.topic = topic
        self.questions = questions
        self.total_points = total_points

    def calculate_points(self, user_answers):
        total_score = 0
        for i, question in enumerate(self.questions):
            user_answer = user_answers[i]
            total_score += question.evaluate(user_answer) 

        return total_score

    def get_total_points(self):
        return self.total_points
