from tkinter import simpledialog, messagebox

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

"""def load_default_tests(self):
        for test in DEFAULT_TESTS:
            self.manager.save_test(test)"""
