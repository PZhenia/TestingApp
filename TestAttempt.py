class TestAttempt:
    def __init__(self, test_name, questions):
        self.test_name = test_name  # Назва тесту
        self.questions = questions  # Список питань
        self.score = 0              # Набраний бал
        self.current_question = 0   # Індекс поточного питання

    def answer_question(self, answer):
        #Метод для відповіді на поточне питання
        """set correct_answer to self.questions[self.current_question]['correct']
        if answer equals correct_answer:
            increment self.score by 1
        increment self.current_question by 1"""

    def is_finished(self):
        #Перевіряє, чи закінчився тест
        """return self.current_question is greater than or equal to length of self.questions"""

    def get_result(self):
        #Повертає загальний результат тесту у відсотках
        return (self.score / len(self.questions)) * 100