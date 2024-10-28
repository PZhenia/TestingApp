from tkinter import simpledialog, messagebox
from test import Test  # Імпорт класу Test

class TestCreate:
    def __init__(self, manager):
        self.manager = manager

    def create_test(self):
        title = simpledialog.askstring("Create Test", "Enter test title:")
        if title is None:
            return  # Користувач натиснув Cancel
        topic = simpledialog.askstring("Create Test", "Enter test topic:")
        if topic is None:
            return  # Користувач натиснув Cancel
        questions = []

        while True:
            question = simpledialog.askstring("New Question", "Enter question (or leave blank to finish):")
            if question is None:  # Користувач натиснув Cancel
                return
            if not question:
                break

            q_type = simpledialog.askstring("Question Type", "Enter type (single/multiple/open):")
            if q_type is None:  # Користувач натиснув Cancel
                return
            options = []
            answer = None

            if q_type == "single" or q_type == "multiple":
                options = simpledialog.askstring("Options", "Enter options separated by commas:").split(',')
                if options is None:  # Користувач натиснув Cancel
                    return
                answer = simpledialog.askstring("Answer", "Enter correct answer(s) separated by commas:")
                if answer is None:  # Користувач натиснув Cancel
                    return
            elif q_type == "open":
                answer = simpledialog.askstring("Answer", "Enter correct answer:")
                if answer is None:  # Користувач натиснув Cancel
                    return

            questions.append({"question": question, "type": q_type, "options": options, "answer": answer})

        new_test = Test(title, questions, topic)
        self.manager.save_test(new_test)
        messagebox.showinfo("Success", "Test created successfully.")

