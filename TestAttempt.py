from tkinter import simpledialog, messagebox
from difflib import SequenceMatcher

class TestAttempt:
    def __init__(self, manager):
        self.manager = manager

    def take_test(self, user):
        if not self.manager.tests:
            self.manager.load_default_tests()  # Завантажити тести за замовчуванням

        test_titles = [test.title for test in self.manager.tests]
        selected_test = simpledialog.askstring("Take Test", f"Select test:\n{', '.join(test_titles)}")

        test = next((t for t in self.manager.tests if t.title == selected_test), None)
        if not test:
            messagebox.showerror("Error", "Test not found.")
            return

        score = 0
        for question in test.questions:
            options_text = f"Options: {', '.join(question['options'])}" if question['options'] else ""
            answer = simpledialog.askstring("Question", f"{question['question']}\n{options_text}").strip()

            # Перевіряємо правильність відповіді залежно від типу питання
            if question['type'] == 'single' or question['type'] == 'multiple':
                correct_answers = set(map(str.strip, question['answer'].split(',')))
                user_answers = set(map(str.strip, answer.split(',')))

                if user_answers == correct_answers:
                    score += 1

            elif question['type'] == 'open':
                if answer.lower() == question['answer'].strip().lower():
                    score += 1

        # Зберігаємо результат тесту у прогрес користувача
        user.progress.add_attempt(selected_test, score)
        messagebox.showinfo("Test Completed", f"You scored {score}/{len(test.questions)}")

class ScoringStrategy:
    def evaluate(self, user_answer, correct_answer):
        raise NotImplementedError

class ExactMatchScoring(ScoringStrategy):
    def evaluate(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.strip().lower()

class ApproximateMatchScoring(ScoringStrategy):
    def evaluate(self, user_answer, correct_answer):
        similarity = SequenceMatcher(None, user_answer.strip().lower(), correct_answer.strip().lower()).ratio()
        return similarity > 0.7

class BaseTestAttempt:
    def __init__(self, manager, scoring_strategy):
        self.manager = manager
        self.scoring_strategy = scoring_strategy

class FocusedTestAttempt(BaseTestAttempt):
    def take_test(self, user):
        focused_questions = []
        for test_title, scores in user.progress.test_attempts.items():
            for i, score in enumerate(scores):
                if score == 0:
                    test = next((t for t in self.manager.tests if t.title == test_title), None)
                    if test:
                        focused_questions.extend(test.questions)

        if not focused_questions:
            messagebox.showinfo("Info", "No questions to review.")
            return

        score = 0
        for question in focused_questions:
            options_text = f"Options: {', '.join(question['options'])}" if question['options'] else ""
            answer = simpledialog.askstring("Question", f"{question['question']}\n{options_text}").strip()

            if self.scoring_strategy.evaluate(answer, question['answer']):
                score += 1

        messagebox.showinfo("Test Completed", f"You reviewed {len(focused_questions)} questions and scored {score}.")

class AdaptiveTestAttempt(BaseTestAttempt):
    def take_test(self, user):
        if not self.manager.tests:
            self.manager.load_default_tests()

        test_titles = [test.title for test in self.manager.tests]
        selected_test = simpledialog.askstring("Take Test", f"Select test:\n{', '.join(test_titles)}")

        test = next((t for t in self.manager.tests if t.title == selected_test), None)
        if not test:
            messagebox.showerror("Error", "Test not found.")
            return

        score = 0
        remaining_questions = test.questions.copy()

        while remaining_questions:
            question = remaining_questions.pop(0)
            options_text = f"Options: {', '.join(question['options'])}" if question['options'] else ""
            answer = simpledialog.askstring("Question", f"{question['question']}\n{options_text}").strip()

            if self.scoring_strategy.evaluate(answer, question['answer']):
                score += 1
            else:
                remaining_questions.append(question)

            if len(remaining_questions) > 10:
                break

        messagebox.showinfo("Test Completed", f"You scored {score}/{len(test.questions)} after adaptive selection.")


