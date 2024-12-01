from tkinter import simpledialog, messagebox
from test import Test  

class QuestionCreator:
    def create_question(self):
        raise NotImplementedError("Method must be implemented in subclasses")

# Клас для створення питань із однією відповіддю
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


class TestCreate:
    def __init__(self, manager):
        self.manager = manager
        # Словник для вибору типу питання
        self.question_creators = {
            "single": SingleChoiceQuestionCreator(),
            "multiple": MultipleChoiceQuestionCreator(),
            "open": OpenQuestionCreator()
        }

    def create_test(self):
        title = simpledialog.askstring("Create Test", "Enter test title:")
        if not title:
            return  

        topic = simpledialog.askstring("Create Test", "Enter test topic:")
        if not topic:
            return  

        # Запитуємо, як користувач хоче встановити бали
        set_points_choice = messagebox.askyesno(
            "Points Setup", "Do you want to set points for each question manually?"
        )

        total_points = 0 
        if set_points_choice:
            # Введення балів для кожного питання вручну
            questions = []
            while True:
                question_type = simpledialog.askstring("Question Type", "Enter question type (single/multiple/open):")
                if not question_type:
                    break  

                creator = self.question_creators.get(question_type)
                if not creator:
                    messagebox.showerror("Error", "Invalid question type. Please choose one of the following: single, multiple, open.")
                    continue  

                question = creator.create_question()
                if question:
                    points = simpledialog.askfloat("Points", f"Enter points for the question: {question['question']}")
                    if points is not None:
                        question['points'] = points  
                        total_points += points  
                    questions.append(question)

        else:
            # Введення загальної кількості балів для тесту
            total_points = simpledialog.askfloat("Total Points", "Enter the total points for the test:")
            if total_points is None:
                return  

            questions = []
            while True:
                question_type = simpledialog.askstring("Question Type", "Enter question type (single/multiple/open):")
                if not question_type:
                    break  

                creator = self.question_creators.get(question_type)
                if not creator:
                    messagebox.showerror("Error", "Invalid question type. Please choose one of the following: single, multiple, open.")
                    continue  

                question = creator.create_question()
                if question:
                    questions.append(question)

            # Розподіляємо загальні бали на всі питання
            num_questions = len(questions)
            points_per_question = total_points / num_questions if num_questions > 0 else 0
            for question in questions:
                question['points'] = points_per_question  

        if not questions:
            messagebox.showinfo("Info", "No questions were created.")
            return

        new_test = Test(title=title, topic=topic, questions=questions, total_points=total_points)

        self.manager.save_test(new_test)

        messagebox.showinfo("Success", "Test created successfully.")

