from tkinter import simpledialog, messagebox

# Базовий клас для створення питань
class QuestionCreator:
    def create_question(self):
        raise NotImplementedError("Method must be implemented in subclasses")

# Клас для створення питань із однією правильною відповіддю
class SingleChoiceQuestionCreator(QuestionCreator):
    def create_question(self):
        question = simpledialog.askstring("Single Choice Question", "Enter the question:")
        if not question:
            return None

        options = simpledialog.askstring("Options", "Enter options separated by commas:")
        if not options:
            return None

        correct_answer = simpledialog.askstring("Correct Answer", "Enter the correct answer (one option):")
        if not correct_answer:
            return None

        return {
            "question": question,
            "type": "single",
            "options": options.split(","),
            "answer": correct_answer.strip(),
            "points": None
        }

# Клас для створення питань із кількома правильними відповідями
class MultipleChoiceQuestionCreator(QuestionCreator):
    def create_question(self):
        question = simpledialog.askstring("Multiple Choice Question", "Enter the question:")
        if not question:
            return None

        options = simpledialog.askstring("Options", "Enter options separated by commas:")
        if not options:
            return None

        correct_answers = simpledialog.askstring("Correct Answers", "Enter correct answers separated by commas:")
        if not correct_answers:
            return None

        return {
            "question": question,
            "type": "multiple",
            "options": options.split(","),
            "answer": correct_answers.split(","),
            "points": None
        }

# Клас для створення відкритих питань
class OpenQuestionCreator(QuestionCreator):
    def create_question(self):
        question = simpledialog.askstring("Open Question", "Enter the question:")
        if not question:
            return None

        correct_answer = simpledialog.askstring("Correct Answer", "Enter the correct answer:")
        if not correct_answer:
            return None

        return {
            "question": question,
            "type": "open",
            "options": None,
            "answer": correct_answer.strip(),
            "points": None
        }

# Стратегія: Ручний розподіл балів
class ManualPointsStrategy:
    def allocate_points(self, questions):
        total_points = 0
        for question in questions:
            points = simpledialog.askfloat("Points", f"Enter points for the question: {question['question']}")
            if points is not None:
                question['points'] = points
                total_points += points
        return total_points

# Стратегія: Автоматичний розподіл балів
class AutoPointsStrategy:
    def __init__(self, total_points):
        self.total_points = total_points

    def allocate_points(self, questions):
        num_questions = len(questions)
        if num_questions == 0:
            return 0
        points_per_question = self.total_points / num_questions
        for question in questions:
            question['points'] = points_per_question
        return self.total_points

# Клас для створення тестів
class TestCreate:
    def __init__(self, points_strategy):
        """
        points_strategy: Об'єкт стратегії для розподілу балів.
        """
        self.points_strategy = points_strategy
        self.questions = []

    def create_test(self):
        title = simpledialog.askstring("Create Test", "Enter test title:")
        if not title:
            return

        topic = simpledialog.askstring("Create Test", "Enter test topic:")
        if not topic:
            return

        self.questions = self.create_questions()

        if not self.questions:
            messagebox.showinfo("Info", "No questions were created.")
            return

        # Використання стратегії для розподілу балів
        total_points = self.points_strategy.allocate_points(self.questions)

        new_test = Test(title=title, topic=topic, questions=self.questions, total_points=total_points)
        self.save_test(new_test)

        messagebox.showinfo("Success", "Test created successfully.")

    def create_questions(self):
        """Метод для створення списку питань."""
        question_creators = {
            "single": SingleChoiceQuestionCreator(),
            "multiple": MultipleChoiceQuestionCreator(),
            "open": OpenQuestionCreator()
        }

        questions = []
        while True:
            question_type = simpledialog.askstring("Question Type", "Enter question type (single/multiple/open):")
            if not question_type:
                break

            creator = question_creators.get(question_type)
            if not creator:
                messagebox.showerror("Error", "Invalid question type. Please choose one of the following: single, multiple, open.")
                continue

            question = creator.create_question()
            if question:
                questions.append(question)
        return questions

    def save_test(self, test):
        """Симуляція збереження тесту."""
        print(f"Saving test: {test.title}, Topic: {test.topic}, Questions: {len(test.questions)}, Points: {test.total_points}")

# Симуляція класу Test
class Test:
    def __init__(self, title, topic, questions, total_points):
        self.title = title
        self.topic = topic
        self.questions = questions
        self.total_points = total_points

# Використання стратегій
# Ручний спосіб
manual_strategy = ManualPointsStrategy()
manual_test_creator = TestCreate(points_strategy=manual_strategy)
manual_test_creator.create_test()

# Автоматичний спосіб
auto_strategy = AutoPointsStrategy(total_points=100)
auto_test_creator = TestCreate(points_strategy=auto_strategy)
auto_test_creator.create_test()
